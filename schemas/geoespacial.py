from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID
from decimal import Decimal

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

# =================== PARCELA ===================

class ParcelaBase(BaseModel):
    nombre: Optional[str] = None
    superficie_ha: Optional[Decimal] = None
    sistema_manejo_id: Optional[int] = None
    tenencia: Optional[str] = None
    topografia: Optional[str] = None
    productor_id: UUID
    ubicacion_id: Optional[UUID] = None
    poligono: str
    densidad_plantas_ha: Optional[int] = None
    observaciones_sitio: Optional[str] = None


class ParcelaCreate(ParcelaBase):
    pass


class ParcelaRespuesta(BaseModel):
    id: UUID
    nombre: Optional[str] = None
    superficie_ha: Optional[Decimal] = None
    sistema_manejo_id: Optional[int] = None
    tenencia: Optional[str] = None
    topografia: Optional[str] = None
    productor_id: UUID
    ubicacion_id: Optional[UUID] = None
    poligono: Optional[str] = None
    densidad_plantas_ha: Optional[int] = None
    observaciones_sitio: Optional[str] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True
		
# =================== UBICACION ===================

from uuid import UUID
from decimal import Decimal


class UbicacionCreate(BaseModel):
    nombre: Optional[str] = None
    tipo_ubicacion: Optional[str] = None
    descripcion: Optional[str] = None

    latitud: Decimal
    longitud: Decimal

    altitud_m: Optional[Decimal] = None
    altitud_fuente: Optional[str] = None
    precision_gps: Optional[Decimal] = None

    municipio_id: Optional[int] = None

    sistema_referencia: Optional[str] = "WGS84"
    fuente_captura_id: Optional[int] = None

    tags: Optional[list[str]] = None


class UbicacionRespuesta(BaseModel):
    id: UUID
    nombre: Optional[str] = None
    tipo_ubicacion: Optional[str] = None
    descripcion: Optional[str] = None

    latitud: Decimal
    longitud: Decimal

    altitud_m: Optional[Decimal] = None
    altitud_fuente: Optional[str] = None
    precision_gps: Optional[Decimal] = None

    municipio_id: Optional[int] = None

    sistema_referencia: Optional[str] = None
    fuente_captura_id: Optional[int] = None

    tags: Optional[list[str]] = None

    activo: Optional[bool] = None

    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True
				