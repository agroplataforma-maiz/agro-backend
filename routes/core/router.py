from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID


from database import get_db
from models.core import Organizacion, OrganizacionMiembro
from models.sistema import Usuario
from schemas.core import OrganizacionCrear, OrganizacionRespuesta, OrganizacionMiembroCrear, OrganizacionMiembroRespuesta
from core.security import requiere_rol
from schemas.usuarios import Rol


router = APIRouter()

solo_admin = requiere_rol(Rol.administrador)


@router.post(
    "/organizaciones",
    response_model=OrganizacionRespuesta,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(solo_admin)],
    tags=["Organizaciones"]
)
def crear_organizacion(
    datos: OrganizacionCrear,
    db: Session = Depends(get_db)
):
    existente = (
        db.query(Organizacion)
        .filter(Organizacion.nombre == datos.nombre)
        .first()
    )

    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una organizacion con ese nombre"
        )

    organizacion = Organizacion(
        nombre=datos.nombre,
        descripcion=datos.descripcion
    )

    db.add(organizacion)
    db.commit()
    db.refresh(organizacion)

    return organizacion


@router.get(
    "/organizaciones",
    response_model=list[OrganizacionRespuesta],
    tags=["Organizaciones"]
)
def listar_organizaciones(
    db: Session = Depends(get_db)
):
    return (
        db.query(Organizacion)
        .filter(Organizacion.activo.is_(True))
        .order_by(Organizacion.nombre)
        .all()
    )

# ============================================================
# AGREGAR MIEMBRO A UNA ORGANIZACION
# ============================================================

@router.post(
    "/organizaciones/{organizacion_id}/miembros",
    response_model=OrganizacionMiembroRespuesta,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(solo_admin)],
    tags=["Organizaciones"]
)
def agregar_miembro(
    organizacion_id: UUID,
    datos: OrganizacionMiembroCrear,
    db: Session = Depends(get_db)
):
    # Verificar que la organización exista y esté activa
    organizacion = (
        db.query(Organizacion)
        .filter(
            Organizacion.id == organizacion_id,
            Organizacion.activo.is_(True)
        )
        .first()
    )

    if not organizacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organización no encontrada"
        )

    # Verificar que el usuario exista y esté activo
    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.id == datos.usuario_id,
            Usuario.activo.is_(True)
        )
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    # Solo estos roles pueden pertenecer a una organización
    roles_permitidos = {
        Rol.administrador,
        Rol.investigador,
        Rol.tecnico_campo
    }

    if usuario.rol not in roles_permitidos:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El rol del usuario no puede pertenecer a una organización"
        )

    # Verificar que no esté ya registrado
    existente = (
        db.query(OrganizacionMiembro)
        .filter(
            OrganizacionMiembro.organizacion_id == organizacion_id,
            OrganizacionMiembro.usuario_id == datos.usuario_id
        )
        .first()
    )

    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya pertenece a esta organización"
        )

    miembro = OrganizacionMiembro(
        organizacion_id=organizacion_id,
        usuario_id=datos.usuario_id
    )

    db.add(miembro)
    db.commit()
    db.refresh(miembro)

    return miembro

@router.get(
    "/organizaciones/{organizacion_id}/miembros",
    response_model=list[OrganizacionMiembroRespuesta],
    tags=["Organizaciones"]
)
def listar_miembros(
    organizacion_id: UUID,
    db: Session = Depends(get_db)
):
    organizacion = (
        db.query(Organizacion)
        .filter(Organizacion.id == organizacion_id)
        .first()
    )

    if not organizacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organización no encontrada"
        )

    return (
        db.query(OrganizacionMiembro)
        .filter(
            OrganizacionMiembro.organizacion_id == organizacion_id,
            OrganizacionMiembro.activo.is_(True)
        )
        .all()
    )

# ============================================================
# DESACTIVAR MIEMBRO DE UNA ORGANIZACION
# ============================================================

@router.delete(
    "/organizaciones/{organizacion_id}/miembros/{usuario_id}",
    response_model=OrganizacionMiembroRespuesta,
    tags=["Organizaciones"],
    dependencies=[Depends(solo_admin)]
)
def eliminar_miembro(
    organizacion_id: UUID,
    usuario_id: UUID,
    db: Session = Depends(get_db)
):
    miembro = (
        db.query(OrganizacionMiembro)
        .filter(
            OrganizacionMiembro.organizacion_id == organizacion_id,
            OrganizacionMiembro.usuario_id == usuario_id,
            OrganizacionMiembro.activo.is_(True)
        )
        .first()
    )

    if not miembro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no es miembro activo de esta organización"
        )

    miembro.activo = False

    db.commit()
    db.refresh(miembro)

    return miembro

# ============================================================
# DESACTIVAR ORGANIZACION Y SUS MIEMBROS
# ============================================================

@router.delete(
    "/organizaciones/{organizacion_id}",
    response_model=OrganizacionRespuesta,
    tags=["Organizaciones"],
    dependencies=[Depends(solo_admin)]
)
def desactivar_organizacion(
    organizacion_id: UUID,
    db: Session = Depends(get_db)
):
    organizacion = (
        db.query(Organizacion)
        .filter(
            Organizacion.id == organizacion_id,
            Organizacion.activo.is_(True)
        )
        .first()
    )

    if not organizacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organización no encontrada o ya está inactiva"
        )

    # Desactivar la organización
    organizacion.activo = False

    # Desactivar todos sus miembros
    db.query(OrganizacionMiembro).filter(
        OrganizacionMiembro.organizacion_id == organizacion_id,
        OrganizacionMiembro.activo.is_(True)
    ).update(
        {
            OrganizacionMiembro.activo: False
        },
        synchronize_session=False
    )

    db.commit()
    db.refresh(organizacion)

    return organizacion