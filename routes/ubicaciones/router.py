from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db
from models.core import Ubicacion
from schemas.geoespacial import UbicacionCreate, UbicacionRespuesta


router = APIRouter()


# ============================================================
# CREAR UBICACION
# ============================================================

@router.post(
    "",
    response_model=UbicacionRespuesta,
    status_code=status.HTTP_201_CREATED
)
def crear_ubicacion(
    datos: UbicacionCreate,
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # Crear geometría POINT a partir de latitud y longitud
    # --------------------------------------------------------

    try:
        geom = db.execute(
            text(
                """
                SELECT ST_SetSRID(
                    ST_MakePoint(:longitud, :latitud),
                    4326
                )
                """
            ),
            {
                "longitud": datos.longitud,
                "latitud": datos.latitud
            }
        ).scalar()

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo crear la geometría de ubicación"
        )

    if geom is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Coordenadas inválidas"
        )

    # --------------------------------------------------------
    # Crear ubicación
    # --------------------------------------------------------

    ubicacion = Ubicacion(
        nombre=datos.nombre,
        tipo_ubicacion=datos.tipo_ubicacion,
        descripcion=datos.descripcion,
        latitud=datos.latitud,
        longitud=datos.longitud,
        altitud_m=datos.altitud_m,
        altitud_fuente=datos.altitud_fuente,
        precision_gps=datos.precision_gps,
        municipio_id=datos.municipio_id,
        sistema_referencia=datos.sistema_referencia,
        fuente_captura_id=datos.fuente_captura_id,
        tags=datos.tags,
        geom=geom,
    )

    try:
        db.add(ubicacion)
        db.commit()
        db.refresh(ubicacion)

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo registrar la ubicación"
        )

    return ubicacion


# ============================================================
# LISTAR UBICACIONES
# ============================================================

@router.get("")
def listar_ubicaciones(
    db: Session = Depends(get_db)
):
    ubicaciones = db.execute(
        text("""
            SELECT
                id,
                nombre,
                tipo_ubicacion,
                descripcion,
                latitud,
                longitud,
                altitud_m,
                altitud_fuente,
                precision_gps,
                municipio_id,
                sistema_referencia,
                fuente_captura_id,
                tags,
                activo,
                creado_en,
                actualizado_en,
                ST_AsText(geom) AS geom
            FROM core.ubicacion
            ORDER BY creado_en DESC
        """)
    ).mappings().all()

    return {
        "count": len(ubicaciones),
        "results": [dict(ubicacion) for ubicacion in ubicaciones]
    }


# ============================================================
# OBTENER UBICACION
# ============================================================

@router.get(
    "/{ubicacion_id}",
    response_model=UbicacionRespuesta
)
def obtener_ubicacion(
    ubicacion_id,
    db: Session = Depends(get_db)
):

    ubicacion = (
        db.query(Ubicacion)
        .filter(Ubicacion.id == ubicacion_id)
        .first()
    )

    if not ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ubicación no encontrada"
        )

    return ubicacion

# ============================================================
# ELIMINAR UBICACION
# ============================================================

@router.delete(
    "/{ubicacion_id}",
    status_code=status.HTTP_200_OK
)
def eliminar_ubicacion(
    ubicacion_id,
    db: Session = Depends(get_db)
):

    ubicacion = (
        db.query(Ubicacion)
        .filter(Ubicacion.id == ubicacion_id)
        .first()
    )

    if not ubicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ubicación no encontrada"
        )

    try:
        db.delete(ubicacion)
        db.commit()

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar la ubicación porque está siendo utilizada"
        )

    return {
        "ok": True,
        "mensaje": "Ubicación eliminada correctamente"
    }