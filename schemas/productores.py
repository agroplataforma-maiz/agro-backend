from datetime import date, datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

class GeneroProductor(str, Enum):
    masculino = "masculino"
    femenino = "femenino"
    no_binario = "no_binario"
    prefiere_no_decir = "prefiere_no_decir"


class EstadoCivilProductor(str, Enum):
    soltero = "soltero"
    casado = "casado"
    union_libre = "union_libre"
    divorciado = "divorciado"
    viudo = "viudo"
    otro = "otro"


class ProductorCrear(BaseModel):
    nombres: str

    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None

    fecha_nacimiento: Optional[date] = None

    genero: Optional[GeneroProductor] = None
    estado_civil: Optional[EstadoCivilProductor] = None

    anios_experiencia: Optional[int] = None
    telefono: Optional[str] = None
    correo_electronico: Optional[EmailStr] = None

    tipo_productor_id: Optional[int] = None
    comunidad_id: Optional[UUID] = None
    municipio_id: Optional[int] = None
    localidad_id: Optional[int] = None
    ubicacion_id: Optional[UUID] = None

    # Cuenta de usuario existente que se desea vincular
    user_id: Optional[UUID] = None
    
    username: Optional[str] = None
    password: Optional[str] = None


class ProductorRespuesta(BaseModel):
    id: UUID
    nombres: str

    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    telefono: Optional[str] = None
    correo_electronico: Optional[str] = None

    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class ProductorVisualizadorActualizar(BaseModel):
    """
    Datos que faltan para convertir un usuario visualizador
    en productor.

    Los datos existentes del usuario se conservan automáticamente.
    """

    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero: Optional[GeneroProductor] = None
    estado_civil: Optional[EstadoCivilProductor] = None
    anios_experiencia: Optional[int] = None
    telefono: Optional[str] = None
    tipo_productor_id: Optional[int] = None
    comunidad_id: Optional[UUID] = None
    municipio_id: Optional[int] = None
    localidad_id: Optional[int] = None
    ubicacion_id: Optional[UUID] = None    

    