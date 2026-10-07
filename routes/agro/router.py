from fastapi import APIRouter, Depends, HTTPException, Query
from uuid import UUID
from datetime import date

from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db

from models.geografico import HistorialParcela, ActividadCampo
from models.core import Siembra
from models.germoplasma import ColorGrano, RazaMaiz, EstadoConservacion, UsoMaiz, Germoplasma
from models.agronomico import TipoPractica, PracticaAgricola, SistemaManejo, SistemaCultivo, MetodoAlmacenamiento
from models.social import ProductorPractica

import schemas.geografico as geografico_schemas
import schemas.core as core_schemas
import schemas.germoplasma as germplasma_schemes
import schemas.agronomico as agronomico_schemes

router = APIRouter()

# GERMOPLASMA DE MAÍZ NATIVO

# =================== CATALOGO: RAZA MAIZ ===================
# @router.get("/raza_maiz")
# def listar_razas(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(RazaMaiz)
#     total = query.count()
#     razas = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": razas}

# @router.get("/raza_maiz/{raza_id}", response_model=germplasma_schemes.RazaMaiz)
# def obtener_raza(raza_id: int, db: Session = Depends(get_db)):
# 	raza = db.query(RazaMaiz).filter(RazaMaiz.id == raza_id).first()
# 	if not raza:
# 		raise HTTPException(status_code=404, detail="Raza no encontrada")
# 	return raza

# @router.post("/raza_maiz", response_model=germplasma_schemes.RazaMaiz)
# def crear_raza(raza: germplasma_schemes.RazaMaizCreate, db: Session = Depends(get_db)):
# 	db_raza = RazaMaiz(**raza.dict())
# 	db.add(db_raza)
# 	db.commit()
# 	db.refresh(db_raza)
# 	return db_raza

# @router.put("/raza_maiz/{raza_id}", response_model=germplasma_schemes.RazaMaiz)
# def actualizar_raza(raza_id: int, raza: germplasma_schemes.RazaMaizCreate, db: Session = Depends(get_db)):
# 	db_raza = db.query(RazaMaiz).filter(RazaMaiz.id == raza_id).first()
# 	if not db_raza:
# 		raise HTTPException(status_code=404, detail="Raza no encontrada")
# 	for key, value in raza.dict().items():
# 		setattr(db_raza, key, value)
# 	db.commit()
# 	db.refresh(db_raza)
# 	return db_raza

# @router.delete("/raza_maiz/{raza_id}")
# def eliminar_raza(raza_id: int, db: Session = Depends(get_db)):
# 	db_raza = db.query(RazaMaiz).filter(RazaMaiz.id == raza_id).first()
# 	if not db_raza:
# 		raise HTTPException(status_code=404, detail="Raza no encontrada")
# 	db.delete(db_raza)
# 	db.commit()
# 	return {"ok": True}

# # =================== CATALOGO: COLOR GRANO ===================
# @router.get("/color_grano")
# def listar_colores(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(ColorGrano)
#     total = query.count()
#     colores = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": colores}

# @router.get("/color_grano/{color_id}", response_model=germplasma_schemes.ColorGrano)
# def obtener_color(color_id: int, db: Session = Depends(get_db)):
# 	color = db.query(ColorGrano).filter(ColorGrano.id == color_id).first()
# 	if not color:
# 		raise HTTPException(status_code=404, detail="Color no encontrado")
# 	return color

# @router.post("/color_grano", response_model=germplasma_schemes.ColorGrano)
# def crear_color(color: germplasma_schemes.ColorGranoCreate, db: Session = Depends(get_db)):
# 	db_color = ColorGrano(**color.dict())
# 	db.add(db_color)
# 	db.commit()
# 	db.refresh(db_color)
# 	return db_color

# @router.put("/color_grano/{color_id}", response_model=germplasma_schemes.ColorGrano)
# def actualizar_color(color_id: int, color: germplasma_schemes.ColorGranoCreate, db: Session = Depends(get_db)):
# 	db_color = db.query(ColorGrano).filter(ColorGrano.id == color_id).first()
# 	if not db_color:
# 		raise HTTPException(status_code=404, detail="Color no encontrado")
# 	for key, value in color.dict().items():
# 		setattr(db_color, key, value)
# 	db.commit()
# 	db.refresh(db_color)
# 	return db_color

