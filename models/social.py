
from sqlalchemy import DECIMAL, Boolean, Column, Date, ForeignKey, Integer, SmallInteger, String, Text, TIMESTAMP, Computed, Table, MetaData
from sqlalchemy.orm import relationship
from database import Base

metadata = Base.metadata

# Tabla de asociación explícita para GastronomiaTradicional <-> Productor
gastronomia_productor = Table(
    'gastronomia_productor',
    metadata,
    Column('gastronomia_id', Integer, ForeignKey('cultural.gastronomia_tradicional.id'), primary_key=True),
    Column('productor_id', Integer, ForeignKey('social.productor.id'), primary_key=True),
    Column('es_preparador', Boolean, default=False),
    schema='cultural'
)


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

class Productor(Base):
    __tablename__ = "productor"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True, autoincrement=True)  # Identificador único del productor
    nombres = Column(String(150), nullable=False)  # Nombres del productor
    apellido_paterno = Column(String(100))  # Apellido paterno
    apellido_materno = Column(String(100))  # Apellido materno
    fecha_nacimiento = Column(Date, default=None)  # Fecha de nacimiento
    genero = Column(
        String(30),
        nullable=True,
        comment="Género del productor: masculino, femenino, no_binario, prefiere_no_decir"
    )
    estado_civil = Column(
        String(30),
        nullable=True,
        comment="Estado civil: soltero, casado, union_libre, divorciado, viudo, otro"
    )
    anios_experiencia = Column(SmallInteger)  # Años de experiencia en la actividad
    telefono = Column(String(20))  # Teléfono de contacto
    correo_electronico = Column(String(150), default=None)  # Correo electrónico (opcional)
    tipo_productor_id = Column(Integer, ForeignKey('catalogo.tipo_productor.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True)  # FK tipo de productor
    municipio_id = Column(Integer, ForeignKey('catalogo.municipio.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True)  # FK municipio
    localidad_id = Column(Integer, ForeignKey('catalogo.localidad.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True)  # FK localidad
    fecha_registro = Column(Date, default=None)  # Fecha de registro de datos
    created_at = Column(TIMESTAMP, server_default="now()")  # Timestamp de creación
    updated_at = Column(TIMESTAMP, server_default="now()")  # Timestamp de actualización

class ProductorPractica(Base):
    __tablename__ = "productor_practica"
    __table_args__ = {'schema': 'social'}
    productor_id = Column(Integer, ForeignKey('social.productor.id'), primary_key=True)
    practica_id = Column(Integer, ForeignKey('catalogo.practica_agricola.id'), primary_key=True)

class ProductorLengua(Base):
    __tablename__ = "productor_lengua"
    __table_args__ = {'schema': 'social'}
    productor_id = Column(Integer, ForeignKey('social.productor.id'), primary_key=True)
    lengua_id = Column(Integer, ForeignKey('catalogo.lengua.id'), primary_key=True)
    es_materna = Column(Boolean, default=False)

class Consentimiento(Base):
    __tablename__ = "consentimiento"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    fecha = Column(Date)
    tipo = Column(String(20))
    autoriza_foto = Column(Boolean, default=False)
    autoriza_datos = Column(Boolean, default=False)
    autoriza_publicacion = Column(Boolean, default=False)
    observaciones = Column(Text)
    registrado_por = Column(String(150))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class PerfilSocioeconomico(Base):
    __tablename__ = "perfil_socioeconomico"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'), unique=True)
    escolaridad = Column(String(30))
    escolaridad_otra = Column(String(100))
    superficie_total_ha = Column(DECIMAL(8,4))
    superficie_maiz_ha = Column(DECIMAL(8,4))
    otros_cultivos = Column(Text)
    decision_siembra = Column(String(50))
    peso_kg = Column(DECIMAL(5,2))
    talla_cm = Column(DECIMAL(5,2))
    imc = Column(DECIMAL(5,2))
    pct_grasa = Column(DECIMAL(5,2))
    circunferencia_cintura_cm = Column(DECIMAL(5,2))
    circunferencia_cadera_cm = Column(DECIMAL(5,2))
    circunferencia_pantorrilla_cm = Column(DECIMAL(5,2))
    diagnostico_enfermedad = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class SeguridadAlimentaria(Base):
    __tablename__ = "seguridad_alimentaria"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    num_personas_hogar = Column(SmallInteger)
    num_hombres_adultos = Column(SmallInteger)
    num_mujeres_adultas = Column(SmallInteger)
    num_ninos = Column(SmallInteger)
    num_ninas = Column(SmallInteger)
    gasto_semanal_maiz = Column(DECIMAL(8,2))
    gasto_semanal_frijol = Column(DECIMAL(8,2))
    produce_suficiente_maiz = Column(String(20))
    alimentacion_variada = Column(Boolean)
    alimentacion_variada_razon = Column(Text)
    freq_tortilla = Column(String(20))
    freq_tamales = Column(String(20))
    freq_atole = Column(String(20))
    freq_pozole = Column(String(20))
    otros_alimentos = Column(Text)
    elcsa_preocupacion = Column(SmallInteger)
    elcsa_poca_variedad = Column(SmallInteger)
    elcsa_salto_comida = Column(SmallInteger)
    elcsa_comio_menos = Column(SmallInteger)
    elcsa_sintio_hambre = Column(SmallInteger)
    elcsa_dejo_comer_dia = Column(SmallInteger)
    elcsa_puntaje_total = Column(SmallInteger, Computed("<expresion>"))  
    nivel_inseguridad = Column(String(30), Computed("<expresion>")) 
    fecha_evaluacion = Column(Date)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class RedIntercambio(Base):
    __tablename__ = "red_intercambio"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    frecuencia_intercambio_semilla = Column(String(30))
    participa_ferias_semillas = Column(Boolean, default=False)
    ferias_descripcion = Column(Text)
    decision_cultivos = Column(String(50))
    servicio_agua_entubada = Column(Boolean, default=False)
    servicio_electricidad = Column(Boolean, default=False)
    servicio_internet = Column(Boolean, default=False)
    servicio_drenaje = Column(Boolean, default=False)
    tiene_telefono_movil = Column(Boolean, default=False)
    tiene_radio = Column(Boolean, default=False)
    recibio_capacitacion = Column(Boolean, default=False)
    capacitacion_fuente = Column(String(200))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class VulnerabilidadClimatica(Base):
    __tablename__ = "vulnerabilidad_climatica"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    # ...campos omitidos por brevedad...
    updated_at = Column(TIMESTAMP)

class GeolocalizacionProductor(Base):
    __tablename__ = "geolocalizacion_productor"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    # ...campos omitidos por brevedad...
    updated_at = Column(TIMESTAMP)

class Notificacion(Base):
    __tablename__ = "notificacion"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('auth.usuarios.id', ondelete="CASCADE"), nullable=True)
    titulo = Column(String(200), nullable=False)
    mensaje = Column(Text, nullable=False)
    tipo = Column(String(50), default='informacion', comment="Tipo: informacion, alerta, recordatorio, aviso")
    leida = Column(Boolean, default=False)
    fecha_envio = Column(TIMESTAMP, server_default="now()")
    created_at = Column(TIMESTAMP, server_default="now()")
    updated_at = Column(TIMESTAMP, server_default="now()")