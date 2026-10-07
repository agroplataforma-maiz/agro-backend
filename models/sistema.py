from sqlalchemy import Column, String, Boolean, DateTime, BigInteger, Text, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.sql import func
from database import Base
from schemas.usuarios import Rol


class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "sistema"}
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    nombre_completo = Column(String(200))
    rol = Column(ENUM(Rol, name="rol", schema="sistema", create_type=False), nullable=False, default=Rol.visualizador)
    activo = Column(Boolean, default=True)
    ultimo_acceso = Column(DateTime(timezone=True))
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    actualizado_en = Column(DateTime(timezone=True), nullable=False, server_default=func.now())


class Bitacora(Base):
    __tablename__ = "bitacora"
    __table_args__ = (CheckConstraint("nivel IN ('INFO', 'WARNING', 'ERROR')", name="chk_bitacora_nivel",), {"schema": "sistema"},)
    
    id = Column(BigInteger, primary_key=True,autoincrement=True,)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="SET NULL",) ,nullable=True, )
    accion = Column(String(50), nullable=False,)
    modulo = Column(String(50), nullable=False,)
    descripcion = Column(Text, nullable=True,)
    ip = Column(String(50), nullable=True,)
    user_agent = Column(Text, nullable=True,)
    nivel = Column(String(10), nullable=False, default="INFO", server_default="INFO",)
    fecha = Column(DateTime(timezone=True), nullable=False, server_default=func.now(),)    