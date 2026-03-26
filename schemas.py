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
	# ...existing code...
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
	# ...existing code...
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
	# ...existing code...
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

# =================== AGRONÓMICO ===================
class TipoPracticaBase(BaseModel):
	nombre: str

class TipoPracticaCreate(TipoPracticaBase):
	pass

class TipoPractica(TipoPracticaBase):
	id: int
	class Config:
		from_attributes = True

class PracticaAgricolaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
	tipo_id: Optional[int] = None

class PracticaAgricolaCreate(PracticaAgricolaBase):
	pass

class PracticaAgricola(PracticaAgricolaBase):
	id: int
	class Config:
		from_attributes = True

class SistemaManejoBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
	es_tradicional: Optional[bool] = None

class SistemaManejoCreate(SistemaManejoBase):
	pass

class SistemaManejo(SistemaManejoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	# ...existing code...
	class Config:
		from_attributes = True

class TipoFenotipoBase(BaseModel):
	nombre: str
	unidad: Optional[str] = None
	descripcion: Optional[str] = None

class TipoFenotipoCreate(TipoFenotipoBase):
	pass

class TipoFenotipo(TipoFenotipoBase):
	id: int
	class Config:
		from_attributes = True

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
	# ...existing code...
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
	# ...existing code...
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
	# ...existing code...
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
	# ...existing code...
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
	# ...existing code...
	class Config:
		from_attributes = True

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
	# ...existing code...
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
	# ...existing code...
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
	# ...existing code...
	class Config:
		from_attributes = True

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
	# ...existing code...
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
	# ...existing code...
	class Config:
		from_attributes = True

# =================== TRAZABILIDAD ===================
class OrigenMuestraBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None

class OrigenMuestraCreate(OrigenMuestraBase):
	pass

class OrigenMuestra(OrigenMuestraBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	# ...existing code...
	class Config:
		from_attributes = True
