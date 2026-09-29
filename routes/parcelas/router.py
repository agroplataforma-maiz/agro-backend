from uuid import UUID
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db
from models.core import Parcela
from models.core import Productor
from models.geografico import HistorialParcela
from models.social import TecnicoCampo, TecnicoProductor, ProductorUsuario

import schemas.geografico as geografico_schemas
from schemas.geoespacial import ParcelaCreate, ParcelaRespuesta
from core.security import get_usuario_actual, requiere_rol
from schemas.usuarios import Rol


router = APIRouter()


# ============================================================
# CREAR PARCELA
# ============================================================

@router.post(
    "",
    response_model=ParcelaRespuesta,
    status_code=status.HTTP_201_CREATED,
    summary="Crear parcela",
    description="""
Registra una parcela asociada a un productor.

Comportamiento:
- Productor: el productor se obtiene automáticamente desde el usuario autenticado.
- Técnico de campo: debe indicar un productor que tenga asignado y activo.

Otros campos:
- `sistema_manejo_id`: ID existente en catalogo.sistema_manejo.
- `tenencia`: ejidal, privada, comunal, rentada, prestada o desconocida.
- `topografia`: plana, ondulada, ladera, terraza o barranco.
- `ubicacion_id`: UUID de una ubicación existente o null.
- `poligono`: geometría en formato WKT.
"""
)
def crear_parcela(
    datos: ParcelaCreate,
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):
    rol = str(usuario_actual["rol"])

    # ============================================================
    # DETERMINAR PRODUCTOR
    # ============================================================

    productor_id = datos.productor_id

    # ============================================================
    # PRODUCTOR
    # ============================================================

    if rol == Rol.productor.value:

        productor_usuario = (
            db.query(ProductorUsuario)
            .filter(
                ProductorUsuario.user_id == usuario_actual["id"]
            )
            .first()
        )

        if not productor_usuario:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El usuario productor no tiene un perfil de productor registrado"
            )

        # El backend obtiene automáticamente el productor
        productor_id = productor_usuario.productor_id

    # ============================================================
    # TÉCNICO DE CAMPO
    # ============================================================

    elif rol == Rol.tecnico_campo.value:

        if not productor_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El técnico debe indicar el productor al que pertenece la parcela"
            )

        tecnico = (
            db.query(TecnicoCampo)
            .filter(
                TecnicoCampo.user_id == usuario_actual["id"]
            )
            .first()
        )

        if not tecnico:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El usuario actual no está registrado como técnico de campo"
            )

        asignacion = (
            db.query(TecnicoProductor)
            .filter(
                TecnicoProductor.tecnico_campo_id == tecnico.id,
                TecnicoProductor.productor_id == productor_id,
                TecnicoProductor.estado == "activo"
            )
            .first()
        )

        if not asignacion:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El productor no está asignado a este técnico de campo"
            )

    # ============================================================
    # VERIFICAR QUE EL PRODUCTOR EXISTA
    # ============================================================

    productor = (
        db.query(Productor)
        .filter(Productor.id == productor_id)
        .first()
    )

    if not productor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Productor no encontrado"
        )

    # ============================================================
    # CREAR PARCELA
    # ============================================================

    try:

        resultado = db.execute(
            text(
                """
                INSERT INTO core.parcela (
                    nombre,
                    superficie_ha,
                    sistema_manejo_id,
                    tenencia,
                    topografia,
                    productor_id,
                    ubicacion_id,
                    poligono,
                    densidad_plantas_ha,
                    observaciones_sitio
                )
                VALUES (
                    :nombre,
                    :superficie_ha,
                    :sistema_manejo_id,
                    :tenencia,
                    :topografia,
                    :productor_id,
                    :ubicacion_id,
                    ST_GeomFromText(:poligono, 4326),
                    :densidad_plantas_ha,
                    :observaciones_sitio
                )
                RETURNING id
                """
            ),
            {
                "nombre": datos.nombre,
                "superficie_ha": datos.superficie_ha,
                "sistema_manejo_id": datos.sistema_manejo_id,
                "tenencia": datos.tenencia,
                "topografia": datos.topografia,
                "productor_id": productor_id,
                "ubicacion_id": datos.ubicacion_id,
                "poligono": datos.poligono,
                "densidad_plantas_ha": datos.densidad_plantas_ha,
                "observaciones_sitio": datos.observaciones_sitio,
            }
        )

        parcela_id = resultado.scalar_one()

        db.commit()

    except Exception as e:

        db.rollback()

        print(
            "ERROR AL REGISTRAR PARCELA:",
            repr(e)
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    # ============================================================
    # RECUPERAR PARCELA
    # ============================================================

    parcela = (
        db.query(Parcela)
        .filter(Parcela.id == parcela_id)
        .first()
    )

    if not parcela:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="La parcela fue creada pero no pudo recuperarse"
        )

    poligono_wkt = db.execute(
        text(
            """
            SELECT ST_AsText(poligono)
            FROM core.parcela
            WHERE id = :id
            """
        ),
        {"id": parcela.id}
    ).scalar()

    return {
        "id": parcela.id,
        "nombre": parcela.nombre,
        "superficie_ha": parcela.superficie_ha,
        "sistema_manejo_id": parcela.sistema_manejo_id,
        "tenencia": parcela.tenencia,
        "topografia": parcela.topografia,
        "productor_id": parcela.productor_id,
        "ubicacion_id": parcela.ubicacion_id,
        "poligono": poligono_wkt,
        "densidad_plantas_ha": parcela.densidad_plantas_ha,
        "observaciones_sitio": parcela.observaciones_sitio,
        "creado_en": parcela.creado_en,
        "actualizado_en": parcela.actualizado_en,
    }
