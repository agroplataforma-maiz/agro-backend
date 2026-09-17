from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db
from models.core import Parcela
from models.core import Productor
from models.social import TecnicoCampo, TecnicoProductor, ProductorUsuario
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
    rol = str(usuario_actual["rol"])

    # ============================================================
    # VALIDAR ROL
    # ============================================================

    if rol not in [Rol.productor.value, Rol.tecnico_campo.value]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo un productor o un técnico de campo puede registrar una parcela"
        )

    # ============================================================
    # VALIDACIÓN DEL PRODUCTOR
    # ============================================================

    if rol == Rol.productor.value:

        productor_usuario = (
            db.query(ProductorUsuario)
            .filter(ProductorUsuario.user_id == usuario_actual["id"])
            .first()
        )

        if not productor_usuario:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El usuario productor no tiene un perfil de productor registrado"
            )

        if productor_usuario.productor_id != datos.productor_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Un productor solo puede registrar parcelas propias"
            )

    # ============================================================
    # VALIDACIÓN DEL TÉCNICO
    # ============================================================

    if rol == Rol.tecnico_campo.value:

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

    # ============================================================
    # VERIFICAR QUE EL PRODUCTOR EXISTA
    # ============================================================

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
# LISTAR TODAS LAS PARCELAS
# ============================================================

@router.get(
    "/todas",
    response_model=list[ParcelaRespuesta],
    summary="Listar todas las parcelas",
    description="Obtiene todas las parcelas registradas en la base de datos."
)
def listar_todas_las_parcelas(
    db: Session = Depends(get_db)
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
