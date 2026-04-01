from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.orm import Session
from database import get_db

from models.social import Consentimiento, GeolocalizacionProductor, Lengua, Notificacion, PerfilSocioeconomico, Productor, ProductorLengua, ProductorPractica, PuebloOriginario, RedIntercambio, SeguridadAlimentaria, TipoProductor, VulnerabilidadClimatica 

from models.agronomico import PracticaAgricola, TipoPractica

import schemas.social as schemes
import schemas.agronomico as agronomico_schemes

router = APIRouter()

# =================== CATALOGO: TIPO PRODUCTOR ===================
@router.get("/tipo_productor")
def listar_tipo_productor(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoProductor)
    total = query.count()
    tipos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": tipos}

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
@router.get("/lengua")
def listar_lenguas(
    productor_id: int = Query(None),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Lengua)
    if productor_id is not None:
        query = query.join(ProductorLengua).filter(ProductorLengua.productor_id == productor_id)
    total = query.count()
    lenguas = query.offset(offset).limit(limit).all()
    return {"count": total, "results": lenguas}

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

# =================== SOCIAL: PRODUCTOR ===================
@router.get("/productor", response_model=list[schemes.ProductorOut])
def listar_productores(db: Session = Depends(get_db)):
    return db.query(Productor).all()

@router.get("/productor/{productor_id}", response_model=schemes.ProductorOut)
def obtener_productor(productor_id: int, db: Session = Depends(get_db)):
    productor = db.query(Productor).filter(Productor.id == productor_id).first()
    if not productor:
        raise HTTPException(status_code=404, detail="Productor no encontrado")
    return productor

@router.post("/productor", response_model=schemes.ProductorOut)
def crear_productor(productor: schemes.ProductorCreate, db: Session = Depends(get_db)):
    db_productor = Productor(**productor.dict())
    db.add(db_productor)
    db.commit()
    db.refresh(db_productor)
    return db_productor

@router.put("/productor/{productor_id}", response_model=schemes.ProductorOut)
def actualizar_productor(productor_id: int, productor: schemes.ProductorUpdate, db: Session = Depends(get_db)):
    actualizado = db.query(Productor).filter(Productor.id == productor_id).first()
    if actualizado:
        for key, value in productor.dict(exclude_unset=True).items():
            setattr(actualizado, key, value)
        db.commit()
        db.refresh(actualizado)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Productor no encontrado")
    return actualizado

@router.delete("/productor/{productor_id}")
def eliminar_productor(productor_id: int, db: Session = Depends(get_db)):
    eliminado = db.query(Productor).filter(Productor.id == productor_id).first()
    if not eliminado:
        raise HTTPException(status_code=404, detail="Productor no encontrado")
    db.delete(eliminado)
    db.commit()
    return {"ok": True}

@router.get("/practica_agricola", response_model=list[agronomico_schemes.PracticaAgricolaConTipo])
def listar_practicas_agricolas(productor_id: int = Query(None), db: Session = Depends(get_db)):
    if productor_id is not None:
        practicas = (
            db.query(PracticaAgricola)
            .join(ProductorPractica, PracticaAgricola.id == ProductorPractica.practica_id)
            .filter(ProductorPractica.productor_id == productor_id)
            .all()
        )
    else:
        practicas = db.query(PracticaAgricola).all()

    resultado = []
    for practica in practicas:
        tipo = db.query(TipoPractica).filter(TipoPractica.id == practica.tipo_id).first()
        practica_dict = {
            'id': practica.id,
            'nombre': practica.nombre,
            'descripcion': practica.descripcion,
            'tipo_practica': {
                'nombre': tipo.nombre if tipo else None,
                'descripcion': getattr(tipo, 'descripcion', None)
            }
        }
        resultado.append(practica_dict)
    return resultado

# ProductorPractica endpoints
@router.get("/productores_practica", response_model=list[schemes.ProductorPracticaOut])
def listar_productores_practica(db: Session = Depends(get_db)):
    return db.query(ProductorPractica).all()

@router.get("/productores_practica/{practica_id}", response_model=list[agronomico_schemes.PracticaAgricolaConTipo])
def obtener_productor_practica(practica_id: int, db: Session = Depends(get_db)):
    practica = db.query(ProductorPractica).filter(ProductorPractica.id == practica_id).first()
    if not practica:
        raise HTTPException(status_code=404, detail="Productor práctica no encontrado")
    return practica

@router.post("/productores_practica", response_model=schemes.ProductorPracticaOut)
def crear_productor_practica(practica: schemes.ProductorPracticaCreate, db: Session = Depends(get_db)):
    db_practica = ProductorPractica(**practica.dict())
    db.add(db_practica)
    db.commit()
    db.refresh(db_practica)
    return db_practica

