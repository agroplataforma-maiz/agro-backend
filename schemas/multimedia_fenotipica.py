from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class MultimediaFenotipicaCrear(BaseModel):
    evaluacion_id: int

    tipo: Optional[
        Literal[
            "planta",
            "mazorca",
            "parcela",
            "productor",
            "plaga",
            "enfermedad",
            "contexto",
            "dron",
            "satelital"
        ]
    ] = None

    ruta_archivo: str
    nombre_archivo: Optional[str] = None

    campo_origen: Optional[str] = None
    uuid_envio: Optional[str] = None

    subtipo: Optional[
        Literal[
            "planta_completa",
            "mazorca_evaluada",
            "granos_medicion",
            "espiga",
            "plaga_enfermedad",
            "parcela",
            "dron",
            "satelital",
            "otro"
        ]
    ] = None

    fecha_captura: Optional[datetime] = None

    modelo_captura: Optional[str] = None
    resolucion: Optional[str] = None
    notas: Optional[str] = None
