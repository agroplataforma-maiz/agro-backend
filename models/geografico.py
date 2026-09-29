from sqlalchemy import Column, Integer, SmallInteger, Boolean, Text, Date, DateTime, ForeignKey, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID

from database import Base

class HistorialParcela(Base):
    __tablename__ = "historial_parcela"
    __table_args__ = {"schema": "geografico"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    parcela_id = Column(UUID(as_uuid=True), ForeignKey("core.parcela.id", ondelete="CASCADE"), nullable=True)
    anios_cultivando = Column(SmallInteger)
    siempre_maiz_nativo = Column(Boolean, default=False)
    cultivos_anteriores = Column(Text)
    uso_fertilizantes_hist = Column(Boolean,default=False)
    detalle_fertilizantes = Column(Text)
    registrado_por = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="SET NULL"), nullable=True)
    fuente_id = Column(Integer, ForeignKey("trazabilidad.fuente.id", ondelete="SET NULL"), nullable=True)
    fecha_registro = Column(Date)
    creado_en = Column(DateTime(timezone=True))
    actualizado_en = Column(DateTime(timezone=True))

class ActividadCampo(Base):
    __tablename__ = "actividad_campo"
    __table_args__ = {"schema": "geografico"}

    id = Column(Integer, primary_key=True, index=True)
    visita_id = Column(Integer, ForeignKey("geo.visita_campo.id", ondelete="CASCADE"), nullable=False)
    practica_id = Column(Integer, ForeignKey("catalogo.practica_agricola.id", ondelete="RESTRICT"), nullable=False)
    fecha_actividad = Column(Date)
    descripcion = Column(Text)
    observaciones = Column(Text)
    registrado_por = Column(UUID(as_uuid=True), ForeignKey("sistema.usuario.id", ondelete="SET NULL"))
    creado_en = Column(TIMESTAMP(timezone=True), server_default=func.now())
    actualizado_en = Column(TIMESTAMP(timezone=True), server_default=func.now())    