@router.put("/productores_practica/{practica_id}", response_model=schemes.ProductorPracticaOut)
def actualizar_productor_practica(practica_id: int, practica: schemes.ProductorPracticaUpdate, db: Session = Depends(get_db)):
    db_practica = db.query(ProductorPractica).filter(ProductorPractica.id == practica_id).first()
    if not db_practica:
        raise HTTPException(status_code=404, detail="Productor práctica no encontrado")
    for key, value in practica.dict(exclude_unset=True).items():
        setattr(db_practica, key, value)
    db.commit()
    db.refresh(db_practica)
    return db_practica

@router.delete("/productores_practica/{practica_id}")
def eliminar_productor_practica(practica_id: int, db: Session = Depends(get_db)):
    db_practica = db.query(ProductorPractica).filter(ProductorPractica.id == practica_id).first()
    if not db_practica:
        raise HTTPException(status_code=404, detail="Productor práctica no encontrado")
    db.delete(db_practica)
    db.commit()
    return {"ok": True}


# ProductorLengua endpoints
@router.get("/productores_lengua", response_model=list[schemes.ProductorLenguaOut])
def listar_productores_lengua(db: Session = Depends(get_db)):
    return db.query(ProductorLengua).all()

@router.get("/productores_lengua/{lengua_id}", response_model=schemes.ProductorLenguaOut)
def obtener_productor_lengua(lengua_id: int, db: Session = Depends(get_db)):
    lengua = db.query(ProductorLengua).filter(ProductorLengua.id == lengua_id).first()
    if not lengua:
        raise HTTPException(status_code=404, detail="Productor lengua no encontrado")
    return lengua

@router.post("/productores_lengua", response_model=schemes.ProductorLenguaOut)
def crear_productor_lengua(lengua: schemes.ProductorLenguaCreate, db: Session = Depends(get_db)):
    db_lengua = ProductorLengua(**lengua.dict())
    db.add(db_lengua)
    db.commit()
    db.refresh(db_lengua)
    return db_lengua

@router.put("/productores_lengua/{lengua_id}", response_model=schemes.ProductorLenguaOut)
def actualizar_productor_lengua(lengua_id: int, lengua: schemes.ProductorLenguaUpdate, db: Session = Depends(get_db)):
    db_lengua = db.query(ProductorLengua).filter(ProductorLengua.id == lengua_id).first()
    if not db_lengua:
        raise HTTPException(status_code=404, detail="Productor lengua no encontrado")
    for key, value in lengua.dict(exclude_unset=True).items():
        setattr(db_lengua, key, value)
    db.commit()
    db.refresh(db_lengua)
    return db_lengua

@router.delete("/productores_lengua/{lengua_id}")
def eliminar_productor_lengua(lengua_id: int, db: Session = Depends(get_db)):
    db_lengua = db.query(ProductorLengua).filter(ProductorLengua.id == lengua_id).first()
    if not db_lengua:
        raise HTTPException(status_code=404, detail="Productor lengua no encontrado")
    db.delete(db_lengua)
    db.commit()
    return {"ok": True}


# RedIntercambio endpoints
@router.get("/red_intercambio", response_model=list[schemes.RedIntercambioOut])
def listar_redes_intercambio(productor_id: int = Query(None), db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(RedIntercambio).filter(RedIntercambio.productor_id == productor_id).all()
    return db.query(RedIntercambio).all()

@router.get("/red_intercambio/{red_id}", response_model=schemes.RedIntercambioOut)
def obtener_red_intercambio(red_id: int, db: Session = Depends(get_db)):
    red = db.query(RedIntercambio).filter(RedIntercambio.id == red_id).first()
    if not red:
        raise HTTPException(status_code=404, detail="Red de intercambio no encontrada")
    return red

@router.post("/red_intercambio", response_model=schemes.RedIntercambioOut)
def crear_red_intercambio(red: schemes.RedIntercambioCreate, db: Session = Depends(get_db)):
    db_red = RedIntercambio(**red.dict())
    db.add(db_red)
    db.commit()
    db.refresh(db_red)
    return db_red

@router.put("/red_intercambio/{red_id}", response_model=schemes.RedIntercambioOut)
def actualizar_red_intercambio(red_id: int, red: schemes.RedIntercambioUpdate, db: Session = Depends(get_db)):
    db_red = db.query(RedIntercambio).filter(RedIntercambio.id == red_id).first()
    if not db_red:
        raise HTTPException(status_code=404, detail="Red de intercambio no encontrada")
    for key, value in red.dict(exclude_unset=True).items():
        setattr(db_red, key, value)
    db.commit()
    db.refresh(db_red)
    return db_red

@router.delete("/red_intercambio/{red_id}")
def eliminar_red_intercambio(red_id: int, db: Session = Depends(get_db)):
    db_red = db.query(RedIntercambio).filter(RedIntercambio.id == red_id).first()
    if not db_red:
        raise HTTPException(status_code=404, detail="Red de intercambio no encontrada")
    db.delete(db_red)
    db.commit()
    return {"ok": True}


# VulnerabilidadClimatica endpoints
@router.get("/climatica", response_model=list[schemes.VulnerabilidadClimaticaOut])
def listar_climaticas(productor_id: int = Query(None), db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.productor_id == productor_id).all()
    return db.query(VulnerabilidadClimatica).all()

@router.get("/climatica/{vulnerabilidad_id}", response_model=schemes.VulnerabilidadClimaticaOut)
def obtener_climatica(vulnerabilidad_id: int, db: Session = Depends(get_db)):
    vulnerabilidad = db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.id == vulnerabilidad_id).first()
    if not vulnerabilidad:
        raise HTTPException(status_code=404, detail="Vulnerabilidad climática no encontrada")
    return vulnerabilidad

