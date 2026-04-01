from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from database import get_db

from models.cultural import TipoRitualAgricola, TipoNarrativaOral, CategoriaSaberAgricola, Ocasion, MecanismoTransmision, VinculoMaiz

import schemas.cultural as schemes

from schemas.social import GastronomiaTradicionalCreate, GastronomiaTradicionalOut, GastronomiaTradicionalUpdate, IdentidadCulturalCreate, IdentidadCulturalOut, IdentidadCulturalUpdate, NarrativaOralCreate, NarrativaOralOut, NarrativaOralUpdate, NombreLenguaOriginariaCreate, NombreLenguaOriginariaOut, NombreLenguaOriginariaUpdate, RitualAgricolaCreate, RitualAgricolaOut, RitualAgricolaUpdate, SaberTradicionalCreate, SaberTradicionalOut, SaberTradicionalUpdate, TransmisionConocimientoCreate, TransmisionConocimientoOut, TransmisionConocimientoUpdate

from models.cultural import GastronomiaTradicional, IdentidadCultural, NarrativaOral, NombreLenguaOriginaria, RitualAgricola, SaberTradicional, TransmisionConocimiento

router = APIRouter()

# =================== CATALOGO: TIPO RITUAL AGRICOLA ===================
from fastapi import Query

@router.get("/tipo_ritual_agricola")
def listar_tipo_ritual_agricola(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoRitualAgricola)
    total = query.count()
    tipos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": tipos}

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

