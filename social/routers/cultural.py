from sqlalchemy.orm import Session

def get_saber_tradicional(db: Session, saber_id: int):
    return db.query(SaberTradicional).filter(SaberTradicional.id == saber_id).first()

def create_saber_tradicional(db: Session, saber_data):
    saber = SaberTradicional(**saber_data.dict())
    db.add(saber)
    db.commit()
    db.refresh(saber)
    return saber

def update_saber_tradicional(db: Session, saber_id: int, saber_data):
    saber = db.query(SaberTradicional).filter(SaberTradicional.id == saber_id).first()
    if saber:
        for key, value in saber_data.dict(exclude_unset=True).items():
            setattr(saber, key, value)
        db.commit()
        db.refresh(saber)
    return saber

def delete_saber_tradicional(db: Session, saber_id: int):
    saber = db.query(SaberTradicional).filter(SaberTradicional.id == saber_id).first()
    if saber:
        db.delete(saber)
        db.commit()
        return True
    return False
def get_saberes_tradicionales(db: Session):
    return db.query(SaberTradicional).all()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SaberTradicional, RitualAgricola, NarrativaOral, GastronomiaTradicional, TransmisionConocimiento, IdentidadCultural, NombreLenguaOriginaria
from schemas import (
    SaberTradicionalCreate, SaberTradicionalUpdate, SaberTradicionalOut,
    RitualAgricolaCreate, RitualAgricolaUpdate, RitualAgricolaOut,
    NarrativaOralCreate, NarrativaOralUpdate, NarrativaOralOut,
    GastronomiaTradicionalCreate, GastronomiaTradicionalUpdate, GastronomiaTradicionalOut,
    TransmisionConocimientoCreate, TransmisionConocimientoUpdate, TransmisionConocimientoOut,
    IdentidadCulturalCreate, IdentidadCulturalUpdate, IdentidadCulturalOut,
    NombreLenguaOriginariaCreate, NombreLenguaOriginariaUpdate, NombreLenguaOriginariaOut
)
from db import get_db

router = APIRouter(prefix="/cultural", tags=["cultural"])

# SaberTradicional
@router.get("/saberes_tradicionales", response_model=list[SaberTradicionalOut])
def listar_saberes_tradicionales(db: Session = Depends(get_db)):
    return get_saberes_tradicionales(db)

@router.get("/saberes_tradicionales/{saber_id}", response_model=SaberTradicionalOut)
def obtener_saber_tradicional(saber_id: int, db: Session = Depends(get_db)):
    saber = get_saber_tradicional(db, saber_id)
    if not saber:
        raise HTTPException(status_code=404, detail="Saber tradicional no encontrado")
    return saber

@router.post("/saberes_tradicionales", response_model=SaberTradicionalOut)
def crear_saber_tradicional(saber: SaberTradicionalCreate, db: Session = Depends(get_db)):
    return create_saber_tradicional(db, saber)

@router.put("/saberes_tradicionales/{saber_id}", response_model=SaberTradicionalOut)
def actualizar_saber_tradicional(saber_id: int, saber: SaberTradicionalUpdate, db: Session = Depends(get_db)):
    actualizado = update_saber_tradicional(db, saber_id, saber)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Saber tradicional no encontrado")
    return actualizado