# ============================================================
# LISTAR PARCELAS
# ============================================================

@router.get(
    "",
    response_model=list[ParcelaRespuesta],
    summary="Listar parcelas",
    description="Obtiene todas las parcelas registradas en la plataforma."
)
def listar_parcelas(
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):
    parcelas = (
        db.query(Parcela)
        .order_by(Parcela.creado_en.desc())
        .all()
    )

    resultado = []

    for parcela in parcelas:

        poligono_wkt = db.execute(
            text(
                """
                SELECT ST_AsText(poligono)
                FROM core.parcela
                WHERE id = :id
                """
            ),
            {"id": parcela.id}
        ).scalar()

        resultado.append({
            "id": parcela.id,
            "nombre": parcela.nombre,
            "superficie_ha": parcela.superficie_ha,
            "sistema_manejo_id": parcela.sistema_manejo_id,
            "tenencia": parcela.tenencia,
            "topografia": parcela.topografia,
            "productor_id": parcela.productor_id,
            "ubicacion_id": parcela.ubicacion_id,
            "poligono": poligono_wkt,
            "densidad_plantas_ha": parcela.densidad_plantas_ha,
            "observaciones_sitio": parcela.observaciones_sitio,
            "creado_en": parcela.creado_en,
            "actualizado_en": parcela.actualizado_en,
        })

    return resultado

# ============================================================
# MIS PARCELAS COMO PRODUCTOR
# ============================================================

@router.get(
    "/mis-parcelas",
    response_model=list[ParcelaRespuesta],
    summary="Listar mis parcelas como productor",
    description="Obtiene únicamente las parcelas pertenecientes al productor autenticado."
)
def listar_mis_parcelas(
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):
    rol = str(usuario_actual["rol"])

    if rol != Rol.productor.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Este endpoint es únicamente para usuarios productores"
        )

    productor_usuario = (
        db.query(ProductorUsuario)
        .filter(ProductorUsuario.user_id == usuario_actual["id"])
        .first()
    )

    if not productor_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no tiene un perfil de productor registrado"
        )

    parcelas = (
        db.query(Parcela)
        .filter(Parcela.productor_id == productor_usuario.productor_id)
        .order_by(Parcela.creado_en.desc())
        .all()
    )

    resultado = []

    for parcela in parcelas:

        poligono_wkt = db.execute(
            text("""
                SELECT ST_AsText(poligono)
                FROM core.parcela
                WHERE id = :id
            """),
            {"id": parcela.id}
        ).scalar()

        resultado.append({
            "id": parcela.id,
            "nombre": parcela.nombre,
            "superficie_ha": parcela.superficie_ha,
            "sistema_manejo_id": parcela.sistema_manejo_id,
            "tenencia": parcela.tenencia,
            "topografia": parcela.topografia,
            "productor_id": parcela.productor_id,
            "ubicacion_id": parcela.ubicacion_id,
            "poligono": poligono_wkt,
            "densidad_plantas_ha": parcela.densidad_plantas_ha,
            "observaciones_sitio": parcela.observaciones_sitio,
            "creado_en": parcela.creado_en,
            "actualizado_en": parcela.actualizado_en,
        })

    return resultado


