from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# =================== AMBIENTAL ===================
class ClaseUsoSueloBase(BaseModel):
	codigo: str
	nombre: str
	categoria_general: Optional[str] = None
	descripcion: Optional[str] = None
	relevante_maiz: Optional[bool] = None
	activo: Optional[bool] = None
class ClaseUsoSueloCreate(ClaseUsoSueloBase):
	pass
class ClaseUsoSuelo(ClaseUsoSueloBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class TipoEventoClimaticoBase(BaseModel):
	nombre: str
	severidad_base: Optional[int] = None
	descripcion: Optional[str] = None
class TipoEventoClimaticoCreate(TipoEventoClimaticoBase):
	pass
class TipoEventoClimatico(TipoEventoClimaticoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class VariableAmbientalBase(BaseModel):
	nombre: str
	unidad: Optional[str] = None
	valor_min: Optional[float] = None
	valor_max: Optional[float] = None
class VariableAmbientalCreate(VariableAmbientalBase):
	pass
class VariableAmbiental(VariableAmbientalBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class TipoAmenazaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoAmenazaCreate(TipoAmenazaBase):
	pass
class TipoAmenaza(TipoAmenazaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True