@router.post("/climatica", response_model=schemes.VulnerabilidadClimaticaOut)
def crear_vulnerabilidad_climatica(vulnerabilidad: schemes.VulnerabilidadClimaticaCreate, db: Session = Depends(get_db)):
    db_vulnerabilidad = VulnerabilidadClimatica(**vulnerabilidad.dict())
    db.add(db_vulnerabilidad)
    db.commit()
    db.refresh(db_vulnerabilidad)
    return db_vulnerabilidad

@router.put("/climatica/{vulnerabilidad_id}", response_model=schemes.VulnerabilidadClimaticaOut)
def actualizar_climatica(vulnerabilidad_id: int, vulnerabilidad: schemes.VulnerabilidadClimaticaUpdate, db: Session = Depends(get_db)):
    db_vulnerabilidad = db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.id == vulnerabilidad_id).first()
    if not db_vulnerabilidad:
        raise HTTPException(status_code=404, detail="Vulnerabilidad climática no encontrada")
    for key, value in vulnerabilidad.dict(exclude_unset=True).items():
        setattr(db_vulnerabilidad, key, value)
    db.commit()
    db.refresh(db_vulnerabilidad)
    return db_vulnerabilidad

@router.delete("/climatica/{vulnerabilidad_id}")
def eliminar_climatica(vulnerabilidad_id: int, db: Session = Depends(get_db)):
    db_vulnerabilidad = db.query(VulnerabilidadClimatica).filter(VulnerabilidadClimatica.id == vulnerabilidad_id).first()
    if not db_vulnerabilidad:
        raise HTTPException(status_code=404, detail="Vulnerabilidad climática no encontrada")
    db.delete(db_vulnerabilidad)
    db.commit()
    return {"ok": True}


# GeolocalizacionProductor endpoints
@router.get("/geo/", response_model=list[schemes.GeolocalizacionProductorOut])
def listar_geo_productor(productor_id: int = Query(None), db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.productor_id == productor_id).all()
    return db.query(GeolocalizacionProductor).all()


@router.get("/geo/{geoloc_id}", response_model=schemes.GeolocalizacionProductorOut)
def obtener_geo_productor(geoloc_id: int, db: Session = Depends(get_db)):
    geoloc = db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.id == geoloc_id).first()
    if not geoloc:
        raise HTTPException(status_code=404, detail="Geolocalización de productor no encontrada")
    return geoloc

@router.post("/geo", response_model=schemes.GeolocalizacionProductorOut)
def crear_geo_productor(geoloc: schemes.GeolocalizacionProductorCreate, db: Session = Depends(get_db)):
    db_geoloc = GeolocalizacionProductor(**geoloc.dict())
    db.add(db_geoloc)
    db.commit()
    db.refresh(db_geoloc)
    return db_geoloc

@router.put("/geo/{geoloc_id}", response_model=schemes.GeolocalizacionProductorOut)
def actualizar_geo_productor(geoloc_id: int, geoloc: schemes.GeolocalizacionProductorUpdate, db: Session = Depends(get_db)):
    db_geoloc = db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.id == geoloc_id).first()
    if not db_geoloc:
        raise HTTPException(status_code=404, detail="Geolocalización de productor no encontrada")
    for key, value in geoloc.dict(exclude_unset=True).items():
        setattr(db_geoloc, key, value)
    db.commit()
    db.refresh(db_geoloc)
    return db_geoloc

