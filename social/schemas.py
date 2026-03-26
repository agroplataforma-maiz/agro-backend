
from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Utilidad para Config de Pydantic v2
class Config:
    from_attributes = True


# --- PRODUCTOR ---
class ProductorBase(BaseModel):
    nombres: str
    apellido_paterno: Optional[str]
    apellido_materno: Optional[str]
    fecha_nacimiento: Optional[date]
    genero: Optional[str]
    estado_civil: Optional[str]
    anios_experiencia: Optional[int]
    fecha_registro: Optional[date]
    comunidad_id: Optional[int]

class ProductorCreate(ProductorBase):
    pass

class ProductorUpdate(ProductorBase):
    pass

class ProductorOut(ProductorBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    
    class Config:
        from_attributes = True


# --- CONSENTIMIENTO ---
class ConsentimientoBase(BaseModel):
    productor_id: int
    fecha: Optional[date]
    tipo: Optional[str]
    autoriza_foto: Optional[bool]
    autoriza_datos: Optional[bool]
    autoriza_publicacion: Optional[bool]
    observaciones: Optional[str]
    registrado_por: Optional[str]

class ConsentimientoCreate(ConsentimientoBase):
    pass

class ConsentimientoUpdate(ConsentimientoBase):
    pass

class ConsentimientoOut(ConsentimientoBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- PERFIL SOCIOECONOMICO ---
class PerfilSocioeconomicoBase(BaseModel):
    productor_id: int
    escolaridad: Optional[str]
    escolaridad_otra: Optional[str]
    superficie_total_ha: Optional[float]
    superficie_maiz_ha: Optional[float]
    otros_cultivos: Optional[str]
    decision_siembra: Optional[str]
    peso_kg: Optional[float]
    talla_cm: Optional[float]
    imc: Optional[float]
    pct_grasa: Optional[float]
    circunferencia_cintura_cm: Optional[float]
    circunferencia_cadera_cm: Optional[float]
    circunferencia_pantorrilla_cm: Optional[float]
    diagnostico_enfermedad: Optional[str]
    fecha_registro: Optional[date]

class PerfilSocioeconomicoCreate(PerfilSocioeconomicoBase):
    pass

class PerfilSocioeconomicoUpdate(PerfilSocioeconomicoBase):
    pass

class PerfilSocioeconomicoOut(PerfilSocioeconomicoBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- SEGURIDAD ALIMENTARIA ---
class SeguridadAlimentariaBase(BaseModel):
    productor_id: int
    num_personas_hogar: Optional[int]
    num_hombres_adultos: Optional[int]
    num_mujeres_adultas: Optional[int]
    num_ninos: Optional[int]
    num_ninas: Optional[int]
    gasto_semanal_maiz: Optional[float]
    gasto_semanal_frijol: Optional[float]
    produce_suficiente_maiz: Optional[str]
    alimentacion_variada: Optional[bool]
    alimentacion_variada_razon: Optional[str]
    freq_tortilla: Optional[str]
    freq_tamales: Optional[str]
    freq_atole: Optional[str]
    freq_pozole: Optional[str]
    otros_alimentos: Optional[str]
    elcsa_preocupacion: Optional[int]
    elcsa_poca_variedad: Optional[int]
    elcsa_salto_comida: Optional[int]
    elcsa_comio_menos: Optional[int]
    elcsa_sintio_hambre: Optional[int]
    elcsa_dejo_comer_dia: Optional[int]
    elcsa_puntaje_total: Optional[int]
    nivel_inseguridad: Optional[str]
    fecha_evaluacion: Optional[date]

class SeguridadAlimentariaCreate(SeguridadAlimentariaBase):
    pass

class SeguridadAlimentariaUpdate(SeguridadAlimentariaBase):
    pass

class SeguridadAlimentariaOut(SeguridadAlimentariaBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True


# --- RED INTERCAMBIO ---
class RedIntercambioBase(BaseModel):
    productor_id: int
    frecuencia_intercambio_semilla: Optional[str]
    participa_ferias_semillas: Optional[bool]
    ferias_descripcion: Optional[str]
    decision_cultivos: Optional[str]
    servicio_agua_entubada: Optional[bool]
    servicio_electricidad: Optional[bool]
    servicio_internet: Optional[bool]
    servicio_drenaje: Optional[bool]
    tiene_telefono_movil: Optional[bool]
    tiene_radio: Optional[bool]
    recibio_capacitacion: Optional[bool]
    capacitacion_fuente: Optional[str]

class RedIntercambioCreate(RedIntercambioBase):
    pass

class RedIntercambioUpdate(RedIntercambioBase):
    pass

class RedIntercambioOut(RedIntercambioBase):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        from_attributes = True

# --- PRODUCTOR PRACTICA ---
class ProductorPracticaBase(BaseModel):
    productor_id: int
    practica_id: int

class ProductorPracticaCreate(ProductorPracticaBase):
    pass

class ProductorPracticaUpdate(ProductorPracticaBase):
    pass

class ProductorPracticaOut(ProductorPracticaBase):
    class Config:
        from_attributes = True

# --- PRODUCTOR LENGUA ---
class ProductorLenguaBase(BaseModel):
    productor_id: int
    lengua_id: int
    es_materna: Optional[bool]

class ProductorLenguaCreate(ProductorLenguaBase):
    pass

class ProductorLenguaUpdate(ProductorLenguaBase):
    pass

class ProductorLenguaOut(ProductorLenguaBase):
    class Config:
        from_attributes = True

# --- VULNERABILIDAD CLIMATICA ---
class VulnerabilidadClimaticaBase(BaseModel):
    # Agrega aquí los campos según el modelo
    pass

class VulnerabilidadClimaticaCreate(VulnerabilidadClimaticaBase):
    pass

class VulnerabilidadClimaticaUpdate(VulnerabilidadClimaticaBase):
    pass

class VulnerabilidadClimaticaOut(VulnerabilidadClimaticaBase):
    class Config:
        from_attributes = True

# --- GEOLOCALIZACION PRODUCTOR ---
class GeolocalizacionProductorBase(BaseModel):
    # Agrega aquí los campos según el modelo
    pass

class GeolocalizacionProductorCreate(GeolocalizacionProductorBase):
    pass

class GeolocalizacionProductorUpdate(GeolocalizacionProductorBase):
    pass

class GeolocalizacionProductorOut(GeolocalizacionProductorBase):
    class Config:
        from_attributes = True

# --- CULTURALES ---
# --- SABER TRADICIONAL ---
class SaberTradicionalBase(BaseModel):
    productor_id: int
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
    productor_id: int
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
