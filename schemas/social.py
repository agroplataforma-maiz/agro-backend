from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# =================== SOCIOCULTURAL ===================
class TipoProductorBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoProductorCreate(TipoProductorBase):
	pass
class TipoProductor(TipoProductorBase):
	id: int
	class Config:
		from_attributes = True

class LenguaBase(BaseModel):
	nombre: str
	nombre_original: Optional[str] = None
	familia_linguistica: Optional[str] = None
	variante: Optional[str] = None
	clave_inali: Optional[str] = None
class LenguaCreate(LenguaBase):
	pass
class Lengua(LenguaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class PuebloOriginarioBase(BaseModel):
	nombre: str
	nombre_propio: Optional[str] = None
	lengua_id: Optional[int] = None
	region_historica: Optional[str] = None
	municipios_presencia: Optional[str] = None
class PuebloOriginarioCreate(PuebloOriginarioBase):
	pass
class PuebloOriginario(PuebloOriginarioBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True


