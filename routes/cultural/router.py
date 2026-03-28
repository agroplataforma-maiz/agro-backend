from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from database import get_db

from models.cultural import TipoRitualAgricola, TipoNarrativaOral, CategoriaSaberAgricola, Ocasion, MecanismoTransmision, VinculoMaiz

import schemas.cultural as schemes

router = APIRouter()

# =================== TIPO RITUAL AGRICOLA ===================
@router.get("/tipo_ritual_agricola", response_model=list[schemes.TipoRitualAgricola])
def listar_tipo_ritual_agricola(db: Session = Depends(get_db)):
    return db.query(TipoRitualAgricola).all()

@router.get("/tipo_ritual_agricola/{ritual_id}", response_model=schemes.TipoRitualAgricola)
def obtener_tipo_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    ritual = db.query(TipoRitualAgricola).filter(TipoRitualAgricola.id == ritual_id).first()
    if not ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    return ritual

@router.post("/tipo_ritual_agricola", response_model=schemes.TipoRitualAgricola)
def crear_tipo_ritual_agricola(ritual: schemes.TipoRitualAgricolaCreate, db: Session = Depends(get_db)):
    db_ritual = TipoRitualAgricola(**ritual.dict())
    db.add(db_ritual)
    db.commit()
    db.refresh(db_ritual)
    return db_ritual

