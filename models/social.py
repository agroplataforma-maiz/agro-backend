from sqlalchemy import Column, ForeignKey, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

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