# @router.delete("/color_grano/{color_id}")
# def eliminar_color(color_id: int, db: Session = Depends(get_db)):
# 	db_color = db.query(ColorGrano).filter(ColorGrano.id == color_id).first()
# 	if not db_color:
# 		raise HTTPException(status_code=404, detail="Color no encontrado")
# 	db.delete(db_color)
# 	db.commit()
# 	return {"ok": True}

# # =================== CATALOGO: ESTADO CONSERVACION ===================
# @router.get("/estado_conservacion")
# def listar_estados_conservacion(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(EstadoConservacion)
#     total = query.count()
#     estados = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": estados}

# @router.get("/estado_conservacion/{estado_id}", response_model=germplasma_schemes.EstadoConservacion)
# def obtener_estado_conservacion(estado_id: int, db: Session = Depends(get_db)):
# 	estado = db.query(EstadoConservacion).filter(EstadoConservacion.id == estado_id).first()
# 	if not estado:
# 		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
# 	return estado

# @router.post("/estado_conservacion", response_model=germplasma_schemes.EstadoConservacion)
# def crear_estado_conservacion(estado: germplasma_schemes.EstadoConservacionCreate, db: Session = Depends(get_db)):
# 	db_estado = EstadoConservacion(**estado.dict())
# 	db.add(db_estado)
# 	db.commit()
# 	db.refresh(db_estado)
# 	return db_estado

# @router.put("/estado_conservacion/{estado_id}", response_model=germplasma_schemes.EstadoConservacion)
# def actualizar_estado_conservacion(estado_id: int, estado: germplasma_schemes.EstadoConservacionCreate, db: Session = Depends(get_db)):
# 	db_estado = db.query(EstadoConservacion).filter(EstadoConservacion.id == estado_id).first()
# 	if not db_estado:
# 		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
# 	for key, value in estado.dict().items():
# 		setattr(db_estado, key, value)
# 	db.commit()
# 	db.refresh(db_estado)
# 	return db_estado

# @router.delete("/estado_conservacion/{estado_id}")
# def eliminar_estado_conservacion(estado_id: int, db: Session = Depends(get_db)):
# 	db_estado = db.query(EstadoConservacion).filter(EstadoConservacion.id == estado_id).first()
# 	if not db_estado:
# 		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
# 	db.delete(db_estado)
# 	db.commit()
# 	return {"ok": True}

# # =================== CATALOGO: USO MAIZ ===================
# @router.get("/uso_maiz")
# def listar_usos_maiz(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(UsoMaiz)
#     total = query.count()
#     usos = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": usos}

# @router.get("/uso_maiz/{uso_id}", response_model=germplasma_schemes.UsoMaiz)
# def obtener_uso_maiz(uso_id: int, db: Session = Depends(get_db)):
# 	uso = db.query(UsoMaiz).filter(UsoMaiz.id == uso_id).first()
# 	if not uso:
# 		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
# 	return uso

# @router.post("/uso_maiz", response_model=germplasma_schemes.UsoMaiz)
# def crear_uso_maiz(uso: germplasma_schemes.UsoMaizCreate, db: Session = Depends(get_db)):
# 	db_uso = UsoMaiz(**uso.dict())
# 	db.add(db_uso)
# 	db.commit()
# 	db.refresh(db_uso)
# 	return db_uso

# @router.put("/uso_maiz/{uso_id}", response_model=germplasma_schemes.UsoMaiz)
# def actualizar_uso_maiz(uso_id: int, uso: germplasma_schemes.UsoMaizCreate, db: Session = Depends(get_db)):
# 	db_uso = db.query(UsoMaiz).filter(UsoMaiz.id == uso_id).first()
# 	if not db_uso:
# 		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
# 	for key, value in uso.dict().items():
# 		setattr(db_uso, key, value)
# 	db.commit()
# 	db.refresh(db_uso)
# 	return db_uso

