from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoFenotipoBase(BaseModel):
	nombre: str
	unidad: Optional[str] = None
	descripcion: Optional[str] = None
class TipoFenotipoCreate(TipoFenotipoBase):
	pass
class TipoFenotipo(TipoFenotipoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class EtapaFenologicaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class EtapaFenologicaCreate(EtapaFenologicaBase):
	pass
class EtapaFenologica(EtapaFenologicaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True