from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from database import get_db

from models.germoplasma import ColorGrano, RazaMaiz, EstadoConservacion, UsoMaiz
from models.agronomico import TipoPractica, PracticaAgricola, SistemaManejo, SistemaCultivo, MetodoAlmacenamiento

import schemas.germoplasma as germplasma_schemes
import schemas.agronomico as agronomico_schemes

router = APIRouter()

# GERMOPLASMA DE MAÍZ NATIVO

# =================== RAZA MAIZ ===================
@router.get("/raza_maiz", response_model=list[germplasma_schemes.RazaMaiz])
def listar_razas(db: Session = Depends(get_db)):
	return db.query(RazaMaiz).all()

@router.get("/raza_maiz/{raza_id}", response_model=germplasma_schemes.RazaMaiz)
def obtener_raza(raza_id: int, db: Session = Depends(get_db)):
	raza = db.query(RazaMaiz).filter(RazaMaiz.id == raza_id).first()
	if not raza:
		raise HTTPException(status_code=404, detail="Raza no encontrada")
	return raza

@router.post("/raza_maiz", response_model=germplasma_schemes.RazaMaiz)
def crear_raza(raza: germplasma_schemes.RazaMaizCreate, db: Session = Depends(get_db)):
	db_raza = RazaMaiz(**raza.dict())
	db.add(db_raza)
	db.commit()
	db.refresh(db_raza)
	return db_raza

@router.put("/raza_maiz/{raza_id}", response_model=germplasma_schemes.RazaMaiz)
def actualizar_raza(raza_id: int, raza: germplasma_schemes.RazaMaizCreate, db: Session = Depends(get_db)):
	db_raza = db.query(RazaMaiz).filter(RazaMaiz.id == raza_id).first()
	if not db_raza:
		raise HTTPException(status_code=404, detail="Raza no encontrada")
	for key, value in raza.dict().items():
		setattr(db_raza, key, value)
	db.commit()
	db.refresh(db_raza)
	return db_raza

@router.delete("/raza_maiz/{raza_id}")
def eliminar_raza(raza_id: int, db: Session = Depends(get_db)):
	db_raza = db.query(RazaMaiz).filter(RazaMaiz.id == raza_id).first()
	if not db_raza:
		raise HTTPException(status_code=404, detail="Raza no encontrada")
	db.delete(db_raza)
	db.commit()
	return {"ok": True}

# =================== COLOR GRANO ===================
@router.get("/color_grano", response_model=list[germplasma_schemes.ColorGrano])
def listar_colores(db: Session = Depends(get_db)):
	return db.query(ColorGrano).all()

@router.get("/color_grano/{color_id}", response_model=germplasma_schemes.ColorGrano)
def obtener_color(color_id: int, db: Session = Depends(get_db)):
	color = db.query(ColorGrano).filter(ColorGrano.id == color_id).first()
	if not color:
		raise HTTPException(status_code=404, detail="Color no encontrado")
	return color

@router.post("/color_grano", response_model=germplasma_schemes.ColorGrano)
def crear_color(color: germplasma_schemes.ColorGranoCreate, db: Session = Depends(get_db)):
	db_color = ColorGrano(**color.dict())
	db.add(db_color)
	db.commit()
	db.refresh(db_color)
	return db_color

@router.put("/color_grano/{color_id}", response_model=germplasma_schemes.ColorGrano)
def actualizar_color(color_id: int, color: germplasma_schemes.ColorGranoCreate, db: Session = Depends(get_db)):
	db_color = db.query(ColorGrano).filter(ColorGrano.id == color_id).first()
	if not db_color:
		raise HTTPException(status_code=404, detail="Color no encontrado")
	for key, value in color.dict().items():
		setattr(db_color, key, value)
	db.commit()
	db.refresh(db_color)
	return db_color

@router.delete("/color_grano/{color_id}")
def eliminar_color(color_id: int, db: Session = Depends(get_db)):
	db_color = db.query(ColorGrano).filter(ColorGrano.id == color_id).first()
	if not db_color:
		raise HTTPException(status_code=404, detail="Color no encontrado")
	db.delete(db_color)
	db.commit()
	return {"ok": True}

