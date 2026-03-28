from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

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

class SistemaCultivo(Base):
	__tablename__ = "sistema_cultivo"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

class MetodoAlmacenamiento(Base):
	__tablename__ = "metodo_almacenamiento"
	__table_args__ = {"schema": "catalogo"}
	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(50), unique=True, nullable=False)
	descripcion = Column(Text)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)

