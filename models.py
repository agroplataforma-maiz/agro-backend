from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, DECIMAL, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship
from db import Base

# =================== GERMOPLASMA ===================
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

# =================== AGRONÓMICO ===================
class TipoPractica(Base):
	__tablename__ = "tipo_practica"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	practicas = relationship("PracticaAgricola", back_populates="tipo")

class PracticaAgricola(Base):
	__tablename__ = "practica_agricola"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(150), nullable=False)
	descripcion = Column(Text)
	tipo_id = Column(Integer, ForeignKey("catalogo.tipo_practica.id"))
	tipo = relationship("TipoPractica", back_populates="practicas")

class SistemaManejo(Base):
	__tablename__ = "sistema_manejo"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	descripcion = Column(Text)
	es_tradicional = Column(Boolean)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class TipoFenotipo(Base):
	__tablename__ = "tipo_fenotipo"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	unidad = Column(String(50))
	descripcion = Column(Text)

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
	municipios = relationship("Municipio", back_populates="estado")

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
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	estado = relationship("Estado", back_populates="municipios")
	comunidades = relationship("Comunidad", back_populates="municipio")
	localidades = relationship("Localidad", back_populates="municipio")

class Comunidad(Base):
	__tablename__ = "comunidad"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(200), nullable=False)
	nombre_lengua_orig = Column(String(200))
	tipo = Column(String(50))
	municipio_id = Column(Integer, ForeignKey("catalogo.municipio.id"), nullable=False)
	poblacion_total = Column(Integer)
	num_localidades = Column(SmallInteger)
	fuente = Column(String(100), default="INEGI 2020")
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	municipio = relationship("Municipio", back_populates="comunidades")
	localidades = relationship("Localidad", back_populates="comunidad")

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
	municipio = relationship("Municipio", back_populates="localidades")
	comunidad = relationship("Comunidad", back_populates="localidades")
	colonias = relationship("Colonia", back_populates="localidad")

class Colonia(Base):
	__tablename__ = "colonia"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(200), nullable=False)
	tipo = Column(String(50))
	codigo_postal = Column(CHAR(5))
	latitud = Column(DECIMAL(10,7))
	longitud = Column(DECIMAL(10,7))
	localidad_id = Column(Integer, ForeignKey("catalogo.localidad.id"), nullable=False)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	localidad = relationship("Localidad", back_populates="colonias")

# =================== AMBIENTAL ===================
class ClaseUsoSuelo(Base):
	__tablename__ = "clase_uso_suelo"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	codigo = Column(String(20), unique=True, nullable=False)
	nombre = Column(String(100), nullable=False)
	categoria_general = Column(String(100))
	descripcion = Column(Text)
	relevante_maiz = Column(Boolean, default=False)
	activo = Column(Boolean, default=True)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class TipoEventoClimatico(Base):
	__tablename__ = "tipo_evento_climatico"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	severidad_base = Column(SmallInteger)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class VariableAmbiental(Base):
	__tablename__ = "variable_ambiental"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	unidad = Column(String(50))
	valor_min = Column(DECIMAL)
	valor_max = Column(DECIMAL)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

# =================== SOCIOCULTURAL ===================
class TipoProductor(Base):
	__tablename__ = "tipo_productor"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	descripcion = Column(Text)

class Lengua(Base):
	__tablename__ = "lengua"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	nombre_original = Column(String(100))
	familia_linguistica = Column(String(100))
	variante = Column(String(100))
	clave_inali = Column(String(20))
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	pueblos = relationship("PuebloOriginario", back_populates="lengua")

class PuebloOriginario(Base):
	__tablename__ = "pueblo_originario"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(150), nullable=False)
	nombre_propio = Column(String(150))
	lengua_id = Column(Integer, ForeignKey("catalogo.lengua.id"))
	region_historica = Column(String(200))
	municipios_presencia = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	lengua = relationship("Lengua", back_populates="pueblos")

# =================== TRAZABILIDAD ===================
class OrigenMuestra(Base):
	__tablename__ = "origen_muestra"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
