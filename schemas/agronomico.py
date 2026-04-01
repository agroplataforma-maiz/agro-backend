from typing import Dict
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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
	class Config:
		from_attributes = True

class SistemaCultivoBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class SistemaCultivoCreate(SistemaCultivoBase):
	pass
class SistemaCultivo(SistemaCultivoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class MetodoAlmacenamientoBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class MetodoAlmacenamientoCreate(MetodoAlmacenamientoBase):
	pass
class MetodoAlmacenamiento(MetodoAlmacenamientoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

# Esquema para respuesta anidada de tipo_practica en PracticaAgricola
class TipoPracticaNested(BaseModel):
	nombre: str | None = None
	descripcion: str | None = None

class PracticaAgricolaConTipo(BaseModel):
	id: int
	nombre: str
	descripcion: str | None = None
	tipo_practica: TipoPracticaNested

	class Config:
		from_attributes = True