@router.delete("/tipo_ritual_agricola/{ritual_id}")
def eliminar_tipo_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    db_ritual = db.query(TipoRitualAgricola).filter(TipoRitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    db.delete(db_ritual)
    db.commit()
    return {"ok": True}

# =================== CATALOGO: TIPO NARRATIVA ORAL ===================
@router.get("/tipo_narrativa_oral")
def listar_tipo_narrativa_oral(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(TipoNarrativaOral)
    total = query.count()
    tipos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": tipos}

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

# =================== CATALOGO: CATEGORIA SABER AGRICOLA ===================
@router.get("/categoria_saber_agricola")
def listar_categoria_saber_agricola(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(CategoriaSaberAgricola)
    total = query.count()
    categorias = query.offset(offset).limit(limit).all()
    return {"count": total, "results": categorias}

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

# =================== CATALOGO: OCASION ===================
from fastapi import Query

@router.get("/ocasion")
def listar_ocasion(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Ocasion)
    total = query.count()
    ocasiones = query.offset(offset).limit(limit).all()
    return {"count": total, "results": ocasiones}

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

# ===================CATALOGO: MECANISMO TRANSMISION ===================
@router.get("/mecanismo_transmision")
def listar_mecanismo_transmision(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(MecanismoTransmision)
    total = query.count()
    mecanismos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": mecanismos}

@router.get("/mecanismo_transmision/{transmision_id}", response_model=schemes.MecanismoTransmision)
def obtener_mecanismo_transmision(transmision_id: int, db: Session = Depends(get_db)):
    mecanismo = db.query(MecanismoTransmision).filter(MecanismoTransmision.id == transmision_id).first()
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

@router.put("/mecanismo_transmision/{transmision_id}", response_model=schemes.MecanismoTransmision)
def actualizar_mecanismo_transmision(transmision_id: int, mecanismo: schemes.MecanismoTransmisionCreate, db: Session = Depends(get_db)):
    db_mecanismo = db.query(MecanismoTransmision).filter(MecanismoTransmision.id == transmision_id).first()
    if not db_mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    for key, value in mecanismo.dict().items():
        setattr(db_mecanismo, key, value)
    db.commit()
    db.refresh(db_mecanismo)
    return db_mecanismo

@router.delete("/mecanismo_transmision/{transmision_id}")
def eliminar_mecanismo_transmision(transmision_id: int, db: Session = Depends(get_db)):
    db_mecanismo = db.query(MecanismoTransmision).filter(MecanismoTransmision.id == transmision_id).first()
    if not db_mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    db.delete(db_mecanismo)
    db.commit()
    return {"ok": True}

# =================== VINCULO MAIZ ===================
@router.get("/vinculo_maiz")
def listar_vinculo_maiz(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(VinculoMaiz)
    total = query.count()
    vinculos = query.offset(offset).limit(limit).all()
    return {"count": total, "results": vinculos}

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


# RitualAgricola CRUD inline
@router.get("/rituales_agricolas", response_model=list[RitualAgricolaOut])
def listar_rituales_agricolas(db: Session = Depends(get_db)):
    return db.query(RitualAgricola).all()

@router.get("/rituales_agricolas/{ritual_id}", response_model=RitualAgricolaOut)
def obtener_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    ritual = db.query(RitualAgricola).filter(RitualAgricola.id == ritual_id).first()
    if not ritual:
        raise HTTPException(status_code=404, detail="Ritual agrícola no encontrado")
    return ritual

@router.post("/rituales_agricolas", response_model=RitualAgricolaOut)
def crear_ritual_agricola(ritual: RitualAgricolaCreate, db: Session = Depends(get_db)):
    db_ritual = RitualAgricola(**ritual.dict())
    db.add(db_ritual)
    db.commit()
    db.refresh(db_ritual)
    return db_ritual

@router.put("/rituales_agricolas/{ritual_id}", response_model=RitualAgricolaOut)
def actualizar_ritual_agricola(ritual_id: int, ritual: RitualAgricolaUpdate, db: Session = Depends(get_db)):
    db_ritual = db.query(RitualAgricola).filter(RitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Ritual agrícola no encontrado")
    for key, value in ritual.dict(exclude_unset=True).items():
        setattr(db_ritual, key, value)
    db.commit()
    db.refresh(db_ritual)
    return db_ritual

@router.delete("/rituales_agricolas/{ritual_id}")
def eliminar_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    db_ritual = db.query(RitualAgricola).filter(RitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Ritual agrícola no encontrado")
    db.delete(db_ritual)
    db.commit()
    return {"ok": True}

# =================== CULTURAL: NARRATIVA ORAL ===================
@router.get("/narrativa", response_model=list[NarrativaOralOut])
def listar_narrativas_orales(productor_id: int = None, db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(NarrativaOral).filter(NarrativaOral.productor_id == productor_id).all()
    return db.query(NarrativaOral).all()

@router.get("/narrativa/{narrativa_id}", response_model=NarrativaOralOut)
def obtener_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    narrativa = db.query(NarrativaOral).filter(NarrativaOral.id == narrativa_id).first()
    if not narrativa:
        raise HTTPException(status_code=404, detail="Narrativa oral no encontrada")
    return narrativa

@router.post("/narrativa", response_model=NarrativaOralOut)
def crear_narrativa_oral(narrativa: NarrativaOralCreate, db: Session = Depends(get_db)):
    db_narrativa = NarrativaOral(**narrativa.dict())
    db.add(db_narrativa)
    db.commit()
    db.refresh(db_narrativa)
    return db_narrativa

@router.put("/narrativa/{narrativa_id}", response_model=NarrativaOralOut)
def actualizar_narrativa_oral(narrativa_id: int, narrativa: NarrativaOralUpdate, db: Session = Depends(get_db)):
    db_narrativa = db.query(NarrativaOral).filter(NarrativaOral.id == narrativa_id).first()
    if not db_narrativa:
        raise HTTPException(status_code=404, detail="Narrativa oral no encontrada")
    for key, value in narrativa.dict(exclude_unset=True).items():
        setattr(db_narrativa, key, value)
    db.commit()
    db.refresh(db_narrativa)
    return db_narrativa

@router.delete("/narrativa/{narrativa_id}")
def eliminar_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    db_narrativa = db.query(NarrativaOral).filter(NarrativaOral.id == narrativa_id).first()
    if not db_narrativa:
        raise HTTPException(status_code=404, detail="Narrativa oral no encontrada")
    db.delete(db_narrativa)
    db.commit()
    return {"ok": True}

# ================== CULTURAL: GASTRONOMÍA TRADICIONAL ===================
@router.get("/gastronomia", response_model=list[GastronomiaTradicionalOut])
def listar_gastronomias_tradicionales(productor_id: int = None, db: Session = Depends(get_db)):
    if productor_id is not None:
        # Obtener los IDs de platillos asociados al productor
        from models.social import gastronomia_productor
        platillo_ids = [row.gastronomia_id for row in db.execute(
            gastronomia_productor.select().where(gastronomia_productor.c.productor_id == productor_id)
        )]
        if not platillo_ids:
            return []
        return db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id.in_(platillo_ids)).all()
    return db.query(GastronomiaTradicional).all()

@router.get("/gastronomia/{gastronomia_id}", response_model=GastronomiaTradicionalOut)
def obtener_gastronomia_tradicional(gastronomia_id: int, db: Session = Depends(get_db)):
    gastronomia = db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id == gastronomia_id).first()
    if not gastronomia:
        raise HTTPException(status_code=404, detail="Gastronomía tradicional no encontrada")
    return gastronomia

@router.post("/gastronomia", response_model=GastronomiaTradicionalOut)
def crear_gastronomia_tradicional(gastronomia: GastronomiaTradicionalCreate, db: Session = Depends(get_db)):
    db_gastronomia = GastronomiaTradicional(**gastronomia.dict())
    db.add(db_gastronomia)
    db.commit()
    db.refresh(db_gastronomia)
    return db_gastronomia

@router.put("/gastronomia/{gastronomia_id}", response_model=GastronomiaTradicionalOut)
def actualizar_gastronomia_tradicional(gastronomia_id: int, gastronomia: GastronomiaTradicionalUpdate, db: Session = Depends(get_db)):
    db_gastronomia = db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id == gastronomia_id).first()
    if not db_gastronomia:
        raise HTTPException(status_code=404, detail="Gastronomía tradicional no encontrada")
    for key, value in gastronomia.dict(exclude_unset=True).items():
        setattr(db_gastronomia, key, value)
    db.commit()
    db.refresh(db_gastronomia)
    return db_gastronomia

@router.delete("/gastronomia/{gastronomia_id}")
def eliminar_gastronomia_tradicional(gastronomia_id: int, db: Session = Depends(get_db)):
    db_gastronomia = db.query(GastronomiaTradicional).filter(GastronomiaTradicional.id == gastronomia_id).first()
    if not db_gastronomia:
        raise HTTPException(status_code=404, detail="Gastronomía tradicional no encontrada")
    db.delete(db_gastronomia)
    db.commit()
    return {"ok": True}

# ================== CULTURAL: TRANSMISION CONOCIMIENTO ===================
@router.get("/transmision", response_model=list[TransmisionConocimientoOut])
def listar_transmisiones_conocimiento(productor_id: int = None, db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(TransmisionConocimiento).filter(TransmisionConocimiento.productor_id == productor_id).all()
    return db.query(TransmisionConocimiento).all()

@router.get("/transmision/{transmision_id}", response_model=TransmisionConocimientoOut)
def obtener_transmision_conocimiento(transmision_id: int, db: Session = Depends(get_db)):
    transmision = db.query(TransmisionConocimiento).filter(TransmisionConocimiento.id == transmision_id).first()
    if not transmision:
        raise HTTPException(status_code=404, detail="Transmisión de conocimiento no encontrada")
    return transmision

@router.post("/transmision", response_model=TransmisionConocimientoOut)
def crear_transmision_conocimiento(transmision: TransmisionConocimientoCreate, db: Session = Depends(get_db)):
    db_transmision = TransmisionConocimiento(**transmision.dict())
    db.add(db_transmision)
    db.commit()
    db.refresh(db_transmision)
    return db_transmision

@router.put("/transmision/{transmision_id}", response_model=TransmisionConocimientoOut)
def actualizar_transmision_conocimiento(transmision_id: int, transmision: TransmisionConocimientoUpdate, db: Session = Depends(get_db)):
    db_transmision = db.query(TransmisionConocimiento).filter(TransmisionConocimiento.id == transmision_id).first()
    if not db_transmision:
        raise HTTPException(status_code=404, detail="Transmisión de conocimiento no encontrada")
    for key, value in transmision.dict(exclude_unset=True).items():
        setattr(db_transmision, key, value)
    db.commit()
    db.refresh(db_transmision)
    return db_transmision

@router.delete("/transmision/{transmision_id}")
def eliminar_transmision_conocimiento(transmision_id: int, db: Session = Depends(get_db)):
    db_transmision = db.query(TransmisionConocimiento).filter(TransmisionConocimiento.id == transmision_id).first()
    if not db_transmision:
        raise HTTPException(status_code=404, detail="Transmisión de conocimiento no encontrada")
    db.delete(db_transmision)
    db.commit()
    return {"ok": True}

# ================== CULTURAL: IDENTIDAD CULTURAL ===================
@router.get("/identidad", response_model=list[IdentidadCulturalOut])
def listar_identidades_culturales(productor_id: int = None, db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(IdentidadCultural).filter(IdentidadCultural.productor_id == productor_id).all()
    return db.query(IdentidadCultural).all()

@router.get("/identidad/{identidad_id}", response_model=IdentidadCulturalOut)
def obtener_identidad_cultural(identidad_id: int, db: Session = Depends(get_db)):
    identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if not identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    return identidad

@router.post("/identidad", response_model=IdentidadCulturalOut)
def crear_identidad_cultural(identidad: IdentidadCulturalCreate, db: Session = Depends(get_db)):
    db_identidad = IdentidadCultural(**identidad.dict())
    db.add(db_identidad)
    db.commit()
    db.refresh(db_identidad)
    return db_identidad

@router.put("/identidad/{identidad_id}", response_model=IdentidadCulturalOut)
def actualizar_identidad_cultural(identidad_id: int, identidad: IdentidadCulturalUpdate, db: Session = Depends(get_db)):
    db_identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if not db_identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    for key, value in identidad.dict(exclude_unset=True).items():
        setattr(db_identidad, key, value)
    db.commit()
    db.refresh(db_identidad)
    return db_identidad

@router.delete("/identidad/{identidad_id}")
def eliminar_identidad_cultural(identidad_id: int, db: Session = Depends(get_db)):
    db_identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if not db_identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    db.delete(db_identidad)
    db.commit()
    return {"ok": True}

@router.get("/identidad/{identidad_id}", response_model=IdentidadCulturalOut)
def obtener_identidad_cultural(identidad_id: int, db: Session = Depends(get_db)):
    identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if not identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    return identidad

@router.post("/identidad", response_model=IdentidadCulturalOut)
def crear_identidad_cultural(identidad: IdentidadCulturalCreate, db: Session = Depends(get_db)):
    db_identidad = IdentidadCultural(**identidad.dict())
    db.add(db_identidad)
    db.commit()
    db.refresh(db_identidad)
    return db_identidad

@router.put("/identidad/{identidad_id}", response_model=IdentidadCulturalOut)
def actualizar_identidad_cultural(identidad_id: int, identidad: IdentidadCulturalUpdate, db: Session = Depends(get_db)):
    db_identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if not db_identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    for key, value in identidad.dict(exclude_unset=True).items():
        setattr(db_identidad, key, value)
    db.commit()
    db.refresh(db_identidad)
    return db_identidad

@router.delete("/identidad/{identidad_id}")
def eliminar_identidad_cultural(identidad_id: int, db: Session = Depends(get_db)):
    db_identidad = db.query(IdentidadCultural).filter(IdentidadCultural.id == identidad_id).first()
    if not db_identidad:
        raise HTTPException(status_code=404, detail="Identidad cultural no encontrada")
    db.delete(db_identidad)
    db.commit()
    return {"ok": True}


# NombreLenguaOriginaria CRUD inline
@router.get("/nombres_lenguas_originarias", response_model=list[NombreLenguaOriginariaOut])
def listar_nombres_lenguas_originarias(db: Session = Depends(get_db)):
    return db.query(NombreLenguaOriginaria).all()

@router.get("/nombres_lenguas_originarias/{nombre_id}", response_model=NombreLenguaOriginariaOut)
def obtener_nombre_lengua_originaria(nombre_id: int, db: Session = Depends(get_db)):
    nombre = db.query(NombreLenguaOriginaria).filter(NombreLenguaOriginaria.id == nombre_id).first()
    if not nombre:
        raise HTTPException(status_code=404, detail="Nombre de lengua originaria no encontrado")
    return nombre

@router.post("/nombres_lenguas_originarias", response_model=NombreLenguaOriginariaOut)
def crear_nombre_lengua_originaria(nombre: NombreLenguaOriginariaCreate, db: Session = Depends(get_db)):
    db_nombre = NombreLenguaOriginaria(**nombre.dict())
    db.add(db_nombre)
    db.commit()
    db.refresh(db_nombre)
    return db_nombre

@router.put("/nombres_lenguas_originarias/{nombre_id}", response_model=NombreLenguaOriginariaOut)
def actualizar_nombre_lengua_originaria(nombre_id: int, nombre: NombreLenguaOriginariaUpdate, db: Session = Depends(get_db)):
    db_nombre = db.query(NombreLenguaOriginaria).filter(NombreLenguaOriginaria.id == nombre_id).first()
    if not db_nombre:
        raise HTTPException(status_code=404, detail="Nombre de lengua originaria no encontrado")
    for key, value in nombre.dict(exclude_unset=True).items():
        setattr(db_nombre, key, value)
    db.commit()
    db.refresh(db_nombre)
    return db_nombre

@router.delete("/nombres_lenguas_originarias/{nombre_id}")
def eliminar_nombre_lengua_originaria(nombre_id: int, db: Session = Depends(get_db)):
    db_nombre = db.query(NombreLenguaOriginaria).filter(NombreLenguaOriginaria.id == nombre_id).first()
    if not db_nombre:
        raise HTTPException(status_code=404, detail="Nombre de lengua originaria no encontrado")
    db.delete(db_nombre)
    db.commit()
    return {"ok": True}

# ================== CULTURAL: SABER TRADICIONAL ===================
@router.get("/saber_maiz", response_model=list[SaberTradicionalOut])
def listar_saberes_tradicionales(productor_id: int = None, db: Session = Depends(get_db)):
    if productor_id is not None:
        return db.query(SaberTradicional).filter(SaberTradicional.productor_id == productor_id).all()
    return db.query(SaberTradicional).all()

@router.get("/saber_maiz/{saber_id}", response_model=SaberTradicionalOut)
def obtener_saber_tradicional(saber_id: int, db: Session = Depends(get_db)):
    saber = db.query(SaberTradicional).filter(SaberTradicional.id == saber_id).first()
    if not saber:
        raise HTTPException(status_code=404, detail="Saber tradicional no encontrado")
    return saber

@router.post("/saber_maiz", response_model=SaberTradicionalOut)
def crear_saber_tradicional(saber: SaberTradicionalCreate, db: Session = Depends(get_db)):
    db_saber = SaberTradicional(**saber.dict())
    db.add(db_saber)
    db.commit()
    db.refresh(db_saber)
    return db_saber

@router.put("/saber_maiz/{saber_id}", response_model=SaberTradicionalOut)
def actualizar_saber_tradicional(saber_id: int, saber: SaberTradicionalUpdate, db: Session = Depends(get_db)):
    db_saber = db.query(SaberTradicional).filter(SaberTradicional.id == saber_id).first()
    if not db_saber:
        raise HTTPException(status_code=404, detail="Saber tradicional no encontrado")
    for key, value in saber.dict(exclude_unset=True).items():
        setattr(db_saber, key, value)
    db.commit()
    db.refresh(db_saber)
    return db_saber

@router.delete("/saber_maiz/{saber_id}")
def eliminar_saber_tradicional(saber_id: int, db: Session = Depends(get_db)):
    db_saber = db.query(SaberTradicional).filter(SaberTradicional.id == saber_id).first()
    if not db_saber:
        raise HTTPException(status_code=404, detail="Saber tradicional no encontrado")
    db.delete(db_saber)
    db.commit()
    return {"ok": True}