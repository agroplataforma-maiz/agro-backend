from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID


from database import get_db
from models.core import Organizacion, OrganizacionMiembro
from models.sistema import Usuario
from schemas.core import OrganizacionCrear, OrganizacionRespuesta, OrganizacionMiembroCrear, OrganizacionMiembroRespuesta, OrganizacionPropietarioRespuesta, InvestigadorDisponibleRespuesta
from core.security import requiere_rol, get_usuario_actual
from schemas.usuarios import Rol


router = APIRouter()

solo_admin = requiere_rol(Rol.administrador)

@router.get(
    "/organizaciones/investigadores-disponibles",
    response_model=list[InvestigadorDisponibleRespuesta],
    tags=["Organizaciones"],
    dependencies=[Depends(solo_admin)]
)
def listar_investigadores_disponibles(
    db: Session = Depends(get_db)
):
    investigadores = (
        db.query(Usuario)
        .filter(
            Usuario.rol == Rol.investigador,
            Usuario.activo.is_(True),

            # No debe ser propietario de otra organización
            ~db.query(Organizacion)
            .filter(
                Organizacion.propietario_id == Usuario.id,
                Organizacion.activo.is_(True)
            )
            .exists(),

            # No debe pertenecer como miembro a otra organización
            ~db.query(OrganizacionMiembro)
            .filter(
                OrganizacionMiembro.usuario_id == Usuario.id,
                OrganizacionMiembro.activo.is_(True)
            )
            .exists()
        )
        .order_by(Usuario.nombre_completo)
        .all()
    )

    return investigadores

@router.get(
    "/organizaciones/propietarios",
    response_model=list[OrganizacionPropietarioRespuesta],
    tags=["Organizaciones"]
)
def listar_propietarios_organizaciones(
    db: Session = Depends(get_db)
):
    resultados = (
        db.query(
            Organizacion.id.label("organizacion_id"),
            Organizacion.nombre.label("organizacion_nombre"),
            Usuario.id.label("propietario_id"),
            Usuario.nombre_completo.label("propietario_nombre"),
            Usuario.email.label("propietario_email")
        )
        .join(
            Usuario,
            Usuario.id == Organizacion.propietario_id
        )
        .filter(
            Organizacion.activo.is_(True),
            Usuario.activo.is_(True)
        )
        .order_by(Organizacion.nombre)
        .all()
    )

    return resultados

def verificar_propietario(
    organizacion_id: UUID,
    usuario_actual,
    db: Session
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
            detail="Organización no encontrada"
        )

    if organizacion.propietario_id != usuario_actual["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo el propietario de la organización puede realizar esta acción"
        )

    return organizacion

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
 
    propietario = (
        db.query(Usuario)
        .filter(
            Usuario.id == datos.propietario_id,
            Usuario.activo.is_(True)
        )
        .first()
    )

    if not propietario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario seleccionado como propietario no existe o está inactivo"
        )

    # El propietario debe ser investigador
    if propietario.rol != Rol.investigador:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo los investigadores pueden ser propietarios de una organización"
        ) 
   
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
    
    organizacion_existente = (
        db.query(Organizacion)
        .filter(
            Organizacion.propietario_id == datos.propietario_id,
            Organizacion.activo.is_(True)
        )
        .first()
    )

    if organizacion_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El investigador ya es propietario de otra organización"
        )

    membresia_existente = (
        db.query(OrganizacionMiembro)
        .filter(
            OrganizacionMiembro.usuario_id == datos.propietario_id,
            OrganizacionMiembro.activo.is_(True)
        )
        .first()
    )

    if membresia_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El investigador ya pertenece a otra organización"
        )

    # Crear organización solamente después de pasar todas las validaciones
    organizacion = Organizacion(
        nombre=datos.nombre,
        descripcion=datos.descripcion,
        propietario_id=datos.propietario_id
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
    tags=["Organizaciones"]
)
def agregar_miembro(
    organizacion_id: UUID,
    datos: OrganizacionMiembroCrear,
    usuario_actual=Depends(get_usuario_actual),
    db: Session = Depends(get_db)
):
    # Verificar que el usuario actual sea el propietario
    organizacion = verificar_propietario(
        organizacion_id,
        usuario_actual,
        db
    )

    # Verificar que el usuario a agregar exista y esté activo
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
            detail="Usuario no encontrado o inactivo"
        )

    # Verificar que el usuario no pertenezca ya a otra organización
    otra_membresia = (
        db.query(OrganizacionMiembro)
        .filter(
            OrganizacionMiembro.usuario_id == datos.usuario_id,
            OrganizacionMiembro.activo.is_(True),
            OrganizacionMiembro.organizacion_id != organizacion_id
        )
        .first()
    )

    if otra_membresia:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya pertenece a otra organización"
        )

    # Un propietario no puede pertenecer a otra organización
    es_propietario = (
        db.query(Organizacion)
        .filter(
            Organizacion.propietario_id == datos.usuario_id,
            Organizacion.activo.is_(True),
            Organizacion.id != organizacion_id
        )
        .first()
    )

    if es_propietario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya es propietario de otra organización"
        )        

    # Roles permitidos dentro de una organización
    roles_permitidos = {
        Rol.administrador,
        Rol.investigador,
        Rol.tecnico_campo,
        Rol.productor
    }

    if usuario.rol not in roles_permitidos:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El rol del usuario no puede pertenecer a una organización"
        )

    # Verificar si ya existe como miembro
    existente = (
        db.query(OrganizacionMiembro)
        .filter(
            OrganizacionMiembro.organizacion_id == organizacion_id,
            OrganizacionMiembro.usuario_id == datos.usuario_id
        )
        .first()
    )

    if existente:
        if existente.activo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El usuario ya pertenece a esta organización"
            )

        # Reactivar membresía anterior
        existente.activo = True
        db.commit()
        db.refresh(existente)

        return existente

    # Crear nuevo miembro
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
    tags=["Organizaciones"]
)
def eliminar_miembro(
    organizacion_id: UUID,
    usuario_id: UUID,
    usuario_actual=Depends(get_usuario_actual),
    db: Session = Depends(get_db)
):
    # Verificar que el usuario actual sea el propietario
    organizacion = verificar_propietario(
        organizacion_id,
        usuario_actual,
        db
    )

    # Buscar miembro activo
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

    # El propietario no se elimina como miembro mediante este endpoint
    if usuario_id == organizacion.propietario_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El propietario no puede ser eliminado de su propia organización"
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