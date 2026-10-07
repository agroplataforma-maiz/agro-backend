from database import Base
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Date, SmallInteger, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text

class TipoFenotipo(Base):
	__tablename__ = "tipo_fenotipo"
	__table_args__ = {"schema": "catalogo"}

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	unidad = Column(String(50))
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class EtapaFenologica(Base):
	__tablename__ = "etapa_fenologica"
	__table_args__ = {"schema": "catalogo"}

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(30), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class MuestraNutrimental(Base):
    __tablename__ = "muestra_nutrimental"
    __table_args__ = {"schema": "fenotipico"}
  
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_muestra = Column(String(30), unique=True, nullable=False)
    germoplasma_id = Column(UUID(as_uuid=True), ForeignKey("core.germoplasma.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False)
    parcela_id = Column(UUID(as_uuid=True), ForeignKey("core.parcela.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False)
    comunidad_id = Column(UUID(as_uuid=True), ForeignKey("core.comunidad.id", onupdate="CASCADE", ondelete="SET NULL"))
    fecha_colecta = Column(Date)
    peso_muestra_g = Column(Numeric(8, 2))
    condicion_muestra = Column(String(50))
    laboratorio = Column(String(200))
    fecha_analisis = Column(Date)
    notas = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP,server_default=text("now()"))


class SubmuestraNutrimental(Base):
    __tablename__ = "submuestra_nutrimental"
    __table_args__ = {"schema": "fenotipico"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    muestra_id = Column(Integer, ForeignKey("fenotipico.muestra_nutrimental.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    numero_submuestra = Column(SmallInteger, nullable=False)
    color_mazorca = Column(String(50))
    color_olote = Column(String(50))
    largo_cm = Column(Numeric(6, 2))
    diametro_cm = Column(Numeric(6, 2))
    peso_mazorca_g = Column(Numeric(8, 2))
    numero_hileras = Column(SmallInteger)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"))	