from database import Base
from sqlalchemy import CHAR, DECIMAL, Column, ForeignKey, Integer, String, Boolean, TIMESTAMP, SmallInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text

# =================== TERRITORIAL ===================
class Estado(Base):
	__tablename__ = "estado"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	clave_inegi = Column(CHAR(2), unique=True, nullable=False)
	nombre = Column(String(100), nullable=False)
	abreviatura = Column(String(10))
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class Municipio(Base):
	__tablename__ = "municipio"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	clave_inegi = Column(CHAR(3), nullable=False)
	clave_completa = Column(CHAR(5), unique=True, nullable=False)
	nombre = Column(String(150), nullable=False)
	nombre_corto = Column(String(100))
	cabecera = Column(String(150))
	region = Column(String(100), default="Huasteca Potosina")
	estado_id = Column(Integer, ForeignKey("catalogo.estado.id"), nullable=False)
	latitud_centroide = Column(DECIMAL(10,7))
	longitud_centroide = Column(DECIMAL(10,7))
	superficie_km2 = Column(DECIMAL(10,2))
	created_at = Column("creado_en", TIMESTAMP(timezone=True), nullable=False)
	updated_at = Column("actualizado_en", TIMESTAMP(timezone=True), nullable=False)

class Localidad(Base):
	__tablename__ = "localidad"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	clave_inegi = Column(CHAR(9), nullable=False)
	nombre = Column(String(200), nullable=False)
	nombre_lengua_orig = Column(String(200))
	tipo = Column(String(50))
	categoria = Column(String(100))
	poblacion_total = Column(Integer)
	num_viviendas = Column(Integer)
	grado_marginacion = Column(String(30))
	indigena = Column(Boolean, default=False)
	latitud = Column(DECIMAL(10,7))
	longitud = Column(DECIMAL(10,7))
	altitud_m = Column(DECIMAL(8,2))
	municipio_id = Column(Integer, ForeignKey("catalogo.municipio.id"), nullable=False)
	comunidad_id = Column(Integer, ForeignKey("catalogo.comunidad.id"))
	fuente = Column(String(100), default="INEGI 2020")
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class Colonia(Base):
	__tablename__ = "colonia"
	__table_args__ = {"schema": "core"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(200), nullable=False)
	tipo = Column(String(50))
	codigo_postal = Column(CHAR(5))
	latitud = Column(DECIMAL(10,7))
	longitud = Column(DECIMAL(10,7))
	localidad_id = Column(Integer, ForeignKey("catalogo.localidad.id"), nullable=False)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)