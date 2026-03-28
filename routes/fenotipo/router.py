from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from database import get_db

from models.fenotipo import TipoFenotipo, EtapaFenologica

import schemas.fenotipo as schemes

router = APIRouter()

# =================== TIPO FENOTIPO ===================
@router.get("/tipo_fenotipo", response_model=list[schemes.TipoFenotipo])
def listar_tipo_fenotipo(db: Session = Depends(get_db)):
    return db.query(TipoFenotipo).all()

@router.get("/tipo_fenotipo/{fenotipo_id}", response_model=schemes.TipoFenotipo)
def obtener_tipo_fenotipo(fenotipo_id: int, db: Session = Depends(get_db)):
    fenotipo = db.query(TipoFenotipo).filter(TipoFenotipo.id == fenotipo_id).first()
    if not fenotipo:
        raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
    return fenotipo

@router.post("/tipo_fenotipo", response_model=schemes.TipoFenotipo)
def crear_tipo_fenotipo(fenotipo: schemes.TipoFenotipoCreate, db: Session = Depends(get_db)):
    db_fenotipo = TipoFenotipo(**fenotipo.dict())
    db.add(db_fenotipo)
    db.commit()
    db.refresh(db_fenotipo)
    return db_fenotipo

@router.put("/tipo_fenotipo/{fenotipo_id}", response_model=schemes.TipoFenotipo)
def actualizar_tipo_fenotipo(fenotipo_id: int, fenotipo: schemes.TipoFenotipoCreate, db: Session = Depends(get_db)):
    db_fenotipo = db.query(TipoFenotipo).filter(TipoFenotipo.id == fenotipo_id).first()
    if not db_fenotipo:
        raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
    for key, value in fenotipo.dict().items():
        setattr(db_fenotipo, key, value)
    db.commit()
    db.refresh(db_fenotipo)
    return db_fenotipo

@router.delete("/tipo_fenotipo/{fenotipo_id}")
def eliminar_tipo_fenotipo(fenotipo_id: int, db: Session = Depends(get_db)):
    db_fenotipo = db.query(TipoFenotipo).filter(TipoFenotipo.id == fenotipo_id).first()
    if not db_fenotipo:
        raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
    db.delete(db_fenotipo)
    db.commit()
    return {"ok": True}

# =================== ETAPA FENOLÓGICA ===================
@router.get("/etapa_fenologica", response_model=list[schemes.EtapaFenologica])
def listar_etapa_fenologica(db: Session = Depends(get_db)):
    return db.query(EtapaFenologica).all()

@router.get("/etapa_fenologica/{etapa_id}", response_model=schemes.EtapaFenologica)
def obtener_etapa_fenologica(etapa_id: int, db: Session = Depends(get_db)):
    etapa = db.query(EtapaFenologica).filter(EtapaFenologica.id == etapa_id).first()
    if not etapa:
        raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
    return etapa

@router.post("/etapa_fenologica", response_model=schemes.EtapaFenologica)
def crear_etapa_fenologica(etapa: schemes.EtapaFenologicaCreate, db: Session = Depends(get_db)):
    db_etapa = EtapaFenologica(**etapa.dict())
    db.add(db_etapa)
    db.commit()
    db.refresh(db_etapa)
    return db_etapa

@router.put("/etapa_fenologica/{etapa_id}", response_model=schemes.EtapaFenologica)
def actualizar_etapa_fenologica(etapa_id: int, etapa: schemes.EtapaFenologicaCreate, db: Session = Depends(get_db)):
    db_etapa = db.query(EtapaFenologica).filter(EtapaFenologica.id == etapa_id).first()
    if not db_etapa:
        raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
    for key, value in etapa.dict().items():
        setattr(db_etapa, key, value)
    db.commit()
    db.refresh(db_etapa)
    return db_etapa

@router.delete("/etapa_fenologica/{etapa_id}")
def eliminar_etapa_fenologica(etapa_id: int, db: Session = Depends(get_db)):
    db_etapa = db.query(EtapaFenologica).filter(EtapaFenologica.id == etapa_id).first()
    if not db_etapa:
        raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
    db.delete(db_etapa)
    db.commit()
    return {"ok": True}