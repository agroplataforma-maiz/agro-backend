from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class MultimediaCulturalCrear(BaseModel):
    entidad_tipo: Literal[
        "saber_tradicional",
        "ritual_agricola",
        "narrativa_oral",
        "gastronomia_tradicional",
        "nombre_lengua_originaria",
        "identidad_cultural",
        "transmision_conocimiento",
        "sesion_entrevista"
    ]

    entidad_id: int

    tipo_medio: Literal[
        "foto",
        "audio",
        "video"
    ]

    nombre_archivo: str

    campo_origen: Optional[str] = None
    descripcion: Optional[str] = None

    consentimiento_verificado: bool = False

    productor_id: Optional[int] = None
    duracion_seg: Optional[int] = None

    resolucion: Optional[str] = None
    peso_kb: Optional[int] = None
    formato: Optional[str] = None

    uuid_envio: Optional[str] = None

    fecha_captura: Optional[datetime] = None