# ============================================================
# PARCELAS ASIGNADAS AL TÉCNICO DE CAMPO
# ============================================================

@router.get(
    "/asignadas",
    response_model=list[ParcelaRespuesta],
    summary="Listar parcelas asignadas al técnico",
    description="Obtiene las parcelas pertenecientes a los productores asignados al técnico de campo autenticado."
)
def listar_parcelas_asignadas(
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):
    rol = str(usuario_actual["rol"])

    if rol != Rol.tecnico_campo.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Este endpoint es únicamente para técnicos de campo"
        )

    tecnico = (
        db.query(TecnicoCampo)
        .filter(TecnicoCampo.user_id == usuario_actual["id"])
        .first()
    )

    if not tecnico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no está registrado como técnico de campo"
        )

    productores_asignados = (
        db.query(TecnicoProductor.productor_id)
        .filter(
            TecnicoProductor.tecnico_campo_id == tecnico.id,
            TecnicoProductor.estado == "activo"
        )
        .all()
    )

    productor_ids = [p[0] for p in productores_asignados]

    if not productor_ids:
        return []

    parcelas = (
        db.query(Parcela)
        .filter(Parcela.productor_id.in_(productor_ids))
        .order_by(Parcela.creado_en.desc())
        .all()
    )

    resultado = []

    for parcela in parcelas:

        poligono_wkt = db.execute(
            text("""
                SELECT ST_AsText(poligono)
                FROM core.parcela
                WHERE id = :id
            """),
            {"id": parcela.id}
        ).scalar()

        resultado.append({
            "id": parcela.id,
            "nombre": parcela.nombre,
            "superficie_ha": parcela.superficie_ha,
            "sistema_manejo_id": parcela.sistema_manejo_id,
            "tenencia": parcela.tenencia,
            "topografia": parcela.topografia,
            "productor_id": parcela.productor_id,
            "ubicacion_id": parcela.ubicacion_id,
            "poligono": poligono_wkt,
            "densidad_plantas_ha": parcela.densidad_plantas_ha,
            "observaciones_sitio": parcela.observaciones_sitio,
            "creado_en": parcela.creado_en,
            "actualizado_en": parcela.actualizado_en,
        })

    return resultado

# ============================================================
# ASIGNAR UBICACIÓN A PARCELA
# ============================================================

@router.put(
    "/{parcela_id}/ubicacion",
    response_model=ParcelaRespuesta,
    summary="Asignar ubicación a parcela",
    description="Asigna una ubicación POINT existente a una parcela."
)
def asignar_ubicacion_parcela(
    parcela_id: UUID,
    ubicacion_id: UUID,
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):
    parcela = (
        db.query(Parcela)
        .filter(Parcela.id == parcela_id)
        .first()
    )

    if not parcela:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parcela no encontrada"
        )

    ubicacion = db.execute(
        text(
            """
            SELECT id
            FROM core.ubicacion
            WHERE id = :ubicacion_id
              AND activo = TRUE
            """
        ),
        {"ubicacion_id": ubicacion_id}
    ).scalar()

    if not ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ubicación no encontrada"
        )

    parcela.ubicacion_id = ubicacion_id

    try:
        db.commit()
        db.refresh(parcela)

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    poligono_wkt = db.execute(
        text(
            """
            SELECT ST_AsText(poligono)
            FROM core.parcela
            WHERE id = :id
            """
        ),
        {"id": parcela.id}
    ).scalar()

    return {
        "id": parcela.id,
        "nombre": parcela.nombre,
        "superficie_ha": parcela.superficie_ha,
        "sistema_manejo_id": parcela.sistema_manejo_id,
        "tenencia": parcela.tenencia,
        "topografia": parcela.topografia,
        "productor_id": parcela.productor_id,
        "ubicacion_id": parcela.ubicacion_id,
        "poligono": poligono_wkt,
        "densidad_plantas_ha": parcela.densidad_plantas_ha,
        "observaciones_sitio": parcela.observaciones_sitio,
        "creado_en": parcela.creado_en,
        "actualizado_en": parcela.actualizado_en,
    }

