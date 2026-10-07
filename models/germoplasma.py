from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, SmallInteger, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text

from database import Base

class RazaMaiz(Base):
	__tablename__ = "raza_maiz"
	__table_args__ = {"schema": "catalogo"}

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	descripcion = Column(Text)
	region_origen = Column(String(150))
	tipo_ciclo = Column(String(50))
	es_nativa = Column(Boolean, default=True)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class ColorGrano(Base):
	__tablename__ = "color_grano"
	__table_args__ = {"schema": "catalogo"}

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	es_nativo = Column(Boolean, default=True)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class EstadoConservacion(Base):
	__tablename__ = "estado_conservacion"
	__table_args__ = {"schema": "catalogo"}

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	nivel_riesgo = Column(SmallInteger)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class UsoMaiz(Base):
	__tablename__ = "uso_maiz"
	__table_args__ = {"schema": "catalogo"}
	
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class Germoplasma(Base):
    __tablename__ = "germoplasma"
    __table_args__ = {"schema": "core"}

    id = Column( UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    codigo_accesion = Column(String(30), unique=True, nullable=False)
    nombre_local = Column(String(200), nullable=False)
    nombre_lengua_orig = Column(String(200))
    raza_id = Column(Integer, ForeignKey("catalogo.raza_maiz.id", onupdate="CASCADE", ondelete="SET NULL"))
    color_grano_id = Column(Integer, ForeignKey("catalogo.color_grano.id", onupdate="CASCADE", ondelete="SET NULL"))
    ciclo_vegetativo = Column(String(50))
    duracion_dias = Column(SmallInteger)
    estado_conservacion_id = Column(Integer, ForeignKey("catalogo.estado_conservacion.id", onupdate="CASCADE", ondelete="SET NULL"))
    origen_muestra_id = Column(Integer, ForeignKey("trazabilidad.origen_material_agricola.id", onupdate="CASCADE", ondelete="SET NULL"))
    comunidad_id = Column(UUID(as_uuid=True), ForeignKey("core.comunidad.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False)
    ubicacion_id = Column(UUID(as_uuid=True), ForeignKey("core.ubicacion.id", onupdate="CASCADE", ondelete="SET NULL"))
    colector_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", onupdate="CASCADE", ondelete="SET NULL"))
    notas = Column(Text)
    fecha_registro = Column(Date, server_default=text("CURRENT_DATE"))
    creado_en = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    actualizado_en = Column(TIMESTAMP(timezone=True), server_default=text("now()"))