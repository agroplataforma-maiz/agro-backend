from enum import Enum
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime
from uuid import UUID

from core.constants import ACCESS_TOKEN_EXPIRE_MINUTES
# ═══════════════════════════════════════════════════════
# ROLES
# ═══════════════════════════════════════════════════════
class Rol(str, Enum):
    administrador  = "administrador"
    investigador   = "investigador"
    tecnico_campo  = "tecnico_campo"
    visualizador   = "visualizador"
    productor      = "productor"
 
 
PERMISOS = {
    Rol.administrador: {
        "puede_crear_usuarios", "puede_eliminar", "puede_editar_catalogos",
        "puede_ver_todo", "puede_exportar", "puede_configurar",
    },
    Rol.investigador: {
        "puede_ver_todo", "puede_crear_productores", "puede_editar_datos",
        "puede_exportar",
    },
    Rol.tecnico_campo: {
        "puede_crear_productores", "puede_editar_datos_propios",
    },
    Rol.visualizador: {
        "puede_ver_todo",
    },
    Rol.productor: {
        "puede_ver_propio",
    },
}


class UsuarioRegistro(BaseModel):
    username: str
    email: EmailStr
    password: str
    nombre_completo: Optional[str] = None
    rol: Rol = Rol.visualizador
 
    @validator("username")
    def username_valido(cls, v):
        if len(v) < 3:
            raise ValueError("El username debe tener al menos 3 caracteres")
        # Permitir letras, números, guion, guion bajo y punto
        permitido = v.replace("_", "").replace("-", "").replace(".", "")
        if not permitido.isalnum():
            raise ValueError("El username solo puede contener letras, números, -, _ y .")
        return v.lower()
 
    @validator("password")
    def password_seguro(cls, v):
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return v
 
 
class UsuarioLogin(BaseModel):
    identificador: str   # email o username
    password: str
 
 
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES * 60
    usuario: dict
 
 
class UsuarioPublico(BaseModel):
    id: UUID
    username: str
    email: str
    nombre_completo: Optional[str] = None
    rol: Rol
    activo: bool
    ultimo_acceso: Optional[datetime] = None
    creado_en: datetime
    actualizado_en: datetime
 
    class Config:
        from_attributes = True
 
 
class CambioRol(BaseModel):
    rol: Rol


class ActualizarUsuario(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    nombre_completo: Optional[str] = None
    rol: Optional[Rol] = None
    activo: Optional[bool] = None

    @validator("username")
    def username_valido(cls, v):
        if v is not None:
            if len(v) < 3:
                raise ValueError("El username debe tener al menos 3 caracteres")
            permitido = v.replace("_", "").replace("-", "").replace(".", "")
            if not permitido.isalnum():
                raise ValueError("El username solo puede contener letras, números, -, _ y .")
            return v.lower()
        return v
 
 
class ActualizarPerfil(BaseModel):
    nombre_completo: Optional[str] = None
    email: Optional[EmailStr] = None
    password_actual: Optional[str] = None
    password_nuevo: Optional[str] = None
 
    @validator("password_nuevo")
    def password_nuevo_seguro(cls, v):
        if v and len(v) < 8:
            raise ValueError("La nueva contraseña debe tener al menos 8 caracteres")
        return v


class CambiarPassword(BaseModel):
    password_actual: str
    password_nuevo: str

    @validator("password_nuevo")
    def password_nuevo_seguro(cls, v):
        if len(v) < 8:
            raise ValueError("La nueva contraseña debe tener al menos 8 caracteres")
        return v


class ResetPassword(BaseModel):
    password_nuevo: str

    @validator("password_nuevo")
    def password_seguro(cls, v):
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return v