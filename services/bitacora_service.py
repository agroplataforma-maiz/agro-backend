from typing import Optional
from uuid import UUID

from fastapi import Request
from sqlalchemy.orm import Session

from models.sistema import Bitacora


def registrar_bitacora(
    db: Session,
    accion: str,
    modulo: str,
    usuario_id: Optional[UUID] = None,
    descripcion: Optional[str] = None,
    request: Optional[Request] = None,
    nivel: str = "INFO",
):
    """
    Registra una actividad en sistema.bitacora.
    """

    ip = None
    user_agent = None

    if request is not None:
        if request.client is not None:
            ip = request.client.host

        user_agent = request.headers.get("user-agent")

    registro = Bitacora(
        usuario_id=usuario_id,
        accion=accion,
        modulo=modulo,
        descripcion=descripcion,
        ip=ip,
        user_agent=user_agent,
        nivel=nivel,
    )

    db.add(registro)
    db.commit()
    db.refresh(registro)

    return registro