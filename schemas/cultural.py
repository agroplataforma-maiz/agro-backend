from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoRitualAgricolaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoRitualAgricolaCreate(TipoRitualAgricolaBase):
	pass
class TipoRitualAgricola(TipoRitualAgricolaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class TipoNarrativaOralBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoNarrativaOralCreate(TipoNarrativaOralBase):
	pass
class TipoNarrativaOral(TipoNarrativaOralBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class CategoriaSaberAgricolaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class CategoriaSaberAgricolaCreate(CategoriaSaberAgricolaBase):
	pass
class CategoriaSaberAgricola(CategoriaSaberAgricolaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class OcasionBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class OcasionCreate(OcasionBase):
	pass
class Ocasion(OcasionBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class MecanismoTransmisionBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class MecanismoTransmisionCreate(MecanismoTransmisionBase):
	pass
class MecanismoTransmision(MecanismoTransmisionBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class VinculoMaizBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class VinculoMaizCreate(VinculoMaizBase):
	pass
class VinculoMaiz(VinculoMaizBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True