# =================== HISTORIAL DE PARCELA ===================

@router.get(
    "/{parcela_id}/historial",
    response_model=list[geografico_schemas.HistorialParcelaRespuesta]
)
def consultar_historial_parcela(
    parcela_id: UUID,
    db: Session = Depends(get_db)
):
    historial = (
        db.query(HistorialParcela)
        .filter(HistorialParcela.parcela_id == parcela_id)
        .order_by(HistorialParcela.fecha_registro.desc())
        .all()
    )

    return historial

@router.put(
    "/historial-parcela/{historial_id}",
    response_model=geografico_schemas.HistorialParcelaRespuesta
)
def actualizar_historial_parcela(
    historial_id: int,
    historial: geografico_schemas.HistorialParcelaCreate,
    db: Session = Depends(get_db)
):
    registro = (
        db.query(HistorialParcela)
        .filter(HistorialParcela.id == historial_id)
        .first()
    )

    if not registro:
        raise HTTPException(
            status_code=404,
            detail="Historial de parcela no encontrado"
        )

    registro.anios_cultivando = historial.anios_cultivando
    registro.siempre_maiz_nativo = historial.siempre_maiz_nativo
    registro.cultivos_anteriores = historial.cultivos_anteriores
    registro.uso_fertilizantes_hist = historial.uso_fertilizantes_hist
    registro.detalle_fertilizantes = historial.detalle_fertilizantes
    registro.registrado_por = historial.registrado_por
    registro.fuente_id = historial.fuente_id
    registro.fecha_registro = historial.fecha_registro

    db.commit()
    db.refresh(registro)

    return registro

@router.delete("/historial-parcela/{historial_id}")
def eliminar_historial_parcela(
    historial_id: int,
    db: Session = Depends(get_db)
):
    registro = (
        db.query(HistorialParcela)
        .filter(HistorialParcela.id == historial_id)
        .first()
    )

    if not registro:
        raise HTTPException(
            status_code=404,
            detail="Historial de parcela no encontrado"
        )

    db.delete(registro)
    db.commit()

    return {
        "ok": True,
        "mensaje": "Historial de parcela eliminado correctamente"
    } 

# =================== SUPERFICIE DE PARCELA ===================

@router.get("/{parcela_id}/superficie")
def calcular_superficie_parcela(
    parcela_id: UUID,
    db: Session = Depends(get_db)
):
    parcela = (
        db.query(Parcela)
        .filter(Parcela.id == parcela_id)
        .first()
    )

    if not parcela:
        raise HTTPException(
            status_code=404,
            detail="Parcela no encontrada"
        )

    if parcela.poligono is None:
        raise HTTPException(
            status_code=400,
            detail="La parcela no tiene un polígono definido"
        )

    superficie_m2 = db.execute(
        text("""
            SELECT ST_Area(
                ST_Transform(poligono, 32614)
            )
            FROM core.parcela
            WHERE id = :parcela_id
        """),
        {"parcela_id": parcela_id}
    ).scalar()

    if superficie_m2 is None:
        raise HTTPException(
            status_code=400,
            detail="No fue posible calcular la superficie"
        )

    superficie_ha = superficie_m2 / 10000

    parcela.superficie_ha = superficie_ha

    db.commit()
    db.refresh(parcela)

    return {
        "parcela_id": parcela.id,
        "superficie_m2": superficie_m2,
        "superficie_ha": superficie_ha
    }

