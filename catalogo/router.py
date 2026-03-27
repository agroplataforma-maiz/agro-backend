from pydoc import text

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
import models
import schemas

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
    
# GERMOPLASMA DE MAÍZ NATIVO

# =================== RAZA MAIZ ===================
@router.get("/raza_maiz", response_model=list[schemas.RazaMaiz])
def listar_razas(db: Session = Depends(get_db)):
	return db.query(models.RazaMaiz).all()

@router.get("/raza_maiz/{raza_id}", response_model=schemas.RazaMaiz)
def obtener_raza(raza_id: int, db: Session = Depends(get_db)):
	raza = db.query(models.RazaMaiz).filter(models.RazaMaiz.id == raza_id).first()
	if not raza:
		raise HTTPException(status_code=404, detail="Raza no encontrada")
	return raza

@router.post("/raza_maiz", response_model=schemas.RazaMaiz)
def crear_raza(raza: schemas.RazaMaizCreate, db: Session = Depends(get_db)):
	db_raza = models.RazaMaiz(**raza.dict())
	db.add(db_raza)
	db.commit()
	db.refresh(db_raza)
	return db_raza

@router.put("/raza_maiz/{raza_id}", response_model=schemas.RazaMaiz)
def actualizar_raza(raza_id: int, raza: schemas.RazaMaizCreate, db: Session = Depends(get_db)):
	db_raza = db.query(models.RazaMaiz).filter(models.RazaMaiz.id == raza_id).first()
	if not db_raza:
		raise HTTPException(status_code=404, detail="Raza no encontrada")
	for key, value in raza.dict().items():
		setattr(db_raza, key, value)
	db.commit()
	db.refresh(db_raza)
	return db_raza

@router.delete("/raza_maiz/{raza_id}")
def eliminar_raza(raza_id: int, db: Session = Depends(get_db)):
	db_raza = db.query(models.RazaMaiz).filter(models.RazaMaiz.id == raza_id).first()
	if not db_raza:
		raise HTTPException(status_code=404, detail="Raza no encontrada")
	db.delete(db_raza)
	db.commit()
	return {"ok": True}

# =================== COLOR GRANO ===================
@router.get("/color_grano", response_model=list[schemas.ColorGrano])
def listar_colores(db: Session = Depends(get_db)):
	return db.query(models.ColorGrano).all()

@router.get("/color_grano/{color_id}", response_model=schemas.ColorGrano)
def obtener_color(color_id: int, db: Session = Depends(get_db)):
	color = db.query(models.ColorGrano).filter(models.ColorGrano.id == color_id).first()
	if not color:
		raise HTTPException(status_code=404, detail="Color no encontrado")
	return color

@router.post("/color_grano", response_model=schemas.ColorGrano)
def crear_color(color: schemas.ColorGranoCreate, db: Session = Depends(get_db)):
	db_color = models.ColorGrano(**color.dict())
	db.add(db_color)
	db.commit()
	db.refresh(db_color)
	return db_color

@router.put("/color_grano/{color_id}", response_model=schemas.ColorGrano)
def actualizar_color(color_id: int, color: schemas.ColorGranoCreate, db: Session = Depends(get_db)):
	db_color = db.query(models.ColorGrano).filter(models.ColorGrano.id == color_id).first()
	if not db_color:
		raise HTTPException(status_code=404, detail="Color no encontrado")
	for key, value in color.dict().items():
		setattr(db_color, key, value)
	db.commit()
	db.refresh(db_color)
	return db_color

@router.delete("/color_grano/{color_id}")
def eliminar_color(color_id: int, db: Session = Depends(get_db)):
	db_color = db.query(models.ColorGrano).filter(models.ColorGrano.id == color_id).first()
	if not db_color:
		raise HTTPException(status_code=404, detail="Color no encontrado")
	db.delete(db_color)
	db.commit()
	return {"ok": True}

# =================== ESTADO CONSERVACION ===================
@router.get("/estado_conservacion", response_model=list[schemas.EstadoConservacion])
def listar_estados_conservacion(db: Session = Depends(get_db)):
	return db.query(models.EstadoConservacion).all()

@router.get("/estado_conservacion/{estado_id}", response_model=schemas.EstadoConservacion)
def obtener_estado_conservacion(estado_id: int, db: Session = Depends(get_db)):
	estado = db.query(models.EstadoConservacion).filter(models.EstadoConservacion.id == estado_id).first()
	if not estado:
		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
	return estado

@router.post("/estado_conservacion", response_model=schemas.EstadoConservacion)
def crear_estado_conservacion(estado: schemas.EstadoConservacionCreate, db: Session = Depends(get_db)):
	db_estado = models.EstadoConservacion(**estado.dict())
	db.add(db_estado)
	db.commit()
	db.refresh(db_estado)
	return db_estado

@router.put("/estado_conservacion/{estado_id}", response_model=schemas.EstadoConservacion)
def actualizar_estado_conservacion(estado_id: int, estado: schemas.EstadoConservacionCreate, db: Session = Depends(get_db)):
	db_estado = db.query(models.EstadoConservacion).filter(models.EstadoConservacion.id == estado_id).first()
	if not db_estado:
		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
	for key, value in estado.dict().items():
		setattr(db_estado, key, value)
	db.commit()
	db.refresh(db_estado)
	return db_estado

@router.delete("/estado_conservacion/{estado_id}")
def eliminar_estado_conservacion(estado_id: int, db: Session = Depends(get_db)):
	db_estado = db.query(models.EstadoConservacion).filter(models.EstadoConservacion.id == estado_id).first()
	if not db_estado:
		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
	db.delete(db_estado)
	db.commit()
	return {"ok": True}

# =================== USO MAIZ ===================
@router.get("/uso_maiz", response_model=list[schemas.UsoMaiz])
def listar_usos_maiz(db: Session = Depends(get_db)):
	return db.query(models.UsoMaiz).all()

@router.get("/uso_maiz/{uso_id}", response_model=schemas.UsoMaiz)
def obtener_uso_maiz(uso_id: int, db: Session = Depends(get_db)):
	uso = db.query(models.UsoMaiz).filter(models.UsoMaiz.id == uso_id).first()
	if not uso:
		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
	return uso

@router.post("/uso_maiz", response_model=schemas.UsoMaiz)
def crear_uso_maiz(uso: schemas.UsoMaizCreate, db: Session = Depends(get_db)):
	db_uso = models.UsoMaiz(**uso.dict())
	db.add(db_uso)
	db.commit()
	db.refresh(db_uso)
	return db_uso

@router.put("/uso_maiz/{uso_id}", response_model=schemas.UsoMaiz)
def actualizar_uso_maiz(uso_id: int, uso: schemas.UsoMaizCreate, db: Session = Depends(get_db)):
	db_uso = db.query(models.UsoMaiz).filter(models.UsoMaiz.id == uso_id).first()
	if not db_uso:
		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
	for key, value in uso.dict().items():
		setattr(db_uso, key, value)
	db.commit()
	db.refresh(db_uso)
	return db_uso

@router.delete("/uso_maiz/{uso_id}")
def eliminar_uso_maiz(uso_id: int, db: Session = Depends(get_db)):
	db_uso = db.query(models.UsoMaiz).filter(models.UsoMaiz.id == uso_id).first()
	if not db_uso:
		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
	db.delete(db_uso)
	db.commit()
	return {"ok": True}

# EJE AGRONÓMICO

# =================== TIPO PRACTICA ===================
@router.get("/tipo_practica", response_model=list[schemas.TipoPractica])
def listar_tipo_practica(db: Session = Depends(get_db)):
    return db.query(models.TipoPractica).all()

