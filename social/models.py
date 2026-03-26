from sqlalchemy import Column, Integer, String, Date, Boolean, SmallInteger, Text, ForeignKey, DECIMAL, TIMESTAMP, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Productor(Base):
    __tablename__ = "productor"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    nombres = Column(String(150), nullable=False)
    apellido_paterno = Column(String(100))
    apellido_materno = Column(String(100))
    fecha_nacimiento = Column(Date)
    genero = Column(String(30))
    estado_civil = Column(String(30))
    anios_experiencia = Column(SmallInteger)
    fecha_registro = Column(Date)
    comunidad_id = Column(Integer, ForeignKey('catalogo.comunidad.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

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
    fecha_registro = Column(Date)
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
    elcsa_puntaje_total = Column(SmallInteger)
    nivel_inseguridad = Column(String(30))
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
    # ...campos omitidos por brevedad...
    updated_at = Column(TIMESTAMP)

class GeolocalizacionProductor(Base):
    __tablename__ = "geolocalizacion_productor"
    __table_args__ = {'schema': 'social'}
    id = Column(Integer, primary_key=True)
    # ...campos omitidos por brevedad...
    updated_at = Column(TIMESTAMP)

# Modelos culturales (solo ejemplo, puedes expandir igual que los sociales)
class SaberTradicional(Base):
    __tablename__ = "saber_tradicional"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    comunidad_id = Column(Integer, ForeignKey('catalogo.comunidad.id'))
    categoria = Column(String(80))
    descripcion = Column(Text)
    descripcion_lengua_orig = Column(Text)
    lengua_id = Column(Integer, ForeignKey('catalogo.lengua.id'))
    aprendio_de = Column(String(50))
    generaciones_estimadas = Column(SmallInteger)
    esta_vigente = Column(Boolean, default=True)
    razon_perdida = Column(Text)
    considera_importante = Column(Boolean, default=True)
    importancia_descripcion = Column(Text)
    tiene_evidencia_audio = Column(Boolean, default=False)
    tiene_evidencia_video = Column(Boolean, default=False)
    tiene_evidencia_foto = Column(Boolean, default=False)
    ruta_archivo_multimedia = Column(String(500))
    fecha_registro = Column(Date)
    registrado_por = Column(String(150))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


# --- MODELOS CULTURALES FALTANTES ---
class RitualAgricola(Base):
    __tablename__ = "ritual_agricola"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    comunidad_id = Column(Integer, ForeignKey('catalogo.comunidad.id'))
    nombre = Column(String(150), nullable=False)
    nombre_lengua_orig = Column(String(150))
    lengua_id = Column(Integer, ForeignKey('catalogo.lengua.id'))
    tipo = Column(String(80))
    mes_aproximado = Column(Integer)
    vinculado_ciclo_agricola = Column(String(80))
    descripcion = Column(Text)
    descripcion_lengua_orig = Column(Text)
    participantes = Column(Text)
    elementos_utilizados = Column(Text)
    lugar_realizacion = Column(String(150))
    frecuencia_actual = Column(String(80))
    esta_vigente = Column(Boolean, default=True)
    razon_perdida = Column(Text)
    esfuerzos_recuperacion = Column(Text)
    tiene_evidencia_audio = Column(Boolean, default=False)
    tiene_evidencia_video = Column(Boolean, default=False)
    tiene_evidencia_foto = Column(Boolean, default=False)
    ruta_archivo_multimedia = Column(String(500))
    fecha_registro = Column(Date)
    registrado_por = Column(String(150))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class NarrativaOral(Base):
    __tablename__ = "narrativa_oral"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    comunidad_id = Column(Integer, ForeignKey('catalogo.comunidad.id'))
    productor_id = Column(Integer, ForeignKey('social.productor.id'))
    tipo = Column(String(80))
    titulo = Column(String(200))
    titulo_lengua_orig = Column(String(200))
    lengua_id = Column(Integer, ForeignKey('catalogo.lengua.id'))
    contenido_resumen = Column(Text)
    contenido_transcripcion = Column(Text)
    contenido_lengua_orig = Column(Text)
    temas_principales = Column(Text)
    vinculo_maiz = Column(String(80))
    circunstancia_narracion = Column(Text)
    audiencia_habitual = Column(Text)
    aprendio_de = Column(String(80))
    generaciones_estimadas = Column(SmallInteger)
    esta_vigente = Column(Boolean, default=True)
    tiene_audio = Column(Boolean, default=False)
    tiene_video = Column(Boolean, default=False)
    ruta_archivo_multimedia = Column(String(500))
    fecha_registro = Column(Date)
    registrado_por = Column(String(150))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class GastronomiaTradicional(Base):
    __tablename__ = "gastronomia_tradicional"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    comunidad_id = Column(Integer, ForeignKey('catalogo.comunidad.id'))
    nombre_platillo = Column(String(150), nullable=False)
    nombre_lengua_orig = Column(String(150))
    lengua_id = Column(Integer, ForeignKey('catalogo.lengua.id'))
    # Agrega aquí los campos restantes según el modelo
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class TransmisionConocimiento(Base):
    __tablename__ = "transmision_conocimiento"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    # Agrega aquí los campos según el modelo
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class IdentidadCultural(Base):
    __tablename__ = "identidad_cultural"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    # Agrega aquí los campos según el modelo
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class NombreLenguaOriginaria(Base):
    __tablename__ = "nombre_lengua_originaria"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    # Agrega aquí los campos según el modelo
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

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