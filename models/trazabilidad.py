from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Text, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class TipoProductoDron(Base):
	__tablename__ = "tipo_producto_dron"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class FormatoArchivo(Base):
	__tablename__ = "formato_archivo"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(20), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class TipoCapaSIG(Base):
	__tablename__ = "tipo_capa_sig"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class FuenteCaptura(Base):
	__tablename__ = "fuente_captura"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class FuenteInformacion(Base):
	__tablename__ = "fuente_informacion"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	descripcion = Column(Text)
	tipo = Column(String(30))
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class OrigenSemilla(Base):
	__tablename__ = "origen_semilla"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class OrigenMuestra(Base):
	__tablename__ = "origen_muestra"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class TrazabilidadFormatoArchivo(Base):
    __tablename__ = "formato_archivo"
    __table_args__ = {"schema": "trazabilidad"}

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), unique=True, nullable=False)
    descripcion = Column(Text)
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))

class TrazabilidadFuente(Base):
    __tablename__ = "fuente"
    __table_args__ = {"schema": "trazabilidad"}

    id = Column(Integer, primary_key=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)
    tipo = Column(String(30), nullable=False)
    sub_tipo = Column(String(30))
    es_captura = Column(Boolean, server_default=text("false"))
    es_informacion = Column(Boolean, server_default=text("false"))
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
	
class OrigenMaterialAgricola(Base):
    __tablename__ = "origen_material_agricola"
    __table_args__ = {"schema": "trazabilidad"}

    id = Column(Integer, primary_key=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(80), unique=True, nullable=False)
    descripcion = Column(Text)
    tipo = Column(String(30), nullable=False)
    sub_tipo = Column(String(30))
    creado_en = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()")
    )
    actualizado_en = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()")
    )


class Multimedia(Base):
    __tablename__ = "multimedia"
    __table_args__ = {"schema": "trazabilidad"}

    id = Column(Integer, primary_key=True)
    entidad_tipo = Column(String(50), nullable=False)
    entidad_id = Column(UUID(as_uuid=True), nullable=False)
    tipo_medio = Column(String(20), nullable=False)
    subtipo = Column(String(40))
    nombre_archivo = Column(String(300), nullable=False)
    ruta_almacenamiento = Column(String(500), nullable=False)
    formato_archivo_id = Column(Integer, ForeignKey("trazabilidad.formato_archivo.id", onupdate="CASCADE", ondelete="SET NULL"),)
    descripcion = Column(Text)
    peso_kb = Column(Integer)
    resolucion = Column(String(30))
    fecha_captura = Column(Date)
    uuid_envio = Column(String(100))
    fuente_id = Column(Integer, ForeignKey("trazabilidad.fuente.id", onupdate="CASCADE", ondelete="SET NULL"),)
    registrado_por = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", onupdate="CASCADE", ondelete="SET NULL"),)
    creado_en = Column(DateTime(timezone=True), server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), server_default=text("now()"))