@router.put("/tipo_ritual_agricola/{ritual_id}", response_model=schemes.TipoRitualAgricola)
def actualizar_tipo_ritual_agricola(ritual_id: int, ritual: schemes.TipoRitualAgricolaCreate, db: Session = Depends(get_db)):
    db_ritual = db.query(TipoRitualAgricola).filter(TipoRitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    for key, value in ritual.dict().items():
        setattr(db_ritual, key, value)
    db.commit()
    db.refresh(db_ritual)
    return db_ritual

@router.delete("/tipo_ritual_agricola/{ritual_id}")
def eliminar_tipo_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    db_ritual = db.query(TipoRitualAgricola).filter(TipoRitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    db.delete(db_ritual)
    db.commit()
    return {"ok": True}


# =================== TIPO NARRATIVA ORAL ===================
@router.get("/tipo_narrativa_oral", response_model=list[schemes.TipoNarrativaOral])
def listar_tipo_narrativa_oral(db: Session = Depends(get_db)):
    return db.query(TipoNarrativaOral).all()

@router.get("/tipo_narrativa_oral/{narrativa_id}", response_model=schemes.TipoNarrativaOral)
def obtener_tipo_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    narrativa = db.query(TipoNarrativaOral).filter(TipoNarrativaOral.id == narrativa_id).first()
    if not narrativa:
        raise HTTPException(status_code=404, detail="Tipo de narrativa oral no encontrado")
    return narrativa

@router.post("/tipo_narrativa_oral", response_model=schemes.TipoNarrativaOral)
def crear_tipo_narrativa_oral(narrativa: schemes.TipoNarrativaOralCreate, db: Session = Depends(get_db)):
    db_narrativa = TipoNarrativaOral(**narrativa.dict())
    db.add(db_narrativa)
    db.commit()
    db.refresh(db_narrativa)
    return db_narrativa

@router.put("/tipo_narrativa_oral/{narrativa_id}", response_model=schemes.TipoNarrativaOral)
def actualizar_tipo_narrativa_oral(narrativa_id: int, narrativa: schemes.TipoNarrativaOralCreate, db: Session = Depends(get_db)):
    db_narrativa = db.query(TipoNarrativaOral).filter(TipoNarrativaOral.id == narrativa_id).first()
    if not db_narrativa:
        raise HTTPException(status_code=404, detail="Tipo de narrativa oral no encontrado")
    for key, value in narrativa.dict().items():
        setattr(db_narrativa, key, value)
    db.commit()
    db.refresh(db_narrativa)
    return db_narrativa

@router.delete("/tipo_narrativa_oral/{narrativa_id}")
def eliminar_tipo_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    db_narrativa = db.query(TipoNarrativaOral).filter(TipoNarrativaOral.id == narrativa_id).first()
    if not db_narrativa:
        raise HTTPException(status_code=404, detail="Tipo de narrativa oral no encontrado")
    db.delete(db_narrativa)
    db.commit()
    return {"ok": True}

# =================== SABER AGRICOLA ===================
@router.get("/categoria_saber_agricola", response_model=list[schemes.CategoriaSaberAgricola])
def listar_categoria_saber_agricola(db: Session = Depends(get_db)):
    return db.query(CategoriaSaberAgricola).all()

@router.get("/categoria_saber_agricola/{categoria_id}", response_model=schemes.CategoriaSaberAgricola)
def obtener_categoria_saber_agricola(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(CategoriaSaberAgricola).filter(CategoriaSaberAgricola.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría de saber agrícola no encontrada")
    return categoria

@router.post("/categoria_saber_agricola", response_model=schemes.CategoriaSaberAgricola)
def crear_categoria_saber_agricola(categoria: schemes.CategoriaSaberAgricolaCreate, db: Session = Depends(get_db)):
    db_categoria = CategoriaSaberAgricola(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.put("/categoria_saber_agricola/{categoria_id}", response_model=schemes.CategoriaSaberAgricola)
def actualizar_categoria_saber_agricola(categoria_id: int, categoria: schemes.CategoriaSaberAgricolaCreate, db: Session = Depends(get_db)):
    db_categoria = db.query(CategoriaSaberAgricola).filter(CategoriaSaberAgricola.id == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría de saber agrícola no encontrada")
    for key, value in categoria.dict().items():
        setattr(db_categoria, key, value)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.delete("/categoria_saber_agricola/{categoria_id}")
def eliminar_categoria_saber_agricola(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = db.query(CategoriaSaberAgricola).filter(CategoriaSaberAgricola.id == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría de saber agrícola no encontrada")
    db.delete(db_categoria)
    db.commit()
    return {"ok": True}

# =================== OCASION ===================
@router.get("/ocasion", response_model=list[schemes.Ocasion])
def listar_ocasion(db: Session = Depends(get_db)):
    return db.query(Ocasion).all()

@router.get("/ocasion/{ocasion_id}", response_model=schemes.Ocasion)
def obtener_ocasion(ocasion_id: int, db: Session = Depends(get_db)):
    ocasion = db.query(Ocasion).filter(Ocasion.id == ocasion_id).first()
    if not ocasion:
        raise HTTPException(status_code=404, detail="Ocasión no encontrada")
    return ocasion

@router.post("/ocasion", response_model=schemes.Ocasion)
def crear_ocasion(ocasion: schemes.OcasionCreate, db: Session = Depends(get_db)):
    db_ocasion = Ocasion(**ocasion.dict())
    db.add(db_ocasion)
    db.commit()
    db.refresh(db_ocasion)
    return db_ocasion

@router.put("/ocasion/{ocasion_id}", response_model=schemes.Ocasion)
def actualizar_ocasion(ocasion_id: int, ocasion: schemes.OcasionCreate, db: Session = Depends(get_db)):
    db_ocasion = db.query(Ocasion).filter(Ocasion.id == ocasion_id).first()
    if not db_ocasion:
        raise HTTPException(status_code=404, detail="Ocasión no encontrada")
    for key, value in ocasion.dict().items():
        setattr(db_ocasion, key, value)
    db.commit()
    db.refresh(db_ocasion)
    return db_ocasion

@router.delete("/ocasion/{ocasion_id}")
def eliminar_ocasion(ocasion_id: int, db: Session = Depends(get_db)):
    db_ocasion = db.query(Ocasion).filter(Ocasion.id == ocasion_id).first()
    if not db_ocasion:
        raise HTTPException(status_code=404, detail="Ocasión no encontrada")
    db.delete(db_ocasion)
    db.commit()
    return {"ok": True}

# =================== MECANISMO TRANSMISION ===================
@router.get("/mecanismo_transmision", response_model=list[schemes.MecanismoTransmision])
def listar_mecanismo_transmision(db: Session = Depends(get_db)):
    return db.query(MecanismoTransmision).all()

@router.get("/mecanismo_transmision/{mecanismo_id}", response_model=schemes.MecanismoTransmision)
def obtener_mecanismo_transmision(mecanismo_id: int, db: Session = Depends(get_db)):
    mecanismo = db.query(MecanismoTransmision).filter(MecanismoTransmision.id == mecanismo_id).first()
    if not mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    return mecanismo

@router.post("/mecanismo_transmision", response_model=schemes.MecanismoTransmision)
def crear_mecanismo_transmision(mecanismo: schemes.MecanismoTransmisionCreate, db: Session = Depends(get_db)):
    db_mecanismo = MecanismoTransmision(**mecanismo.dict())
    db.add(db_mecanismo)
    db.commit()
    db.refresh(db_mecanismo)
    return db_mecanismo

@router.put("/mecanismo_transmision/{mecanismo_id}", response_model=schemes.MecanismoTransmision)
def actualizar_mecanismo_transmision(mecanismo_id: int, mecanismo: schemes.MecanismoTransmisionCreate, db: Session = Depends(get_db)):
    db_mecanismo = db.query(MecanismoTransmision).filter(MecanismoTransmision.id == mecanismo_id).first()
    if not db_mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    for key, value in mecanismo.dict().items():
        setattr(db_mecanismo, key, value)
    db.commit()
    db.refresh(db_mecanismo)
    return db_mecanismo

@router.delete("/mecanismo_transmision/{mecanismo_id}")
def eliminar_mecanismo_transmision(mecanismo_id: int, db: Session = Depends(get_db)):
    db_mecanismo = db.query(MecanismoTransmision).filter(MecanismoTransmision.id == mecanismo_id).first()
    if not db_mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    db.delete(db_mecanismo)
    db.commit()
    return {"ok": True}

# =================== VINCULO MAIZ ===================
@router.get("/vinculo_maiz", response_model=list[schemes.VinculoMaiz])
def listar_vinculo_maiz(db: Session = Depends(get_db)):
    return db.query(VinculoMaiz).all()

@router.get("/vinculo_maiz/{vinculo_id}", response_model=schemes.VinculoMaiz)
def obtener_vinculo_maiz(vinculo_id: int, db: Session = Depends(get_db)):
    vinculo = db.query(VinculoMaiz).filter(VinculoMaiz.id == vinculo_id).first()
    if not vinculo:
        raise HTTPException(status_code=404, detail="Vínculo con el maíz no encontrado")
    return vinculo

@router.post("/vinculo_maiz", response_model=schemes.VinculoMaiz)
def crear_vinculo_maiz(vinculo: schemes.VinculoMaizCreate, db: Session = Depends(get_db)):
    db_vinculo = VinculoMaiz(**vinculo.dict())
    db.add(db_vinculo)
    db.commit()
    db.refresh(db_vinculo)
    return db_vinculo

@router.put("/vinculo_maiz/{vinculo_id}", response_model=schemes.VinculoMaiz)
def actualizar_vinculo_maiz(vinculo_id: int, vinculo: schemes.VinculoMaizCreate, db: Session = Depends(get_db)):
    db_vinculo = db.query(VinculoMaiz).filter(VinculoMaiz.id == vinculo_id).first()
    if not db_vinculo:
        raise HTTPException(status_code=404, detail="Vínculo con el maíz no encontrado")
    for key, value in vinculo.dict().items():
        setattr(db_vinculo, key, value)
    db.commit()
    db.refresh(db_vinculo)
    return db_vinculo

@router.delete("/vinculo_maiz/{vinculo_id}")
def eliminar_vinculo_maiz(vinculo_id: int, db: Session = Depends(get_db)):
    db_vinculo = db.query(VinculoMaiz).filter(VinculoMaiz.id == vinculo_id).first()
    if not db_vinculo:
        raise HTTPException(status_code=404, detail="Vínculo con el maíz no encontrado")
    db.delete(db_vinculo)
    db.commit()
    return {"ok": True}