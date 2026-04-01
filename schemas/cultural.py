from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

# --- CULTURALES ---
# --- SABER TRADICIONAL ---
class SaberTradicionalBase(BaseModel):
    # productor_id eliminado del esquema
    comunidad_id: int
    categoria: Optional[str]
    descripcion: Optional[str]
    descripcion_lengua_orig: Optional[str]
    lengua_id: Optional[int]
    aprendio_de: Optional[str]
    generaciones_estimadas: Optional[int]
    esta_vigente: Optional[bool]
    razon_perdida: Optional[str]
    considera_importante: Optional[bool]
    importancia_descripcion: Optional[str]
    tiene_evidencia_audio: Optional[bool]
    tiene_evidencia_video: Optional[bool]
    tiene_evidencia_foto: Optional[bool]
    ruta_archivo_multimedia: Optional[str]
    fecha_registro: Optional[date]
    registrado_por: Optional[str]

class SaberTradicionalCreate(SaberTradicionalBase):
    pass

class SaberTradicionalUpdate(SaberTradicionalBase):
    pass

class SaberTradicionalOut(SaberTradicionalBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- RITUAL AGRICOLA ---
class RitualAgricolaBase(BaseModel):
    comunidad_id: int
    nombre: str
    nombre_lengua_orig: Optional[str]
    lengua_id: Optional[int]
    tipo: Optional[str]
    mes_aproximado: Optional[int]
    vinculado_ciclo_agricola: Optional[str]
    descripcion: Optional[str]
    descripcion_lengua_orig: Optional[str]
    participantes: Optional[str]
    elementos_utilizados: Optional[str]
    lugar_realizacion: Optional[str]
    frecuencia_actual: Optional[str]
    esta_vigente: Optional[bool]
    razon_perdida: Optional[str]
    esfuerzos_recuperacion: Optional[str]
    tiene_evidencia_audio: Optional[bool]
    tiene_evidencia_video: Optional[bool]
    tiene_evidencia_foto: Optional[bool]
    ruta_archivo_multimedia: Optional[str]
    fecha_registro: Optional[date]
    registrado_por: Optional[str]

class RitualAgricolaCreate(RitualAgricolaBase):
    pass

class RitualAgricolaUpdate(RitualAgricolaBase):
    pass

class RitualAgricolaOut(RitualAgricolaBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- NARRATIVA ORAL ---
class NarrativaOralBase(BaseModel):
    comunidad_id: int
    # productor_id eliminado del esquema
    tipo: Optional[str]
    titulo: Optional[str]
    titulo_lengua_orig: Optional[str]
    lengua_id: Optional[int]
    contenido_resumen: Optional[str]
    contenido_transcripcion: Optional[str]
    contenido_lengua_orig: Optional[str]
    temas_principales: Optional[str]
    vinculo_maiz: Optional[str]
    circunstancia_narracion: Optional[str]
    audiencia_habitual: Optional[str]
    aprendio_de: Optional[str]
    generaciones_estimadas: Optional[int]
    esta_vigente: Optional[bool]
    tiene_audio: Optional[bool]
    tiene_video: Optional[bool]
    ruta_archivo_multimedia: Optional[str]
    fecha_registro: Optional[date]
    registrado_por: Optional[str]

class NarrativaOralCreate(NarrativaOralBase):
    pass

class NarrativaOralUpdate(NarrativaOralBase):
    pass

class NarrativaOralOut(NarrativaOralBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- GASTRONOMIA TRADICIONAL ---
class GastronomiaTradicionalBase(BaseModel):
    comunidad_id: int
    nombre_platillo: str
    nombre_lengua_orig: Optional[str]
    lengua_id: Optional[int]
    # Agrega aquí los campos restantes según el modelo

class GastronomiaTradicionalCreate(GastronomiaTradicionalBase):
    pass

class GastronomiaTradicionalUpdate(GastronomiaTradicionalBase):
    pass

class GastronomiaTradicionalOut(GastronomiaTradicionalBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- TRANSMISION CONOCIMIENTO ---
class TransmisionConocimientoBase(BaseModel):
    # Agrega aquí los campos según el modelo
    pass

class TransmisionConocimientoCreate(TransmisionConocimientoBase):
    pass

class TransmisionConocimientoUpdate(TransmisionConocimientoBase):
    pass

class TransmisionConocimientoOut(TransmisionConocimientoBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- IDENTIDAD CULTURAL ---
class IdentidadCulturalBase(BaseModel):
    # Agrega aquí los campos según el modelo
    pass

class IdentidadCulturalCreate(IdentidadCulturalBase):
    pass

class IdentidadCulturalUpdate(IdentidadCulturalBase):
    pass

class IdentidadCulturalOut(IdentidadCulturalBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- NOMBRE LENGUA ORIGINARIA ---
class NombreLenguaOriginariaBase(BaseModel):
    # Agrega aquí los campos según el modelo
    pass

class NombreLenguaOriginariaCreate(NombreLenguaOriginariaBase):
    pass

class NombreLenguaOriginariaUpdate(NombreLenguaOriginariaBase):
    pass

class NombreLenguaOriginariaOut(NombreLenguaOriginariaBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True

class TipoRitualAgricolaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoRitualAgricolaCreate(TipoRitualAgricolaBase):
	pass
class TipoRitualAgricola(TipoRitualAgricolaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class TipoNarrativaOralBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class TipoNarrativaOralCreate(TipoNarrativaOralBase):
	pass
class TipoNarrativaOral(TipoNarrativaOralBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class CategoriaSaberAgricolaBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class CategoriaSaberAgricolaCreate(CategoriaSaberAgricolaBase):
	pass
class CategoriaSaberAgricola(CategoriaSaberAgricolaBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class OcasionBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class OcasionCreate(OcasionBase):
	pass
class Ocasion(OcasionBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class MecanismoTransmisionBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class MecanismoTransmisionCreate(MecanismoTransmisionBase):
	pass
class MecanismoTransmision(MecanismoTransmisionBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True

class VinculoMaizBase(BaseModel):
	nombre: str
	descripcion: Optional[str] = None
class VinculoMaizCreate(VinculoMaizBase):
	pass
class VinculoMaiz(VinculoMaizBase):
	id: int
	created_at: datetime | None
	updated_at: datetime | None
	class Config:
		from_attributes = True