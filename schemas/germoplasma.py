from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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