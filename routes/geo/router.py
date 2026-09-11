from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from database import get_db

from models.territorio import Estado, Municipio, Localidad, Colonia
from models.core import Comunidad
import schemas.geoespacial as schemas

router = APIRouter()

# -- EJE TERRITORIAL --

# =================== CATALOGO: ESTADO ===================
@router.get("/estado")
def listar_estados(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Estado)
    total = query.count()
    estados = query.offset(offset).limit(limit).all()
    return {"count": total, "results": estados}

@router.get("/estado/{estado_id}", response_model=schemas.Estado)
def obtener_estado(estado_id: int, db: Session = Depends(get_db)):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado

@router.post("/estado", response_model=schemas.Estado)
def crear_estado(estado: schemas.EstadoCreate, db: Session = Depends(get_db)):
    db_estado = Estado(**estado.dict())
    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)
    return db_estado

@router.put("/estado/{estado_id}", response_model=schemas.Estado)
def actualizar_estado(estado_id: int, estado: schemas.EstadoCreate, db: Session = Depends(get_db)):
    db_estado = db.query(Estado).filter(Estado.id == estado_id).first()
    if not db_estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    for key, value in estado.dict().items():
        setattr(db_estado, key, value)
    db.commit()
    db.refresh(db_estado)
    return db_estado

@router.delete("/estado/{estado_id}")
def eliminar_estado(estado_id: int, db: Session = Depends(get_db)):
    db_estado = db.query(Estado).filter(Estado.id == estado_id).first()
    if not db_estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    db.delete(db_estado)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: MUNICIPIO ===================
@router.get("/municipio")
def listar_municipios(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Municipio)
    total = query.count()
    municipios = query.offset(offset).limit(limit).all()
    return {"count": total, "results": municipios}

@router.get("/municipio/{municipio_id}", response_model=schemas.Municipio)
def obtener_municipio(municipio_id: int, db: Session = Depends(get_db)):
    municipio = db.query(Municipio).filter(Municipio.id == municipio_id).first()
    if not municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    return municipio

@router.post("/municipio", response_model=schemas.Municipio)
def crear_municipio(municipio: schemas.MunicipioCreate, db: Session = Depends(get_db)):
    db_municipio = Municipio(**municipio.dict())
    db.add(db_municipio)
    db.commit()
    db.refresh(db_municipio)
    return db_municipio

@router.put("/municipio/{municipio_id}", response_model=schemas.Municipio)
def actualizar_municipio(municipio_id: int, municipio: schemas.MunicipioCreate, db: Session = Depends(get_db)):
    db_municipio = db.query(Municipio).filter(Municipio.id == municipio_id).first()
    if not db_municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    for key, value in municipio.dict().items():
        setattr(db_municipio, key, value)
    db.commit()
    db.refresh(db_municipio)
    return db_municipio

@router.delete("/municipio/{municipio_id}")
def eliminar_municipio(municipio_id: int, db: Session = Depends(get_db)):
    db_municipio = db.query(Municipio).filter(Municipio.id == municipio_id).first()
    if not db_municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    db.delete(db_municipio)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: COMUNIDAD ===================
@router.get("/comunidad")
def listar_comunidades(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Comunidad)
    total = query.count()
    comunidades = query.offset(offset).limit(limit).all()
    return {"count": total, "results": comunidades}

@router.get("/comunidad/{comunidad_id}", response_model=schemas.Comunidad)
def obtener_comunidad(comunidad_id: int, db: Session = Depends(get_db)):
    comunidad = db.query(Comunidad).filter(Comunidad.id == comunidad_id).first()
    if not comunidad:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada")
    return comunidad

@router.post("/comunidad", response_model=schemas.Comunidad)
def crear_comunidad(comunidad: schemas.ComunidadCreate, db: Session = Depends(get_db)):
    db_comunidad = Comunidad(**comunidad.dict())
    db.add(db_comunidad)
    db.commit()
    db.refresh(db_comunidad)
    return db_comunidad

