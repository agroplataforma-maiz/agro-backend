from uuid import UUID
from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field


class OrganizacionCrear(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=200)
    descripcion: str | None = None
    propietario_id: UUID


class OrganizacionRespuesta(BaseModel):
    id: UUID
    nombre: str
    descripcion: str | None = None
    propietario_id: UUID
    activo: bool

    class Config:
        from_attributes = True


class OrganizacionMiembroCrear(BaseModel):
    usuario_id: UUID


class OrganizacionMiembroRespuesta(BaseModel):
    id: UUID
    organizacion_id: UUID
    usuario_id: UUID
    fecha_ingreso: datetime
    activo: bool

    class Config:
        from_attributes = True

# =================== SIEMBRA ===================

class SiembraBase(BaseModel):
    parcela_id: UUID
    germoplasma_id: UUID
    fecha_siembra: Optional[date] = None
    fecha_corte: Optional[date] = None
    fecha_cosecha: Optional[date] = None
    densidad: Optional[float] = None
    rendimiento_kg_ha: Optional[float] = None
    ciclo_agricola: Optional[str] = None


class SiembraCreate(SiembraBase):
    pass


class SiembraRespuesta(SiembraBase):
    id: UUID
    edad_dias: Optional[int] = None
    edad_meses: Optional[int] = None
    edad_anios: Optional[int] = None

    class Config:
        from_attributes = True

class OrganizacionPropietarioRespuesta(BaseModel):
    organizacion_id: UUID
    organizacion_nombre: str
    propietario_id: UUID
    propietario_nombre: str
    propietario_email: str

    class Config:
        from_attributes = True

class InvestigadorDisponibleRespuesta(BaseModel):
    id: UUID
    nombre_completo: str
    email: str

    class Config:
        from_attributes = True

# =================== COMUNIDAD ===================

class ComunidadBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=200)
    nombre_lengua_orig: Optional[str] = None
    tipo: Optional[str] = None
    municipio_id: int
    ubicacion_id: Optional[UUID] = None
    presencia_maiz_nativo: bool = False
    presencia_historica_maiz: bool = False
    diversidad_ecologica_score: Optional[int] = Field(
        default=None,
        ge=1,
        le=5
    )
    riqueza_cultural_score: Optional[int] = Field(
        default=None,
        ge=1,
        le=5
    )
    prioridad_muestreo: str = "media"
    poblacion_total: Optional[int] = None
    num_localidades: Optional[int] = None
    fuente: Optional[str] = "INEGI 2020"


class ComunidadCrear(ComunidadBase):
    pass


class ComunidadRespuesta(ComunidadBase):
    id: UUID
    activo: bool

    class Config:
        from_attributes = True        