from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.orm import Session
from database import get_db

from models.fenotipo import TipoFenotipo, EtapaFenologica, MuestraNutrimental, SubmuestraNutrimental
import schemas.fenotipo as schemes

router = APIRouter()

# =================== MUESTRA NUTRIMENTAL ===================

@router.post(
    "/muestras-nutrimentales",
    response_model=schemes.MuestraNutrimentalResponse,
    status_code=201
)
def crear_muestra_nutrimental(
    muestra: schemes.MuestraNutrimentalCreate,
    db: Session = Depends(get_db)
):
    # Verificar que no exista el código de muestra
    existente = (
        db.query(MuestraNutrimental)
        .filter(
            MuestraNutrimental.codigo_muestra == muestra.codigo_muestra
        )
        .first()
    )

    if existente:
        raise HTTPException(
            status_code=409,
            detail="El código de muestra ya está registrado"
        )

    try:
        # ==========================
        # 1. Crear la muestra
        # ==========================

        db_muestra = MuestraNutrimental(
            codigo_muestra=muestra.codigo_muestra,
            germoplasma_id=muestra.germoplasma_id,
            parcela_id=muestra.parcela_id,
            comunidad_id=muestra.comunidad_id,
            fecha_colecta=muestra.fecha_colecta,
            peso_muestra_g=muestra.peso_muestra_g,
            condicion_muestra=muestra.condicion_muestra,
            laboratorio=muestra.laboratorio,
            fecha_analisis=muestra.fecha_analisis,
            notas=muestra.notas
        )

        db.add(db_muestra)

        # Genera el ID de la muestra antes de crear
        # las submuestras
        db.flush()

        # ==========================
        # 2. Crear submuestras
        # ==========================

        for submuestra in muestra.submuestras:

            db_submuestra = SubmuestraNutrimental(
                muestra_id=db_muestra.id,
                numero_submuestra=submuestra.numero_submuestra,
                color_mazorca=submuestra.color_mazorca,
                color_olote=submuestra.color_olote,
                largo_cm=submuestra.largo_cm,
                diametro_cm=submuestra.diametro_cm,
                peso_mazorca_g=submuestra.peso_mazorca_g,
                numero_hileras=submuestra.numero_hileras
            )

            db.add(db_submuestra)

        # ==========================
        # 3. Guardar todo
        # ==========================

        db.commit()

        db.refresh(db_muestra)

        # Obtener las submuestras creadas
        submuestras = (
            db.query(SubmuestraNutrimental)
            .filter(
                SubmuestraNutrimental.muestra_id == db_muestra.id
            )
            .order_by(
                SubmuestraNutrimental.numero_submuestra
            )
            .all()
        )

        # ==========================
        # 4. Construir respuesta
        # ==========================

        return {
            "id": db_muestra.id,
            "codigo_muestra": db_muestra.codigo_muestra,
            "germoplasma_id": db_muestra.germoplasma_id,
            "parcela_id": db_muestra.parcela_id,
            "comunidad_id": db_muestra.comunidad_id,
            "fecha_colecta": db_muestra.fecha_colecta,
            "peso_muestra_g": db_muestra.peso_muestra_g,
            "condicion_muestra": db_muestra.condicion_muestra,
            "laboratorio": db_muestra.laboratorio,
            "fecha_analisis": db_muestra.fecha_analisis,
            "notas": db_muestra.notas,
            "submuestras": submuestras,
            "created_at": db_muestra.created_at,
            "updated_at": db_muestra.updated_at
        }

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=f"No se pudo registrar la muestra nutrimental: {str(e)}"
        )
# =================== LISTAR MUESTRAS NUTRIMENTALES ===================

@router.get(
    "/muestras-nutrimentales",
    response_model=list[schemes.MuestraNutrimentalResponse]
)
def listar_muestras_nutrimentales(
    db: Session = Depends(get_db)
):
    muestras = (
        db.query(MuestraNutrimental)
        .order_by(MuestraNutrimental.id.desc())
        .all()
    )

    resultados = []

    for muestra in muestras:

        submuestras = (
            db.query(SubmuestraNutrimental)
            .filter(
                SubmuestraNutrimental.muestra_id == muestra.id
            )
            .order_by(
                SubmuestraNutrimental.numero_submuestra
            )
            .all()
        )

        resultados.append({
            "id": muestra.id,
            "codigo_muestra": muestra.codigo_muestra,
            "germoplasma_id": muestra.germoplasma_id,
            "parcela_id": muestra.parcela_id,
            "comunidad_id": muestra.comunidad_id,
            "fecha_colecta": muestra.fecha_colecta,
            "peso_muestra_g": muestra.peso_muestra_g,
            "condicion_muestra": muestra.condicion_muestra,
            "laboratorio": muestra.laboratorio,
            "fecha_analisis": muestra.fecha_analisis,
            "notas": muestra.notas,
            "submuestras": submuestras,
            "created_at": muestra.created_at,
            "updated_at": muestra.updated_at
        })

    return resultados
    
