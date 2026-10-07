from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
from decimal import Decimal
from uuid import UUID

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

class SubmuestraNutrimentalBase(BaseModel):
    numero_submuestra: int = Field(gt=0)

    color_mazorca: Optional[str] = None
    color_olote: Optional[str] = None

    largo_cm: Optional[Decimal] = Field(default=None, ge=0)
    diametro_cm: Optional[Decimal] = Field(default=None, ge=0)
    peso_mazorca_g: Optional[Decimal] = Field(default=None, ge=0)

    numero_hileras: Optional[int] = Field(default=None, gt=0)


class SubmuestraNutrimentalCreate(SubmuestraNutrimentalBase):
    pass


class SubmuestraNutrimentalResponse(SubmuestraNutrimentalBase):
    id: int
    muestra_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class MuestraNutrimentalBase(BaseModel):
    codigo_muestra: str = Field(max_length=30)

    germoplasma_id: UUID
    parcela_id: UUID
    comunidad_id: Optional[UUID] = None

    fecha_colecta: Optional[date] = None

    peso_muestra_g: Optional[Decimal] = Field(default=None, ge=0)
    condicion_muestra: Optional[str] = None
    laboratorio: Optional[str] = None
    fecha_analisis: Optional[date] = None
    notas: Optional[str] = None


class MuestraNutrimentalCreate(MuestraNutrimentalBase):
    submuestras: List[SubmuestraNutrimentalCreate] = Field(
        min_length=1
    )


class MuestraNutrimentalResponse(MuestraNutrimentalBase):
    id: int
    submuestras: List[SubmuestraNutrimentalResponse] = []

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