@router.delete("/geo/{geoloc_id}")
def eliminar_geo_productor(geoloc_id: int, db: Session = Depends(get_db)):
    db_geoloc = db.query(GeolocalizacionProductor).filter(GeolocalizacionProductor.id == geoloc_id).first()
    if not db_geoloc:
        raise HTTPException(status_code=404, detail="Geolocalización de productor no encontrada")
    db.delete(db_geoloc)
    db.commit()
    return {"ok": True}


# Consentimiento endpoints
@router.get("/consentimiento", response_model=list[schemes.ConsentimientoOut])
def listar_consentimientos(db: Session = Depends(get_db)):
    return db.query(Consentimiento).all()

@router.get("/consentimiento/{consentimiento_id}", response_model=schemes.ConsentimientoOut)
def obtener_consentimiento(consentimiento_id: int, db: Session = Depends(get_db)):
    consentimiento = db.query(Consentimiento).filter(Consentimiento.id == consentimiento_id).first()
    if not consentimiento:
        raise HTTPException(status_code=404, detail="Consentimiento no encontrado")
    return consentimiento

@router.post("/consentimiento", response_model=schemes.ConsentimientoOut)
def crear_consentimiento(consentimiento: schemes.ConsentimientoCreate, db: Session = Depends(get_db)):
    db_consentimiento = Consentimiento(**consentimiento.dict())
    db.add(db_consentimiento)
    db.commit()
    db.refresh(db_consentimiento)
    return db_consentimiento

@router.put("/consentimiento/{consentimiento_id}", response_model=schemes.ConsentimientoOut)
def actualizar_consentimiento(consentimiento_id: int, consentimiento: schemes.ConsentimientoUpdate, db: Session = Depends(get_db)):
    db_consentimiento = db.query(Consentimiento).filter(Consentimiento.id == consentimiento_id).first()
    if not db_consentimiento:
        raise HTTPException(status_code=404, detail="Consentimiento no encontrado")
    for key, value in consentimiento.dict(exclude_unset=True).items():
        setattr(db_consentimiento, key, value)
    db.commit()
    db.refresh(db_consentimiento)
    return db_consentimiento

@router.delete("/consentimiento/{consentimiento_id}")
def eliminar_consentimiento(consentimiento_id: int, db: Session = Depends(get_db)):
    db_consentimiento = db.query(Consentimiento).filter(Consentimiento.id == consentimiento_id).first()
    if not db_consentimiento:
        raise HTTPException(status_code=404, detail="Consentimiento no encontrado")
    db.delete(db_consentimiento)
    db.commit()
    return {"ok": True}


# PerfilSocioeconomico endpoints
@router.get("/socioeconomico", response_model=list[schemes.PerfilSocioeconomicoOut])
def listar_perfiles_socioeconomicos(productor_id: int = Query(None), db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.productor_id == productor_id).all()
    return db.query(PerfilSocioeconomico).all()

@router.get("/socioeconomico/{perfil_id}", response_model=schemes.PerfilSocioeconomicoOut)
def obtener_perfil_socioeconomico(perfil_id: int, db: Session = Depends(get_db)):
    perfil = db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.id == perfil_id).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil socioeconómico no encontrado")
    return perfil

@router.post("/socioeconomico", response_model=schemes.PerfilSocioeconomicoOut)
def crear_perfil_socioeconomico(perfil: schemes.PerfilSocioeconomicoCreate, db: Session = Depends(get_db)):
    db_perfil = PerfilSocioeconomico(**perfil.dict())
    db.add(db_perfil)
    db.commit()
    db.refresh(db_perfil)
    return db_perfil

@router.put("/socioeconomico/{perfil_id}", response_model=schemes.PerfilSocioeconomicoOut)
def actualizar_perfil_socioeconomico(perfil_id: int, perfil: schemes.PerfilSocioeconomicoUpdate, db: Session = Depends(get_db)):
    db_perfil = db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.id == perfil_id).first()
    if not db_perfil:
        raise HTTPException(status_code=404, detail="Perfil socioeconómico no encontrado")
    for key, value in perfil.dict(exclude_unset=True).items():
        setattr(db_perfil, key, value)
    db.commit()
    db.refresh(db_perfil)
    return db_perfil

@router.delete("/socioeconomico/{perfil_id}")
def eliminar_perfil_socioeconomico(perfil_id: int, db: Session = Depends(get_db)):
    db_perfil = db.query(PerfilSocioeconomico).filter(PerfilSocioeconomico.id == perfil_id).first()
    if not db_perfil:
        raise HTTPException(status_code=404, detail="Perfil socioeconómico no encontrado")
    db.delete(db_perfil)
    db.commit()
    return {"ok": True}


