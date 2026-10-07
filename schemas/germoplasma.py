from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID
from datetime import date

# =================== GERMOPLASMA ===================
class RazaMaizBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
	region_origen: Optional[str] = None
	tipo_ciclo: Optional[str] = None
	es_nativa: Optional[bool] = True
class RazaMaizCreate(RazaMaizBase):
	pass
class RazaMaiz(RazaMaizBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class ColorGranoBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
	es_nativo: Optional[bool] = True
class ColorGranoCreate(ColorGranoBase):
	pass
class ColorGrano(ColorGranoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class EstadoConservacionBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
	nivel_riesgo: Optional[int] = None
class EstadoConservacionCreate(EstadoConservacionBase):
	pass
class EstadoConservacion(EstadoConservacionBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class UsoMaizBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class UsoMaizCreate(UsoMaizBase):
	pass
class UsoMaiz(UsoMaizBase):
	id: int
	class Config:
		from_attributes = True

class GermoplasmaBase(BaseModel):
    codigo_accesion: str = Field(..., min_length=1, max_length=30)
    nombre_local: str = Field(..., min_length=1, max_length=200)

    nombre_lengua_orig: Optional[str] = None

    raza_id: Optional[int] = None
    color_grano_id: Optional[int] = None

    ciclo_vegetativo: Optional[str] = None
    duracion_dias: Optional[int] = None

    estado_conservacion_id: Optional[int] = None
    origen_muestra_id: Optional[int] = None

    comunidad_id: UUID
    ubicacion_id: Optional[UUID] = None
    colector_id: Optional[UUID] = None

    notas: Optional[str] = None
    fecha_registro: Optional[date] = None


class GermoplasmaCrear(GermoplasmaBase):
    pass


class GermoplasmaRespuesta(GermoplasmaBase):
    id: UUID

    class Config:
        from_attributes = True
		