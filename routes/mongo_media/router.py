from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db
from bson import ObjectId
from bson.errors import InvalidId

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from core.security import get_usuario_actual

from database_mongo import multimedia_collection, medios_parcela_collection, medios_culturales_collection, evidencias_fenotipicas_collection

from storage_s3 import AWS_BUCKET, subir_archivo, generar_url_temporal

from schemas.multimedia_trazabilidad import MultimediaCrear
from schemas.multimedia_parcela import MultimediaParcelaCrear
from schemas.multimedia_cultural import MultimediaCulturalCrear
from schemas.multimedia_fenotipica import MultimediaFenotipicaCrear


router = APIRouter(
    tags=["MongoDB"]
)


# ==========================================================
# FUNCIONES GENERALES
# ==========================================================

def serializar(documento):
    if not documento:
        return None

    documento = dict(documento)

    documento["id"] = str(
        documento.pop("_id")
    )

    return documento


def crear_documento(
    coleccion,
    datos,
    usuario
):

    documento = datos.model_dump(
        exclude_none=True
    )

    ahora = datetime.now(
        timezone.utc
    )

    documento["registrado_por"] = str(
        usuario["id"]
    )

    documento["creado_en"] = ahora
    documento["actualizado_en"] = ahora

    resultado = coleccion.insert_one(
        documento
    )

    documento["_id"] = resultado.inserted_id

    return serializar(
        documento
    )


def listar_documentos(
    coleccion
):

    documentos = coleccion.find()

    return [
        serializar(documento)
        for documento in documentos
    ]


def obtener_documento(
    coleccion,
    mongo_id
):

    try:
        object_id = ObjectId(
            mongo_id
        )

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="ID MongoDB inválido"
        )

    documento = coleccion.find_one(
        {
            "_id": object_id
        }
    )

    if not documento:
        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado"
        )

    return serializar(
        documento
    )


# ==========================================================
# MULTIMEDIA
# ==========================================================

@router.post(
    "/multimedia",
    status_code=201
)
def crear_multimedia(
    datos: MultimediaCrear,
    usuario=Depends(get_usuario_actual)
):

    return crear_documento(
        multimedia_collection,
        datos,
        usuario
    )


@router.get("/multimedia")
def listar_multimedia(
    usuario=Depends(get_usuario_actual)
):

    return listar_documentos(
        multimedia_collection
    )


@router.get(
    "/multimedia/{mongo_id}"
)
def obtener_multimedia(
    mongo_id: str,
    usuario=Depends(get_usuario_actual)
):

    return obtener_documento(
        multimedia_collection,
        mongo_id
    )


# ==========================================================
# MEDIOS PARCELA
# ==========================================================

@router.post(
    "/medios-parcela",
    status_code=201
)
def crear_medio_parcela(
    datos: MultimediaParcelaCrear,
    usuario=Depends(get_usuario_actual)
):

    return crear_documento(
        medios_parcela_collection,
        datos,
        usuario
    )

