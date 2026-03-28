from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from database import get_db

from models.social import Lengua, PuebloOriginario, TipoProductor 

import schemas.social as schemes

router = APIRouter()

# =================== TIPO PRODUCTOR ===================
@router.get("/tipo_productor", response_model=list[schemes.TipoProductor])
def listar_tipo_productor(db: Session = Depends(get_db)):
    return db.query(TipoProductor).all()

@router.get("/tipo_productor/{tipo_id}", response_model=schemes.TipoProductor)
def obtener_tipo_productor(tipo_id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoProductor).filter(TipoProductor.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de productor no encontrado")
    return tipo

@router.post("/tipo_productor", response_model=schemes.TipoProductor)
def crear_tipo_productor(tipo: schemes.TipoProductorCreate, db: Session = Depends(get_db)):
    db_tipo = TipoProductor(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.put("/tipo_productor/{tipo_id}", response_model=schemes.TipoProductor)
def actualizar_tipo_productor(tipo_id: int, tipo: schemes.TipoProductorCreate, db: Session = Depends(get_db)):
    db_tipo = db.query(TipoProductor).filter(TipoProductor.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de productor no encontrado")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipo_productor/{tipo_id}")
def eliminar_tipo_productor(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = db.query(TipoProductor).filter(TipoProductor.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de productor no encontrado")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}

# =================== LENGUA ===================
@router.get("/lengua", response_model=list[schemes.Lengua])
def listar_lenguas(db: Session = Depends(get_db)):
    return db.query(Lengua).all()

@router.get("/lengua/{lengua_id}", response_model=schemes.Lengua)
def obtener_lengua(lengua_id: int, db: Session = Depends(get_db)):
    lengua = db.query(Lengua).filter(Lengua.id == lengua_id).first()
    if not lengua:
        raise HTTPException(status_code=404, detail="Lengua no encontrada")
    return lengua

@router.post("/lengua", response_model=schemes.Lengua)
def crear_lengua(lengua: schemes.LenguaCreate, db: Session = Depends(get_db)):
    db_lengua = Lengua(**lengua.dict())
    db.add(db_lengua)
    db.commit()
    db.refresh(db_lengua)
    return db_lengua

@router.put("/lengua/{lengua_id}", response_model=schemes.Lengua)
def actualizar_lengua(lengua_id: int, lengua: schemes.LenguaCreate, db: Session = Depends(get_db)):
    db_lengua = db.query(Lengua).filter(Lengua.id == lengua_id).first()
    if not db_lengua:
        raise HTTPException(status_code=404, detail="Lengua no encontrada")
    for key, value in lengua.dict().items():
        setattr(db_lengua, key, value)
    db.commit()
    db.refresh(db_lengua)
    return db_lengua

@router.delete("/lengua/{lengua_id}")
def eliminar_lengua(lengua_id: int, db: Session = Depends(get_db)):
    db_lengua = db.query(Lengua).filter(Lengua.id == lengua_id).first()
    if not db_lengua:
        raise HTTPException(status_code=404, detail="Lengua no encontrada")
    db.delete(db_lengua)
    db.commit()
    return {"ok": True}

# =================== PUEBLO ORIGINARIO ===================
@router.get("/pueblo_originario", response_model=list[schemes.PuebloOriginario])
def listar_pueblos_originarios(db: Session = Depends(get_db)):
    return db.query(PuebloOriginario).all()

@router.get("/pueblo_originario/{pueblo_id}", response_model=schemes.PuebloOriginario)
def obtener_pueblo_originario(pueblo_id: int, db: Session = Depends(get_db)):
    pueblo = db.query(PuebloOriginario).filter(PuebloOriginario.id == pueblo_id).first()
    if not pueblo:
        raise HTTPException(status_code=404, detail="Pueblo originario no encontrado")
    return pueblo

@router.post("/pueblo_originario", response_model=schemes.PuebloOriginario)
def crear_pueblo_originario(pueblo: schemes.PuebloOriginarioCreate, db: Session = Depends(get_db)):
    db_pueblo = PuebloOriginario(**pueblo.dict())
    db.add(db_pueblo)
    db.commit()
    db.refresh(db_pueblo)
    return db_pueblo

@router.put("/pueblo_originario/{pueblo_id}", response_model=schemes.PuebloOriginario)
def actualizar_pueblo_originario(pueblo_id: int, pueblo: schemes.PuebloOriginarioCreate, db: Session = Depends(get_db)):
    db_pueblo = db.query(PuebloOriginario).filter(PuebloOriginario.id == pueblo_id).first()
    if not db_pueblo:
        raise HTTPException(status_code=404, detail="Pueblo originario no encontrado")
    for key, value in pueblo.dict().items():
        setattr(db_pueblo, key, value)
    db.commit()
    db.refresh(db_pueblo)
    return db_pueblo

@router.delete("/pueblo_originario/{pueblo_id}")
def eliminar_pueblo_originario(pueblo_id: int, db: Session = Depends(get_db)):
    db_pueblo = db.query(PuebloOriginario).filter(PuebloOriginario.id == pueblo_id).first()
    if not db_pueblo:
        raise HTTPException(status_code=404, detail="Pueblo originario no encontrado")
    db.delete(db_pueblo)
    db.commit()
    return {"ok": True}