@router.put("/comunidad/{comunidad_id}", response_model=schemas.Comunidad)
def actualizar_comunidad(comunidad_id: int, comunidad: schemas.ComunidadCreate, db: Session = Depends(get_db)):
    db_comunidad = db.query(Comunidad).filter(Comunidad.id == comunidad_id).first()
    if not db_comunidad:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada")
    for key, value in comunidad.dict().items():
        setattr(db_comunidad, key, value)
    db.commit()
    db.refresh(db_comunidad)
    return db_comunidad

@router.delete("/comunidad/{comunidad_id}")
def eliminar_comunidad(comunidad_id: int, db: Session = Depends(get_db)):
    db_comunidad = db.query(Comunidad).filter(Comunidad.id == comunidad_id).first()
    if not db_comunidad:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada")
    db.delete(db_comunidad)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: LOCALIDAD ===================
@router.get("/localidad")
def listar_localidades(
    municipio_id: int = Query(None, description="ID del municipio para filtrar localidades"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Localidad)
    if municipio_id is not None:
        query = query.filter(Localidad.municipio_id == municipio_id)
    total = query.count()
    localidades = query.offset(offset).limit(limit).all()
    return {"count": total, "results": localidades}

@router.get("/localidad/{localidad_id}", response_model=schemas.Localidad)
def obtener_localidad(localidad_id: int, db: Session = Depends(get_db)):
    localidad = db.query(Localidad).filter(Localidad.id == localidad_id).first()
    if not localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    return localidad

@router.post("/localidad", response_model=schemas.Localidad)
def crear_localidad(localidad: schemas.LocalidadCreate, db: Session = Depends(get_db)):
    db_localidad = Localidad(**localidad.dict())
    db.add(db_localidad)
    db.commit()
    db.refresh(db_localidad)
    return db_localidad

@router.put("/localidad/{localidad_id}", response_model=schemas.Localidad)
def actualizar_localidad(localidad_id: int, localidad: schemas.LocalidadCreate, db: Session = Depends(get_db)):
    db_localidad = db.query(Localidad).filter(Localidad.id == localidad_id).first()
    if not db_localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    for key, value in localidad.dict().items():
        setattr(db_localidad, key, value)
    db.commit()
    db.refresh(db_localidad)
    return db_localidad

@router.delete("/localidad/{localidad_id}")
def eliminar_localidad(localidad_id: int, db: Session = Depends(get_db)):
    db_localidad = db.query(Localidad).filter(Localidad.id == localidad_id).first()
    if not db_localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    db.delete(db_localidad)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: COLONIA ===================
@router.get("/colonia")
def listar_colonias(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Colonia)
    total = query.count()
    colonias = query.offset(offset).limit(limit).all()
    return {"count": total, "results": colonias}

@router.get("/colonia/{colonia_id}", response_model=schemas.Colonia)
def obtener_colonia(colonia_id: int, db: Session = Depends(get_db)):
    colonia = db.query(Colonia).filter(Colonia.id == colonia_id).first()
    if not colonia:
        raise HTTPException(status_code=404, detail="Colonia no encontrada")
    return colonia

@router.post("/colonia", response_model=schemas.Colonia)
def crear_colonia(colonia: schemas.ColoniaCreate, db: Session = Depends(get_db)):
    db_colonia = Colonia(**colonia.dict())
    db.add(db_colonia)
    db.commit()
    db.refresh(db_colonia)
    return db_colonia

@router.put("/colonia/{colonia_id}", response_model=schemas.Colonia)
def actualizar_colonia(colonia_id: int, colonia: schemas.ColoniaCreate, db: Session = Depends(get_db)):
    db_colonia = db.query(Colonia).filter(Colonia.id == colonia_id).first()
    if not db_colonia:
        raise HTTPException(status_code=404, detail="Colonia no encontrada")
    for key, value in colonia.dict().items():
        setattr(db_colonia, key, value)
    db.commit()
    db.refresh(db_colonia)
    return db_colonia

@router.delete("/colonia/{colonia_id}")
def eliminar_colonia(colonia_id: int, db: Session = Depends(get_db)):
    db_colonia = db.query(Colonia).filter(Colonia.id == colonia_id).first()
    if not db_colonia:
        raise HTTPException(status_code=404, detail="Colonia no encontrada")
    db.delete(db_colonia)
    db.commit()
    return {"ok": True}

