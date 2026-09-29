from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from uuid import UUID


# =================== HISTORIAL DE PARCELA ===================

class HistorialParcelaBase(BaseModel):
    parcela_id: UUID
    anios_cultivando: Optional[int] = None
    siempre_maiz_nativo: Optional[bool] = False
    cultivos_anteriores: Optional[str] = None
    uso_fertilizantes_hist: Optional[bool] = False
    detalle_fertilizantes: Optional[str] = None
    registrado_por: Optional[UUID] = None
    fuente_id: Optional[int] = None
    fecha_registro: Optional[date] = None


class HistorialParcelaCreate(HistorialParcelaBase):
    pass


class HistorialParcelaRespuesta(HistorialParcelaBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True

# =================== ACTIVIDAD DE CAMPO ===================

class ActividadCampoBase(BaseModel):
    visita_id: int
    practica_id: int
    fecha_actividad: Optional[date] = None
    descripcion: Optional[str] = None
    observaciones: Optional[str] = None
    registrado_por: Optional[UUID] = None


class ActividadCampoCreate(ActividadCampoBase):
    pass


class ActividadCampoRespuesta(ActividadCampoBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True        