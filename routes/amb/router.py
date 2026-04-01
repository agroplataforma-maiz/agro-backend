from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.orm import Session
from database import get_db

from models.ambiental import ClaseUsoSuelo, TipoAmenaza, TipoEventoClimatico, VariableAmbiental 

import schemas.ambiental as schemas

router = APIRouter()

# -- EJE AMBIENTAL --

# =================== CATALOGO: TIPO EVENTO CLIMATICO ===================
@router.get("/tipo_evento_climatico")
def listar_tipo_evento_climatico(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoEventoClimatico)
    total = query.count()
    tipos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": tipos}

@router.get("/tipo_evento_climatico/{tipo_id}", response_model=schemas.TipoEventoClimatico)
def obtener_tipo_evento_climatico(tipo_id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoEventoClimatico).filter(TipoEventoClimatico.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de evento climático no encontrado")
    return tipo

@router.post("/tipo_evento_climatico", response_model=schemas.TipoEventoClimatico)
def crear_tipo_evento_climatico(tipo: schemas.TipoEventoClimaticoCreate, db: Session = Depends(get_db)):
    db_tipo = TipoEventoClimatico(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.put("/tipo_evento_climatico/{tipo_id}", response_model=schemas.TipoEventoClimatico)
def actualizar_tipo_evento_climatico(tipo_id: int, tipo: schemas.TipoEventoClimaticoCreate, db: Session = Depends(get_db)):
    db_tipo = db.query(TipoEventoClimatico).filter(TipoEventoClimatico.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de evento climático no encontrado")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipo_evento_climatico/{tipo_id}")
def eliminar_tipo_evento_climatico(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = db.query(TipoEventoClimatico).filter(TipoEventoClimatico.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de evento climático no encontrado")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: VARIABLE AMBIENTAL ===================
@router.get("/variable_ambiental")
def listar_variable_ambiental(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(VariableAmbiental)
    total = query.count()
    variables = query.offset(offset).limit(limit).all()
    return {"count": total, "results": variables}

@router.get("/variable_ambiental/{variable_id}", response_model=schemas.VariableAmbiental)
def obtener_variable_ambiental(variable_id: int, db: Session = Depends(get_db)):
    variable = db.query(VariableAmbiental).filter(VariableAmbiental.id == variable_id).first()
    if not variable:
        raise HTTPException(status_code=404, detail="Variable ambiental no encontrada")
    return variable

@router.post("/variable_ambiental", response_model=schemas.VariableAmbiental)
def crear_variable_ambiental(variable: schemas.VariableAmbientalCreate, db: Session = Depends(get_db)):
    db_variable = VariableAmbiental(**variable.dict())
    db.add(db_variable)
    db.commit()
    db.refresh(db_variable)
    return db_variable

@router.put("/variable_ambiental/{variable_id}", response_model=schemas.VariableAmbiental)
def actualizar_variable_ambiental(variable_id: int, variable: schemas.VariableAmbientalCreate, db: Session = Depends(get_db)):
    db_variable = db.query(VariableAmbiental).filter(VariableAmbiental.id == variable_id).first()
    if not db_variable:
        raise HTTPException(status_code=404, detail="Variable ambiental no encontrada")
    for key, value in variable.dict().items():
        setattr(db_variable, key, value)
    db.commit()
    db.refresh(db_variable)
    return db_variable

@router.delete("/variable_ambiental/{variable_id}")
def eliminar_variable_ambiental(variable_id: int, db: Session = Depends(get_db)):
    db_variable = db.query(VariableAmbiental).filter(VariableAmbiental.id == variable_id).first()
    if not db_variable:
        raise HTTPException(status_code=404, detail="Variable ambiental no encontrada")
    db.delete(db_variable)
    db.commit()
    return {"ok": True}

# =================== CATALOGO:TIPO AMENAZA ===================
@router.get("/tipo_amenaza")
def listar_tipo_amenaza(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoAmenaza)
    total = query.count()
    amenazas = query.offset(offset).limit(limit).all()
    return {"count": total, "results": amenazas}

@router.get("/tipo_amenaza/{amenaza_id}", response_model=schemas.TipoAmenaza)
def obtener_tipo_amenaza(amenaza_id: int, db: Session = Depends(get_db)):
    amenaza = db.query(TipoAmenaza).filter(TipoAmenaza.id == amenaza_id).first()
    if not amenaza:
        raise HTTPException(status_code=404, detail="Tipo de amenaza no encontrado")
    return amenaza

@router.post("/tipo_amenaza", response_model=schemas.TipoAmenaza)
def crear_tipo_amenaza(amenaza: schemas.TipoAmenazaCreate, db: Session = Depends(get_db)):
    db_amenaza = TipoAmenaza(**amenaza.dict())
    db.add(db_amenaza)
    db.commit()
    db.refresh(db_amenaza)
    return db_amenaza

@router.put("/tipo_amenaza/{amenaza_id}", response_model=schemas.TipoAmenaza)
def actualizar_tipo_amenaza(amenaza_id: int, amenaza: schemas.TipoAmenazaCreate, db: Session = Depends(get_db)):
    db_amenaza = db.query(TipoAmenaza).filter(TipoAmenaza.id == amenaza_id).first()
    if not db_amenaza:
        raise HTTPException(status_code=404, detail="Tipo de amenaza no encontrado")
    for key, value in amenaza.dict().items():
        setattr(db_amenaza, key, value)
    db.commit()
    db.refresh(db_amenaza)
    return db_amenaza

@router.delete("/tipo_amenaza/{amenaza_id}")
def eliminar_tipo_amenaza(amenaza_id: int, db: Session = Depends(get_db)):
    db_amenaza = db.query(TipoAmenaza).filter(TipoAmenaza.id == amenaza_id).first()
    if not db_amenaza:
        raise HTTPException(status_code=404, detail="Tipo de amenaza no encontrado")
    db.delete(db_amenaza)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: CLASE USO SUELO ===================
@router.get("/clase_uso_suelo")
def listar_clase_uso_suelo(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(ClaseUsoSuelo)
    total = query.count()
    clases = query.offset(offset).limit(limit).all()
    return {"count": total, "results": clases}

@router.get("/clase_uso_suelo/{clase_id}", response_model=schemas.ClaseUsoSuelo)
def obtener_clase_uso_suelo(clase_id: int, db: Session = Depends(get_db)):
    clase = db.query(ClaseUsoSuelo).filter(ClaseUsoSuelo.id == clase_id).first()
    if not clase:
        raise HTTPException(status_code=404, detail="Clase de uso de suelo no encontrada")
    return clase

@router.post("/clase_uso_suelo", response_model=schemas.ClaseUsoSuelo)
def crear_clase_uso_suelo(clase: schemas.ClaseUsoSueloCreate, db: Session = Depends(get_db)):
    db_clase = ClaseUsoSuelo(**clase.dict())
    db.add(db_clase)
    db.commit()
    db.refresh(db_clase)
    return db_clase

@router.put("/clase_uso_suelo/{clase_id}", response_model=schemas.ClaseUsoSuelo)
def actualizar_clase_uso_suelo(clase_id: int, clase: schemas.ClaseUsoSueloCreate, db: Session = Depends(get_db)):
    db_clase = db.query(ClaseUsoSuelo).filter(ClaseUsoSuelo.id == clase_id).first()
    if not db_clase:
        raise HTTPException(status_code=404, detail="Clase de uso de suelo no encontrada")
    for key, value in clase.dict().items():
        setattr(db_clase, key, value)
    db.commit()
    db.refresh(db_clase)
    return db_clase

@router.delete("/clase_uso_suelo/{clase_id}")
def eliminar_clase_uso_suelo(clase_id: int, db: Session = Depends(get_db)):
    db_clase = db.query(ClaseUsoSuelo).filter(ClaseUsoSuelo.id == clase_id).first()
    if not db_clase:
        raise HTTPException(status_code=404, detail="Clase de uso de suelo no encontrada")
    db.delete(db_clase)
    db.commit()
    return {"ok": True}