@router.get("/tipo_practica/{tipo_id}", response_model=schemas.TipoPractica)
def obtener_tipo_practica(tipo_id: int, db: Session = Depends(get_db)):
    tipo = db.query(models.TipoPractica).filter(models.TipoPractica.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
    return tipo

@router.post("/tipo_practica", response_model=schemas.TipoPractica)
def crear_tipo_practica(tipo: schemas.TipoPracticaCreate, db: Session = Depends(get_db)):
    db_tipo = models.TipoPractica(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.put("/tipo_practica/{tipo_id}", response_model=schemas.TipoPractica)
def actualizar_tipo_practica(tipo_id: int, tipo: schemas.TipoPracticaCreate, db: Session = Depends(get_db)):
    db_tipo = db.query(models.TipoPractica).filter(models.TipoPractica.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipo_practica/{tipo_id}")
def eliminar_tipo_practica(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = db.query(models.TipoPractica).filter(models.TipoPractica.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}

# =================== PRACTICA AGRICOLA ===================
@router.get("/practica_agricola", response_model=list[schemas.PracticaAgricola])
def listar_practicas_agricolas(db: Session = Depends(get_db)):
    return db.query(models.PracticaAgricola).all()

@router.get("/practica_agricola/{practica_id}", response_model=schemas.PracticaAgricola)
def obtener_practica_agricola(practica_id: int, db: Session = Depends(get_db)):
    practica = db.query(models.PracticaAgricola).filter(models.PracticaAgricola.id == practica_id).first()
    if not practica:
        raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
    return practica

@router.post("/practica_agricola", response_model=schemas.PracticaAgricola)
def crear_practica_agricola(practica: schemas.PracticaAgricolaCreate, db: Session = Depends(get_db)):
    db_practica = models.PracticaAgricola(**practica.dict())
    db.add(db_practica)
    db.commit()
    db.refresh(db_practica)
    return db_practica

@router.put("/practica_agricola/{practica_id}", response_model=schemas.PracticaAgricola)
def actualizar_practica_agricola(practica_id: int, practica: schemas.PracticaAgricolaCreate, db: Session = Depends(get_db)):
    db_practica = db.query(models.PracticaAgricola).filter(models.PracticaAgricola.id == practica_id).first()
    if not db_practica:
        raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
    for key, value in practica.dict().items():
        setattr(db_practica, key, value)
    db.commit()
    db.refresh(db_practica)
    return db_practica

@router.delete("/practica_agricola/{practica_id}")
def eliminar_practica_agricola(practica_id: int, db: Session = Depends(get_db)):
    db_practica = db.query(models.PracticaAgricola).filter(models.PracticaAgricola.id == practica_id).first()
    if not db_practica:
        raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
    db.delete(db_practica)
    db.commit()
    return {"ok": True}

# =================== SISTEMA MANEJO ===================
@router.get("/sistema_manejo", response_model=list[schemas.SistemaManejo])
def listar_sistemas_manejo(db: Session = Depends(get_db)):
    return db.query(models.SistemaManejo).all()

@router.get("/sistema_manejo/{sistema_id}", response_model=schemas.SistemaManejo)
def obtener_sistema_manejo(sistema_id: int, db: Session = Depends(get_db)):
    sistema = db.query(models.SistemaManejo).filter(models.SistemaManejo.id == sistema_id).first()
    if not sistema:
        raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
    return sistema

@router.post("/sistema_manejo", response_model=schemas.SistemaManejo)
def crear_sistema_manejo(sistema: schemas.SistemaManejoCreate, db: Session = Depends(get_db)):
    db_sistema = models.SistemaManejo(**sistema.dict())
    db.add(db_sistema)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.put("/sistema_manejo/{sistema_id}", response_model=schemas.SistemaManejo)
def actualizar_sistema_manejo(sistema_id: int, sistema: schemas.SistemaManejoCreate, db: Session = Depends(get_db)):
    db_sistema = db.query(models.SistemaManejo).filter(models.SistemaManejo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
    for key, value in sistema.dict().items():
        setattr(db_sistema, key, value)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.delete("/sistema_manejo/{sistema_id}")
def eliminar_sistema_manejo(sistema_id: int, db: Session = Depends(get_db)):
    db_sistema = db.query(models.SistemaManejo).filter(models.SistemaManejo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
    db.delete(db_sistema)
    db.commit()
    return {"ok": True}

# =================== SISTEMA CULTIVO ===================
@router.get("/sistema_cultivo", response_model=list[schemas.SistemaCultivo])
def listar_sistema_cultivo(db: Session = Depends(get_db)):
    return db.query(models.SistemaCultivo).all()

@router.get("/sistema_cultivo/{sistema_id}", response_model=schemas.SistemaCultivo)
def obtener_sistema_cultivo(sistema_id: int, db: Session = Depends(get_db)):
    sistema = db.query(models.SistemaCultivo).filter(models.SistemaCultivo.id == sistema_id).first()
    if not sistema:
        raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
    return sistema

@router.post("/sistema_cultivo", response_model=schemas.SistemaCultivo)
def crear_sistema_cultivo(sistema: schemas.SistemaCultivoCreate, db: Session = Depends(get_db)):
    db_sistema = models.SistemaCultivo(**sistema.dict())
    db.add(db_sistema)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.put("/sistema_cultivo/{sistema_id}", response_model=schemas.SistemaCultivo)
def actualizar_sistema_cultivo(sistema_id: int, sistema: schemas.SistemaCultivoCreate, db: Session = Depends(get_db)):
    db_sistema = db.query(models.SistemaCultivo).filter(models.SistemaCultivo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
    for key, value in sistema.dict().items():
        setattr(db_sistema, key, value)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.delete("/sistema_cultivo/{sistema_id}")
def eliminar_sistema_cultivo(sistema_id: int, db: Session = Depends(get_db)):
    db_sistema = db.query(models.SistemaCultivo).filter(models.SistemaCultivo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
    db.delete(db_sistema)
    db.commit()
    return {"ok": True}


# =================== METODO ALMACENAMIENTO ===================
@router.get("/metodo_almacenamiento", response_model=list[schemas.MetodoAlmacenamiento])
def listar_metodo_almacenamiento(db: Session = Depends(get_db)):
    return db.query(models.MetodoAlmacenamiento).all()

@router.get("/metodo_almacenamiento/{metodo_id}", response_model=schemas.MetodoAlmacenamiento)
def obtener_metodo_almacenamiento(metodo_id: int, db: Session = Depends(get_db)):
    metodo = db.query(models.MetodoAlmacenamiento).filter(models.MetodoAlmacenamiento.id == metodo_id).first()
    if not metodo:
        raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
    return metodo

@router.post("/metodo_almacenamiento", response_model=schemas.MetodoAlmacenamiento)
def crear_metodo_almacenamiento(metodo: schemas.MetodoAlmacenamientoCreate, db: Session = Depends(get_db)):
    db_metodo = models.MetodoAlmacenamiento(**metodo.dict())
    db.add(db_metodo)
    db.commit()
    db.refresh(db_metodo)
    return db_metodo

@router.put("/metodo_almacenamiento/{metodo_id}", response_model=schemas.MetodoAlmacenamiento)
def actualizar_metodo_almacenamiento(metodo_id: int, metodo: schemas.MetodoAlmacenamientoCreate, db: Session = Depends(get_db)):
    db_metodo = db.query(models.MetodoAlmacenamiento).filter(models.MetodoAlmacenamiento.id == metodo_id).first()
    if not db_metodo:
        raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
    for key, value in metodo.dict().items():
        setattr(db_metodo, key, value)
    db.commit()
    db.refresh(db_metodo)
    return db_metodo

@router.delete("/metodo_almacenamiento/{metodo_id}")
def eliminar_metodo_almacenamiento(metodo_id: int, db: Session = Depends(get_db)):
    db_metodo = db.query(models.MetodoAlmacenamiento).filter(models.MetodoAlmacenamiento.id == metodo_id).first()
    if not db_metodo:
        raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
    db.delete(db_metodo)
    db.commit()
    return {"ok": True}

# =================== TIPO FENOTIPO ===================
@router.get("/tipo_fenotipo", response_model=list[schemas.TipoFenotipo])
def listar_tipo_fenotipo(db: Session = Depends(get_db)):
    return db.query(models.TipoFenotipo).all()

@router.get("/tipo_fenotipo/{fenotipo_id}", response_model=schemas.TipoFenotipo)
def obtener_tipo_fenotipo(fenotipo_id: int, db: Session = Depends(get_db)):
    fenotipo = db.query(models.TipoFenotipo).filter(models.TipoFenotipo.id == fenotipo_id).first()
    if not fenotipo:
        raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
    return fenotipo

@router.post("/tipo_fenotipo", response_model=schemas.TipoFenotipo)
def crear_tipo_fenotipo(fenotipo: schemas.TipoFenotipoCreate, db: Session = Depends(get_db)):
    db_fenotipo = models.TipoFenotipo(**fenotipo.dict())
    db.add(db_fenotipo)
    db.commit()
    db.refresh(db_fenotipo)
    return db_fenotipo

@router.put("/tipo_fenotipo/{fenotipo_id}", response_model=schemas.TipoFenotipo)
def actualizar_tipo_fenotipo(fenotipo_id: int, fenotipo: schemas.TipoFenotipoCreate, db: Session = Depends(get_db)):
    db_fenotipo = db.query(models.TipoFenotipo).filter(models.TipoFenotipo.id == fenotipo_id).first()
    if not db_fenotipo:
        raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
    for key, value in fenotipo.dict().items():
        setattr(db_fenotipo, key, value)
    db.commit()
    db.refresh(db_fenotipo)
    return db_fenotipo

@router.delete("/tipo_fenotipo/{fenotipo_id}")
def eliminar_tipo_fenotipo(fenotipo_id: int, db: Session = Depends(get_db)):
    db_fenotipo = db.query(models.TipoFenotipo).filter(models.TipoFenotipo.id == fenotipo_id).first()
    if not db_fenotipo:
        raise HTTPException(status_code=404, detail="Tipo de fenotipo no encontrado")
    db.delete(db_fenotipo)
    db.commit()
    return {"ok": True}

# =================== ETAPA FENOLÓGICA ===================
@router.get("/etapa_fenologica", response_model=list[schemas.EtapaFenologica])
def listar_etapa_fenologica(db: Session = Depends(get_db)):
    return db.query(models.EtapaFenologica).all()

@router.get("/etapa_fenologica/{etapa_id}", response_model=schemas.EtapaFenologica)
def obtener_etapa_fenologica(etapa_id: int, db: Session = Depends(get_db)):
    etapa = db.query(models.EtapaFenologica).filter(models.EtapaFenologica.id == etapa_id).first()
    if not etapa:
        raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
    return etapa

@router.post("/etapa_fenologica", response_model=schemas.EtapaFenologica)
def crear_etapa_fenologica(etapa: schemas.EtapaFenologicaCreate, db: Session = Depends(get_db)):
    db_etapa = models.EtapaFenologica(**etapa.dict())
    db.add(db_etapa)
    db.commit()
    db.refresh(db_etapa)
    return db_etapa

@router.put("/etapa_fenologica/{etapa_id}", response_model=schemas.EtapaFenologica)
def actualizar_etapa_fenologica(etapa_id: int, etapa: schemas.EtapaFenologicaCreate, db: Session = Depends(get_db)):
    db_etapa = db.query(models.EtapaFenologica).filter(models.EtapaFenologica.id == etapa_id).first()
    if not db_etapa:
        raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
    for key, value in etapa.dict().items():
        setattr(db_etapa, key, value)
    db.commit()
    db.refresh(db_etapa)
    return db_etapa

@router.delete("/etapa_fenologica/{etapa_id}")
def eliminar_etapa_fenologica(etapa_id: int, db: Session = Depends(get_db)):
    db_etapa = db.query(models.EtapaFenologica).filter(models.EtapaFenologica.id == etapa_id).first()
    if not db_etapa:
        raise HTTPException(status_code=404, detail="Etapa fenológica no encontrada")
    db.delete(db_etapa)
    db.commit()
    return {"ok": True}

# -- EJE TERRITORIAL --

# =================== ESTADO ===================
@router.get("/estado", response_model=list[schemas.Estado])
def listar_estados(db: Session = Depends(get_db)):
    return db.query(models.Estado).all()

@router.get("/estado/{estado_id}", response_model=schemas.Estado)
def obtener_estado(estado_id: int, db: Session = Depends(get_db)):
    estado = db.query(models.Estado).filter(models.Estado.id == estado_id).first()
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado

@router.post("/estado", response_model=schemas.Estado)
def crear_estado(estado: schemas.EstadoCreate, db: Session = Depends(get_db)):
    db_estado = models.Estado(**estado.dict())
    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)
    return db_estado

@router.put("/estado/{estado_id}", response_model=schemas.Estado)
def actualizar_estado(estado_id: int, estado: schemas.EstadoCreate, db: Session = Depends(get_db)):
    db_estado = db.query(models.Estado).filter(models.Estado.id == estado_id).first()
    if not db_estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    for key, value in estado.dict().items():
        setattr(db_estado, key, value)
    db.commit()
    db.refresh(db_estado)
    return db_estado

@router.delete("/estado/{estado_id}")
def eliminar_estado(estado_id: int, db: Session = Depends(get_db)):
    db_estado = db.query(models.Estado).filter(models.Estado.id == estado_id).first()
    if not db_estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    db.delete(db_estado)
    db.commit()
    return {"ok": True}

# =================== MUNICIPIO ===================
@router.get("/municipio", response_model=list[schemas.Municipio])
def listar_municipios(db: Session = Depends(get_db)):
    return db.query(models.Municipio).all()

@router.get("/municipio/{municipio_id}", response_model=schemas.Municipio)
def obtener_municipio(municipio_id: int, db: Session = Depends(get_db)):
    municipio = db.query(models.Municipio).filter(models.Municipio.id == municipio_id).first()
    if not municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    return municipio

@router.post("/municipio", response_model=schemas.Municipio)
def crear_municipio(municipio: schemas.MunicipioCreate, db: Session = Depends(get_db)):
    db_municipio = models.Municipio(**municipio.dict())
    db.add(db_municipio)
    db.commit()
    db.refresh(db_municipio)
    return db_municipio

@router.put("/municipio/{municipio_id}", response_model=schemas.Municipio)
def actualizar_municipio(municipio_id: int, municipio: schemas.MunicipioCreate, db: Session = Depends(get_db)):
    db_municipio = db.query(models.Municipio).filter(models.Municipio.id == municipio_id).first()
    if not db_municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    for key, value in municipio.dict().items():
        setattr(db_municipio, key, value)
    db.commit()
    db.refresh(db_municipio)
    return db_municipio

@router.delete("/municipio/{municipio_id}")
def eliminar_municipio(municipio_id: int, db: Session = Depends(get_db)):
    db_municipio = db.query(models.Municipio).filter(models.Municipio.id == municipio_id).first()
    if not db_municipio:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    db.delete(db_municipio)
    db.commit()
    return {"ok": True}

# =================== COMUNIDAD ===================
@router.get("/comunidad", response_model=list[schemas.Comunidad])
def listar_comunidades(db: Session = Depends(get_db)):
    return db.query(models.Comunidad).all()

@router.get("/comunidad/{comunidad_id}", response_model=schemas.Comunidad)
def obtener_comunidad(comunidad_id: int, db: Session = Depends(get_db)):
    comunidad = db.query(models.Comunidad).filter(models.Comunidad.id == comunidad_id).first()
    if not comunidad:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada")
    return comunidad

@router.post("/comunidad", response_model=schemas.Comunidad)
def crear_comunidad(comunidad: schemas.ComunidadCreate, db: Session = Depends(get_db)):
    db_comunidad = models.Comunidad(**comunidad.dict())
    db.add(db_comunidad)
    db.commit()
    db.refresh(db_comunidad)
    return db_comunidad

@router.put("/comunidad/{comunidad_id}", response_model=schemas.Comunidad)
def actualizar_comunidad(comunidad_id: int, comunidad: schemas.ComunidadCreate, db: Session = Depends(get_db)):
    db_comunidad = db.query(models.Comunidad).filter(models.Comunidad.id == comunidad_id).first()
    if not db_comunidad:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada")
    for key, value in comunidad.dict().items():
        setattr(db_comunidad, key, value)
    db.commit()
    db.refresh(db_comunidad)
    return db_comunidad

@router.delete("/comunidad/{comunidad_id}")
def eliminar_comunidad(comunidad_id: int, db: Session = Depends(get_db)):
    db_comunidad = db.query(models.Comunidad).filter(models.Comunidad.id == comunidad_id).first()
    if not db_comunidad:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada")
    db.delete(db_comunidad)
    db.commit()
    return {"ok": True}

# =================== LOCALIDAD ===================
@router.get("/localidad", response_model=list[schemas.Localidad])
def listar_localidades(db: Session = Depends(get_db)):
    return db.query(models.Localidad).all()

@router.get("/localidad/{localidad_id}", response_model=schemas.Localidad)
def obtener_localidad(localidad_id: int, db: Session = Depends(get_db)):
    localidad = db.query(models.Localidad).filter(models.Localidad.id == localidad_id).first()
    if not localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    return localidad

@router.post("/localidad", response_model=schemas.Localidad)
def crear_localidad(localidad: schemas.LocalidadCreate, db: Session = Depends(get_db)):
    db_localidad = models.Localidad(**localidad.dict())
    db.add(db_localidad)
    db.commit()
    db.refresh(db_localidad)
    return db_localidad

@router.put("/localidad/{localidad_id}", response_model=schemas.Localidad)
def actualizar_localidad(localidad_id: int, localidad: schemas.LocalidadCreate, db: Session = Depends(get_db)):
    db_localidad = db.query(models.Localidad).filter(models.Localidad.id == localidad_id).first()
    if not db_localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    for key, value in localidad.dict().items():
        setattr(db_localidad, key, value)
    db.commit()
    db.refresh(db_localidad)
    return db_localidad

@router.delete("/localidad/{localidad_id}")
def eliminar_localidad(localidad_id: int, db: Session = Depends(get_db)):
    db_localidad = db.query(models.Localidad).filter(models.Localidad.id == localidad_id).first()
    if not db_localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    db.delete(db_localidad)
    db.commit()
    return {"ok": True}

# =================== COLONIA ===================
@router.get("/colonia", response_model=list[schemas.Colonia])
def listar_colonias(db: Session = Depends(get_db)):
    return db.query(models.Colonia).all()

@router.get("/colonia/{colonia_id}", response_model=schemas.Colonia)
def obtener_colonia(colonia_id: int, db: Session = Depends(get_db)):
    colonia = db.query(models.Colonia).filter(models.Colonia.id == colonia_id).first()
    if not colonia:
        raise HTTPException(status_code=404, detail="Colonia no encontrada")
    return colonia

@router.post("/colonia", response_model=schemas.Colonia)
def crear_colonia(colonia: schemas.ColoniaCreate, db: Session = Depends(get_db)):
    db_colonia = models.Colonia(**colonia.dict())
    db.add(db_colonia)
    db.commit()
    db.refresh(db_colonia)
    return db_colonia

@router.put("/colonia/{colonia_id}", response_model=schemas.Colonia)
def actualizar_colonia(colonia_id: int, colonia: schemas.ColoniaCreate, db: Session = Depends(get_db)):
    db_colonia = db.query(models.Colonia).filter(models.Colonia.id == colonia_id).first()
    if not db_colonia:
        raise HTTPException(status_code=404, detail="Colonia no encontrada")
    for key, value in colonia.dict().items():
        setattr(db_colonia, key, value)
    db.commit()
    db.refresh(db_colonia)
    return db_colonia

@router.delete("/colonia/{colonia_id}")
def eliminar_colonia(colonia_id: int, db: Session = Depends(get_db)):
    db_colonia = db.query(models.Colonia).filter(models.Colonia.id == colonia_id).first()
    if not db_colonia:
        raise HTTPException(status_code=404, detail="Colonia no encontrada")
    db.delete(db_colonia)
    db.commit()
    return {"ok": True}

# =================== CLASE USO SUELO ===================
@router.get("/clase_uso_suelo", response_model=list[schemas.ClaseUsoSuelo])
def listar_clase_uso_suelo(db: Session = Depends(get_db)):
    return db.query(models.ClaseUsoSuelo).all()

@router.get("/clase_uso_suelo/{clase_id}", response_model=schemas.ClaseUsoSuelo)
def obtener_clase_uso_suelo(clase_id: int, db: Session = Depends(get_db)):
    clase = db.query(models.ClaseUsoSuelo).filter(models.ClaseUsoSuelo.id == clase_id).first()
    if not clase:
        raise HTTPException(status_code=404, detail="Clase de uso de suelo no encontrada")
    return clase

@router.post("/clase_uso_suelo", response_model=schemas.ClaseUsoSuelo)
def crear_clase_uso_suelo(clase: schemas.ClaseUsoSueloCreate, db: Session = Depends(get_db)):
    db_clase = models.ClaseUsoSuelo(**clase.dict())
    db.add(db_clase)
    db.commit()
    db.refresh(db_clase)
    return db_clase

@router.put("/clase_uso_suelo/{clase_id}", response_model=schemas.ClaseUsoSuelo)
def actualizar_clase_uso_suelo(clase_id: int, clase: schemas.ClaseUsoSueloCreate, db: Session = Depends(get_db)):
    db_clase = db.query(models.ClaseUsoSuelo).filter(models.ClaseUsoSuelo.id == clase_id).first()
    if not db_clase:
        raise HTTPException(status_code=404, detail="Clase de uso de suelo no encontrada")
    for key, value in clase.dict().items():
        setattr(db_clase, key, value)
    db.commit()
    db.refresh(db_clase)
    return db_clase

@router.delete("/clase_uso_suelo/{clase_id}")
def eliminar_clase_uso_suelo(clase_id: int, db: Session = Depends(get_db)):
    db_clase = db.query(models.ClaseUsoSuelo).filter(models.ClaseUsoSuelo.id == clase_id).first()
    if not db_clase:
        raise HTTPException(status_code=404, detail="Clase de uso de suelo no encontrada")
    db.delete(db_clase)
    db.commit()
    return {"ok": True}

# -- EJE AMBIENTAL --

# =================== TIPO EVENTO CLIMATICO ===================
@router.get("/tipo_evento_climatico", response_model=list[schemas.TipoEventoClimatico])
def listar_tipo_evento_climatico(db: Session = Depends(get_db)):
    return db.query(models.TipoEventoClimatico).all()

@router.get("/tipo_evento_climatico/{tipo_id}", response_model=schemas.TipoEventoClimatico)
def obtener_tipo_evento_climatico(tipo_id: int, db: Session = Depends(get_db)):
    tipo = db.query(models.TipoEventoClimatico).filter(models.TipoEventoClimatico.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de evento climático no encontrado")
    return tipo

@router.post("/tipo_evento_climatico", response_model=schemas.TipoEventoClimatico)
def crear_tipo_evento_climatico(tipo: schemas.TipoEventoClimaticoCreate, db: Session = Depends(get_db)):
    db_tipo = models.TipoEventoClimatico(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.put("/tipo_evento_climatico/{tipo_id}", response_model=schemas.TipoEventoClimatico)
def actualizar_tipo_evento_climatico(tipo_id: int, tipo: schemas.TipoEventoClimaticoCreate, db: Session = Depends(get_db)):
    db_tipo = db.query(models.TipoEventoClimatico).filter(models.TipoEventoClimatico.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de evento climático no encontrado")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipo_evento_climatico/{tipo_id}")
def eliminar_tipo_evento_climatico(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = db.query(models.TipoEventoClimatico).filter(models.TipoEventoClimatico.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de evento climático no encontrado")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}

# =================== VARIABLE AMBIENTAL ===================
@router.get("/variable_ambiental", response_model=list[schemas.VariableAmbiental])
def listar_variable_ambiental(db: Session = Depends(get_db)):
    return db.query(models.VariableAmbiental).all()

@router.get("/variable_ambiental/{variable_id}", response_model=schemas.VariableAmbiental)
def obtener_variable_ambiental(variable_id: int, db: Session = Depends(get_db)):
    variable = db.query(models.VariableAmbiental).filter(models.VariableAmbiental.id == variable_id).first()
    if not variable:
        raise HTTPException(status_code=404, detail="Variable ambiental no encontrada")
    return variable

@router.post("/variable_ambiental", response_model=schemas.VariableAmbiental)
def crear_variable_ambiental(variable: schemas.VariableAmbientalCreate, db: Session = Depends(get_db)):
    db_variable = models.VariableAmbiental(**variable.dict())
    db.add(db_variable)
    db.commit()
    db.refresh(db_variable)
    return db_variable

@router.put("/variable_ambiental/{variable_id}", response_model=schemas.VariableAmbiental)
def actualizar_variable_ambiental(variable_id: int, variable: schemas.VariableAmbientalCreate, db: Session = Depends(get_db)):
    db_variable = db.query(models.VariableAmbiental).filter(models.VariableAmbiental.id == variable_id).first()
    if not db_variable:
        raise HTTPException(status_code=404, detail="Variable ambiental no encontrada")
    for key, value in variable.dict().items():
        setattr(db_variable, key, value)
    db.commit()
    db.refresh(db_variable)
    return db_variable

@router.delete("/variable_ambiental/{variable_id}")
def eliminar_variable_ambiental(variable_id: int, db: Session = Depends(get_db)):
    db_variable = db.query(models.VariableAmbiental).filter(models.VariableAmbiental.id == variable_id).first()
    if not db_variable:
        raise HTTPException(status_code=404, detail="Variable ambiental no encontrada")
    db.delete(db_variable)
    db.commit()
    return {"ok": True}

# =================== TIPO AMENAZA ===================
@router.get("/tipo_amenaza", response_model=list[schemas.TipoAmenaza])
def listar_tipo_amenaza(db: Session = Depends(get_db)):
    return db.query(models.TipoAmenaza).all()

@router.get("/tipo_amenaza/{amenaza_id}", response_model=schemas.TipoAmenaza)
def obtener_tipo_amenaza(amenaza_id: int, db: Session = Depends(get_db)):
    amenaza = db.query(models.TipoAmenaza).filter(models.TipoAmenaza.id == amenaza_id).first()
    if not amenaza:
        raise HTTPException(status_code=404, detail="Tipo de amenaza no encontrado")
    return amenaza

@router.post("/tipo_amenaza", response_model=schemas.TipoAmenaza)
def crear_tipo_amenaza(amenaza: schemas.TipoAmenazaCreate, db: Session = Depends(get_db)):
    db_amenaza = models.TipoAmenaza(**amenaza.dict())
    db.add(db_amenaza)
    db.commit()
    db.refresh(db_amenaza)
    return db_amenaza

@router.put("/tipo_amenaza/{amenaza_id}", response_model=schemas.TipoAmenaza)
def actualizar_tipo_amenaza(amenaza_id: int, amenaza: schemas.TipoAmenazaCreate, db: Session = Depends(get_db)):
    db_amenaza = db.query(models.TipoAmenaza).filter(models.TipoAmenaza.id == amenaza_id).first()
    if not db_amenaza:
        raise HTTPException(status_code=404, detail="Tipo de amenaza no encontrado")
    for key, value in amenaza.dict().items():
        setattr(db_amenaza, key, value)
    db.commit()
    db.refresh(db_amenaza)
    return db_amenaza

@router.delete("/tipo_amenaza/{amenaza_id}")
def eliminar_tipo_amenaza(amenaza_id: int, db: Session = Depends(get_db)):
    db_amenaza = db.query(models.TipoAmenaza).filter(models.TipoAmenaza.id == amenaza_id).first()
    if not db_amenaza:
        raise HTTPException(status_code=404, detail="Tipo de amenaza no encontrado")
    db.delete(db_amenaza)
    db.commit()
    return {"ok": True}

# -- EJE SOCIOCULTURAL --

# =================== TIPO PRODUCTOR ===================
@router.get("/tipo_productor", response_model=list[schemas.TipoProductor])
def listar_tipo_productor(db: Session = Depends(get_db)):
    return db.query(models.TipoProductor).all()

@router.get("/tipo_productor/{tipo_id}", response_model=schemas.TipoProductor)
def obtener_tipo_productor(tipo_id: int, db: Session = Depends(get_db)):
    tipo = db.query(models.TipoProductor).filter(models.TipoProductor.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de productor no encontrado")
    return tipo

@router.post("/tipo_productor", response_model=schemas.TipoProductor)
def crear_tipo_productor(tipo: schemas.TipoProductorCreate, db: Session = Depends(get_db)):
    db_tipo = models.TipoProductor(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.put("/tipo_productor/{tipo_id}", response_model=schemas.TipoProductor)
def actualizar_tipo_productor(tipo_id: int, tipo: schemas.TipoProductorCreate, db: Session = Depends(get_db)):
    db_tipo = db.query(models.TipoProductor).filter(models.TipoProductor.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de productor no encontrado")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipo_productor/{tipo_id}")
def eliminar_tipo_productor(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = db.query(models.TipoProductor).filter(models.TipoProductor.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de productor no encontrado")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}

# =================== LENGUA ===================
@router.get("/lengua", response_model=list[schemas.Lengua])
def listar_lenguas(db: Session = Depends(get_db)):
    return db.query(models.Lengua).all()

@router.get("/lengua/{lengua_id}", response_model=schemas.Lengua)
def obtener_lengua(lengua_id: int, db: Session = Depends(get_db)):
    lengua = db.query(models.Lengua).filter(models.Lengua.id == lengua_id).first()
    if not lengua:
        raise HTTPException(status_code=404, detail="Lengua no encontrada")
    return lengua

@router.post("/lengua", response_model=schemas.Lengua)
def crear_lengua(lengua: schemas.LenguaCreate, db: Session = Depends(get_db)):
    db_lengua = models.Lengua(**lengua.dict())
    db.add(db_lengua)
    db.commit()
    db.refresh(db_lengua)
    return db_lengua

@router.put("/lengua/{lengua_id}", response_model=schemas.Lengua)
def actualizar_lengua(lengua_id: int, lengua: schemas.LenguaCreate, db: Session = Depends(get_db)):
    db_lengua = db.query(models.Lengua).filter(models.Lengua.id == lengua_id).first()
    if not db_lengua:
        raise HTTPException(status_code=404, detail="Lengua no encontrada")
    for key, value in lengua.dict().items():
        setattr(db_lengua, key, value)
    db.commit()
    db.refresh(db_lengua)
    return db_lengua

@router.delete("/lengua/{lengua_id}")
def eliminar_lengua(lengua_id: int, db: Session = Depends(get_db)):
    db_lengua = db.query(models.Lengua).filter(models.Lengua.id == lengua_id).first()
    if not db_lengua:
        raise HTTPException(status_code=404, detail="Lengua no encontrada")
    db.delete(db_lengua)
    db.commit()
    return {"ok": True}

# =================== PUEBLO ORIGINARIO ===================
@router.get("/pueblo_originario", response_model=list[schemas.PuebloOriginario])
def listar_pueblos_originarios(db: Session = Depends(get_db)):
    return db.query(models.PuebloOriginario).all()

@router.get("/pueblo_originario/{pueblo_id}", response_model=schemas.PuebloOriginario)
def obtener_pueblo_originario(pueblo_id: int, db: Session = Depends(get_db)):
    pueblo = db.query(models.PuebloOriginario).filter(models.PuebloOriginario.id == pueblo_id).first()
    if not pueblo:
        raise HTTPException(status_code=404, detail="Pueblo originario no encontrado")
    return pueblo

@router.post("/pueblo_originario", response_model=schemas.PuebloOriginario)
def crear_pueblo_originario(pueblo: schemas.PuebloOriginarioCreate, db: Session = Depends(get_db)):
    db_pueblo = models.PuebloOriginario(**pueblo.dict())
    db.add(db_pueblo)
    db.commit()
    db.refresh(db_pueblo)
    return db_pueblo

@router.put("/pueblo_originario/{pueblo_id}", response_model=schemas.PuebloOriginario)
def actualizar_pueblo_originario(pueblo_id: int, pueblo: schemas.PuebloOriginarioCreate, db: Session = Depends(get_db)):
    db_pueblo = db.query(models.PuebloOriginario).filter(models.PuebloOriginario.id == pueblo_id).first()
    if not db_pueblo:
        raise HTTPException(status_code=404, detail="Pueblo originario no encontrado")
    for key, value in pueblo.dict().items():
        setattr(db_pueblo, key, value)
    db.commit()
    db.refresh(db_pueblo)
    return db_pueblo

@router.delete("/pueblo_originario/{pueblo_id}")
def eliminar_pueblo_originario(pueblo_id: int, db: Session = Depends(get_db)):
    db_pueblo = db.query(models.PuebloOriginario).filter(models.PuebloOriginario.id == pueblo_id).first()
    if not db_pueblo:
        raise HTTPException(status_code=404, detail="Pueblo originario no encontrado")
    db.delete(db_pueblo)
    db.commit()
    return {"ok": True}


# =================== TIPO RITUAL AGRICOLA ===================
@router.get("/tipo_ritual_agricola", response_model=list[schemas.TipoRitualAgricola])
def listar_tipo_ritual_agricola(db: Session = Depends(get_db)):
    return db.query(models.TipoRitualAgricola).all()

@router.get("/tipo_ritual_agricola/{ritual_id}", response_model=schemas.TipoRitualAgricola)
def obtener_tipo_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    ritual = db.query(models.TipoRitualAgricola).filter(models.TipoRitualAgricola.id == ritual_id).first()
    if not ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    return ritual

@router.post("/tipo_ritual_agricola", response_model=schemas.TipoRitualAgricola)
def crear_tipo_ritual_agricola(ritual: schemas.TipoRitualAgricolaCreate, db: Session = Depends(get_db)):
    db_ritual = models.TipoRitualAgricola(**ritual.dict())
    db.add(db_ritual)
    db.commit()
    db.refresh(db_ritual)
    return db_ritual

@router.put("/tipo_ritual_agricola/{ritual_id}", response_model=schemas.TipoRitualAgricola)
def actualizar_tipo_ritual_agricola(ritual_id: int, ritual: schemas.TipoRitualAgricolaCreate, db: Session = Depends(get_db)):
    db_ritual = db.query(models.TipoRitualAgricola).filter(models.TipoRitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    for key, value in ritual.dict().items():
        setattr(db_ritual, key, value)
    db.commit()
    db.refresh(db_ritual)
    return db_ritual

@router.delete("/tipo_ritual_agricola/{ritual_id}")
def eliminar_tipo_ritual_agricola(ritual_id: int, db: Session = Depends(get_db)):
    db_ritual = db.query(models.TipoRitualAgricola).filter(models.TipoRitualAgricola.id == ritual_id).first()
    if not db_ritual:
        raise HTTPException(status_code=404, detail="Tipo de ritual agrícola no encontrado")
    db.delete(db_ritual)
    db.commit()
    return {"ok": True}


# =================== TIPO NARRATIVA ORAL ===================
@router.get("/tipo_narrativa_oral", response_model=list[schemas.TipoNarrativaOral])
def listar_tipo_narrativa_oral(db: Session = Depends(get_db)):
    return db.query(models.TipoNarrativaOral).all()

@router.get("/tipo_narrativa_oral/{narrativa_id}", response_model=schemas.TipoNarrativaOral)
def obtener_tipo_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    narrativa = db.query(models.TipoNarrativaOral).filter(models.TipoNarrativaOral.id == narrativa_id).first()
    if not narrativa:
        raise HTTPException(status_code=404, detail="Tipo de narrativa oral no encontrado")
    return narrativa

@router.post("/tipo_narrativa_oral", response_model=schemas.TipoNarrativaOral)
def crear_tipo_narrativa_oral(narrativa: schemas.TipoNarrativaOralCreate, db: Session = Depends(get_db)):
    db_narrativa = models.TipoNarrativaOral(**narrativa.dict())
    db.add(db_narrativa)
    db.commit()
    db.refresh(db_narrativa)
    return db_narrativa

@router.put("/tipo_narrativa_oral/{narrativa_id}", response_model=schemas.TipoNarrativaOral)
def actualizar_tipo_narrativa_oral(narrativa_id: int, narrativa: schemas.TipoNarrativaOralCreate, db: Session = Depends(get_db)):
    db_narrativa = db.query(models.TipoNarrativaOral).filter(models.TipoNarrativaOral.id == narrativa_id).first()
    if not db_narrativa:
        raise HTTPException(status_code=404, detail="Tipo de narrativa oral no encontrado")
    for key, value in narrativa.dict().items():
        setattr(db_narrativa, key, value)
    db.commit()
    db.refresh(db_narrativa)
    return db_narrativa

@router.delete("/tipo_narrativa_oral/{narrativa_id}")
def eliminar_tipo_narrativa_oral(narrativa_id: int, db: Session = Depends(get_db)):
    db_narrativa = db.query(models.TipoNarrativaOral).filter(models.TipoNarrativaOral.id == narrativa_id).first()
    if not db_narrativa:
        raise HTTPException(status_code=404, detail="Tipo de narrativa oral no encontrado")
    db.delete(db_narrativa)
    db.commit()
    return {"ok": True}

# =================== SABER AGRICOLA ===================
@router.get("/categoria_saber_agricola", response_model=list[schemas.CategoriaSaberAgricola])
def listar_categoria_saber_agricola(db: Session = Depends(get_db)):
    return db.query(models.CategoriaSaberAgricola).all()

@router.get("/categoria_saber_agricola/{categoria_id}", response_model=schemas.CategoriaSaberAgricola)
def obtener_categoria_saber_agricola(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.CategoriaSaberAgricola).filter(models.CategoriaSaberAgricola.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría de saber agrícola no encontrada")
    return categoria

@router.post("/categoria_saber_agricola", response_model=schemas.CategoriaSaberAgricola)
def crear_categoria_saber_agricola(categoria: schemas.CategoriaSaberAgricolaCreate, db: Session = Depends(get_db)):
    db_categoria = models.CategoriaSaberAgricola(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.put("/categoria_saber_agricola/{categoria_id}", response_model=schemas.CategoriaSaberAgricola)
def actualizar_categoria_saber_agricola(categoria_id: int, categoria: schemas.CategoriaSaberAgricolaCreate, db: Session = Depends(get_db)):
    db_categoria = db.query(models.CategoriaSaberAgricola).filter(models.CategoriaSaberAgricola.id == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría de saber agrícola no encontrada")
    for key, value in categoria.dict().items():
        setattr(db_categoria, key, value)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.delete("/categoria_saber_agricola/{categoria_id}")
def eliminar_categoria_saber_agricola(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = db.query(models.CategoriaSaberAgricola).filter(models.CategoriaSaberAgricola.id == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría de saber agrícola no encontrada")
    db.delete(db_categoria)
    db.commit()
    return {"ok": True}

# =================== OCASION ===================
@router.get("/ocasion", response_model=list[schemas.Ocasion])
def listar_ocasion(db: Session = Depends(get_db)):
    return db.query(models.Ocasion).all()

@router.get("/ocasion/{ocasion_id}", response_model=schemas.Ocasion)
def obtener_ocasion(ocasion_id: int, db: Session = Depends(get_db)):
    ocasion = db.query(models.Ocasion).filter(models.Ocasion.id == ocasion_id).first()
    if not ocasion:
        raise HTTPException(status_code=404, detail="Ocasión no encontrada")
    return ocasion

@router.post("/ocasion", response_model=schemas.Ocasion)
def crear_ocasion(ocasion: schemas.OcasionCreate, db: Session = Depends(get_db)):
    db_ocasion = models.Ocasion(**ocasion.dict())
    db.add(db_ocasion)
    db.commit()
    db.refresh(db_ocasion)
    return db_ocasion

@router.put("/ocasion/{ocasion_id}", response_model=schemas.Ocasion)
def actualizar_ocasion(ocasion_id: int, ocasion: schemas.OcasionCreate, db: Session = Depends(get_db)):
    db_ocasion = db.query(models.Ocasion).filter(models.Ocasion.id == ocasion_id).first()
    if not db_ocasion:
        raise HTTPException(status_code=404, detail="Ocasión no encontrada")
    for key, value in ocasion.dict().items():
        setattr(db_ocasion, key, value)
    db.commit()
    db.refresh(db_ocasion)
    return db_ocasion

@router.delete("/ocasion/{ocasion_id}")
def eliminar_ocasion(ocasion_id: int, db: Session = Depends(get_db)):
    db_ocasion = db.query(models.Ocasion).filter(models.Ocasion.id == ocasion_id).first()
    if not db_ocasion:
        raise HTTPException(status_code=404, detail="Ocasión no encontrada")
    db.delete(db_ocasion)
    db.commit()
    return {"ok": True}

# =================== MECANISMO TRANSMISION ===================
@router.get("/mecanismo_transmision", response_model=list[schemas.MecanismoTransmision])
def listar_mecanismo_transmision(db: Session = Depends(get_db)):
    return db.query(models.MecanismoTransmision).all()

@router.get("/mecanismo_transmision/{mecanismo_id}", response_model=schemas.MecanismoTransmision)
def obtener_mecanismo_transmision(mecanismo_id: int, db: Session = Depends(get_db)):
    mecanismo = db.query(models.MecanismoTransmision).filter(models.MecanismoTransmision.id == mecanismo_id).first()
    if not mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    return mecanismo

@router.post("/mecanismo_transmision", response_model=schemas.MecanismoTransmision)
def crear_mecanismo_transmision(mecanismo: schemas.MecanismoTransmisionCreate, db: Session = Depends(get_db)):
    db_mecanismo = models.MecanismoTransmision(**mecanismo.dict())
    db.add(db_mecanismo)
    db.commit()
    db.refresh(db_mecanismo)
    return db_mecanismo

@router.put("/mecanismo_transmision/{mecanismo_id}", response_model=schemas.MecanismoTransmision)
def actualizar_mecanismo_transmision(mecanismo_id: int, mecanismo: schemas.MecanismoTransmisionCreate, db: Session = Depends(get_db)):
    db_mecanismo = db.query(models.MecanismoTransmision).filter(models.MecanismoTransmision.id == mecanismo_id).first()
    if not db_mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    for key, value in mecanismo.dict().items():
        setattr(db_mecanismo, key, value)
    db.commit()
    db.refresh(db_mecanismo)
    return db_mecanismo

@router.delete("/mecanismo_transmision/{mecanismo_id}")
def eliminar_mecanismo_transmision(mecanismo_id: int, db: Session = Depends(get_db)):
    db_mecanismo = db.query(models.MecanismoTransmision).filter(models.MecanismoTransmision.id == mecanismo_id).first()
    if not db_mecanismo:
        raise HTTPException(status_code=404, detail="Mecanismo de transmisión no encontrado")
    db.delete(db_mecanismo)
    db.commit()
    return {"ok": True}

# =================== VINCULO MAIZ ===================
@router.get("/vinculo_maiz", response_model=list[schemas.VinculoMaiz])
def listar_vinculo_maiz(db: Session = Depends(get_db)):
    return db.query(models.VinculoMaiz).all()

@router.get("/vinculo_maiz/{vinculo_id}", response_model=schemas.VinculoMaiz)
def obtener_vinculo_maiz(vinculo_id: int, db: Session = Depends(get_db)):
    vinculo = db.query(models.VinculoMaiz).filter(models.VinculoMaiz.id == vinculo_id).first()
    if not vinculo:
        raise HTTPException(status_code=404, detail="Vínculo con el maíz no encontrado")
    return vinculo

@router.post("/vinculo_maiz", response_model=schemas.VinculoMaiz)
def crear_vinculo_maiz(vinculo: schemas.VinculoMaizCreate, db: Session = Depends(get_db)):
    db_vinculo = models.VinculoMaiz(**vinculo.dict())
    db.add(db_vinculo)
    db.commit()
    db.refresh(db_vinculo)
    return db_vinculo

@router.put("/vinculo_maiz/{vinculo_id}", response_model=schemas.VinculoMaiz)
def actualizar_vinculo_maiz(vinculo_id: int, vinculo: schemas.VinculoMaizCreate, db: Session = Depends(get_db)):
    db_vinculo = db.query(models.VinculoMaiz).filter(models.VinculoMaiz.id == vinculo_id).first()
    if not db_vinculo:
        raise HTTPException(status_code=404, detail="Vínculo con el maíz no encontrado")
    for key, value in vinculo.dict().items():
        setattr(db_vinculo, key, value)
    db.commit()
    db.refresh(db_vinculo)
    return db_vinculo

@router.delete("/vinculo_maiz/{vinculo_id}")
def eliminar_vinculo_maiz(vinculo_id: int, db: Session = Depends(get_db)):
    db_vinculo = db.query(models.VinculoMaiz).filter(models.VinculoMaiz.id == vinculo_id).first()
    if not db_vinculo:
        raise HTTPException(status_code=404, detail="Vínculo con el maíz no encontrado")
    db.delete(db_vinculo)
    db.commit()
    return {"ok": True}

# -- EJE DE TRAZABILIDAD Y GEODATOS --

# =================== TIPO PRODUCTO DRON ===================
@router.get("/tipo_producto_dron", response_model=list[schemas.TipoProductoDron])
def listar_tipo_producto_dron(db: Session = Depends(get_db)):
    return db.query(models.TipoProductoDron).all()

@router.get("/tipo_producto_dron/{producto_id}", response_model=schemas.TipoProductoDron)
def obtener_tipo_producto_dron(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(models.TipoProductoDron).filter(models.TipoProductoDron.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Tipo de producto de dron no encontrado")
    return producto

@router.post("/tipo_producto_dron", response_model=schemas.TipoProductoDron)
def crear_tipo_producto_dron(producto: schemas.TipoProductoDronCreate, db: Session = Depends(get_db)):
    db_producto = models.TipoProductoDron(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.put("/tipo_producto_dron/{producto_id}", response_model=schemas.TipoProductoDron)
def actualizar_tipo_producto_dron(producto_id: int, producto: schemas.TipoProductoDronCreate, db: Session = Depends(get_db)):
    db_producto = db.query(models.TipoProductoDron).filter(models.TipoProductoDron.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Tipo de producto de dron no encontrado")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/tipo_producto_dron/{producto_id}")
def eliminar_tipo_producto_dron(producto_id: int, db: Session = Depends(get_db)):
    db_producto = db.query(models.TipoProductoDron).filter(models.TipoProductoDron.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Tipo de producto de dron no encontrado")
    db.delete(db_producto)
    db.commit()
    return {"ok": True}

# =================== FORMATO ARCHIVO ===================
@router.get("/formato_archivo", response_model=list[schemas.FormatoArchivo])
def listar_formato_archivo(db: Session = Depends(get_db)):
    return db.query(models.FormatoArchivo).all()

@router.get("/formato_archivo/{formato_id}", response_model=schemas.FormatoArchivo)
def obtener_formato_archivo(formato_id: int, db: Session = Depends(get_db)):
    formato = db.query(models.FormatoArchivo).filter(models.FormatoArchivo.id == formato_id).first()
    if not formato:
        raise HTTPException(status_code=404, detail="Formato de archivo no encontrado")
    return formato

@router.post("/formato_archivo", response_model=schemas.FormatoArchivo)
def crear_formato_archivo(formato: schemas.FormatoArchivoCreate, db: Session = Depends(get_db)):
    db_formato = models.FormatoArchivo(**formato.dict())
    db.add(db_formato)
    db.commit()
    db.refresh(db_formato)
    return db_formato

@router.put("/formato_archivo/{formato_id}", response_model=schemas.FormatoArchivo)
def actualizar_formato_archivo(formato_id: int, formato: schemas.FormatoArchivoCreate, db: Session = Depends(get_db)):
    db_formato = db.query(models.FormatoArchivo).filter(models.FormatoArchivo.id == formato_id).first()
    if not db_formato:
        raise HTTPException(status_code=404, detail="Formato de archivo no encontrado")
    for key, value in formato.dict().items():
        setattr(db_formato, key, value)
    db.commit()
    db.refresh(db_formato)
    return db_formato

@router.delete("/formato_archivo/{formato_id}")
def eliminar_formato_archivo(formato_id: int, db: Session = Depends(get_db)):
    db_formato = db.query(models.FormatoArchivo).filter(models.FormatoArchivo.id == formato_id).first()
    if not db_formato:
        raise HTTPException(status_code=404, detail="Formato de archivo no encontrado")
    db.delete(db_formato)
    db.commit()
    return {"ok": True}

# =================== TIPO CAPA SIG ===================
@router.get("/tipo_capa_sig", response_model=list[schemas.TipoCapaSIG])
def listar_tipo_capa_sig(db: Session = Depends(get_db)):
    return db.query(models.TipoCapaSIG).all()

@router.get("/tipo_capa_sig/{capa_id}", response_model=schemas.TipoCapaSIG)
def obtener_tipo_capa_sig(capa_id: int, db: Session = Depends(get_db)):
    capa = db.query(models.TipoCapaSIG).filter(models.TipoCapaSIG.id == capa_id).first()
    if not capa:
        raise HTTPException(status_code=404, detail="Tipo de capa SIG no encontrado")
    return capa

@router.post("/tipo_capa_sig", response_model=schemas.TipoCapaSIG)
def crear_tipo_capa_sig(capa: schemas.TipoCapaSIGCreate, db: Session = Depends(get_db)):
    db_capa = models.TipoCapaSIG(**capa.dict())
    db.add(db_capa)
    db.commit()
    db.refresh(db_capa)
    return db_capa

@router.put("/tipo_capa_sig/{capa_id}", response_model=schemas.TipoCapaSIG)
def actualizar_tipo_capa_sig(capa_id: int, capa: schemas.TipoCapaSIGCreate, db: Session = Depends(get_db)):
    db_capa = db.query(models.TipoCapaSIG).filter(models.TipoCapaSIG.id == capa_id).first()
    if not db_capa:
        raise HTTPException(status_code=404, detail="Tipo de capa SIG no encontrado")
    for key, value in capa.dict().items():
        setattr(db_capa, key, value)
    db.commit()
    db.refresh(db_capa)
    return db_capa

@router.delete("/tipo_capa_sig/{capa_id}")
def eliminar_tipo_capa_sig(capa_id: int, db: Session = Depends(get_db)):
    db_capa = db.query(models.TipoCapaSIG).filter(models.TipoCapaSIG.id == capa_id).first()
    if not db_capa:
        raise HTTPException(status_code=404, detail="Tipo de capa SIG no encontrado")
    db.delete(db_capa)
    db.commit()
    return {"ok": True}

# =================== FUENTE CAPTURA ===================
@router.get("/fuente_captura", response_model=list[schemas.FuenteCaptura])
def listar_fuente_captura(db: Session = Depends(get_db)):
    return db.query(models.FuenteCaptura).all()

@router.get("/fuente_captura/{fuente_id}", response_model=schemas.FuenteCaptura)
def obtener_fuente_captura(fuente_id: int, db: Session = Depends(get_db)):
    fuente = db.query(models.FuenteCaptura).filter(models.FuenteCaptura.id == fuente_id).first()
    if not fuente:
        raise HTTPException(status_code=404, detail="Fuente de captura no encontrada")
    return fuente

@router.post("/fuente_captura", response_model=schemas.FuenteCaptura)
def crear_fuente_captura(fuente: schemas.FuenteCapturaCreate, db: Session = Depends(get_db)):
    db_fuente = models.FuenteCaptura(**fuente.dict())
    db.add(db_fuente)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.put("/fuente_captura/{fuente_id}", response_model=schemas.FuenteCaptura)
def actualizar_fuente_captura(fuente_id: int, fuente: schemas.FuenteCapturaCreate, db: Session = Depends(get_db)):
    db_fuente = db.query(models.FuenteCaptura).filter(models.FuenteCaptura.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de captura no encontrada")
    for key, value in fuente.dict().items():
        setattr(db_fuente, key, value)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.delete("/fuente_captura/{fuente_id}")
def eliminar_fuente_captura(fuente_id: int, db: Session = Depends(get_db)):
    db_fuente = db.query(models.FuenteCaptura).filter(models.FuenteCaptura.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de captura no encontrada")
    db.delete(db_fuente)
    db.commit()
    return {"ok": True}

# =================== FUENTE INFORMACION ===================
@router.get("/fuente_informacion", response_model=list[schemas.FuenteInformacion])
def listar_fuente_informacion(db: Session = Depends(get_db)):
    return db.query(models.FuenteInformacion).all()

@router.get("/fuente_informacion/{fuente_id}", response_model=schemas.FuenteInformacion)
def obtener_fuente_informacion(fuente_id: int, db: Session = Depends(get_db)):
    fuente = db.query(models.FuenteInformacion).filter(models.FuenteInformacion.id == fuente_id).first()
    if not fuente:
        raise HTTPException(status_code=404, detail="Fuente de información no encontrada")
    return fuente

@router.post("/fuente_informacion", response_model=schemas.FuenteInformacion)
def crear_fuente_informacion(fuente: schemas.FuenteInformacionCreate, db: Session = Depends(get_db)):
    db_fuente = models.FuenteInformacion(**fuente.dict())
    db.add(db_fuente)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.put("/fuente_informacion/{fuente_id}", response_model=schemas.FuenteInformacion)
def actualizar_fuente_informacion(fuente_id: int, fuente: schemas.FuenteInformacionCreate, db: Session = Depends(get_db)):
    db_fuente = db.query(models.FuenteInformacion).filter(models.FuenteInformacion.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de información no encontrada")
    for key, value in fuente.dict().items():
        setattr(db_fuente, key, value)
    db.commit()
    db.refresh(db_fuente)
    return db_fuente

@router.delete("/fuente_informacion/{fuente_id}")
def eliminar_fuente_informacion(fuente_id: int, db: Session = Depends(get_db)):
    db_fuente = db.query(models.FuenteInformacion).filter(models.FuenteInformacion.id == fuente_id).first()
    if not db_fuente:
        raise HTTPException(status_code=404, detail="Fuente de información no encontrada")
    db.delete(db_fuente)
    db.commit()
    return {"ok": True}

# =================== ORIGEN MUESTRA ===================
@router.get("/origen_muestra", response_model=list[schemas.OrigenMuestra])
def listar_origen_muestra(db: Session = Depends(get_db)):
    return db.query(models.OrigenMuestra).all()

@router.get("/origen_muestra/{origen_id}", response_model=schemas.OrigenMuestra)
def obtener_origen_muestra(origen_id: int, db: Session = Depends(get_db)):
    origen = db.query(models.OrigenMuestra).filter(models.OrigenMuestra.id == origen_id).first()
    if not origen:
        raise HTTPException(status_code=404, detail="Origen de muestra no encontrado")
    return origen

@router.post("/origen_muestra", response_model=schemas.OrigenMuestra)
def crear_origen_muestra(origen: schemas.OrigenMuestraCreate, db: Session = Depends(get_db)):
    db_origen = models.OrigenMuestra(**origen.dict())
    db.add(db_origen)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.put("/origen_muestra/{origen_id}", response_model=schemas.OrigenMuestra)
def actualizar_origen_muestra(origen_id: int, origen: schemas.OrigenMuestraCreate, db: Session = Depends(get_db)):
    db_origen = db.query(models.OrigenMuestra).filter(models.OrigenMuestra.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de muestra no encontrado")
    for key, value in origen.dict().items():
        setattr(db_origen, key, value)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.delete("/origen_muestra/{origen_id}")
def eliminar_origen_muestra(origen_id: int, db: Session = Depends(get_db)):
    db_origen = db.query(models.OrigenMuestra).filter(models.OrigenMuestra.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de muestra no encontrado")
    db.delete(db_origen)
    db.commit()
    return {"ok": True}

# ORIGEN SEMILLA
@router.get("/origen_semilla", response_model=list[schemas.OrigenSemilla])
def listar_origen_semilla(db: Session = Depends(get_db)):
    return db.query(models.OrigenSemilla).all()

@router.get("/origen_semilla/{origen_id}", response_model=schemas.OrigenSemilla)
def obtener_origen_semilla(origen_id: int, db: Session = Depends(get_db)):
    origen = db.query(models.OrigenSemilla).filter(models.OrigenSemilla.id == origen_id).first()
    if not origen:
        raise HTTPException(status_code=404, detail="Origen de semilla no encontrado")
    return origen

@router.post("/origen_semilla", response_model=schemas.OrigenSemilla)
def crear_origen_semilla(origen: schemas.OrigenSemillaCreate, db: Session = Depends(get_db)):
    db_origen = models.OrigenSemilla(**origen.dict())
    db.add(db_origen)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.put("/origen_semilla/{origen_id}", response_model=schemas.OrigenSemilla)
def actualizar_origen_semilla(origen_id: int, origen: schemas.OrigenSemillaCreate, db: Session = Depends(get_db)):
    db_origen = db.query(models.OrigenSemilla).filter(models.OrigenSemilla.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de semilla no encontrado")
    for key, value in origen.dict().items():
        setattr(db_origen, key, value)
    db.commit()
    db.refresh(db_origen)
    return db_origen

@router.delete("/origen_semilla/{origen_id}")
def eliminar_origen_semilla(origen_id: int, db: Session = Depends(get_db)):
    db_origen = db.query(models.OrigenSemilla).filter(models.OrigenSemilla.id == origen_id).first()
    if not db_origen:
        raise HTTPException(status_code=404, detail="Origen de semilla no encontrado")
    db.delete(db_origen)
    db.commit()
    return {"ok": True}