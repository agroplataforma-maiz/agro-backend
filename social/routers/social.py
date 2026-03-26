from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import (
    Productor, Consentimiento, PerfilSocioeconomico, SeguridadAlimentaria,
    ProductorPractica, ProductorLengua, RedIntercambio, VulnerabilidadClimatica, GeolocalizacionProductor
)
from schemas import (
    ProductorCreate, ProductorUpdate, ProductorOut,
    ConsentimientoCreate, ConsentimientoUpdate, ConsentimientoOut,
    PerfilSocioeconomicoCreate, PerfilSocioeconomicoUpdate, PerfilSocioeconomicoOut,
    SeguridadAlimentariaCreate, SeguridadAlimentariaUpdate, SeguridadAlimentariaOut,
    ProductorPracticaCreate, ProductorPracticaUpdate, ProductorPracticaOut,
    ProductorLenguaCreate, ProductorLenguaUpdate, ProductorLenguaOut,
    RedIntercambioCreate, RedIntercambioUpdate, RedIntercambioOut,
    VulnerabilidadClimaticaCreate, VulnerabilidadClimaticaUpdate, VulnerabilidadClimaticaOut,
    GeolocalizacionProductorCreate, GeolocalizacionProductorUpdate, GeolocalizacionProductorOut
)
from db import get_db

# --- CRUD para Productor ---
def get_productores(db: Session):
    return db.query(Productor).all()

def get_productor(db: Session, productor_id: int):
    return db.query(Productor).filter(Productor.id == productor_id).first()

def create_productor(db: Session, productor_data):
    productor = Productor(**productor_data.dict())
    db.add(productor)
    db.commit()
    db.refresh(productor)
    return productor

def update_productor(db: Session, productor_id: int, productor_data):
    productor = db.query(Productor).filter(Productor.id == productor_id).first()
    if productor:
        for key, value in productor_data.dict(exclude_unset=True).items():
            setattr(productor, key, value)
        db.commit()
        db.refresh(productor)
    return productor

def delete_productor(db: Session, productor_id: int):
    productor = db.query(Productor).filter(Productor.id == productor_id).first()
    if productor:
        db.delete(productor)
        db.commit()
        return True


router = APIRouter(prefix="/social", tags=["social"])

# Productor
@router.get("/productores", response_model=list[ProductorOut])
def listar_productores(db: Session = Depends(get_db)):
    return get_productores(db)

@router.get("/productores/{productor_id}", response_model=ProductorOut)
def obtener_productor(productor_id: int, db: Session = Depends(get_db)):
    productor = get_productor(db, productor_id)
    if not productor:
        raise HTTPException(status_code=404, detail="Productor no encontrado")
    return productor

@router.post("/productores", response_model=ProductorOut)
def crear_productor(productor: ProductorCreate, db: Session = Depends(get_db)):
    return create_productor(db, productor)

@router.put("/productores/{productor_id}", response_model=ProductorOut)
def actualizar_productor(productor_id: int, productor: ProductorUpdate, db: Session = Depends(get_db)):
    actualizado = update_productor(db, productor_id, productor)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Productor no encontrado")
    return actualizado

