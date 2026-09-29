from sqlalchemy import Boolean, Column, Integer, String, Text, DECIMAL, DateTime, ForeignKey, text, Numeric, Date, SmallInteger, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from geoalchemy2 import Geometry

from database import Base
 
class Parcela(Base):

    __tablename__ = "parcela"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"),)
    nombre = Column(String(150))
    superficie_ha = Column(DECIMAL(8, 4))
    sistema_manejo_id = Column(Integer, ForeignKey("catalogo.sistema_manejo.id", ondelete="SET NULL", onupdate="CASCADE",), nullable=True,)
    tenencia = Column(String(50))
    topografia = Column(String(30))
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="RESTRICT", onupdate="CASCADE",), nullable=False,)
    ubicacion_id = Column(UUID(as_uuid=True), ForeignKey("core.ubicacion.id", ondelete="SET NULL", onupdate="CASCADE",), nullable=True,)
    poligono = Column(Geometry(geometry_type="POLYGON", srid=4326,), nullable=False,)
    densidad_plantas_ha = Column(Integer)
    observaciones_sitio = Column(Text)
    creado_en = Column(DateTime(timezone=True), server_default=text("now()"),)
    actualizado_en = Column(DateTime(timezone=True), server_default=text("now()"),)


class Ubicacion(Base):

    __tablename__ = "ubicacion"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    nombre = Column(String(100))
    tipo_ubicacion = Column(String(50))
    descripcion = Column(Text)
    latitud = Column(Numeric(10, 7), nullable=False)
    longitud = Column(Numeric(10, 7), nullable=False)
    altitud_m = Column(Numeric(8, 2))
    altitud_fuente = Column(String(50))
    precision_gps = Column(Numeric(6, 2))
    municipio_id = Column(Integer, ForeignKey("catalogo.municipio.id", onupdate="CASCADE", ondelete="SET NULL"))
    sistema_referencia = Column(String(20), server_default=text("'WGS84'"))
    fuente_captura_id = Column(Integer, ForeignKey("trazabilidad.fuente.id", onupdate="CASCADE", ondelete="SET NULL"),)
    tags = Column(ARRAY(Text))
    activo = Column(Boolean, server_default=text("true"))
    geom = Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), server_default=text("now()"))


class Productor(Base):
    __tablename__ = "productor"
    __table_args__ = {'schema': 'core'}
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))  # Identificador único del productor
    nombres = Column(String(150), nullable=False)  # Nombres del productor
    apellido_paterno = Column(String(100))  # Apellido paterno
    apellido_materno = Column(String(100))  # Apellido materno
    fecha_nacimiento = Column(Date, default=None)  # Fecha de nacimiento
    genero = Column(String(30), nullable=True, comment="Género del productor: masculino, femenino, no_binario, prefiere_no_decir")
    estado_civil = Column(String(30), nullable=True, comment="Estado civil: soltero, casado, union_libre, divorciado, viudo, otro")
    anios_experiencia = Column(SmallInteger)  # Años de experiencia en la actividad
    telefono = Column(String(20))  # Teléfono de contacto
    correo_electronico = Column(String(150), default=None)  # Correo electrónico (opcional)
    tipo_productor_id = Column(Integer, ForeignKey("catalogo.tipo_productor.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)  # FK tipo de productor
    comunidad_id = Column(UUID(as_uuid=True),ForeignKey("core.comunidad.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    municipio_id = Column(Integer, ForeignKey('catalogo.municipio.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True)  # FK municipio
    localidad_id = Column(Integer, ForeignKey('catalogo.localidad.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True)  # FK localidad
    ubicacion_id = Column(UUID(as_uuid=True), ForeignKey("core.ubicacion.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    creado_en = Column(DateTime(timezone=True), server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True),server_default=text("now()"))
    #fecha_registro = Column(Date, default=None)  # Fecha de registro de datos
    #created_at = Column(TIMESTAMP, server_default="now()")  # Timestamp de creación
    #updated_at = Column(TIMESTAMP, server_default="now()")  # Timestamp de actualización
    
class Comunidad(Base):
    __tablename__ = "comunidad"
    __table_args__ = {"schema": "core"}
	
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    nombre = Column(String(200), nullable=False)
    nombre_lengua_orig = Column(String(200))
    tipo = Column(String(50))
    municipio_id = Column(Integer, ForeignKey("catalogo.municipio.id"), nullable=False)
    ubicacion_id = Column(UUID(as_uuid=True), ForeignKey("core.ubicacion.id"))
    presencia_maiz_nativo = Column(Boolean, default=False)
    presencia_historica_maiz = Column(Boolean, default=False)
    diversidad_ecologica_score = Column(SmallInteger)
    riqueza_cultural_score = Column(SmallInteger)
    prioridad_muestreo = Column(String(20), default="media")
    poblacion_total = Column(Integer)
    num_localidades = Column(SmallInteger)
    fuente = Column(String(100), default="INEGI 2020" )
    activo = Column(Boolean, default=True)
    creado_en = Column(TIMESTAMP)
    actualizado_en = Column(TIMESTAMP)

class Organizacion(Base):
    __tablename__ = "organizacion"
    __table_args__ = {"schema": "core"}

    id = Column( UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    nombre = Column( String(200), nullable=False, unique=True)
    descripcion = Column(Text)
    propietario_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="RESTRICT"), nullable=False)
    activo = Column(Boolean, nullable=False, server_default=text("true"))
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    actualizado_en = Column( DateTime(timezone=True), nullable=False, server_default=text("now()"))

class OrganizacionMiembro(Base):
    __tablename__ = "organizacion_miembro"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    organizacion_id = Column(UUID(as_uuid=True), ForeignKey("core.organizacion.id", ondelete="CASCADE"), nullable=False)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="CASCADE"), nullable=False)
    fecha_ingreso = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    activo = Column(Boolean, nullable=False, server_default=text("true"))            

class Siembra(Base):
    __tablename__ = "siembra"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    parcela_id = Column(UUID(as_uuid=True), ForeignKey("core.parcela.id", ondelete="CASCADE"), nullable=False)
    germoplasma_id = Column(UUID(as_uuid=True), ForeignKey("core.germoplasma.id", ondelete="CASCADE"), nullable=False)
    fecha_siembra = Column(Date)
    fecha_corte = Column(Date)
    fecha_cosecha = Column(Date)
    densidad = Column(Numeric)
    rendimiento_kg_ha = Column(Numeric)
    ciclo_agricola = Column(String(20))