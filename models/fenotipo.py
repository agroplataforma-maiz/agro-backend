from database import Base
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP


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