@router.delete("/productores/{productor_id}")
def eliminar_productor(productor_id: int, db: Session = Depends(get_db)):
    eliminado = delete_productor(db, productor_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Productor no encontrado")
    return {"ok": True}

# Consentimiento
@router.get("/consentimientos", response_model=list[ConsentimientoOut])
def listar_consentimientos(db: Session = Depends(get_db)):
    return get_consentimientos(db)

@router.get("/consentimientos/{consentimiento_id}", response_model=ConsentimientoOut)
def obtener_consentimiento(consentimiento_id: int, db: Session = Depends(get_db)):
    consentimiento = get_consentimiento(db, consentimiento_id)
    if not consentimiento:
        raise HTTPException(status_code=404, detail="Consentimiento no encontrado")
    return consentimiento

@router.post("/consentimientos", response_model=ConsentimientoOut)
def crear_consentimiento(consentimiento: ConsentimientoCreate, db: Session = Depends(get_db)):
    return create_consentimiento(db, consentimiento)

@router.put("/consentimientos/{consentimiento_id}", response_model=ConsentimientoOut)
def actualizar_consentimiento(consentimiento_id: int, consentimiento: ConsentimientoUpdate, db: Session = Depends(get_db)):
    actualizado = update_consentimiento(db, consentimiento_id, consentimiento)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Consentimiento no encontrado")
    return actualizado

@router.delete("/consentimientos/{consentimiento_id}")
def eliminar_consentimiento(consentimiento_id: int, db: Session = Depends(get_db)):
    eliminado = delete_consentimiento(db, consentimiento_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Consentimiento no encontrado")
    return {"ok": True}

# PerfilSocioeconomico
@router.get("/perfiles_socioeconomicos", response_model=list[PerfilSocioeconomicoOut])
def listar_perfiles_socioeconomicos(db: Session = Depends(get_db)):
    return get_perfiles_socioeconomicos(db)

@router.get("/perfiles_socioeconomicos/{perfil_id}", response_model=PerfilSocioeconomicoOut)
def obtener_perfil_socioeconomico(perfil_id: int, db: Session = Depends(get_db)):
    perfil = get_perfil_socioeconomico(db, perfil_id)
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil socioeconómico no encontrado")
    return perfil

@router.post("/perfiles_socioeconomicos", response_model=PerfilSocioeconomicoOut)
def crear_perfil_socioeconomico(perfil: PerfilSocioeconomicoCreate, db: Session = Depends(get_db)):
    return create_perfil_socioeconomico(db, perfil)

@router.put("/perfiles_socioeconomicos/{perfil_id}", response_model=PerfilSocioeconomicoOut)
def actualizar_perfil_socioeconomico(perfil_id: int, perfil: PerfilSocioeconomicoUpdate, db: Session = Depends(get_db)):
    actualizado = update_perfil_socioeconomico(db, perfil_id, perfil)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Perfil socioeconómico no encontrado")
    return actualizado

@router.delete("/perfiles_socioeconomicos/{perfil_id}")
def eliminar_perfil_socioeconomico(perfil_id: int, db: Session = Depends(get_db)):
    eliminado = delete_perfil_socioeconomico(db, perfil_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Perfil socioeconómico no encontrado")
    return {"ok": True}

# SeguridadAlimentaria
@router.get("/seguridad_alimentaria", response_model=list[SeguridadAlimentariaOut])
def listar_seguridad_alimentaria(db: Session = Depends(get_db)):
    return get_seguridad_alimentaria(db)

@router.get("/seguridad_alimentaria/{seguridad_id}", response_model=SeguridadAlimentariaOut)
def obtener_seguridad_alimentaria(seguridad_id: int, db: Session = Depends(get_db)):
    seguridad = get_seguridad_alimentaria_by_id(db, seguridad_id)
    if not seguridad:
        raise HTTPException(status_code=404, detail="Seguridad alimentaria no encontrada")
    return seguridad

@router.post("/seguridad_alimentaria", response_model=SeguridadAlimentariaOut)
def crear_seguridad_alimentaria(seguridad: SeguridadAlimentariaCreate, db: Session = Depends(get_db)):
    return create_seguridad_alimentaria(db, seguridad)

@router.put("/seguridad_alimentaria/{seguridad_id}", response_model=SeguridadAlimentariaOut)
def actualizar_seguridad_alimentaria(seguridad_id: int, seguridad: SeguridadAlimentariaUpdate, db: Session = Depends(get_db)):
    actualizado = update_seguridad_alimentaria(db, seguridad_id, seguridad)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Seguridad alimentaria no encontrada")
    return actualizado

@router.delete("/seguridad_alimentaria/{seguridad_id}")
def eliminar_seguridad_alimentaria(seguridad_id: int, db: Session = Depends(get_db)):
    eliminado = delete_seguridad_alimentaria(db, seguridad_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Seguridad alimentaria no encontrada")
    return {"ok": True}

# ProductorPractica
@router.get("/productores_practica", response_model=list[ProductorPracticaOut])
def listar_productores_practica(db: Session = Depends(get_db)):
    return get_productores_practica(db)

@router.get("/productores_practica/{practica_id}", response_model=ProductorPracticaOut)
def obtener_productor_practica(practica_id: int, db: Session = Depends(get_db)):
    practica = get_productor_practica(db, practica_id)
    if not practica:
        raise HTTPException(status_code=404, detail="Productor práctica no encontrado")
    return practica

@router.post("/productores_practica", response_model=ProductorPracticaOut)
def crear_productor_practica(practica: ProductorPracticaCreate, db: Session = Depends(get_db)):
    return create_productor_practica(db, practica)

@router.put("/productores_practica/{practica_id}", response_model=ProductorPracticaOut)
def actualizar_productor_practica(practica_id: int, practica: ProductorPracticaUpdate, db: Session = Depends(get_db)):
    actualizado = update_productor_practica(db, practica_id, practica)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Productor práctica no encontrado")
    return actualizado

@router.delete("/productores_practica/{practica_id}")
def eliminar_productor_practica(practica_id: int, db: Session = Depends(get_db)):
    eliminado = delete_productor_practica(db, practica_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Productor práctica no encontrado")
    return {"ok": True}

# ProductorLengua
@router.get("/productores_lengua", response_model=list[ProductorLenguaOut])
def listar_productores_lengua(db: Session = Depends(get_db)):
    return get_productores_lengua(db)

@router.get("/productores_lengua/{lengua_id}", response_model=ProductorLenguaOut)
def obtener_productor_lengua(lengua_id: int, db: Session = Depends(get_db)):
    lengua = get_productor_lengua(db, lengua_id)
    if not lengua:
        raise HTTPException(status_code=404, detail="Productor lengua no encontrado")
    return lengua

@router.post("/productores_lengua", response_model=ProductorLenguaOut)
def crear_productor_lengua(lengua: ProductorLenguaCreate, db: Session = Depends(get_db)):
    return create_productor_lengua(db, lengua)

@router.put("/productores_lengua/{lengua_id}", response_model=ProductorLenguaOut)
def actualizar_productor_lengua(lengua_id: int, lengua: ProductorLenguaUpdate, db: Session = Depends(get_db)):
    actualizado = update_productor_lengua(db, lengua_id, lengua)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Productor lengua no encontrado")
    return actualizado

@router.delete("/productores_lengua/{lengua_id}")
def eliminar_productor_lengua(lengua_id: int, db: Session = Depends(get_db)):
    eliminado = delete_productor_lengua(db, lengua_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Productor lengua no encontrado")
    return {"ok": True}

# RedIntercambio
@router.get("/redes_intercambio", response_model=list[RedIntercambioOut])
def listar_redes_intercambio(db: Session = Depends(get_db)):
    return get_redes_intercambio(db)

@router.get("/redes_intercambio/{red_id}", response_model=RedIntercambioOut)
def obtener_red_intercambio(red_id: int, db: Session = Depends(get_db)):
    red = get_red_intercambio(db, red_id)
    if not red:
        raise HTTPException(status_code=404, detail="Red de intercambio no encontrada")
    return red

@router.post("/redes_intercambio", response_model=RedIntercambioOut)
def crear_red_intercambio(red: RedIntercambioCreate, db: Session = Depends(get_db)):
    return create_red_intercambio(db, red)

@router.put("/redes_intercambio/{red_id}", response_model=RedIntercambioOut)
def actualizar_red_intercambio(red_id: int, red: RedIntercambioUpdate, db: Session = Depends(get_db)):
    actualizado = update_red_intercambio(db, red_id, red)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Red de intercambio no encontrada")
    return actualizado

@router.delete("/redes_intercambio/{red_id}")
def eliminar_red_intercambio(red_id: int, db: Session = Depends(get_db)):
    eliminado = delete_red_intercambio(db, red_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Red de intercambio no encontrada")
    return {"ok": True}

# VulnerabilidadClimatica
@router.get("/vulnerabilidades_climaticas", response_model=list[VulnerabilidadClimaticaOut])
def listar_vulnerabilidades_climaticas(db: Session = Depends(get_db)):
    return get_vulnerabilidades_climaticas(db)

@router.get("/vulnerabilidades_climaticas/{vulnerabilidad_id}", response_model=VulnerabilidadClimaticaOut)
def obtener_vulnerabilidad_climatica(vulnerabilidad_id: int, db: Session = Depends(get_db)):
    vulnerabilidad = get_vulnerabilidad_climatica(db, vulnerabilidad_id)
    if not vulnerabilidad:
        raise HTTPException(status_code=404, detail="Vulnerabilidad climática no encontrada")
    return vulnerabilidad

@router.post("/vulnerabilidades_climaticas", response_model=VulnerabilidadClimaticaOut)
def crear_vulnerabilidad_climatica(vulnerabilidad: VulnerabilidadClimaticaCreate, db: Session = Depends(get_db)):
    return create_vulnerabilidad_climatica(db, vulnerabilidad)

@router.put("/vulnerabilidades_climaticas/{vulnerabilidad_id}", response_model=VulnerabilidadClimaticaOut)
def actualizar_vulnerabilidad_climatica(vulnerabilidad_id: int, vulnerabilidad: VulnerabilidadClimaticaUpdate, db: Session = Depends(get_db)):
    actualizado = update_vulnerabilidad_climatica(db, vulnerabilidad_id, vulnerabilidad)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Vulnerabilidad climática no encontrada")
    return actualizado

@router.delete("/vulnerabilidades_climaticas/{vulnerabilidad_id}")
def eliminar_vulnerabilidad_climatica(vulnerabilidad_id: int, db: Session = Depends(get_db)):
    eliminado = delete_vulnerabilidad_climatica(db, vulnerabilidad_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Vulnerabilidad climática no encontrada")
    return {"ok": True}

# GeolocalizacionProductor
@router.get("/geolocalizaciones_productor", response_model=list[GeolocalizacionProductorOut])
def listar_geolocalizaciones_productor(db: Session = Depends(get_db)):
    return get_geolocalizaciones_productor(db)

@router.get("/geolocalizaciones_productor/{geoloc_id}", response_model=GeolocalizacionProductorOut)
def obtener_geolocalizacion_productor(geoloc_id: int, db: Session = Depends(get_db)):
    geoloc = get_geolocalizacion_productor(db, geoloc_id)
    if not geoloc:
        raise HTTPException(status_code=404, detail="Geolocalización de productor no encontrada")
    return geoloc

@router.post("/geolocalizaciones_productor", response_model=GeolocalizacionProductorOut)
def crear_geolocalizacion_productor(geoloc: GeolocalizacionProductorCreate, db: Session = Depends(get_db)):
    return create_geolocalizacion_productor(db, geoloc)

@router.put("/geolocalizaciones_productor/{geoloc_id}", response_model=GeolocalizacionProductorOut)
def actualizar_geolocalizacion_productor(geoloc_id: int, geoloc: GeolocalizacionProductorUpdate, db: Session = Depends(get_db)):
    actualizado = update_geolocalizacion_productor(db, geoloc_id, geoloc)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Geolocalización de productor no encontrada")
    return actualizado

@router.delete("/geolocalizaciones_productor/{geoloc_id}")
def eliminar_geolocalizacion_productor(geoloc_id: int, db: Session = Depends(get_db)):
    eliminado = delete_geolocalizacion_productor(db, geoloc_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Geolocalización de productor no encontrada")
    return {"ok": True}

# ProductorPractica
def get_productores_practica(db: Session):
    return db.query(ProductorPractica).all()

def get_productor_practica(db: Session, practica_id: int):
    return db.query(ProductorPractica).filter(ProductorPractica.id == practica_id).first()

def create_productor_practica(db: Session, practica_data):
    practica = ProductorPractica(**practica_data.dict())
    db.add(practica)
    db.commit()
    db.refresh(practica)
    return practica

def update_productor_practica(db: Session, practica_id: int, practica_data):
    practica = db.query(ProductorPractica).filter(ProductorPractica.id == practica_id).first()
    if practica:
        for key, value in practica_data.dict(exclude_unset=True).items():
            setattr(practica, key, value)
        db.commit()
        db.refresh(practica)
    return practica

def delete_productor_practica(db: Session, practica_id: int):
    practica = db.query(ProductorPractica).filter(ProductorPractica.id == practica_id).first()
    if practica:
        db.delete(practica)
        db.commit()
        return True
    return False

# ProductorLengua
def get_productores_lengua(db: Session):
    return db.query(ProductorLengua).all()

def get_productor_lengua(db: Session, lengua_id: int):
    return db.query(ProductorLengua).filter(ProductorLengua.id == lengua_id).first()

def create_productor_lengua(db: Session, lengua_data):
    lengua = ProductorLengua(**lengua_data.dict())
    db.add(lengua)
    db.commit()
    db.refresh(lengua)
    return lengua

def update_productor_lengua(db: Session, lengua_id: int, lengua_data):
    lengua = db.query(ProductorLengua).filter(ProductorLengua.id == lengua_id).first()
    if lengua:
        for key, value in lengua_data.dict(exclude_unset=True).items():
            setattr(lengua, key, value)
        db.commit()
        db.refresh(lengua)
    return lengua

def delete_productor_lengua(db: Session, lengua_id: int):
    lengua = db.query(ProductorLengua).filter(ProductorLengua.id == lengua_id).first()
    if lengua:
        db.delete(lengua)
        db.commit()
        return True
    return False

# RedIntercambio
def get_redes_intercambio(db: Session):
    return db.query(RedIntercambio).all()

def get_red_intercambio(db: Session, red_id: int):
    return db.query(RedIntercambio).filter(RedIntercambio.id == red_id).first()

def create_red_intercambio(db: Session, red_data):
    red = RedIntercambio(**red_data.dict())
    db.add(red)
    db.commit()
    db.refresh(red)
    return red

def update_red_intercambio(db: Session, red_id: int, red_data):
    red = db.query(RedIntercambio).filter(RedIntercambio.id == red_id).first()
    if red:
        for key, value in red_data.dict(exclude_unset=True).items():
            setattr(red, key, value)
        db.commit()
        db.refresh(red)
    return red

def delete_red_intercambio(db: Session, red_id: int):
    red = db.query(RedIntercambio).filter(RedIntercambio.id == red_id).first()
    if red:
        db.delete(red)
        db.commit()
        return True
    return False

# VulnerabilidadClimatica
def get_vulnerabilidades_climaticas(db: Session):
    return db.query(VulnerabilidadClimatica).all()

def get_vulnerabilidad_climatica(db: Session, vulnerabilidad_id: int):
    return db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.id == vulnerabilidad_id).first()

def create_vulnerabilidad_climatica(db: Session, vulnerabilidad_data):
    vulnerabilidad = VulnerabilidadClimatica(**vulnerabilidad_data.dict())
    db.add(vulnerabilidad)
    db.commit()
    db.refresh(vulnerabilidad)
    return vulnerabilidad

def update_vulnerabilidad_climatica(db: Session, vulnerabilidad_id: int, vulnerabilidad_data):
    vulnerabilidad = db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.id == vulnerabilidad_id).first()
    if vulnerabilidad:
        for key, value in vulnerabilidad_data.dict(exclude_unset=True).items():
            setattr(vulnerabilidad, key, value)
        db.commit()
        db.refresh(vulnerabilidad)
    return vulnerabilidad

def delete_vulnerabilidad_climatica(db: Session, vulnerabilidad_id: int):
    vulnerabilidad = db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.id == vulnerabilidad_id).first()
    if vulnerabilidad:
        db.delete(vulnerabilidad)
        db.commit()
        return True
    return False

# GeolocalizacionProductor
def get_geolocalizaciones_productor(db: Session):
    return db.query(GeolocalizacionProductor).all()

def get_geolocalizacion_productor(db: Session, geoloc_id: int):
    return db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.id == geoloc_id).first()

def create_geolocalizacion_productor(db: Session, geoloc_data):
    geoloc = GeolocalizacionProductor(**geoloc_data.dict())
    db.add(geoloc)
    db.commit()
    db.refresh(geoloc)
    return geoloc

def update_geolocalizacion_productor(db: Session, geoloc_id: int, geoloc_data):
    geoloc = db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.id == geoloc_id).first()
    if geoloc:
        for key, value in geoloc_data.dict(exclude_unset=True).items():
            setattr(geoloc, key, value)
        db.commit()
        db.refresh(geoloc)
    return geoloc

def delete_geolocalizacion_productor(db: Session, geoloc_id: int):
    geoloc = db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.id == geoloc_id).first()
    if geoloc:
        db.delete(geoloc)
        db.commit()
        return True
    return False

# CRUD para Consentimiento
def get_consentimientos(db: Session):
    return db.query(Consentimiento).all()

def get_consentimiento(db: Session, consentimiento_id: int):
    return db.query(Consentimiento).filter(Consentimiento.id == consentimiento_id).first()

def create_consentimiento(db: Session, consentimiento_data):
    consentimiento = Consentimiento(**consentimiento_data.dict())
    db.add(consentimiento)
    db.commit()
    db.refresh(consentimiento)
    return consentimiento

def update_consentimiento(db: Session, consentimiento_id: int, consentimiento_data):
    consentimiento = db.query(Consentimiento).filter(Consentimiento.id == consentimiento_id).first()
    if consentimiento:
        for key, value in consentimiento_data.dict(exclude_unset=True).items():
            setattr(consentimiento, key, value)
        db.commit()
        db.refresh(consentimiento)
    return consentimiento

def delete_consentimiento(db: Session, consentimiento_id: int):
    consentimiento = db.query(Consentimiento).filter(Consentimiento.id == consentimiento_id).first()
    if consentimiento:
        db.delete(consentimiento)
        db.commit()
        return True
    return False

# CRUD para PerfilSocioeconomico
def get_perfiles_socioeconomicos(db: Session):
    return db.query(PerfilSocioeconomico).all()

def get_perfil_socioeconomico(db: Session, perfil_id: int):
    return db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.id == perfil_id).first()

def create_perfil_socioeconomico(db: Session, perfil_data):
    perfil = PerfilSocioeconomico(**perfil_data.dict())
    db.add(perfil)
    db.commit()
    db.refresh(perfil)
    return perfil

def update_perfil_socioeconomico(db: Session, perfil_id: int, perfil_data):
    perfil = db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.id == perfil_id).first()
    if perfil:
        for key, value in perfil_data.dict(exclude_unset=True).items():
            setattr(perfil, key, value)
        db.commit()
        db.refresh(perfil)
    return perfil

def delete_perfil_socioeconomico(db: Session, perfil_id: int):
    perfil = db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.id == perfil_id).first()
    if perfil:
        db.delete(perfil)
        db.commit()
        return True
    return False

# CRUD para SeguridadAlimentaria
def get_seguridad_alimentaria(db: Session):
    return db.query(SeguridadAlimentaria).all()

def get_seguridad_alimentaria_by_id(db: Session, seguridad_id: int):
    return db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.id == seguridad_id).first()

def create_seguridad_alimentaria(db: Session, seguridad_data):
    seguridad = SeguridadAlimentaria(**seguridad_data.dict())
    db.add(seguridad)
    db.commit()
    db.refresh(seguridad)
    return seguridad

def update_seguridad_alimentaria(db: Session, seguridad_id: int, seguridad_data):
    seguridad = db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.id == seguridad_id).first()
    if seguridad:
        for key, value in seguridad_data.dict(exclude_unset=True).items():
            setattr(seguridad, key, value)
        db.commit()
        db.refresh(seguridad)
    return seguridad

def delete_seguridad_alimentaria(db: Session, seguridad_id: int):
    seguridad = db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.id == seguridad_id).first()
    if seguridad:
        db.delete(seguridad)
        db.commit()
        return True
    return False
