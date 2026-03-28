from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, SmallInteger

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