# ELCSA endpoints
@router.get("/elcsa", response_model=list[schemes.SeguridadAlimentariaOut])
def listar_seguridad_alimentaria(productor_id: int = Query(None), db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.productor_id == productor_id).all()
    return db.query(SeguridadAlimentaria).all()

@router.get("/elcsa/{seguridad_id}", response_model=schemes.SeguridadAlimentariaOut)
def obtener_seguridad_alimentaria(seguridad_id: int, db: Session = Depends(get_db)):
    seguridad = db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.id == seguridad_id).first()
    if not seguridad:
        raise HTTPException(status_code=404, detail="Seguridad alimentaria no encontrada")
    return seguridad

@router.post("/elcsa", response_model=schemes.SeguridadAlimentariaOut)
def crear_seguridad_alimentaria(seguridad: schemes.SeguridadAlimentariaCreate, db: Session = Depends(get_db)):
    db_seguridad = SeguridadAlimentaria(**seguridad.dict())
    db.add(db_seguridad)
    db.commit()
    db.refresh(db_seguridad)
    return db_seguridad

@router.put("/elcsa/{seguridad_id}", response_model=schemes.SeguridadAlimentariaOut)
def actualizar_seguridad_alimentaria(seguridad_id: int, seguridad: schemes.SeguridadAlimentariaUpdate, db: Session = Depends(get_db)):
    db_seguridad = db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.id == seguridad_id).first()
    if not db_seguridad:
        raise HTTPException(status_code=404, detail="Seguridad alimentaria no encontrada")
    for key, value in seguridad.dict(exclude_unset=True).items():
        setattr(db_seguridad, key, value)
    db.commit()
    db.refresh(db_seguridad)
    return db_seguridad

@router.delete("/elcsa/{seguridad_id}")
def eliminar_seguridad_alimentaria(seguridad_id: int, db: Session = Depends(get_db)):
    db_seguridad = db.query(SeguridadAlimentaria).filter(SeguridadAlimentaria.id == seguridad_id).first()
    if not db_seguridad:
        raise HTTPException(status_code=404, detail="Seguridad alimentaria no encontrada")
    db.delete(db_seguridad)
    db.commit()
    return {"ok": True}


# =================== NOTIFICACIONES ===================
@router.get("/notificaciones", response_model=list[schemes.NotificacionOut])
def listar_notificaciones(
    usuario_id: int = Query(None),
    leida: bool = Query(None),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Notificacion)
    if usuario_id is not None:
        query = query.filter(Notificacion.usuario_id == usuario_id)
    if leida is not None:
        query = query.filter(Notificacion.leida == leida)
    total = query.count()
    notificaciones = query.order_by(Notificacion.fecha_envio.desc()).offset(offset).limit(limit).all()
    return notificaciones

@router.get("/notificaciones/{notificacion_id}", response_model=schemes.NotificacionOut)
def obtener_notificacion(notificacion_id: int, db: Session = Depends(get_db)):
    notificacion = db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()
    if not notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return notificacion

@router.post("/notificaciones", response_model=schemes.NotificacionOut, status_code=201)
def crear_notificacion(notificacion: schemes.NotificacionCreate, db: Session = Depends(get_db)):
    db_notificacion = Notificacion(**notificacion.dict())
    db.add(db_notificacion)
    db.commit()
    db.refresh(db_notificacion)
    return db_notificacion

@router.put("/notificaciones/{notificacion_id}", response_model=schemes.NotificacionOut)
def actualizar_notificacion(notificacion_id: int, notificacion: schemes.NotificacionUpdate, db: Session = Depends(get_db)):
    db_notificacion = db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()
    if not db_notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    for key, value in notificacion.dict(exclude_unset=True).items():
        setattr(db_notificacion, key, value)
    db.commit()
    db.refresh(db_notificacion)
    return db_notificacion

@router.patch("/notificaciones/{notificacion_id}/marcar_leida", response_model=schemes.NotificacionOut)
def marcar_notificacion_leida(notificacion_id: int, db: Session = Depends(get_db)):
    db_notificacion = db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()
    if not db_notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    db_notificacion.leida = True
    db.commit()
    db.refresh(db_notificacion)
    return db_notificacion

@router.delete("/notificaciones/{notificacion_id}")
def eliminar_notificacion(notificacion_id: int, db: Session = Depends(get_db)):
    db_notificacion = db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()
    if not db_notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    db.delete(db_notificacion)
    db.commit()
    return {"ok": True}
