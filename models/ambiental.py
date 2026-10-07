from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, DECIMAL, TIMESTAMP
from database import Base

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

class TipoEventoClimatico(Base):
    __tablename__ = "tipo_evento_climatico"
    __table_args__ = {"schema": "catalogo"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    severidad_base = Column(SmallInteger)
    descripcion = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class TipoAmenaza(Base):
	__tablename__ = "tipo_amenaza"
	__table_args__ = {"schema": "catalogo"}

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(80), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