# =================== ESTADO CONSERVACION ===================
@router.get("/estado_conservacion", response_model=list[germplasma_schemes.EstadoConservacion])
def listar_estados_conservacion(db: Session = Depends(get_db)):
	return db.query(EstadoConservacion).all()

@router.get("/estado_conservacion/{estado_id}", response_model=germplasma_schemes.EstadoConservacion)
def obtener_estado_conservacion(estado_id: int, db: Session = Depends(get_db)):
	estado = db.query(EstadoConservacion).filter(EstadoConservacion.id == estado_id).first()
	if not estado:
		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
	return estado

@router.post("/estado_conservacion", response_model=germplasma_schemes.EstadoConservacion)
def crear_estado_conservacion(estado: germplasma_schemes.EstadoConservacionCreate, db: Session = Depends(get_db)):
	db_estado = EstadoConservacion(**estado.dict())
	db.add(db_estado)
	db.commit()
	db.refresh(db_estado)
	return db_estado

@router.put("/estado_conservacion/{estado_id}", response_model=germplasma_schemes.EstadoConservacion)
def actualizar_estado_conservacion(estado_id: int, estado: germplasma_schemes.EstadoConservacionCreate, db: Session = Depends(get_db)):
	db_estado = db.query(EstadoConservacion).filter(EstadoConservacion.id == estado_id).first()
	if not db_estado:
		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
	for key, value in estado.dict().items():
		setattr(db_estado, key, value)
	db.commit()
	db.refresh(db_estado)
	return db_estado

@router.delete("/estado_conservacion/{estado_id}")
def eliminar_estado_conservacion(estado_id: int, db: Session = Depends(get_db)):
	db_estado = db.query(EstadoConservacion).filter(EstadoConservacion.id == estado_id).first()
	if not db_estado:
		raise HTTPException(status_code=404, detail="Estado de conservación no encontrado")
	db.delete(db_estado)
	db.commit()
	return {"ok": True}

# =================== USO MAIZ ===================
@router.get("/uso_maiz", response_model=list[germplasma_schemes.UsoMaiz])
def listar_usos_maiz(db: Session = Depends(get_db)):
	return db.query(UsoMaiz).all()

@router.get("/uso_maiz/{uso_id}", response_model=germplasma_schemes.UsoMaiz)
def obtener_uso_maiz(uso_id: int, db: Session = Depends(get_db)):
	uso = db.query(UsoMaiz).filter(UsoMaiz.id == uso_id).first()
	if not uso:
		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
	return uso

@router.post("/uso_maiz", response_model=germplasma_schemes.UsoMaiz)
def crear_uso_maiz(uso: germplasma_schemes.UsoMaizCreate, db: Session = Depends(get_db)):
	db_uso = UsoMaiz(**uso.dict())
	db.add(db_uso)
	db.commit()
	db.refresh(db_uso)
	return db_uso

@router.put("/uso_maiz/{uso_id}", response_model=germplasma_schemes.UsoMaiz)
def actualizar_uso_maiz(uso_id: int, uso: germplasma_schemes.UsoMaizCreate, db: Session = Depends(get_db)):
	db_uso = db.query(UsoMaiz).filter(UsoMaiz.id == uso_id).first()
	if not db_uso:
		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
	for key, value in uso.dict().items():
		setattr(db_uso, key, value)
	db.commit()
	db.refresh(db_uso)
	return db_uso

@router.delete("/uso_maiz/{uso_id}")
def eliminar_uso_maiz(uso_id: int, db: Session = Depends(get_db)):
	db_uso = db.query(UsoMaiz).filter(UsoMaiz.id == uso_id).first()
	if not db_uso:
		raise HTTPException(status_code=404, detail="Uso de maíz no encontrado")
	db.delete(db_uso)
	db.commit()
	return {"ok": True}

# EJE AGRONÓMICO

# =================== TIPO PRACTICA ===================
@router.get("/tipo_practica", response_model=list[agronomico_schemes.TipoPractica])
def listar_tipo_practica(db: Session = Depends(get_db)):
    return db.query(TipoPractica).all()

