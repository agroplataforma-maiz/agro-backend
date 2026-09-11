from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db

from models.social import ProductorUsuario
from models.core import Productor, Ubicacion, Comunidad
from models.sistema import Usuario
from models.territorio import Municipio, Localidad
from schemas.productores import ProductorCrear, ProductorRespuesta, ProductorVisualizadorActualizar

from core.security import requiere_rol, hash_password
from schemas.usuarios import Rol


router = APIRouter()


puede_capturar = requiere_rol(
    Rol.administrador,
    Rol.investigador,
    Rol.tecnico_campo
)

@router.get(
    "/lista",
    response_model=list[ProductorRespuesta]
)
def listar_productores(
    db: Session = Depends(get_db),
    usuario_actual=Depends(puede_capturar)
):
    productores = (
        db.query(Productor)
        .order_by(Productor.nombres)
        .all()
    )

    return productores


@router.get("/usuarios-visualizadores")
def obtener_visualizadores(
    db: Session = Depends(get_db),
    usuario_actual=Depends(puede_capturar)
):
    usuarios = (
        db.query(Usuario)
        .filter(
            Usuario.rol == Rol.visualizador,
            Usuario.activo == True
        )
        .order_by(Usuario.username)
        .all()
    )

    return [
        {
            "id": usuario.id,
            "username": usuario.username,
            "email": usuario.email,
            "nombre_completo": usuario.nombre_completo,
            "rol": (
                usuario.rol.value
                if hasattr(usuario.rol, "value")
                else usuario.rol
            )
        }
        for usuario in usuarios
    ]

# ============================================================
# OBTENER UN VISUALIZADOR
# ============================================================

@router.get("/usuarios-visualizadores/{user_id}")
def obtener_visualizador(
    user_id: UUID,
    db: Session = Depends(get_db),
    usuario_actual=Depends(puede_capturar)
):
    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.id == user_id,
            Usuario.rol == Rol.visualizador,
            Usuario.activo == True
        )
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario visualizador no existe o está inactivo"
        )

    return {
        "id": usuario.id,
        "username": usuario.username,
        "email": usuario.email,
        "nombre_completo": usuario.nombre_completo,
        "rol": (
            usuario.rol.value
            if hasattr(usuario.rol, "value")
            else usuario.rol
        )
    }

@router.patch(
    "/usuarios-visualizadores/{user_id}",
    response_model=ProductorRespuesta
)
def actualizar_visualizador_a_productor(
    user_id: UUID,
    datos: ProductorVisualizadorActualizar,
    db: Session = Depends(get_db),
    usuario_actual=Depends(puede_capturar)
):
    # ============================================================
    # 1. BUSCAR USUARIO VISUALIZADOR
    # ============================================================

    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.id == user_id,
            Usuario.activo == True,
            Usuario.rol == Rol.visualizador
        )
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario visualizador no existe o ya no está disponible"
        )

    # ============================================================
    # 2. COMPROBAR QUE NO TENGA PRODUCTOR
    # ============================================================

    relacion_existente = (
        db.query(ProductorUsuario)
        .filter(
            ProductorUsuario.user_id == usuario.id
        )
        .first()
    )

    if relacion_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El usuario ya está vinculado a un productor"
        )

    # ============================================================
    # 3. OBTENER DATOS EXISTENTES DEL USUARIO
    # ============================================================

    nombre_completo = (usuario.nombre_completo or "").strip()

    if not nombre_completo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no tiene nombre registrado"
        )

    partes_nombre = nombre_completo.split()

    # Usamos el primer elemento como nombre.
    # Si existe un segundo, lo usamos como apellido paterno
    # solamente si no se recibió uno en el PATCH.

    nombres = partes_nombre[0]

    apellido_paterno = datos.apellido_paterno

    if not apellido_paterno and len(partes_nombre) >= 2:
        apellido_paterno = partes_nombre[1]

    apellido_materno = datos.apellido_materno

    if not apellido_materno and len(partes_nombre) >= 3:
        apellido_materno = " ".join(partes_nombre[2:])

    # ============================================================
    # 4. CREAR PRODUCTOR CON DATOS EXISTENTES + NUEVOS
    # ============================================================

    productor = Productor(
        nombres=nombres,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,

        fecha_nacimiento=datos.fecha_nacimiento,

        genero=(
            datos.genero.value
            if datos.genero
            else None
        ),

        estado_civil=(
            datos.estado_civil.value
            if datos.estado_civil
            else None
        ),

        anios_experiencia=datos.anios_experiencia,

        telefono=datos.telefono,

        # El correo YA EXISTE en sistema.usuario
        correo_electronico=usuario.email,

        tipo_productor_id=datos.tipo_productor_id,
        comunidad_id=datos.comunidad_id,
        municipio_id=datos.municipio_id,
        localidad_id=datos.localidad_id,
        ubicacion_id=datos.ubicacion_id
    )

    try:

        # ========================================================
        # 5. CREAR PRODUCTOR
        # ========================================================

        db.add(productor)
        db.flush()

        # ========================================================
        # 6. CAMBIAR ROL DEL USUARIO
        # ========================================================

        usuario.rol = Rol.productor

        # ========================================================
        # 7. CREAR RELACIÓN USUARIO → PRODUCTOR
        # ========================================================

        relacion = ProductorUsuario(
            productor_id=productor.id,
            user_id=usuario.id
        )

        db.add(relacion)

        # ========================================================
        # 8. GUARDAR 
        # ========================================================

        db.commit()
        db.refresh(productor)

        return productor

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "No fue posible convertir el visualizador "
                "en productor. Revisa los datos enviados."
            )
        )
        