@router.post(
    "/medios-parcela/upload",
    status_code=201
)
def subir_foto_parcela(
    parcela_id: UUID = Form(...),
    archivo: UploadFile = File(...),

    subtipo: str | None = Form(None),
    descripcion: str | None = Form(None),
    uuid_envio: str | None = Form(None),

    # GPS
    latitud: float = Form(...),
    longitud: float = Form(...),
    altitud_m: float | None = Form(None),
    precision_gps: float | None = Form(None),

    db: Session = Depends(get_db),
    usuario=Depends(get_usuario_actual)
):

    # ======================================================
    # VALIDAR COORDENADAS GPS
    # ======================================================

    if not -90 <= latitud <= 90:
        raise HTTPException(
            status_code=400,
            detail="Latitud inválida"
        )

    if not -180 <= longitud <= 180:
        raise HTTPException(
            status_code=400,
            detail="Longitud inválida"
        )

    # ======================================================
    # VALIDAR TIPO DE ARCHIVO
    # ======================================================

    tipos_permitidos = {
        "image/jpeg",
        "image/png",
        "image/webp",
    }

    if archivo.content_type not in tipos_permitidos:
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten imágenes JPG, PNG o WEBP"
        )

    # ======================================================
    # OBTENER TAMAÑO
    # ======================================================

    archivo.file.seek(0, 2)
    peso_bytes = archivo.file.tell()
    archivo.file.seek(0)

    maximo_bytes = 20 * 1024 * 1024

    if peso_bytes > maximo_bytes:
        raise HTTPException(
            status_code=400,
            detail="La fotografía supera el límite de 20 MB"
        )

    # ======================================================
    # GENERAR NOMBRE ÚNICO
    # ======================================================

    extension = Path(
        archivo.filename or "foto.jpg"
    ).suffix.lower()

    if not extension:
        extension = ".jpg"

    nombre_guardado = f"{uuid4()}{extension}"

    object_key = (
        f"parcelas/"
        f"{parcela_id}/"
        f"{nombre_guardado}"
    )

    # ======================================================
    # SUBIR A OBJECT STORAGE
    # ======================================================

    try:
        subir_archivo(
            archivo.file,
            object_key,
            archivo.content_type
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al subir fotografía: {str(e)}"
        )

    # ======================================================
    # GUARDAR UBICACIÓN EN POSTGIS
    # ======================================================

    try:

        consulta = text("""
            INSERT INTO core.ubicacion (
                nombre,
                tipo_ubicacion,
                descripcion,
                latitud,
                longitud,
                altitud_m,
                precision_gps,
                sistema_referencia,
                geom
            )
            VALUES (
                :nombre,
                'foto_parcela',
                :descripcion,
                :latitud,
                :longitud,
                :altitud_m,
                :precision_gps,
                'WGS84',

                ST_SetSRID(
                    ST_MakePoint(
                        :longitud,
                        :latitud
                    ),
                    4326
                )
            )
            RETURNING id
        """)

        resultado_ubicacion = db.execute(
            consulta,
            {
                "nombre": archivo.filename,
                "descripcion": descripcion,
                "latitud": latitud,
                "longitud": longitud,
                "altitud_m": altitud_m,
                "precision_gps": precision_gps,
            }
        )

        ubicacion_id = resultado_ubicacion.scalar_one()

        db.commit()

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Error al guardar ubicación en PostGIS: {str(e)}"
        )

    # ======================================================
    # GUARDAR METADATA EN MONGODB
    # ======================================================

    ahora = datetime.now(timezone.utc)

    documento = {
        "parcela_id": str(parcela_id),

        # Referencia PostGIS
        "ubicacion_id": str(ubicacion_id),

        "ubicacion": {
            "latitud": latitud,
            "longitud": longitud,
            "altitud_m": altitud_m,
            "precision_gps": precision_gps,
        },

        "tipo_medio": "foto",
        "subtipo": subtipo,

        "nombre_archivo": archivo.filename,
        "nombre_guardado": nombre_guardado,

        "bucket": AWS_BUCKET,
        "object_key": object_key,

        "formato": archivo.content_type,
        "peso_kb": round(peso_bytes / 1024),

        "descripcion": descripcion,
        "uuid_envio": uuid_envio,

        "registrado_por": str(
            usuario["id"]
        ),

        "fecha_captura": ahora,
        "creado_en": ahora,
        "actualizado_en": ahora,
    }

    resultado = medios_parcela_collection.insert_one(
        documento
    )

    # ======================================================
    # GENERAR URL TEMPORAL
    # ======================================================

    url_temporal = generar_url_temporal(
        object_key
    )

    # ======================================================
    # RESPUESTA
    # ======================================================

    return {
        "mensaje": "Fotografía y ubicación guardadas correctamente",

        "mongo_id": str(
            resultado.inserted_id
        ),

        "parcela_id": str(
            parcela_id
        ),

        "ubicacion_id": str(
            ubicacion_id
        ),

        "ubicacion": {
            "latitud": latitud,
            "longitud": longitud,
            "altitud_m": altitud_m,
            "precision_gps": precision_gps,
        },

        "nombre_archivo": archivo.filename,
        "object_key": object_key,
        "url_temporal": url_temporal,
    }

@router.get("/medios-parcela")
def listar_medios_parcela(
    usuario=Depends(get_usuario_actual)
):

    documentos = listar_documentos(
        medios_parcela_collection
    )

    for documento in documentos:

        object_key = documento.get(
            "object_key"
        )

        if object_key:
            documento["url_temporal"] = (
                generar_url_temporal(
                    object_key
                )
            )

    return documentos

