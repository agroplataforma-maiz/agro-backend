from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SAEnum
from sqlalchemy.sql import func
from database import Base
from schemas.usuarios import Rol
 
class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"schema": "auth"}
 
    id              = Column(Integer, primary_key=True, index=True)
    username        = Column(String(50), unique=True, nullable=False, index=True)
    email           = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    nombre_completo = Column(String(200))
    rol             = Column(SAEnum(Rol, name="rol_enum"), default=Rol.visualizador)
    activo          = Column(Boolean, default=True)
    fecha_registro  = Column(DateTime(timezone=True), server_default=func.now())
    ultimo_acceso   = Column(DateTime(timezone=True))