@router.get("/tipo_practica/{tipo_id}", response_model=agronomico_schemes.TipoPractica)
def obtener_tipo_practica(tipo_id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoPractica).filter(TipoPractica.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
    return tipo

@router.post("/tipo_practica", response_model=agronomico_schemes.TipoPractica)
def crear_tipo_practica(tipo: agronomico_schemes.TipoPracticaCreate, db: Session = Depends(get_db)):
    db_tipo = TipoPractica(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.put("/tipo_practica/{tipo_id}", response_model=agronomico_schemes.TipoPractica)
def actualizar_tipo_practica(tipo_id: int, tipo: agronomico_schemes.TipoPracticaCreate, db: Session = Depends(get_db)):
    db_tipo = db.query(TipoPractica).filter(TipoPractica.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipo_practica/{tipo_id}")
def eliminar_tipo_practica(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = db.query(TipoPractica).filter(TipoPractica.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="Tipo de práctica no encontrado")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}

# =================== PRACTICA AGRICOLA ===================
@router.get("/practica_agricola", response_model=list[agronomico_schemes.PracticaAgricola])
def listar_practicas_agricolas(db: Session = Depends(get_db)):
    return db.query(PracticaAgricola).all()

@router.get("/practica_agricola/{practica_id}", response_model=agronomico_schemes.PracticaAgricola)
def obtener_practica_agricola(practica_id: int, db: Session = Depends(get_db)):
    practica = db.query(PracticaAgricola).filter(PracticaAgricola.id == practica_id).first()
    if not practica:
        raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
    return practica

@router.post("/practica_agricola", response_model=agronomico_schemes.PracticaAgricola)
def crear_practica_agricola(practica: agronomico_schemes.PracticaAgricolaCreate, db: Session = Depends(get_db)):
    db_practica = PracticaAgricola(**practica.dict())
    db.add(db_practica)
    db.commit()
    db.refresh(db_practica)
    return db_practica

@router.put("/practica_agricola/{practica_id}", response_model=agronomico_schemes.PracticaAgricola)
def actualizar_practica_agricola(practica_id: int, practica: agronomico_schemes.PracticaAgricolaCreate, db: Session = Depends(get_db)):
    db_practica = db.query(PracticaAgricola).filter(PracticaAgricola.id == practica_id).first()
    if not db_practica:
        raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
    for key, value in practica.dict().items():
        setattr(db_practica, key, value)
    db.commit()
    db.refresh(db_practica)
    return db_practica

@router.delete("/practica_agricola/{practica_id}")
def eliminar_practica_agricola(practica_id: int, db: Session = Depends(get_db)):
    db_practica = db.query(PracticaAgricola).filter(PracticaAgricola.id == practica_id).first()
    if not db_practica:
        raise HTTPException(status_code=404, detail="Práctica agrícola no encontrada")
    db.delete(db_practica)
    db.commit()
    return {"ok": True}

# =================== SISTEMA MANEJO ===================
@router.get("/sistema_manejo", response_model=list[agronomico_schemes.SistemaManejo])
def listar_sistemas_manejo(db: Session = Depends(get_db)):
    return db.query(SistemaManejo).all()

@router.get("/sistema_manejo/{sistema_id}", response_model=agronomico_schemes.SistemaManejo)
def obtener_sistema_manejo(sistema_id: int, db: Session = Depends(get_db)):
    sistema = db.query(SistemaManejo).filter(SistemaManejo.id == sistema_id).first()
    if not sistema:
        raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
    return sistema

@router.post("/sistema_manejo", response_model=agronomico_schemes.SistemaManejo)
def crear_sistema_manejo(sistema: agronomico_schemes.SistemaManejoCreate, db: Session = Depends(get_db)):
    db_sistema = SistemaManejo(**sistema.dict())
    db.add(db_sistema)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.put("/sistema_manejo/{sistema_id}", response_model=agronomico_schemes.SistemaManejo)
def actualizar_sistema_manejo(sistema_id: int, sistema: agronomico_schemes.SistemaManejoCreate, db: Session = Depends(get_db)):
    db_sistema = db.query(SistemaManejo).filter(SistemaManejo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
    for key, value in sistema.dict().items():
        setattr(db_sistema, key, value)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.delete("/sistema_manejo/{sistema_id}")
def eliminar_sistema_manejo(sistema_id: int, db: Session = Depends(get_db)):
    db_sistema = db.query(SistemaManejo).filter(SistemaManejo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de manejo no encontrado")
    db.delete(db_sistema)
    db.commit()
    return {"ok": True}

# =================== SISTEMA CULTIVO ===================
@router.get("/sistema_cultivo", response_model=list[agronomico_schemes.SistemaCultivo])
def listar_sistema_cultivo(db: Session = Depends(get_db)):
    return db.query(SistemaCultivo).all()

@router.get("/sistema_cultivo/{sistema_id}", response_model=agronomico_schemes.SistemaCultivo)
def obtener_sistema_cultivo(sistema_id: int, db: Session = Depends(get_db)):
    sistema = db.query(SistemaCultivo).filter(SistemaCultivo.id == sistema_id).first()
    if not sistema:
        raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
    return sistema

@router.post("/sistema_cultivo", response_model=agronomico_schemes.SistemaCultivo)
def crear_sistema_cultivo(sistema: agronomico_schemes.SistemaCultivoCreate, db: Session = Depends(get_db)):
    db_sistema = SistemaCultivo(**sistema.dict())
    db.add(db_sistema)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.put("/sistema_cultivo/{sistema_id}", response_model=agronomico_schemes.SistemaCultivo)
def actualizar_sistema_cultivo(sistema_id: int, sistema: agronomico_schemes.SistemaCultivoCreate, db: Session = Depends(get_db)):
    db_sistema = db.query(SistemaCultivo).filter(SistemaCultivo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
    for key, value in sistema.dict().items():
        setattr(db_sistema, key, value)
    db.commit()
    db.refresh(db_sistema)
    return db_sistema

@router.delete("/sistema_cultivo/{sistema_id}")
def eliminar_sistema_cultivo(sistema_id: int, db: Session = Depends(get_db)):
    db_sistema = db.query(SistemaCultivo).filter(SistemaCultivo.id == sistema_id).first()
    if not db_sistema:
        raise HTTPException(status_code=404, detail="Sistema de cultivo no encontrado")
    db.delete(db_sistema)
    db.commit()
    return {"ok": True}


# =================== METODO ALMACENAMIENTO ===================
@router.get("/metodo_almacenamiento", response_model=list[agronomico_schemes.MetodoAlmacenamiento])
def listar_metodo_almacenamiento(db: Session = Depends(get_db)):
    return db.query(MetodoAlmacenamiento).all()

@router.get("/metodo_almacenamiento/{metodo_id}", response_model=agronomico_schemes.MetodoAlmacenamiento)
def obtener_metodo_almacenamiento(metodo_id: int, db: Session = Depends(get_db)):
    metodo = db.query(MetodoAlmacenamiento).filter(MetodoAlmacenamiento.id == metodo_id).first()
    if not metodo:
        raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
    return metodo

@router.post("/metodo_almacenamiento", response_model=agronomico_schemes.MetodoAlmacenamiento)
def crear_metodo_almacenamiento(metodo: agronomico_schemes.MetodoAlmacenamientoCreate, db: Session = Depends(get_db)):
    db_metodo = MetodoAlmacenamiento(**metodo.dict())
    db.add(db_metodo)
    db.commit()
    db.refresh(db_metodo)
    return db_metodo

@router.put("/metodo_almacenamiento/{metodo_id}", response_model=agronomico_schemes.MetodoAlmacenamiento)
def actualizar_metodo_almacenamiento(metodo_id: int, metodo: agronomico_schemes.MetodoAlmacenamientoCreate, db: Session = Depends(get_db)):
    db_metodo = db.query(MetodoAlmacenamiento).filter(MetodoAlmacenamiento.id == metodo_id).first()
    if not db_metodo:
        raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
    for key, value in metodo.dict().items():
        setattr(db_metodo, key, value)
    db.commit()
    db.refresh(db_metodo)
    return db_metodo

@router.delete("/metodo_almacenamiento/{metodo_id}")
def eliminar_metodo_almacenamiento(metodo_id: int, db: Session = Depends(get_db)):
    db_metodo = db.query(MetodoAlmacenamiento).filter(MetodoAlmacenamiento.id == metodo_id).first()
    if not db_metodo:
        raise HTTPException(status_code=404, detail="Método de almacenamiento no encontrado")
    db.delete(db_metodo)
    db.commit()
    return {"ok": True}