@router.post(
    "",
    response_model=ProductorRespuesta,
    status_code=status.HTTP_201_CREATED
)
def crear_productor(
    datos: ProductorCrear,
    db: Session = Depends(get_db),
    usuario_actual=Depends(puede_capturar)
):
    """
    Registra un productor.

    Casos:
    1. Productor sin cuenta.
    2. Productor vinculado a un usuario existente.
    3. Productor con una cuenta nueva.
    """

    usuario = None

    # ============================================================
    # 1. USUARIO EXISTENTE MEDIANTE user_id
    # ============================================================

    if datos.user_id:

        usuario = (
            db.query(Usuario)
            .filter(Usuario.id == datos.user_id)
            .first()
        )

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El usuario indicado no existe"
            )

        relacion_existente = (
            db.query(ProductorUsuario)
            .filter(
                ProductorUsuario.user_id == datos.user_id
            )
            .first()
        )

        if relacion_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Este usuario ya está vinculado a un productor"
            )

    # ============================================================
    # 2. CREAR CUENTA NUEVA
    # ============================================================

    if datos.username or datos.password:

        if not datos.username or not datos.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Debes proporcionar username y password"
            )

        if not datos.correo_electronico:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico es obligatorio para crear la cuenta"
            )

        # --------------------------------------------------------
        # Comprobar username
        # --------------------------------------------------------

        usuario_existente = (
            db.query(Usuario)
            .filter(
                Usuario.username == datos.username
            )
            .first()
        )

        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El username ya está registrado"
            )

        # --------------------------------------------------------
        # Comprobar correo
        # --------------------------------------------------------

        email_existente = (
            db.query(Usuario)
            .filter(
                Usuario.email == str(datos.correo_electronico)
            )
            .first()
        )

        if email_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El correo electrónico ya está registrado"
            )

        # --------------------------------------------------------
        # Crear usuario
        # --------------------------------------------------------

        usuario = Usuario(
            username=datos.username,
            email=str(datos.correo_electronico),
            hashed_password=hash_password(datos.password),
            nombre_completo=(
                f"{datos.nombres} "
                f"{datos.apellido_paterno or ''} "
                f"{datos.apellido_materno or ''}"
            ).strip(),
            rol=Rol.productor,
            activo=True
        )

        db.add(usuario)
        db.flush()

    # ============================================================
    # 3. CREAR PRODUCTOR
    # ============================================================

    productor = Productor(
        nombres=datos.nombres,
        apellido_paterno=datos.apellido_paterno,
        apellido_materno=datos.apellido_materno,
        fecha_nacimiento=datos.fecha_nacimiento,
        genero=(
            datos.genero.value
            if datos.genero
            else None
        ),
        estado_civil=(
            datos.estado_civil.value
            if datos.estado_civil
            else None
        ),
        anios_experiencia=datos.anios_experiencia,
        telefono=datos.telefono,
        correo_electronico=(
            str(datos.correo_electronico)
            if datos.correo_electronico
            else None
        ),
        tipo_productor_id=datos.tipo_productor_id,
        comunidad_id=datos.comunidad_id,
        municipio_id=datos.municipio_id,
        localidad_id=datos.localidad_id,
        ubicacion_id=datos.ubicacion_id
    )

    try:

        # ========================================================
        # 4. GUARDAR PRODUCTOR
        # ========================================================

        db.add(productor)
        db.flush()

        # ========================================================
        # 5. VINCULAR USUARIO CON PRODUCTOR
        # ========================================================

        if usuario:

            relacion = ProductorUsuario(
                productor_id=productor.id,
                user_id=usuario.id
            )

            db.add(relacion)

        # ========================================================
        # 6. CONFIRMAR TRANSACCIÓN
        # ========================================================

        db.commit()

        db.refresh(productor)

        return productor

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "No fue posible registrar el productor. "
                "Revisa los datos enviados y las relaciones "
                "con los catálogos."
            )
        )