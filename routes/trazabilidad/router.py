from pydoc import text

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from models.trazabilidad import FormatoArchivo, FuenteCaptura, FuenteInformacion, OrigenMuestra, OrigenSemilla, TipoCapaSIG, TipoProductoDron

import schemas.trazabilidad as trazabilidad

router = APIRouter()

@router.get("/")
def get_catalogo():
    return {"modulo": "Catálogo funcionando"}

@router.get("/healthcheck", tags=["health"])
def healthcheck(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    


# -- EJE DE TRAZABILIDAD Y GEODATOS --

# =================== CATALOGO: TIPO PRODUCTO DRON ===================
from fastapi import Query

@router.get("/tipo_producto_dron")
def listar_tipo_producto_dron(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoProductoDron)
    total = query.count()
    productos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": productos}

@router.get("/tipo_producto_dron/{producto_id}", response_model=trazabilidad.TipoProductoDron)
def obtener_tipo_producto_dron(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(TipoProductoDron).filter(TipoProductoDron.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Tipo de producto de dron no encontrado")
    return producto

@router.post("/tipo_producto_dron", response_model=trazabilidad.TipoProductoDron)
def crear_tipo_producto_dron(producto: trazabilidad.TipoProductoDronCreate, db: Session = Depends(get_db)):
    db_producto = TipoProductoDron(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.put("/tipo_producto_dron/{producto_id}", response_model=trazabilidad.TipoProductoDron)
def actualizar_tipo_producto_dron(producto_id: int, producto: trazabilidad.TipoProductoDronCreate, db: Session = Depends(get_db)):
    db_producto = db.query(TipoProductoDron).filter(TipoProductoDron.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Tipo de producto de dron no encontrado")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/tipo_producto_dron/{producto_id}")
def eliminar_tipo_producto_dron(producto_id: int, db: Session = Depends(get_db)):
    db_producto = db.query(TipoProductoDron).filter(TipoProductoDron.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Tipo de producto de dron no encontrado")
    db.delete(db_producto)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: FORMATO ARCHIVO ===================
@router.get("/formato_archivo")
def listar_formato_archivo(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(FormatoArchivo)
    total = query.count()
    formatos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": formatos}

@router.get("/formato_archivo/{formato_id}", response_model=trazabilidad.FormatoArchivo)
def obtener_formato_archivo(formato_id: int, db: Session = Depends(get_db)):
    formato = db.query(FormatoArchivo).filter(FormatoArchivo.id == formato_id).first()
    if not formato:
        raise HTTPException(status_code=404, detail="Formato de archivo no encontrado")
    return formato

@router.post("/formato_archivo", response_model=trazabilidad.FormatoArchivo)
def crear_formato_archivo(formato: trazabilidad.FormatoArchivoCreate, db: Session = Depends(get_db)):
    db_formato = FormatoArchivo(**formato.dict())
    db.add(db_formato)
    db.commit()
    db.refresh(db_formato)
    return db_formato

@router.put("/formato_archivo/{formato_id}", response_model=trazabilidad.FormatoArchivo)
def actualizar_formato_archivo(formato_id: int, formato: trazabilidad.FormatoArchivoCreate, db: Session = Depends(get_db)):
    db_formato = db.query(FormatoArchivo).filter(FormatoArchivo.id == formato_id).first()
    if not db_formato:
        raise HTTPException(status_code=404, detail="Formato de archivo no encontrado")
    for key, value in formato.dict().items():
        setattr(db_formato, key, value)
    db.commit()
    db.refresh(db_formato)
    return db_formato

@router.delete("/formato_archivo/{formato_id}")
def eliminar_formato_archivo(formato_id: int, db: Session = Depends(get_db)):
    db_formato = db.query(FormatoArchivo).filter(FormatoArchivo.id == formato_id).first()
    if not db_formato:
        raise HTTPException(status_code=404, detail="Formato de archivo no encontrado")
    db.delete(db_formato)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: TIPO CAPA SIG ===================
@router.get("/tipo_capa_sig")
def listar_tipo_capa_sig(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoCapaSIG)
    total = query.count()
    capas = query.offset(offset).limit(limit).all()
    return {"count": total, "results": capas}

@router.get("/tipo_capa_sig/{capa_id}", response_model=trazabilidad.TipoCapaSIG)
def obtener_tipo_capa_sig(capa_id: int, db: Session = Depends(get_db)):
    capa = db.query(TipoCapaSIG).filter(TipoCapaSIG.id == capa_id).first()
    if not capa:
        raise HTTPException(status_code=404, detail="Tipo de capa SIG no encontrado")
    return capa

@router.post("/tipo_capa_sig", response_model=trazabilidad.TipoCapaSIG)
def crear_tipo_capa_sig(capa: trazabilidad.TipoCapaSIGCreate, db: Session = Depends(get_db)):
    db_capa = TipoCapaSIG(**capa.dict())
    db.add(db_capa)
    db.commit()
    db.refresh(db_capa)
    return db_capa

@router.put("/tipo_capa_sig/{capa_id}", response_model=trazabilidad.TipoCapaSIG)
def actualizar_tipo_capa_sig(capa_id: int, capa: trazabilidad.TipoCapaSIGCreate, db: Session = Depends(get_db)):
    db_capa = db.query(TipoCapaSIG).filter(TipoCapaSIG.id == capa_id).first()
    if not db_capa:
        raise HTTPException(status_code=404, detail="Tipo de capa SIG no encontrado")
    for key, value in capa.dict().items():
        setattr(db_capa, key, value)
    db.commit()
    db.refresh(db_capa)
    return db_capa

@router.delete("/tipo_capa_sig/{capa_id}")
def eliminar_tipo_capa_sig(capa_id: int, db: Session = Depends(get_db)):
    db_capa = db.query(TipoCapaSIG).filter(TipoCapaSIG.id == capa_id).first()
    if not db_capa:
        raise HTTPException(status_code=404, detail="Tipo de capa SIG no encontrado")
    db.delete(db_capa)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: FUENTE CAPTURA ===================
@router.get("/fuente_captura")
def listar_fuente_captura(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(FuenteCaptura)
    total = query.count()
    fuentes = query.offset(offset).limit(limit).all()
    return {"count": total, "results": fuentes}

@router.get("/fuente_captura/{fuente_id}", response_model=trazabilidad.FuenteCaptura)
def obtener_fuente_captura(fuente_id: int, db: Session = Depends(get_db)):
    fuente = db.query(FuenteCaptura).filter(FuenteCaptura.id == fuente_id).first()
    if not fuente:
        raise HTTPException(status_code=404, detail="Fuente de captura no encontrada")
    return fuente

@router.post("/fuente_captura", response_model=trazabilidad.FuenteCaptura)
def crear_fuente_captura(fuente: trazabilidad.FuenteCapturaCreate, db: Session = Depends(get_db)):
    db_fuente = FuenteCaptura(**fuente.dict())
    db.add(db_fuente)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.put("/fuente_captura/{fuente_id}", response_model=trazabilidad.FuenteCaptura)
def actualizar_fuente_captura(fuente_id: int, fuente: trazabilidad.FuenteCapturaCreate, db: Session = Depends(get_db)):
    db_fuente = db.query(FuenteCaptura).filter(FuenteCaptura.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de captura no encontrada")
    for key, value in fuente.dict().items():
        setattr(db_fuente, key, value)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.delete("/fuente_captura/{fuente_id}")
def eliminar_fuente_captura(fuente_id: int, db: Session = Depends(get_db)):
    db_fuente = db.query(FuenteCaptura).filter(FuenteCaptura.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de captura no encontrada")
    db.delete(db_fuente)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: FUENTE INFORMACION ===================
from fastapi import Query

@router.get("/fuente_informacion")
def listar_fuente_informacion(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(FuenteInformacion)
    total = query.count()
    fuentes = query.offset(offset).limit(limit).all()
    return {"count": total, "results": fuentes}

@router.get("/fuente_informacion/{fuente_id}", response_model=trazabilidad.FuenteInformacion)
def obtener_fuente_informacion(fuente_id: int, db: Session = Depends(get_db)):
    fuente = db.query(FuenteInformacion).filter(FuenteInformacion.id == fuente_id).first()
    if not fuente:
        raise HTTPException(status_code=404, detail="Fuente de información no encontrada")
    return fuente

@router.post("/fuente_informacion", response_model=trazabilidad.FuenteInformacion)
def crear_fuente_informacion(fuente: trazabilidad.FuenteInformacionCreate, db: Session = Depends(get_db)):
    db_fuente = FuenteInformacion(**fuente.dict())
    db.add(db_fuente)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.put("/fuente_informacion/{fuente_id}", response_model=trazabilidad.FuenteInformacion)
def actualizar_fuente_informacion(fuente_id: int, fuente: trazabilidad.FuenteInformacionCreate, db: Session = Depends(get_db)):
    db_fuente = db.query(FuenteInformacion).filter(FuenteInformacion.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de información no encontrada")
    for key, value in fuente.dict().items():
        setattr(db_fuente, key, value)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.delete("/fuente_informacion/{fuente_id}")
def eliminar_fuente_informacion(fuente_id: int, db: Session = Depends(get_db)):
    db_fuente = db.query(FuenteInformacion).filter(FuenteInformacion.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de información no encontrada")
    db.delete(db_fuente)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: ORIGEN MUESTRA ===================
@router.get("/origen_muestra")
def listar_origen_muestra(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(OrigenMuestra)
    total = query.count()
    origenes = query.offset(offset).limit(limit).all()
    return {"count": total, "results": origenes}

@router.get("/origen_muestra/{origen_id}", response_model=trazabilidad.OrigenMuestra)
def obtener_origen_muestra(origen_id: int, db: Session = Depends(get_db)):
    origen = db.query(OrigenMuestra).filter(OrigenMuestra.id == origen_id).first()
    if not origen:
        raise HTTPException(status_code=404, detail="Origen de muestra no encontrado")
    return origen

@router.post("/origen_muestra", response_model=trazabilidad.OrigenMuestra)
def crear_origen_muestra(origen: trazabilidad.OrigenMuestraCreate, db: Session = Depends(get_db)):
    db_origen = OrigenMuestra(**origen.dict())
    db.add(db_origen)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.put("/origen_muestra/{origen_id}", response_model=trazabilidad.OrigenMuestra)
def actualizar_origen_muestra(origen_id: int, origen: trazabilidad.OrigenMuestraCreate, db: Session = Depends(get_db)):
    db_origen = db.query(OrigenMuestra).filter(OrigenMuestra.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de muestra no encontrado")
    for key, value in origen.dict().items():
        setattr(db_origen, key, value)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.delete("/origen_muestra/{origen_id}")
def eliminar_origen_muestra(origen_id: int, db: Session = Depends(get_db)):
    db_origen = db.query(OrigenMuestra).filter(OrigenMuestra.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de muestra no encontrado")
    db.delete(db_origen)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: ORIGEN SEMILLA ===================
@router.get("/origen_semilla")
def listar_origen_semilla(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(OrigenSemilla)
    total = query.count()
    origenes = query.offset(offset).limit(limit).all()
    return {"count": total, "results": origenes}

@router.get("/origen_semilla/{origen_id}", response_model=trazabilidad.OrigenSemilla)
def obtener_origen_semilla(origen_id: int, db: Session = Depends(get_db)):
    origen = db.query(OrigenSemilla).filter(OrigenSemilla.id == origen_id).first()
    if not origen:
        raise HTTPException(status_code=404, detail="Origen de semilla no encontrado")
    return origen

@router.post("/origen_semilla", response_model=trazabilidad.OrigenSemilla)
def crear_origen_semilla(origen: trazabilidad.OrigenSemillaCreate, db: Session = Depends(get_db)):
    db_origen = OrigenSemilla(**origen.dict())
    db.add(db_origen)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.put("/origen_semilla/{origen_id}", response_model=trazabilidad.OrigenSemilla)
def actualizar_origen_semilla(origen_id: int, origen: trazabilidad.OrigenSemillaCreate, db: Session = Depends(get_db)):
    db_origen = db.query(OrigenSemilla).filter(OrigenSemilla.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de semilla no encontrado")
    for key, value in origen.dict().items():
        setattr(db_origen, key, value)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.delete("/origen_semilla/{origen_id}")
def eliminar_origen_semilla(origen_id: int, db: Session = Depends(get_db)):
    db_origen = db.query(OrigenSemilla).filter(OrigenSemilla.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de semilla no encontrado")
    db.delete(db_origen)
    db.commit()
    return {"ok": True}