# =================== CATALOGO:TIPO FENOTIPO ===================
# @router.get("/tipo_fenotipo")
# def listar_tipo_fenotipo(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(TipoFenotipo)
#     total = query.count()
#     tipos = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": tipos}

# @router.get("/tipo_fenotipo/{fenotipo_id}", response_model=schemes.TipoFenotipo)
# def obtener_tipo_fenotipo(fenotipo_id: int, db: Session = Depends(get_db)):
#     fenotipo = db.query(TipoFenotipo).filter(TipoFenotipo.id == fenotipo_id).first()
#     if not fenotipo:
#         raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
#     return fenotipo

# @router.post("/tipo_fenotipo", response_model=schemes.TipoFenotipo)
# def crear_tipo_fenotipo(fenotipo: schemes.TipoFenotipoCreate, db: Session = Depends(get_db)):
#     db_fenotipo = TipoFenotipo(**fenotipo.dict())
#     db.add(db_fenotipo)
#     db.commit()
#     db.refresh(db_fenotipo)
#     return db_fenotipo

# @router.put("/tipo_fenotipo/{fenotipo_id}", response_model=schemes.TipoFenotipo)
# def actualizar_tipo_fenotipo(fenotipo_id: int, fenotipo: schemes.TipoFenotipoCreate, db: Session = Depends(get_db)):
#     db_fenotipo = db.query(TipoFenotipo).filter(TipoFenotipo.id == fenotipo_id).first()
#     if not db_fenotipo:
#         raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
#     for key, value in fenotipo.dict().items():
#         setattr(db_fenotipo, key, value)
#     db.commit()
#     db.refresh(db_fenotipo)
#     return db_fenotipo

# @router.delete("/tipo_fenotipo/{fenotipo_id}")
# def eliminar_tipo_fenotipo(fenotipo_id: int, db: Session = Depends(get_db)):
#     db_fenotipo = db.query(TipoFenotipo).filter(TipoFenotipo.id == fenotipo_id).first()
#     if not db_fenotipo:
#         raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
#     db.delete(db_fenotipo)
#     db.commit()
#     return {"ok": True}

# # =================== CATALOGO: ETAPA FENOLÓGICA ===================
# @router.get("/etapa_fenologica")
# def listar_etapa_fenologica(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(EtapaFenologica)
#     total = query.count()
#     etapas = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": etapas}

# @router.get("/etapa_fenologica/{etapa_id}", response_model=schemes.EtapaFenologica)
# def obtener_etapa_fenologica(etapa_id: int, db: Session = Depends(get_db)):
#     etapa = db.query(EtapaFenologica).filter(EtapaFenologica.id == etapa_id).first()
#     if not etapa:
#         raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
#     return etapa

# @router.post("/etapa_fenologica", response_model=schemes.EtapaFenologica)
# def crear_etapa_fenologica(etapa: schemes.EtapaFenologicaCreate, db: Session = Depends(get_db)):
#     db_etapa = EtapaFenologica(**etapa.dict())
#     db.add(db_etapa)
#     db.commit()
#     db.refresh(db_etapa)
#     return db_etapa

# @router.put("/etapa_fenologica/{etapa_id}", response_model=schemes.EtapaFenologica)
# def actualizar_etapa_fenologica(etapa_id: int, etapa: schemes.EtapaFenologicaCreate, db: Session = Depends(get_db)):
#     db_etapa = db.query(EtapaFenologica).filter(EtapaFenologica.id == etapa_id).first()
#     if not db_etapa:
#         raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
#     for key, value in etapa.dict().items():
#         setattr(db_etapa, key, value)
#     db.commit()
#     db.refresh(db_etapa)
#     return db_etapa

# @router.delete("/etapa_fenologica/{etapa_id}")
# def eliminar_etapa_fenologica(etapa_id: int, db: Session = Depends(get_db)):
#     db_etapa = db.query(EtapaFenologica).filter(EtapaFenologica.id == etapa_id).first()
#     if not db_etapa:
#         raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
#     db.delete(db_etapa)
#     db.commit()
#     return {"ok": True}