# @router.delete("/uso_maiz/{uso_id}")
# def eliminar_uso_maiz(uso_id: int, db: Session = Depends(get_db)):
# 	db_uso = db.query(UsoMaiz).filter(UsoMaiz.id == uso_id).first()
# 	if not db_uso:
# 		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
# 	db.delete(db_uso)
# 	db.commit()
# 	return {"ok": True}

# # =================== CATALOGO: TIPO PRACTICA ===================
# @router.get("/tipo_practica")
# def listar_tipo_practica(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(TipoPractica)
#     total = query.count()
#     tipos = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": tipos}

# @router.get("/tipo_practica/{tipo_id}", response_model=agronomico_schemes.TipoPractica)
# def obtener_tipo_practica(tipo_id: int, db: Session = Depends(get_db)):
#     tipo = db.query(TipoPractica).filter(TipoPractica.id == tipo_id).first()
#     if not tipo:
#         raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
#     return tipo

# @router.post("/tipo_practica", response_model=agronomico_schemes.TipoPractica)
# def crear_tipo_practica(tipo: agronomico_schemes.TipoPracticaCreate, db: Session = Depends(get_db)):
#     db_tipo = TipoPractica(**tipo.dict())
#     db.add(db_tipo)
#     db.commit()
#     db.refresh(db_tipo)
#     return db_tipo

# @router.put("/tipo_practica/{tipo_id}", response_model=agronomico_schemes.TipoPractica)
# def actualizar_tipo_practica(tipo_id: int, tipo: agronomico_schemes.TipoPracticaCreate, db: Session = Depends(get_db)):
#     db_tipo = db.query(TipoPractica).filter(TipoPractica.id == tipo_id).first()
#     if not db_tipo:
#         raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
#     for key, value in tipo.dict().items():
#         setattr(db_tipo, key, value)
#     db.commit()
#     db.refresh(db_tipo)
#     return db_tipo

# @router.delete("/tipo_practica/{tipo_id}")
# def eliminar_tipo_practica(tipo_id: int, db: Session = Depends(get_db)):
#     db_tipo = db.query(TipoPractica).filter(TipoPractica.id == tipo_id).first()
#     if not db_tipo:
#         raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
#     db.delete(db_tipo)
#     db.commit()
#     return {"ok": True}

# # =================== CATALOGO: PRACTICA AGRICOLA ===================
# @router.get("/practica_agricola")
# def listar_practicas_agricolas(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(PracticaAgricola)
#     total = query.count()
#     practicas = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": practicas}

# @router.get("/practica_agricola/{practica_id}", response_model=agronomico_schemes.PracticaAgricola)
# def obtener_practica_agricola(practica_id: int, db: Session = Depends(get_db)):
#     practica = db.query(PracticaAgricola).filter(PracticaAgricola.id == practica_id).first()
#     if not practica:
#         raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
#     return practica

# @router.post("/practica_agricola", response_model=agronomico_schemes.PracticaAgricola)
# def crear_practica_agricola(practica: agronomico_schemes.PracticaAgricolaCreate, db: Session = Depends(get_db)):
#     db_practica = PracticaAgricola(**practica.dict())
#     db.add(db_practica)
#     db.commit()
#     db.refresh(db_practica)
#     return db_practica

# @router.put("/practica_agricola/{practica_id}", response_model=agronomico_schemes.PracticaAgricola)
# def actualizar_practica_agricola(practica_id: int, practica: agronomico_schemes.PracticaAgricolaCreate, db: Session = Depends(get_db)):
#     db_practica = db.query(PracticaAgricola).filter(PracticaAgricola.id == practica_id).first()
#     if not db_practica:
#         raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
#     for key, value in practica.dict().items():
#         setattr(db_practica, key, value)
#     db.commit()
#     db.refresh(db_practica)
#     return db_practica

# @router.delete("/practica_agricola/{practica_id}")
# def eliminar_practica_agricola(practica_id: int, db: Session = Depends(get_db)):
#     db_practica = db.query(PracticaAgricola).filter(PracticaAgricola.id == practica_id).first()
#     if not db_practica:
#         raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
#     db.delete(db_practica)
#     db.commit()
#     return {"ok": True}

