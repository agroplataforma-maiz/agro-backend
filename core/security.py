from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.usuarios import Rol
from models.sistema import Usuario

import os
from core.constants import ACCESS_TOKEN_EXPIRE_MINUTES

# from app.models.usuario import Usuario
# Por ahora se incluyen modelos de referencia abajo
 
# ═══════════════════════════════════════════════════════
# CONFIGURACIÓN JWT
# ═══════════════════════════════════════════════════════
SECRET_KEY = os.getenv("SECRET_KEY", "b87d68f520f3e3e12917b7d26c54dc151dd5946c1b060e57f3266b611176c88c")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8  # 8 horas
 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/form")
 
#router = APIRouter(prefix="/auth", tags=["Autenticación"])

# ═══════════════════════════════════════════════════════
# UTILIDADES JWT
# ═══════════════════════════════════════════════════════
def hash_password(password: str) -> str:
    return pwd_context.hash(password)
 
 
def verificar_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
 
 
def crear_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload.update({"exp": expire, "iat": datetime.utcnow()})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
 
 
def decodificar_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
 
# ═══════════════════════════════════════════════════════
# DEPENDENCIAS
# ═══════════════════════════════════════════════════════
def get_usuario_actual(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),  # reemplaza con get_db
):
    payload = decodificar_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        usuario_id = UUID(user_id)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ID de usuario inválido en el token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.id == usuario_id,
            Usuario.activo == True
        )
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado o inactivo",
            headers={"WWW-Authenticate": "Bearer"},
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
        ),
    }
     
def requiere_rol(*roles: Rol):
    """Decorador de dependencia para restringir por rol."""
    def verificar(usuario=Depends(get_usuario_actual)):
        if usuario["rol"] not in [r.value for r in roles]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Se requiere uno de estos roles: {[r.value for r in roles]}"
            )
        return usuario
    return verificar
  