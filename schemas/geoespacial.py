from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# =================== TERRITORIAL ===================
class EstadoBase(BaseModel):
	clave_inegi: str
	nombre: str
	abreviatura: Optional[str] = None
class EstadoCreate(EstadoBase):
	pass
class Estado(EstadoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class MunicipioBase(BaseModel):
	clave_inegi: str
	clave_completa: str
	nombre: str
	nombre_corto: Optional[str] = None
	cabecera: Optional[str] = None
	region: Optional[str] = None
	estado_id: int
	latitud_centroide: Optional[float] = None
	longitud_centroide: Optional[float] = None
	superficie_km2: Optional[float] = None
class MunicipioCreate(MunicipioBase):
	pass
class Municipio(MunicipioBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class ComunidadBase(BaseModel):
	nombre: str
	nombre_lengua_orig: Optional[str] = None
	tipo: Optional[str] = None
	municipio_id: int
	poblacion_total: Optional[int] = None
	num_localidades: Optional[int] = None
	fuente: Optional[str] = None
class ComunidadCreate(ComunidadBase):
	pass
class Comunidad(ComunidadBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class LocalidadBase(BaseModel):
	clave_inegi: str
	nombre: str
	nombre_lengua_orig: Optional[str] = None
	tipo: Optional[str] = None
	categoria: Optional[str] = None
	poblacion_total: Optional[int] = None
	num_viviendas: Optional[int] = None
	grado_marginacion: Optional[str] = None
	indigena: Optional[bool] = None
	latitud: Optional[float] = None
	longitud: Optional[float] = None
	altitud_m: Optional[float] = None
	municipio_id: int
	comunidad_id: Optional[int] = None
	fuente: Optional[str] = None
class LocalidadCreate(LocalidadBase):
	pass
class Localidad(LocalidadBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class ColoniaBase(BaseModel):
	nombre: str
	tipo: Optional[str] = None
	codigo_postal: Optional[str] = None
	latitud: Optional[float] = None
	longitud: Optional[float] = None
	localidad_id: int
class ColoniaCreate(ColoniaBase):
	pass
class Colonia(ColoniaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True