@router.post(
    "/medios-parcela/parcela/{parcela_id}/preview-poligono"
)
def preview_poligono_parcela(
    parcela_id: UUID,
    db: Session = Depends(get_db),
    usuario=Depends(get_usuario_actual)
):

    documentos = list(
        medios_parcela_collection.find(
            {
                "parcela_id": str(parcela_id),
                "orden_perimetro": {
                    "$ne": None
                }
            }
        ).sort(
            "orden_perimetro",
            1
        )
    )

    if len(documentos) < 3:
        raise HTTPException(
            status_code=400,
            detail="Se necesitan al menos 3 puntos"
        )

    puntos = []

    for documento in documentos:

        ubicacion = documento.get("ubicacion")

        if not ubicacion:
            continue

        latitud = ubicacion.get("latitud")
        longitud = ubicacion.get("longitud")

        if latitud is None or longitud is None:
            continue

        puntos.append(
            (
                float(longitud),
                float(latitud)
            )
        )

    if len(puntos) < 3:
        raise HTTPException(
            status_code=400,
            detail="No hay suficientes puntos GPS válidos"
        )

    # cerrar polígono
    if puntos[0] != puntos[-1]:
        puntos.append(puntos[0])

    coordenadas = ", ".join(
        f"{lon} {lat}"
        for lon, lat in puntos
    )

    poligono_wkt = (
        f"POLYGON(({coordenadas}))"
    )

    resultado = db.execute(
        text("""
            SELECT
                ST_IsValid(
                    ST_GeomFromText(
                        :poligono,
                        4326
                    )
                ) AS valido,

                ST_IsValidReason(
                    ST_GeomFromText(
                        :poligono,
                        4326
                    )
                ) AS razon,

                ST_AsGeoJSON(
                    ST_GeomFromText(
                        :poligono,
                        4326
                    )
                ) AS geojson,

                ST_Area(
                    ST_GeomFromText(
                        :poligono,
                        4326
                    )::geography
                ) / 10000 AS superficie_ha
        """),
        {
            "poligono": poligono_wkt
        }
    ).mappings().one()

    return {
        "parcela_id": str(parcela_id),
        "valido": resultado["valido"],
        "razon": resultado["razon"],
        "numero_puntos": len(puntos) - 1,
        "superficie_ha": float(
            resultado["superficie_ha"]
        ),
        "poligono": resultado["geojson"],
        "guardado": False
    }
    
@router.get(
    "/medios-parcela/{mongo_id}"
)
def obtener_medio_parcela(
    mongo_id: str,
    usuario=Depends(get_usuario_actual)
):

    documento = obtener_documento(
        medios_parcela_collection,
        mongo_id
    )

    object_key = documento.get("object_key")

    if object_key:
        documento["url_temporal"] = generar_url_temporal(
            object_key
        )

    return documento

# ==========================================================
# MEDIOS CULTURALES
# ==========================================================

@router.post(
    "/medios-culturales",
    status_code=201
)
def crear_medio_cultural(
    datos: MultimediaCulturalCrear,
    usuario=Depends(get_usuario_actual)
):

    return crear_documento(
        medios_culturales_collection,
        datos,
        usuario
    )


@router.get("/medios-culturales")
def listar_medios_culturales(
    usuario=Depends(get_usuario_actual)
):

    return listar_documentos(
        medios_culturales_collection
    )


@router.get(
    "/medios-culturales/{mongo_id}"
)
def obtener_medio_cultural(
    mongo_id: str,
    usuario=Depends(get_usuario_actual)
):

    return obtener_documento(
        medios_culturales_collection,
        mongo_id
    )

# ==========================================================
# EVIDENCIAS FENOTÍPICAS
# ==========================================================

@router.post(
    "/evidencias-fenotipicas",
    status_code=201
)
def crear_evidencia(
    datos: MultimediaFenotipicaCrear,
    usuario=Depends(get_usuario_actual)
):

    return crear_documento(
        evidencias_fenotipicas_collection,
        datos,
        usuario
    )


@router.get(
    "/evidencias-fenotipicas"
)
def listar_evidencias(
    usuario=Depends(get_usuario_actual)
):

    return listar_documentos(
        evidencias_fenotipicas_collection
    )


@router.get(
    "/evidencias-fenotipicas/{mongo_id}"
)
def obtener_evidencia(
    mongo_id: str,
    usuario=Depends(get_usuario_actual)
):

    return obtener_documento(
        evidencias_fenotipicas_collection,
        mongo_id
    )
