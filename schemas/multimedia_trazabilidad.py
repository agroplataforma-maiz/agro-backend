from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class MultimediaCrear(BaseModel):
    entidad_tipo: str
    entidad_id: str

    tipo_medio: Literal[
        "foto",
        "video",
        "documento",
        "audio",
        "otro"
    ]

    subtipo: Optional[str] = None
    nombre_archivo: str
    ruta_almacenamiento: str

    formato_archivo_id: Optional[int] = None

    descripcion: Optional[str] = None
    peso_kb: Optional[int] = None
    resolucion: Optional[str] = None

    fecha_captura: Optional[datetime] = None

    uuid_envio: Optional[str] = None
    fuente_id: Optional[int] = None
