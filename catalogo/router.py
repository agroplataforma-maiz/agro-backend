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
