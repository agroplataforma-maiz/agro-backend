from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db
from models.core import Parcela
from models.core import Productor
from models.social import TecnicoCampo, TecnicoProductor
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

Ejemplo de JSON para Swagger:

- `sistema_manejo_id`: ID existente en catalogo.sistema_manejo.
- `tenencia`: ejidal, privada, comunal, rentada, prestada o desconocida.
- `topografia`: plana, ondulada, ladera, terraza o barranco.
- `productor_id`: UUID de un productor existente.
- `ubicacion_id`: UUID de una ubicación existente o null.
- `poligono`: geometría en formato WKT.
"""
)
def crear_parcela(
    datos: ParcelaCreate,
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):
    rol = usuario_actual["rol"]

    if rol not in [Rol.productor, Rol.tecnico_campo]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo un productor o un técnico de campo puede registrar una parcela"
        )

        if rol == Rol.productor:
             productor = (
                 db.query(Productor)
                 .filter(Productor.user_id == usuario_actual["id"])
                 .first()
        )

        if not productor:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El usuario productor no tiene un perfil de productor registrado"
            )

        if productor.id != datos.productor_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Un productor solo puede registrar parcelas propias"
            )
    if rol == Rol.tecnico_campo:
        tecnico = (
            db.query(TecnicoCampo)
            .filter(TecnicoCampo.user_id == usuario_actual["id"])
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
                TecnicoProductor.productor_id == datos.productor_id,
                TecnicoProductor.estado == "activo"
            )
            .first()
        )

        if not asignacion:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El productor no está asignado a este técnico de campo"
            )        

    productor = (
        db.query(Productor)
        .filter(Productor.id == datos.productor_id)
        .first()
    )

    if not productor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Productor no encontrado"
        )

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
                "productor_id": datos.productor_id,
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
# LISTAR TODAS LAS PARCELAS
# ============================================================

@router.get("")
def listar_parcelas(
    db: Session = Depends(get_db)
):

    parcelas = (
        db.query(Parcela)
        .order_by(Parcela.creado_en.desc())
        .all()
    )

    resultados = []

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

        resultados.append(
            {
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
        )

    return {
        "count": len(resultados),
        "results": resultados
    }


# ============================================================
# OBTENER PARCELA POR ID
# ============================================================

@router.get(
    "/{parcela_id}",
    response_model=ParcelaRespuesta
)
def obtener_parcela(
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parcela no encontrada"
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
# LISTAR PARCELAS DE UN PRODUCTOR
# ============================================================

@router.get(
    "/productor/{productor_id}"
)
def listar_parcelas_productor(
    productor_id: UUID,
    db: Session = Depends(get_db)
):

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

    parcelas = (
        db.query(Parcela)
        .filter(Parcela.productor_id == productor_id)
        .order_by(Parcela.creado_en.desc())
        .all()
    )

    resultados = []

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

        resultados.append(
            {
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
        )

    return {
        "productor_id": productor_id,
        "count": len(resultados),
        "results": resultados
    }

# ============================================================
# CREAR PARCELA COMO TECNICO
# ============================================================

@router.post(
    "/tecnico",
    response_model=ParcelaRespuesta,
    status_code=status.HTTP_201_CREATED
)
def crear_parcela_tecnico(
    datos: ParcelaCreate,
    db: Session = Depends(get_db),
    usuario_actual=Depends(get_usuario_actual)
):

    tecnico = (
        db.query(TecnicoCampo)
        .filter(TecnicoCampo.user_id == usuario_actual["id"])
        .first()
    )

    if not tecnico:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario actual no está registrado como técnico de campo"
        )

    productor = (
        db.query(Productor)
        .filter(Productor.id == datos.productor_id)
        .first()
    )

    if not productor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Productor no encontrado"
        )

    asignacion = (
        db.query(TecnicoProductor)
        .filter(
            TecnicoProductor.tecnico_campo_id == tecnico.id,
            TecnicoProductor.productor_id == datos.productor_id,
            TecnicoProductor.estado == "activo"
        )
        .first()
    )

    if not asignacion:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El productor no está asignado a este técnico de campo"
        )

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
                "productor_id": datos.productor_id,
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
            "ERROR AL REGISTRAR PARCELA COMO TECNICO:",
            repr(e)
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

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