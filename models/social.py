from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, Date, DateTime, ForeignKey, Index, Integer, SmallInteger, String, Text, TIMESTAMP, UniqueConstraint, Table, text
from database import Base
from sqlalchemy.dialects.postgresql import UUID

metadata = Base.metadata

# Tabla de asociación explícita para GastronomiaTradicional <-> Productor
gastronomia_productor = Table(
    'gastronomia_productor',
    metadata,
    Column('gastronomia_id', Integer, ForeignKey('cultural.gastronomia_tradicional.id'), primary_key=True),
    Column('productor_id', UUID(as_uuid=True), ForeignKey('core.productor.id'), primary_key=True),
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

class ProductorUsuario(Base):
    __tablename__ = "productor_usuario"
    __table_args__ = {"schema": "social"}
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="CASCADE"), nullable=False, unique=True)
    creado_en = Column(DateTime(timezone=True), server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), server_default=text("now()"))

class TecnicoCampo(Base):
    __tablename__ = "tecnico_campo"
    __table_args__ = {"schema": "social"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"),)
    user_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="CASCADE"), nullable=False, unique=True,)
    institucion = Column(String(200))
    especialidad = Column(String(150))
    notas = Column(Text)
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))

    
class TecnicoProductor(Base):
    __tablename__ = "tecnico_productor"
    __table_args__ = (
        UniqueConstraint(
            "tecnico_campo_id",
            "productor_id",
            name="tecnico_productor_tecnico_productor_key",
        ),
        CheckConstraint(
            "estado IN ('activo', 'suspendido', 'finalizado')",
            name="tecnico_productor_estado_check",
        ),
        CheckConstraint(
            "fecha_finalizacion IS NULL "
            "OR fecha_finalizacion >= fecha_asignacion",
            name="tecnico_productor_fechas_check",
        ),
        CheckConstraint(
            "(estado = 'finalizado' AND fecha_finalizacion IS NOT NULL) "
            "OR (estado <> 'finalizado' AND fecha_finalizacion IS NULL)",
            name="tecnico_productor_finalizacion_check",
        ),
        Index(
            "idx_tecnico_productor_activo_tecnico",
            "tecnico_campo_id",
            "productor_id",
            postgresql_where=text("estado = 'activo'"),
        ),
        Index(
            "idx_tecnico_productor_activo_productor",
            "productor_id",
            "tecnico_campo_id",
            postgresql_where=text("estado = 'activo'"),
        ),
        {"schema": "social"},
    )
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"),)
    tecnico_campo_id = Column(UUID(as_uuid=True), ForeignKey("social.tecnico_campo.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False,)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False,)
    estado = Column(String(20), nullable=False, server_default=text("'activo'"))
    fecha_asignacion = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"),)
    fecha_finalizacion = Column(DateTime(timezone=True))
    notas = Column(Text)
    motivo_finalizacion = Column(Text)
    asignado_por_usuario_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", onupdate="CASCADE", ondelete="SET NULL"),)
    finalizado_por_usuario_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", onupdate="CASCADE", ondelete="SET NULL"),)
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    actualizado_en = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))

class ProductorPractica(Base):
    __tablename__ = "productor_practica"
    __table_args__ = {'schema': 'social'}
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    practica_id = Column(Integer, ForeignKey("catalogo.practica_agricola.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)

class ProductorLengua(Base):
    __tablename__ = "productor_lengua"
    __table_args__ = {'schema': 'social'}
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    lengua_id = Column(Integer, ForeignKey("catalogo.lengua.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    es_materna = Column(Boolean, default=False)

class Consentimiento(Base):
    __tablename__ = "consentimiento"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
    fecha = Column(Date)
    tipo = Column(String(20))
    autoriza_foto = Column(Boolean, default=False)
    autoriza_datos = Column(Boolean, default=False)
    autoriza_publicacion = Column(Boolean, default=False)
    observaciones = Column(Text)
    registrado_por = Column(UUID(as_uuid=True), ForeignKey("social.tecnico_campo.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class PerfilSocioeconomico(Base):
    __tablename__ = "perfil_socioeconomico"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"), unique=True)
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
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
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
    elcsa_puntaje_total = Column(SmallInteger)
    nivel_inseguridad = Column(String(30))
    #elcsa_puntaje_total = Column(SmallInteger, Computed("<expresion>"))  
    #nivel_inseguridad = Column(String(30), Computed("<expresion>")) 
    fecha_evaluacion = Column(Date)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class RedIntercambio(Base):
    __tablename__ = "red_intercambio"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
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
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
    # ...campos omitidos por brevedad...
    updated_at = Column(TIMESTAMP)

class GeolocalizacionProductor(Base):
    __tablename__ = "geolocalizacion_productor"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
    # ...campos omitidos por brevedad...
    updated_at = Column(TIMESTAMP)

class Notificacion(Base):
    __tablename__ = "notificacion"
    __table_args__ = {'schema': 'sistema'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="CASCADE"), nullable=True)
    titulo = Column(String(200), nullable=False)
    mensaje = Column(Text, nullable=False)
    tipo = Column(String(50), default='informacion', comment="Tipo: informacion, alerta, recordatorio, aviso")
    leida = Column(Boolean, default=False)
    fecha_envio = Column(TIMESTAMP, server_default="now()")
    created_at = Column(TIMESTAMP, server_default="now()")
    updated_at = Column(TIMESTAMP, server_default="now()")

class Investigador(Base):
    __tablename__ = "investigador"
    __table_args__ = {"schema": "social"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="CASCADE"), nullable=False, unique=True)
    institucion = Column(String(200))
    especialidad = Column(String(150))
    orcid = Column(String(30))
    pais = Column(String(80))
    notas = Column(Text)
    creado_en = Column(DateTime(timezone=True), server_default=text("now()"))
    actualizado_en = Column(
    DateTime(timezone=True), server_default=text("now()"))        