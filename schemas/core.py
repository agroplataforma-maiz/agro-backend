from uuid import UUID

from pydantic import BaseModel, Field


class OrganizacionCrear(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=200)
    descripcion: str | None = None


class OrganizacionRespuesta(BaseModel):
    id: UUID
    nombre: str
    descripcion: str | None = None
    activo: bool

    class Config:
        from_attributes = True


class OrganizacionMiembroCrear(BaseModel):
    usuario_id: UUID


class OrganizacionMiembroRespuesta(BaseModel):
    id: UUID
    organizacion_id: UUID
    usuario_id: UUID
    activo: bool

    class Config:
        from_attributes = True