# # =================== CATALOGO: SISTEMA MANEJO ===================
# @router.get("/sistema_manejo")
# def listar_sistemas_manejo(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(SistemaManejo)
#     total = query.count()
#     sistemas = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": sistemas}

# @router.get("/sistema_manejo/{sistema_id}", response_model=agronomico_schemes.SistemaManejo)
# def obtener_sistema_manejo(sistema_id: int, db: Session = Depends(get_db)):
#     sistema = db.query(SistemaManejo).filter(SistemaManejo.id == sistema_id).first()
#     if not sistema:
#         raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
#     return sistema

# @router.post("/sistema_manejo", response_model=agronomico_schemes.SistemaManejo)
# def crear_sistema_manejo(sistema: agronomico_schemes.SistemaManejoCreate, db: Session = Depends(get_db)):
#     db_sistema = SistemaManejo(**sistema.dict())
#     db.add(db_sistema)
#     db.commit()
#     db.refresh(db_sistema)
#     return db_sistema

# @router.put("/sistema_manejo/{sistema_id}", response_model=agronomico_schemes.SistemaManejo)
# def actualizar_sistema_manejo(sistema_id: int, sistema: agronomico_schemes.SistemaManejoCreate, db: Session = Depends(get_db)):
#     db_sistema = db.query(SistemaManejo).filter(SistemaManejo.id == sistema_id).first()
#     if not db_sistema:
#         raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
#     for key, value in sistema.dict().items():
#         setattr(db_sistema, key, value)
#     db.commit()
#     db.refresh(db_sistema)
#     return db_sistema

# @router.delete("/sistema_manejo/{sistema_id}")
# def eliminar_sistema_manejo(sistema_id: int, db: Session = Depends(get_db)):
#     db_sistema = db.query(SistemaManejo).filter(SistemaManejo.id == sistema_id).first()
#     if not db_sistema:
#         raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
#     db.delete(db_sistema)
#     db.commit()
#     return {"ok": True}

# # =================== CATALOGO: SISTEMA CULTIVO ===================
# @router.get("/sistema_cultivo")
# def listar_sistema_cultivo(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(SistemaCultivo)
#     total = query.count()
#     sistemas = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": sistemas}

# @router.get("/sistema_cultivo/{sistema_id}", response_model=agronomico_schemes.SistemaCultivo)
# def obtener_sistema_cultivo(sistema_id: int, db: Session = Depends(get_db)):
#     sistema = db.query(SistemaCultivo).filter(SistemaCultivo.id == sistema_id).first()
#     if not sistema:
#         raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
#     return sistema

# @router.post("/sistema_cultivo", response_model=agronomico_schemes.SistemaCultivo)
# def crear_sistema_cultivo(sistema: agronomico_schemes.SistemaCultivoCreate, db: Session = Depends(get_db)):
#     db_sistema = SistemaCultivo(**sistema.dict())
#     db.add(db_sistema)
#     db.commit()
#     db.refresh(db_sistema)
#     return db_sistema

# @router.put("/sistema_cultivo/{sistema_id}", response_model=agronomico_schemes.SistemaCultivo)
# def actualizar_sistema_cultivo(sistema_id: int, sistema: agronomico_schemes.SistemaCultivoCreate, db: Session = Depends(get_db)):
#     db_sistema = db.query(SistemaCultivo).filter(SistemaCultivo.id == sistema_id).first()
#     if not db_sistema:
#         raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
#     for key, value in sistema.dict().items():
#         setattr(db_sistema, key, value)
#     db.commit()
#     db.refresh(db_sistema)
#     return db_sistema

# @router.delete("/sistema_cultivo/{sistema_id}")
# def eliminar_sistema_cultivo(sistema_id: int, db: Session = Depends(get_db)):
#     db_sistema = db.query(SistemaCultivo).filter(SistemaCultivo.id == sistema_id).first()
#     if not db_sistema:
#         raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
#     db.delete(db_sistema)
#     db.commit()
#     return {"ok": True}


