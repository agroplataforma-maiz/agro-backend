from datetime import datetime
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class MultimediaParcelaCrear(BaseModel):
    parcela_id: UUID
    ubicacion_id: Optional[UUID] = None

    tipo_medio: Literal[
        "foto",
        "video"
    ]

    subtipo: Optional[
        Literal[
            "parcela_general",
            "entorno_colindancias",
            "suelo",
            "cultivo",
            "amenaza",
            "otro"
        ]
    ] = None

    nombre_archivo: str

    campo_origen: Optional[str] = None
    descripcion: Optional[str] = None

    peso_kb: Optional[int] = None
    resolucion: Optional[str] = None
    formato: Optional[str] = None

    uuid_envio: Optional[str] = None

    fuente_informacion_id: Optional[int] = None

    fecha_captura: Optional[datetime] = None
