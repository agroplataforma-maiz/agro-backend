from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, SmallInteger, String, Text, TIMESTAMP
from database import Base
from sqlalchemy.dialects.postgresql import UUID

class TipoRitualAgricola(Base):
	__tablename__ = "tipo_ritual_agricola"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(60), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class TipoNarrativaOral(Base):
	__tablename__ = "tipo_narrativa_oral"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class CategoriaSaberAgricola(Base):
	__tablename__ = "categoria_saber_agricola"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(80), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class Ocasion(Base):
	__tablename__ = "ocasion"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(80), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class MecanismoTransmision(Base):
	__tablename__ = "mecanismo_transmision"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
    # productor_id eliminado, ya no es parte del modelo
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class VinculoMaiz(Base):
	__tablename__ = "vinculo_maiz"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
 
 # Modelos culturales (solo ejemplo, puedes expandir igual que los sociales)
class SaberTradicional(Base):
    __tablename__ = "saber_tradicional"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
    comunidad_id = Column(Integer, ForeignKey('catalogo.comunidad.id'))
    categoria_saber_agricola_id = Column(Integer, ForeignKey('catalogo.categoria_saber_agricola.id'))
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
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
    tipo_narrativa_oral_id = Column(Integer, ForeignKey('catalogo.tipo_narrativa_oral.id'))
    titulo = Column(String(200))
    titulo_lengua_orig = Column(String(200))
    lengua_id = Column(Integer, ForeignKey('catalogo.lengua.id'))
    contenido_resumen = Column(Text)
    contenido_transcripcion = Column(Text)
    contenido_lengua_orig = Column(Text)
    temas_principales = Column(Text)
    vinculo_maiz_id = Column(Integer, ForeignKey('catalogo.vinculo_maiz.id'))
    descripcion_vinculo_maiz = Column(Text)
    circunstancia_narracion = Column(Text)
    audiencia_habitual = Column(String(200))
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
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
    # Agrega aquí los campos según el modelo
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class IdentidadCultural(Base):
    __tablename__ = "identidad_cultural"
    __table_args__ = {'schema': 'cultural'}
    id = Column(Integer, primary_key=True)
    productor_id = Column(UUID(as_uuid=True), ForeignKey("core.productor.id", ondelete="CASCADE", onupdate="CASCADE"))
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