# # =================== CATALOGO: METODO ALMACENAMIENTO ===================
# @router.get("/metodo_almacenamiento")
# def listar_metodo_almacenamiento(
#     limit: int = Query(100, ge=1, le=1000),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(MetodoAlmacenamiento)
#     total = query.count()
#     metodos = query.offset(offset).limit(limit).all()
#     return {"count": total, "results": metodos}

# @router.get("/metodo_almacenamiento/{metodo_id}", response_model=agronomico_schemes.MetodoAlmacenamiento)
# def obtener_metodo_almacenamiento(metodo_id: int, db: Session = Depends(get_db)):
#     metodo = db.query(MetodoAlmacenamiento).filter(MetodoAlmacenamiento.id == metodo_id).first()
#     if not metodo:
#         raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
#     return metodo

# @router.post("/metodo_almacenamiento", response_model=agronomico_schemes.MetodoAlmacenamiento)
# def crear_metodo_almacenamiento(metodo: agronomico_schemes.MetodoAlmacenamientoCreate, db: Session = Depends(get_db)):
#     db_metodo = MetodoAlmacenamiento(**metodo.dict())
#     db.add(db_metodo)
#     db.commit()
#     db.refresh(db_metodo)
#     return db_metodo

# @router.put("/metodo_almacenamiento/{metodo_id}", response_model=agronomico_schemes.MetodoAlmacenamiento)
# def actualizar_metodo_almacenamiento(metodo_id: int, metodo: agronomico_schemes.MetodoAlmacenamientoCreate, db: Session = Depends(get_db)):
#     db_metodo = db.query(MetodoAlmacenamiento).filter(MetodoAlmacenamiento.id == metodo_id).first()
#     if not db_metodo:
#         raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
#     for key, value in metodo.dict().items():
#         setattr(db_metodo, key, value)
#     db.commit()
#     db.refresh(db_metodo)
#     return db_metodo

# @router.delete("/metodo_almacenamiento/{metodo_id}")
# def eliminar_metodo_almacenamiento(metodo_id: int, db: Session = Depends(get_db)):
#     db_metodo = db.query(MetodoAlmacenamiento).filter(MetodoAlmacenamiento.id == metodo_id).first()
#     if not db_metodo:
#         raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
#     db.delete(db_metodo)
#     db.commit()
#     return {"ok": True}


# ============================================================
# GERMOPLASMA
# ============================================================

@router.post(
    "/germoplasma",
    response_model=germplasma_schemes.GermoplasmaRespuesta,
    status_code=201,
    tags=["Germoplasma"]
)
def crear_germoplasma(
    datos: germplasma_schemes.GermoplasmaCrear,
    db: Session = Depends(get_db)
):
    existente = (
        db.query(Germoplasma)
        .filter(Germoplasma.codigo_accesion == datos.codigo_accesion)
        .first()
    )

    if existente:
        raise HTTPException(
            status_code=409,
            detail="El código de accesión ya está registrado"
        )

    germoplasma = Germoplasma(
        codigo_accesion=datos.codigo_accesion,
        nombre_local=datos.nombre_local,
        nombre_lengua_orig=datos.nombre_lengua_orig,
        raza_id=datos.raza_id,
        color_grano_id=datos.color_grano_id,
        ciclo_vegetativo=datos.ciclo_vegetativo,
        duracion_dias=datos.duracion_dias,
        estado_conservacion_id=datos.estado_conservacion_id,
        origen_muestra_id=datos.origen_muestra_id,
        comunidad_id=datos.comunidad_id,
        ubicacion_id=datos.ubicacion_id,
        colector_id=datos.colector_id,
        notas=datos.notas,
        fecha_registro=datos.fecha_registro
    )

    try:
        db.add(germoplasma)
        db.commit()
        db.refresh(germoplasma)

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=f"No se pudo registrar el germoplasma: {str(e)}"
        )

    return germoplasma


@router.get(
    "/germoplasma",
    response_model=list[germplasma_schemes.GermoplasmaRespuesta],
    tags=["Germoplasma"]
)
def listar_germoplasma(
    db: Session = Depends(get_db)
):
    return (
        db.query(Germoplasma)
        .order_by(Germoplasma.fecha_registro.desc())
        .all()
    )