@router.delete("/saberes_tradicionales/{saber_id}")
def eliminar_saber_tradicional(saber_id: int, db: Session = Depends(get_db)):
    eliminado = delete_saber_tradicional(db, saber_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Saber tradicional no encontrado")
    return {"ok": True}

# RitualAgricola
@router.get("/rituales_agricolas", response_model=list[RitualAgricolaOut])
def listar_rituales_agricolas(db: Session = Depends(get_db)):
    return get_rituales_agricolas(db)

@router.get("/rituales_agricolas/{ritual_id}", response_model=RitualAgricolaOut)
def obtener_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    ritual = get_ritual_agricola(db, ritual_id)
    if not ritual:
        raise HTTPException(status_code=404, detail="Ritual agrícola no encontrado")
    return ritual

@router.post("/rituales_agricolas", response_model=RitualAgricolaOut)
def crear_ritual_agricola(ritual: RitualAgricolaCreate, db: Session = Depends(get_db)):
    return create_ritual_agricola(db, ritual)

@router.put("/rituales_agricolas/{ritual_id}", response_model=RitualAgricolaOut)
def actualizar_ritual_agricola(ritual_id: int, ritual: RitualAgricolaUpdate, db: Session = Depends(get_db)):
    actualizado = update_ritual_agricola(db, ritual_id, ritual)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Ritual agrícola no encontrado")
    return actualizado

@router.delete("/rituales_agricolas/{ritual_id}")
def eliminar_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    eliminado = delete_ritual_agricola(db, ritual_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Ritual agrícola no encontrado")
    return {"ok": True}

# NarrativaOral
@router.get("/narrativas_orales", response_model=list[NarrativaOralOut])
def listar_narrativas_orales(db: Session = Depends(get_db)):
    return get_narrativas_orales(db)

@router.get("/narrativas_orales/{narrativa_id}", response_model=NarrativaOralOut)
def obtener_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    narrativa = get_narrativa_oral(db, narrativa_id)
    if not narrativa:
        raise HTTPException(status_code=404, detail="Narrativa oral no encontrada")
    return narrativa

@router.post("/narrativas_orales", response_model=NarrativaOralOut)
def crear_narrativa_oral(narrativa: NarrativaOralCreate, db: Session = Depends(get_db)):
    return create_narrativa_oral(db, narrativa)

@router.put("/narrativas_orales/{narrativa_id}", response_model=NarrativaOralOut)
def actualizar_narrativa_oral(narrativa_id: int, narrativa: NarrativaOralUpdate, db: Session = Depends(get_db)):
    actualizado = update_narrativa_oral(db, narrativa_id, narrativa)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Narrativa oral no encontrada")
    return actualizado

@router.delete("/narrativas_orales/{narrativa_id}")
def eliminar_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    eliminado = delete_narrativa_oral(db, narrativa_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Narrativa oral no encontrada")
    return {"ok": True}

# GastronomiaTradicional
@router.get("/gastronomias_tradicionales", response_model=list[GastronomiaTradicionalOut])
def listar_gastronomias_tradicionales(db: Session = Depends(get_db)):
    return get_gastronomias_tradicionales(db)

@router.get("/gastronomias_tradicionales/{gastronomia_id}", response_model=GastronomiaTradicionalOut)
def obtener_gastronomia_tradicional(gastronomia_id: int, db: Session = Depends(get_db)):
    gastronomia = get_gastronomia_tradicional(db, gastronomia_id)
    if not gastronomia:
        raise HTTPException(status_code=404, detail="Gastronomía tradicional no encontrada")
    return gastronomia

@router.post("/gastronomias_tradicionales", response_model=GastronomiaTradicionalOut)
def crear_gastronomia_tradicional(gastronomia: GastronomiaTradicionalCreate, db: Session = Depends(get_db)):
    return create_gastronomia_tradicional(db, gastronomia)

@router.put("/gastronomias_tradicionales/{gastronomia_id}", response_model=GastronomiaTradicionalOut)
def actualizar_gastronomia_tradicional(gastronomia_id: int, gastronomia: GastronomiaTradicionalUpdate, db: Session = Depends(get_db)):
    actualizado = update_gastronomia_tradicional(db, gastronomia_id, gastronomia)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Gastronomía tradicional no encontrada")
    return actualizado

@router.delete("/gastronomias_tradicionales/{gastronomia_id}")
def eliminar_gastronomia_tradicional(gastronomia_id: int, db: Session = Depends(get_db)):
    eliminado = delete_gastronomia_tradicional(db, gastronomia_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Gastronomía tradicional no encontrada")
    return {"ok": True}

# TransmisionConocimiento
@router.get("/transmisiones_conocimiento", response_model=list[TransmisionConocimientoOut])
def listar_transmisiones_conocimiento(db: Session = Depends(get_db)):
    return get_transmisiones_conocimiento(db)

@router.get("/transmisiones_conocimiento/{transmision_id}", response_model=TransmisionConocimientoOut)
def obtener_transmision_conocimiento(transmision_id: int, db: Session = Depends(get_db)):
    transmision = get_transmision_conocimiento(db, transmision_id)
    if not transmision:
        raise HTTPException(status_code=404, detail="Transmisión de conocimiento no encontrada")
    return transmision

@router.post("/transmisiones_conocimiento", response_model=TransmisionConocimientoOut)
def crear_transmision_conocimiento(transmision: TransmisionConocimientoCreate, db: Session = Depends(get_db)):
    return create_transmision_conocimiento(db, transmision)

@router.put("/transmisiones_conocimiento/{transmision_id}", response_model=TransmisionConocimientoOut)
def actualizar_transmision_conocimiento(transmision_id: int, transmision: TransmisionConocimientoUpdate, db: Session = Depends(get_db)):
    actualizado = update_transmision_conocimiento(db, transmision_id, transmision)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Transmisión de conocimiento no encontrada")
    return actualizado

@router.delete("/transmisiones_conocimiento/{transmision_id}")
def eliminar_transmision_conocimiento(transmision_id: int, db: Session = Depends(get_db)):
    eliminado = delete_transmision_conocimiento(db, transmision_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Transmisión de conocimiento no encontrada")
    return {"ok": True}

# IdentidadCultural
@router.get("/identidades_culturales", response_model=list[IdentidadCulturalOut])
def listar_identidades_culturales(db: Session = Depends(get_db)):
    return get_identidades_culturales(db)

@router.get("/identidades_culturales/{identidad_id}", response_model=IdentidadCulturalOut)
def obtener_identidad_cultural(identidad_id: int, db: Session = Depends(get_db)):
    identidad = get_identidad_cultural(db, identidad_id)
    if not identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    return identidad

@router.post("/identidades_culturales", response_model=IdentidadCulturalOut)
def crear_identidad_cultural(identidad: IdentidadCulturalCreate, db: Session = Depends(get_db)):
    return create_identidad_cultural(db, identidad)

@router.put("/identidades_culturales/{identidad_id}", response_model=IdentidadCulturalOut)
def actualizar_identidad_cultural(identidad_id: int, identidad: IdentidadCulturalUpdate, db: Session = Depends(get_db)):
    actualizado = update_identidad_cultural(db, identidad_id, identidad)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    return actualizado

@router.delete("/identidades_culturales/{identidad_id}")
def eliminar_identidad_cultural(identidad_id: int, db: Session = Depends(get_db)):
    eliminado = delete_identidad_cultural(db, identidad_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    return {"ok": True}

# NombreLenguaOriginaria
@router.get("/nombres_lenguas_originarias", response_model=list[NombreLenguaOriginariaOut])
def listar_nombres_lenguas_originarias(db: Session = Depends(get_db)):
    return get_nombres_lenguas_originarias(db)

@router.get("/nombres_lenguas_originarias/{nombre_id}", response_model=NombreLenguaOriginariaOut)
def obtener_nombre_lengua_originaria(nombre_id: int, db: Session = Depends(get_db)):
    nombre = get_nombre_lengua_originaria(db, nombre_id)
    if not nombre:
        raise HTTPException(status_code=404, detail="Nombre de lengua originaria no encontrado")
    return nombre

@router.post("/nombres_lenguas_originarias", response_model=NombreLenguaOriginariaOut)
def crear_nombre_lengua_originaria(nombre: NombreLenguaOriginariaCreate, db: Session = Depends(get_db)):
    return create_nombre_lengua_originaria(db, nombre)

@router.put("/nombres_lenguas_originarias/{nombre_id}", response_model=NombreLenguaOriginariaOut)
def actualizar_nombre_lengua_originaria(nombre_id: int, nombre: NombreLenguaOriginariaUpdate, db: Session = Depends(get_db)):
    actualizado = update_nombre_lengua_originaria(db, nombre_id, nombre)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Nombre de lengua originaria no encontrado")
    return actualizado

@router.delete("/nombres_lenguas_originarias/{nombre_id}")
def eliminar_nombre_lengua_originaria(nombre_id: int, db: Session = Depends(get_db)):
    eliminado = delete_nombre_lengua_originaria(db, nombre_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Nombre de lengua originaria no encontrado")
    return {"ok": True}



def get_rituales_agricolas(db: Session):
    return db.query(RitualAgricola).all()

def get_ritual_agricola(db: Session, ritual_id: int):
    return db.query(RitualAgricola).filter(RitualAgricola.id == ritual_id).first()

def create_ritual_agricola(db: Session, ritual_data):
    ritual = RitualAgricola(**ritual_data.dict())
    db.add(ritual)
    db.commit()
    db.refresh(ritual)
    return ritual

def update_ritual_agricola(db: Session, ritual_id: int, ritual_data):
    ritual = db.query(RitualAgricola).filter(RitualAgricola.id == ritual_id).first()
    if ritual:
        for key, value in ritual_data.dict(exclude_unset=True).items():
            setattr(ritual, key, value)
        db.commit()
        db.refresh(ritual)
    return ritual

def delete_ritual_agricola(db: Session, ritual_id: int):
    ritual = db.query(RitualAgricola).filter(RitualAgricola.id == ritual_id).first()
    if ritual:
        db.delete(ritual)
        db.commit()
        return True
    return False

# CRUD para NarrativaOral
def get_narrativas_orales(db: Session):
    return db.query(NarrativaOral).all()

def get_narrativa_oral(db: Session, narrativa_id: int):
    return db.query(NarrativaOral).filter(NarrativaOral.id == narrativa_id).first()

def create_narrativa_oral(db: Session, narrativa_data):
    narrativa = NarrativaOral(**narrativa_data.dict())
    db.add(narrativa)
    db.commit()
    db.refresh(narrativa)
    return narrativa

def update_narrativa_oral(db: Session, narrativa_id: int, narrativa_data):
    narrativa = db.query(NarrativaOral).filter(NarrativaOral.id == narrativa_id).first()
    if narrativa:
        for key, value in narrativa_data.dict(exclude_unset=True).items():
            setattr(narrativa, key, value)
        db.commit()
        db.refresh(narrativa)
    return narrativa

def delete_narrativa_oral(db: Session, narrativa_id: int):
    narrativa = db.query(NarrativaOral).filter(NarrativaOral.id == narrativa_id).first()
    if narrativa:
        db.delete(narrativa)
        db.commit()
        return True
    return False

# CRUD para GastronomiaTradicional
def get_gastronomias_tradicionales(db: Session):
    return db.query(GastronomiaTradicional).all()

def get_gastronomia_tradicional(db: Session, gastronomia_id: int):
    return db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id == gastronomia_id).first()

def create_gastronomia_tradicional(db: Session, gastronomia_data):
    gastronomia = GastronomiaTradicional(**gastronomia_data.dict())
    db.add(gastronomia)
    db.commit()
    db.refresh(gastronomia)
    return gastronomia

def update_gastronomia_tradicional(db: Session, gastronomia_id: int, gastronomia_data):
    gastronomia = db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id == gastronomia_id).first()
    if gastronomia:
        for key, value in gastronomia_data.dict(exclude_unset=True).items():
            setattr(gastronomia, key, value)
        db.commit()
        db.refresh(gastronomia)
    return gastronomia

def delete_gastronomia_tradicional(db: Session, gastronomia_id: int):
    gastronomia = db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id == gastronomia_id).first()
    if gastronomia:
        db.delete(gastronomia)
        db.commit()
        return True
    return False

# CRUD para TransmisionConocimiento
def get_transmisiones_conocimiento(db: Session):
    return db.query(TransmisionConocimiento).all()

def get_transmision_conocimiento(db: Session, transmision_id: int):
    return db.query(TransmisionConocimiento).filter(TransmisionConocimiento.id == transmision_id).first()

def create_transmision_conocimiento(db: Session, transmision_data):
    transmision = TransmisionConocimiento(**transmision_data.dict())
    db.add(transmision)
    db.commit()
    db.refresh(transmision)
    return transmision

def update_transmision_conocimiento(db: Session, transmision_id: int, transmision_data):
    transmision = db.query(TransmisionConocimiento).filter(TransmisionConocimiento.id == transmision_id).first()
    if transmision:
        for key, value in transmision_data.dict(exclude_unset=True).items():
            setattr(transmision, key, value)
        db.commit()
        db.refresh(transmision)
    return transmision

def delete_transmision_conocimiento(db: Session, transmision_id: int):
    transmision = db.query(TransmisionConocimiento).filter(TransmisionConocimiento.id == transmision_id).first()
    if transmision:
        db.delete(transmision)
        db.commit()
        return True
    return False

# CRUD para IdentidadCultural
def get_identidades_culturales(db: Session):
    return db.query(IdentidadCultural).all()

def get_identidad_cultural(db: Session, identidad_id: int):
    return db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()

def create_identidad_cultural(db: Session, identidad_data):
    identidad = IdentidadCultural(**identidad_data.dict())
    db.add(identidad)
    db.commit()
    db.refresh(identidad)
    return identidad

def update_identidad_cultural(db: Session, identidad_id: int, identidad_data):
    identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if identidad:
        for key, value in identidad_data.dict(exclude_unset=True).items():
            setattr(identidad, key, value)
        db.commit()
        db.refresh(identidad)
    return identidad

def delete_identidad_cultural(db: Session, identidad_id: int):
    identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if identidad:
        db.delete(identidad)
        db.commit()
        return True
    return False

# CRUD para NombreLenguaOriginaria
def get_nombres_lenguas_originarias(db: Session):
    return db.query(NombreLenguaOriginaria).all()

def get_nombre_lengua_originaria(db: Session, nombre_id: int):
    return db.query(NombreLenguaOriginaria).filter(NombreLenguaOriginaria.id == nombre_id).first()

def create_nombre_lengua_originaria(db: Session, nombre_data):
    nombre = NombreLenguaOriginaria(**nombre_data.dict())
    db.add(nombre)
    db.commit()
    db.refresh(nombre)
    return nombre

def update_nombre_lengua_originaria(db: Session, nombre_id: int, nombre_data):
    nombre = db.query(NombreLenguaOriginaria).filter(NombreLenguaOriginaria.id == nombre_id).first()
    if nombre:
        for key, value in nombre_data.dict(exclude_unset=True).items():
            setattr(nombre, key, value)
        db.commit()
        db.refresh(nombre)
    return nombre

def delete_nombre_lengua_originaria(db: Session, nombre_id: int):
    nombre = db.query(NombreLenguaOriginaria).filter(NombreLenguaOriginaria.id == nombre_id).first()
    if nombre:
        db.delete(nombre)
        db.commit()
        return True
    return False
