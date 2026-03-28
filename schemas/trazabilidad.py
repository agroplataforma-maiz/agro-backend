from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoProductoDronBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoProductoDronCreate(TipoProductoDronBase):
	pass
class TipoProductoDron(TipoProductoDronBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class FormatoArchivoBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class FormatoArchivoCreate(FormatoArchivoBase):
	pass
class FormatoArchivo(FormatoArchivoBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class TipoCapaSIGBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoCapaSIGCreate(TipoCapaSIGBase):
	pass
class TipoCapaSIG(TipoCapaSIGBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class FuenteCapturaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class FuenteCapturaCreate(FuenteCapturaBase):
	pass
class FuenteCaptura(FuenteCapturaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class FuenteInformacionBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
	tipo: Optional[str] = None
class FuenteInformacionCreate(FuenteInformacionBase):
	pass
class FuenteInformacion(FuenteInformacionBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class OrigenSemillaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class OrigenSemillaCreate(OrigenSemillaBase):
	pass
class OrigenSemilla(OrigenSemillaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class OrigenMuestraBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class OrigenMuestraCreate(OrigenMuestraBase):
	pass
class OrigenMuestra(OrigenMuestraBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True