"""
Agroplataforma · Módulo de autenticación
========================================
Endpoints:
  POST /auth/register   → Registrar nuevo usuario
  POST /auth/login      → Login (email o username) → JWT
  GET  /auth/me         → Perfil del usuario autenticado
  PUT  /auth/me         → Actualizar perfil propio
  GET  /auth/usuarios   → Listar usuarios (solo admin)
  PUT  /auth/usuarios/{id}/rol         → Cambiar rol (solo admin)
  POST /auth/usuarios/{id}/desactivar  → Desactivar cuenta (solo admin)
  PUT  /auth/usuarios/{id}/desactivar  → Desactivar cuenta (solo admin)
  PUT  /auth/usuarios/{id}/activar     → Activar cuenta (solo admin)
"""

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter

from models.usuarios import Usuario

# Crear un router propio para autenticación
router = APIRouter()
from core.security import ACCESS_TOKEN_EXPIRE_MINUTES, crear_token, get_usuario_actual, hash_password, requiere_rol, verificar_password
from schemas.usuarios import ActualizarPerfil, CambioRol, Rol, TokenResponse, UsuarioLogin, UsuarioPublico, UsuarioRegistro

solo_admin = requiere_rol(Rol.administrador)
admin_o_investigador = requiere_rol(Rol.administrador, Rol.investigador)
puede_capturar = requiere_rol(Rol.administrador, Rol.investigador, Rol.tecnico_campo)

@router.post("/register", response_model=UsuarioPublico, status_code=201)
def registrar_usuario(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario. El rol por defecto es 'visualizador'.
    Solo un administrador puede registrar con rol elevado.
    """
    # Verificar duplicados
    if db.query(Usuario).filter(
        (Usuario.username == datos.username) | (Usuario.email == datos.email)
    ).first():
        raise HTTPException(status_code=400, detail="Username o email ya registrado")
 
    nuevo = Usuario(
        username=datos.username,
        email=datos.email,
        hashed_password=hash_password(datos.password),
        nombre_completo=datos.nombre_completo,
        rol=datos.rol,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.post("/login", response_model=TokenResponse)
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    """
    Login con email O username + password.
    Devuelve JWT Bearer token.
    """
    ident = datos.identificador.strip().lower()
 
    # Buscar por email o username
    es_email = "@" in ident
    filtro = Usuario.email == ident if es_email else Usuario.username == ident
    usuario = db.query(Usuario).filter(filtro, Usuario.activo == True).first()
 
    if not usuario or not verificar_password(datos.password, usuario.hashed_password):
         raise HTTPException(status_code=401, detail="Credenciales incorrectas")
 
    usuario.ultimo_acceso = datetime.utcnow()
    db.commit()
 
    token = crear_token({
        "sub": str(usuario.id),
        "username": usuario.username,
        "email": usuario.email,
        "rol": usuario.rol.value if hasattr(usuario.rol, 'value') else usuario.rol,
    })
 
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        "usuario": {
            "id": usuario.id,
            "username": usuario.username,
            "email": usuario.email,
            "nombre_completo": usuario.nombre_completo,
            "rol": usuario.rol.value if hasattr(usuario.rol, 'value') else usuario.rol,
        }
    }
 
 
@router.post("/login/form", response_model=TokenResponse)
def login_form(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Endpoint OAuth2 estándar compatible con Swagger UI."""
    from pydantic import ValidationError
    return login(UsuarioLogin(identificador=form_data.username, password=form_data.password), db)
 
 
@router.get("/me", response_model=UsuarioPublico)
def mi_perfil(usuario=Depends(get_usuario_actual), db: Session = Depends(get_db)):
    """Retorna el perfil del usuario autenticado."""
    return db.query(Usuario).filter(Usuario.id == usuario["id"]).first()
 
 
@router.put("/me")
def actualizar_mi_perfil(
    datos: ActualizarPerfil,
    usuario=Depends(get_usuario_actual),
    db: Session = Depends(get_db),
):
    """Actualiza nombre, email o contraseña del usuario autenticado."""
    u = db.query(Usuario).filter(Usuario.id == usuario["id"]).first()
    if datos.password_nuevo:
        if not datos.password_actual or not verificar_password(datos.password_actual, u.hashed_password):
            raise HTTPException(status_code=400, detail="Contraseña actual incorrecta")
        u.hashed_password = hash_password(datos.password_nuevo)
    if datos.nombre_completo: u.nombre_completo = datos.nombre_completo
    if datos.email: u.email = datos.email
    db.commit()
    return {"mensaje": "Perfil actualizado correctamente"}
 

@router.get("/usuarios", dependencies=[Depends(solo_admin)])
def listar_usuarios(db: Session = Depends(get_db)):
    """Lista todos los usuarios. Solo administradores."""
    return db.query(Usuario).all()


@router.put("/usuarios/{usuario_id}/rol", dependencies=[Depends(solo_admin)])
def cambiar_rol(usuario_id: int, datos: CambioRol, db: Session = Depends(get_db)):
    """Cambia el rol de un usuario. Solo administradores."""
    u = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not u: raise HTTPException(404, "Usuario no encontrado")
    u.rol = datos.rol
    db.commit()
    return {"mensaje": f"Rol actualizado a {datos.rol}"}
 
 
@router.post("/usuarios/{usuario_id}/desactivar", dependencies=[Depends(solo_admin)])
def desactivar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Desactiva una cuenta. Solo administradores."""
    u = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not u: raise HTTPException(404, "Usuario no encontrado")
    u.activo = False
    db.commit()
    return {"mensaje": "Usuario desactivado"}


@router.put("/usuarios/{usuario_id}/desactivar", dependencies=[Depends(solo_admin)])
def desactivar_usuario_put(usuario_id: int, db: Session = Depends(get_db)):
    """Desactiva una cuenta. Solo administradores."""
    u = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not u.activo:
        raise HTTPException(status_code=400, detail="El usuario ya está desactivado")
    u.activo = False
    db.commit()
    return {"mensaje": "Usuario desactivado"}


@router.put("/usuarios/{usuario_id}/activar", dependencies=[Depends(solo_admin)])
def activar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Reactiva una cuenta desactivada. Solo administradores."""
    u = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if u.activo:
        raise HTTPException(status_code=400, detail="El usuario ya está activo")
    u.activo = True
    db.commit()
    return {"mensaje": "Usuario activado"}