@router.get(
    "/germoplasma/{germoplasma_id}",
    response_model=germplasma_schemes.GermoplasmaRespuesta,
    tags=["Germoplasma"]
)
def obtener_germoplasma(
    germoplasma_id: UUID,
    db: Session = Depends(get_db)
):
    germoplasma = (
        db.query(Germoplasma)
        .filter(Germoplasma.id == germoplasma_id)
        .first()
    )

    if not germoplasma:
        raise HTTPException(
            status_code=404,
            detail="Germoplasma no encontrado"
        )

    return germoplasma

# =================== SIEMBRA ===================

@router.get("/siembra", tags=["Siembra"])
def listar_siembras(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = db.query(Siembra)

    total = query.count()
    siembras = query.offset(offset).limit(limit).all()

    return {
        "count": total,
        "results": siembras
    }


@router.get(
    "/siembra/{siembra_id}",
    response_model=core_schemas.SiembraRespuesta,
    tags=["Siembra"]
)
def obtener_siembra(
    siembra_id: UUID,
    db: Session = Depends(get_db)
):
    siembra = (
        db.query(Siembra)
        .filter(Siembra.id == siembra_id)
        .first()
    )

    if not siembra:
        raise HTTPException(
            status_code=404,
            detail="Siembra no encontrada"
        )

    edad_dias = None
    edad_meses = None
    edad_anios = None

    if siembra.fecha_siembra:
        if siembra.fecha_corte:
            fecha_final = siembra.fecha_corte
        elif siembra.fecha_cosecha:
            fecha_final = siembra.fecha_cosecha
        else:
            fecha_final = date.today()

        if fecha_final >= siembra.fecha_siembra:
            edad_dias = (
                fecha_final - siembra.fecha_siembra
            ).days

            edad_meses = edad_dias // 30
            edad_anios = edad_dias // 365
    
    return {
        "id": siembra.id,
        "parcela_id": siembra.parcela_id,
        "germoplasma_id": siembra.germoplasma_id,
        "fecha_siembra": siembra.fecha_siembra,
        "fecha_corte": siembra.fecha_corte,
        "fecha_cosecha": siembra.fecha_cosecha,
        "densidad": siembra.densidad,
        "rendimiento_kg_ha": siembra.rendimiento_kg_ha,
        "ciclo_agricola": siembra.ciclo_agricola,
        "edad_dias": edad_dias,
        "edad_meses": edad_meses,
        "edad_anios": edad_anios
    }

@router.post(
    "/siembra",
    response_model=core_schemas.SiembraRespuesta,
    tags=["Siembra"]
)
def crear_siembra(
    siembra: core_schemas.SiembraCreate,
    db: Session = Depends(get_db)
):
    db_siembra = Siembra(**siembra.dict())

    db.add(db_siembra)
    db.commit()
    db.refresh(db_siembra)

    return db_siembra


@router.put(
    "/siembra/{siembra_id}",
    response_model=core_schemas.SiembraRespuesta,
    tags=["Siembra"]
)
def actualizar_siembra(
    siembra_id: UUID,
    siembra: core_schemas.SiembraCreate,
    db: Session = Depends(get_db)
):
    db_siembra = db.query(Siembra).filter(
        Siembra.id == siembra_id
    ).first()

    if not db_siembra:
        raise HTTPException(
            status_code=404,
            detail="Siembra no encontrada"
        )

    for key, value in siembra.dict().items():
        setattr(db_siembra, key, value)

    db.commit()
    db.refresh(db_siembra)

    return db_siembra


@router.delete("/siembra/{siembra_id}", tags=["Siembra"])
def eliminar_siembra(
    siembra_id: UUID,
    db: Session = Depends(get_db)
):
    db_siembra = db.query(Siembra).filter(
        Siembra.id == siembra_id
    ).first()

    if not db_siembra:
        raise HTTPException(
            status_code=404,
            detail="Siembra no encontrada"
        )

    db.delete(db_siembra)
    db.commit()

    return {"ok": True}

# =================== ACTIVIDAD DE CAMPO ===================    

@router.post(
    "/visitas-campo/{visita_id}/actividades",
    response_model=geografico_schemas.ActividadCampoRespuesta,
    tags=["Actividad de campo"]
)
def crear_actividad_campo(
    visita_id: int,
    actividad: geografico_schemas.ActividadCampoCreate,
    db: Session = Depends(get_db)
):
    visita = db.execute(
        text("""
            SELECT id
            FROM geo.visita_campo
            WHERE id = :visita_id
        """),
        {"visita_id": visita_id}
    ).first()

    if not visita:
        raise HTTPException(
            status_code=404,
            detail="La visita de campo no existe"
        )

    practica = db.query(PracticaAgricola).filter(
        PracticaAgricola.id == actividad.practica_id
    ).first()

    if not practica:
        raise HTTPException(
            status_code=404,
            detail="La práctica agrícola no existe"
        )

    nueva_actividad = ActividadCampo(
        visita_id=visita_id,
        practica_id=actividad.practica_id,
        fecha_actividad=actividad.fecha_actividad,
        descripcion=actividad.descripcion,
        observaciones=actividad.observaciones,
        registrado_por=actividad.registrado_por
    )

    db.add(nueva_actividad)
    db.commit()
    db.refresh(nueva_actividad)

    return nueva_actividad

@router.get(
    "/visitas-campo/{visita_id}/actividades",
    response_model=list[geografico_schemas.ActividadCampoRespuesta],
    tags=["Actividad de campo"]
)
def listar_actividades_campo(
    visita_id: int,
    db: Session = Depends(get_db)
):
    actividades = db.query(ActividadCampo).filter(
        ActividadCampo.visita_id == visita_id
    ).order_by(
        ActividadCampo.fecha_actividad.asc(),
        ActividadCampo.id.asc()
    ).all()

    return actividades

@router.get(
    "/actividad-campo/{actividad_id}",
    response_model=geografico_schemas.ActividadCampoRespuesta,
    tags=["Actividad de campo"]
)
def obtener_actividad_campo(
    actividad_id: int,
    db: Session = Depends(get_db)
):
    actividad = db.query(ActividadCampo).filter(
        ActividadCampo.id == actividad_id
    ).first()

    if not actividad:
        raise HTTPException(
            status_code=404,
            detail="La actividad de campo no existe"
        )

    return actividad

@router.put(
    "/actividad-campo/{actividad_id}",
    response_model=geografico_schemas.ActividadCampoRespuesta,
    tags=["Actividad de campo"]
)
def actualizar_actividad_campo(
    actividad_id: int,
    actividad_data: geografico_schemas.ActividadCampoCreate,
    db: Session = Depends(get_db)
):
    actividad = db.query(ActividadCampo).filter(
        ActividadCampo.id == actividad_id
    ).first()

    if not actividad:
        raise HTTPException(
            status_code=404,
            detail="La actividad de campo no existe"
        )

    practica = db.query(PracticaAgricola).filter(
        PracticaAgricola.id == actividad_data.practica_id
    ).first()

    if not practica:
        raise HTTPException(
            status_code=404,
            detail="La práctica agrícola no existe"
        )

    actividad.practica_id = actividad_data.practica_id
    actividad.fecha_actividad = actividad_data.fecha_actividad
    actividad.descripcion = actividad_data.descripcion
    actividad.observaciones = actividad_data.observaciones
    actividad.registrado_por = actividad_data.registrado_por

    db.commit()
    db.refresh(actividad)

    return actividad

@router.delete("/actividad-campo/{actividad_id}", tags=["Actividad de campo"])
def eliminar_actividad_campo(
    actividad_id: int,
    db: Session = Depends(get_db)
):
    actividad = db.query(ActividadCampo).filter(
        ActividadCampo.id == actividad_id
    ).first()

    if not actividad:
        raise HTTPException(
            status_code=404,
            detail="La actividad de campo no existe"
        )

    db.delete(actividad)
    db.commit()

    return {
        "mensaje": "Actividad de campo eliminada correctamente"
    }        