# Agroplataforma Maíz Nativo - Backend Sociocultural

Este proyecto es un backend desarrollado en FastAPI para la gestión de información social y cultural relacionada con el maíz nativo de la Huasteca Potosina. Expone una API RESTful para CRUD de todas las tablas sociales y culturales, conectada a una base de datos y lista para ejecutarse en Docker.

## Características principales
- API RESTful con FastAPI y SQLAlchemy
- CRUD completo para todas las tablas sociales y culturales
- Conexión a base de datos (configurable)
- Contenerización con Docker
- Código organizado por modelos, esquemas y rutas (social y cultural)

## Estructura del proyecto

```
├── Dockerfile
├── main.py
├── requirements.txt
├── models.py
├── schemas.py
├── routers/
│   ├── social.py
│   └── cultural.py
└── ...
```

## Configuración rápida

1. **Clona el repositorio y entra al directorio:**
   ```bash
   git clone <repo_url>
   cd agroplataforma_maiz_nativo/agroplataforma-backend/sociocultural
   ```

2. **Configura la base de datos:**
   - Edita la cadena de conexión en `main.py` o usa variables de entorno según tu configuración.

3. **Instala dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Levanta el servidor de desarrollo:**
   ```bash
   uvicorn main:app --reload
   ```

5. **O usa Docker:**
   ```bash
   docker build -t agroplataforma-sociocultural .
   docker run -p 8000:8000 agroplataforma-sociocultural
   ```

6. **La API estará disponible en:**
   - http://localhost:8000
   - Documentación interactiva: http://localhost:8000/docs

## Uso de la API

- Todos los endpoints sociales están bajo el prefijo `/social`.
- Todos los endpoints culturales están bajo el prefijo `/cultural`.

Ejemplo de endpoints sociales:
- `GET /social/productores` (listar)
- `POST /social/productores` (crear)
- `PUT /social/productores/{id}` (actualizar)
- `DELETE /social/productores/{id}` (eliminar)

Ejemplo de endpoints culturales:
- `GET /cultural/saberes_tradicionales` (listar)
- `POST /cultural/saberes_tradicionales` (crear)
- `PUT /cultural/saberes_tradicionales/{id}` (actualizar)
- `DELETE /cultural/saberes_tradicionales/{id}` (eliminar)

Repite el patrón para las demás tablas sociales y culturales.

## Endpoints disponibles por tabla

| Tabla social                  | Listar (GET)                | Obtener (GET)                | Crear (POST)                | Actualizar (PUT)                | Eliminar (DELETE)                |
|-------------------------------|-----------------------------|------------------------------|-----------------------------|----------------------------------|----------------------------------|
| productores                   | /social/productores         | /social/productores/{id}     | /social/productores         | /social/productores/{id}         | /social/productores/{id}         |
| consentimientos               | /social/consentimientos     | /social/consentimientos/{id} | /social/consentimientos     | /social/consentimientos/{id}     | /social/consentimientos/{id}     |
| perfiles_socioeconomicos      | /social/perfiles_socioeconomicos | /social/perfiles_socioeconomicos/{id} | /social/perfiles_socioeconomicos | /social/perfiles_socioeconomicos/{id} | /social/perfiles_socioeconomicos/{id} |
| seguridad_alimentaria         | /social/seguridad_alimentaria | /social/seguridad_alimentaria/{id} | /social/seguridad_alimentaria | /social/seguridad_alimentaria/{id} | /social/seguridad_alimentaria/{id} |
| productores_practica          | /social/productores_practica | /social/productores_practica/{id} | /social/productores_practica | /social/productores_practica/{id} | /social/productores_practica/{id} |
| productores_lengua            | /social/productores_lengua   | /social/productores_lengua/{id} | /social/productores_lengua   | /social/productores_lengua/{id}   | /social/productores_lengua/{id}   |
| redes_intercambio             | /social/redes_intercambio    | /social/redes_intercambio/{id} | /social/redes_intercambio    | /social/redes_intercambio/{id}    | /social/redes_intercambio/{id}    |
| vulnerabilidades_climaticas   | /social/vulnerabilidades_climaticas | /social/vulnerabilidades_climaticas/{id} | /social/vulnerabilidades_climaticas | /social/vulnerabilidades_climaticas/{id} | /social/vulnerabilidades_climaticas/{id} |
| geolocalizaciones_productor   | /social/geolocalizaciones_productor | /social/geolocalizaciones_productor/{id} | /social/geolocalizaciones_productor | /social/geolocalizaciones_productor/{id} | /social/geolocalizaciones_productor/{id} |

| Tabla cultural                | Listar (GET)                | Obtener (GET)                | Crear (POST)                | Actualizar (PUT)                | Eliminar (DELETE)                |
|-------------------------------|-----------------------------|------------------------------|-----------------------------|----------------------------------|----------------------------------|
| saberes_tradicionales         | /cultural/saberes_tradicionales | /cultural/saberes_tradicionales/{id} | /cultural/saberes_tradicionales | /cultural/saberes_tradicionales/{id} | /cultural/saberes_tradicionales/{id} |
| rituales_agricolas            | /cultural/rituales_agricolas | /cultural/rituales_agricolas/{id} | /cultural/rituales_agricolas | /cultural/rituales_agricolas/{id} | /cultural/rituales_agricolas/{id} |
| narrativas_orales             | /cultural/narrativas_orales  | /cultural/narrativas_orales/{id} | /cultural/narrativas_orales  | /cultural/narrativas_orales/{id}  | /cultural/narrativas_orales/{id}  |
| gastronomias_tradicionales    | /cultural/gastronomias_tradicionales | /cultural/gastronomias_tradicionales/{id} | /cultural/gastronomias_tradicionales | /cultural/gastronomias_tradicionales/{id} | /cultural/gastronomias_tradicionales/{id} |
| transmisiones_conocimiento    | /cultural/transmisiones_conocimiento | /cultural/transmisiones_conocimiento/{id} | /cultural/transmisiones_conocimiento | /cultural/transmisiones_conocimiento/{id} | /cultural/transmisiones_conocimiento/{id} |
| identidades_culturales        | /cultural/identidades_culturales | /cultural/identidades_culturales/{id} | /cultural/identidades_culturales | /cultural/identidades_culturales/{id} | /cultural/identidades_culturales/{id} |
| nombres_lenguas_originarias   | /cultural/nombres_lenguas_originarias | /cultural/nombres_lenguas_originarias/{id} | /cultural/nombres_lenguas_originarias | /cultural/nombres_lenguas_originarias/{id} | /cultural/nombres_lenguas_originarias/{id} |

> Repite el patrón para las demás tablas sociales y culturales definidas en el backend.

Todos los endpoints aceptan y devuelven datos en formato JSON. Consulta la documentación interactiva en `/docs` para ver los modelos y probar los endpoints.

---

**Contacto:**
Para dudas o soporte, contacta a los responsables del proyecto.

## Ejemplo de uso: Crear un productor

```json
POST /social/productores
{
  "nombre": "Juan Pérez",
  "edad": 45,
  "genero": "masculino",
  "comunidad": "La Esperanza",
  "activo": true
}
```

## Ejemplo de respuesta
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "edad": 45,
  "genero": "masculino",
  "comunidad": "La Esperanza",
  "activo": true,
  "created_at": "2026-03-22T12:00:00",
  "updated_at": "2026-03-22T12:00:00"
}
```

Puedes consultar la documentación interactiva en `/docs` para ver todos los modelos y probar los endpoints directamente desde el navegador.
