from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
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