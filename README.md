# Agroplataforma Maíz Nativo - Backend de Catálogos

Este proyecto es un backend desarrollado en FastAPI para la gestión de catálogos agrícolas relacionados con el maíz nativo de la Huasteca Potosina. Expone una API RESTful para CRUD de más de 20 tablas de catálogos, conectada a una base de datos PostgreSQL y lista para ejecutarse en Docker.

## Características principales
- API RESTful con FastAPI y SQLAlchemy
- CRUD completo para todos los catálogos definidos en el esquema SQL
- Conexión a PostgreSQL
- Contenerización con Docker y Docker Compose
- Código organizado por modelos, esquemas, rutas y utilidades

## Estructura del proyecto

```
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── main.py
├── db.py
├── models.py
├── schemas.py
├── routers/
│   └── catalogos.py
├── requirements.txt
└── ...
```

## Configuración rápida

1. **Clona el repositorio y entra al directorio:**
   ```bash
   git clone <repo_url>
   cd agroplataforma_maiz_nativo/agroplataforma-backend
   ```

2. **Copia el archivo de variables de entorno:**
   ```bash
   cp .env.example .env
   # Edita .env con tus credenciales de base de datos
   ```

3. **Levanta todo con Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **La API estará disponible en:**
   - http://localhost:8000
   - Documentación interactiva: http://localhost:8000/docs

## Uso de la API

- Todos los endpoints están bajo el prefijo `/catalogos`.
- Ejemplo de endpoint para razas de maíz:
  - `GET /catalogos/raza_maiz` (listar)
  - `POST /catalogos/raza_maiz` (crear)
  - `PUT /catalogos/raza_maiz/{id}` (actualizar)
  - `DELETE /catalogos/raza_maiz/{id}` (eliminar)

Repite el patrón para los demás catálogos definidos en el esquema.

## Endpoints disponibles por catálogo

| Catálogo                | Listar (GET)                | Obtener (GET)                | Crear (POST)                | Actualizar (PUT)                | Eliminar (DELETE)                |
|------------------------ |-----------------------------|------------------------------|-----------------------------|----------------------------------|----------------------------------|
| raza_maiz               | /catalogos/raza_maiz        | /catalogos/raza_maiz/{id}    | /catalogos/raza_maiz        | /catalogos/raza_maiz/{id}        | /catalogos/raza_maiz/{id}        |
| color_grano             | /catalogos/color_grano      | /catalogos/color_grano/{id}  | /catalogos/color_grano      | /catalogos/color_grano/{id}      | /catalogos/color_grano/{id}      |
| estado_conservacion     | /catalogos/estado_conservacion | /catalogos/estado_conservacion/{id} | /catalogos/estado_conservacion | /catalogos/estado_conservacion/{id} | /catalogos/estado_conservacion/{id} |
| uso_maiz                | /catalogos/uso_maiz         | /catalogos/uso_maiz/{id}     | /catalogos/uso_maiz         | /catalogos/uso_maiz/{id}         | /catalogos/uso_maiz/{id}         |
| clase_uso_suelo         | /catalogos/clase_uso_suelo  | /catalogos/clase_uso_suelo/{id} | /catalogos/clase_uso_suelo  | /catalogos/clase_uso_suelo/{id}  | /catalogos/clase_uso_suelo/{id}  |
| tipo_evento_climatico   | /catalogos/tipo_evento_climatico | /catalogos/tipo_evento_climatico/{id} | /catalogos/tipo_evento_climatico | /catalogos/tipo_evento_climatico/{id} | /catalogos/tipo_evento_climatico/{id} |
| variable_ambiental      | /catalogos/variable_ambiental | /catalogos/variable_ambiental/{id} | /catalogos/variable_ambiental | /catalogos/variable_ambiental/{id} | /catalogos/variable_ambiental/{id} |
| tipo_productor          | /catalogos/tipo_productor   | /catalogos/tipo_productor/{id}| /catalogos/tipo_productor   | /catalogos/tipo_productor/{id}   | /catalogos/tipo_productor/{id}   |
| lengua                  | /catalogos/lengua           | /catalogos/lengua/{id}        | /catalogos/lengua           | /catalogos/lengua/{id}           | /catalogos/lengua/{id}           |
| pueblo_originario       | /catalogos/pueblo_originario| /catalogos/pueblo_originario/{id} | /catalogos/pueblo_originario | /catalogos/pueblo_originario/{id} | /catalogos/pueblo_originario/{id} |
| origen_muestra          | /catalogos/origen_muestra   | /catalogos/origen_muestra/{id}| /catalogos/origen_muestra   | /catalogos/origen_muestra/{id}   | /catalogos/origen_muestra/{id}   |
| estado                  | /catalogos/estado           | /catalogos/estado/{id}        | /catalogos/estado           | /catalogos/estado/{id}           | /catalogos/estado/{id}           |
| municipio               | /catalogos/municipio        | /catalogos/municipio/{id}     | /catalogos/municipio        | /catalogos/municipio/{id}        | /catalogos/municipio/{id}        |
| comunidad               | /catalogos/comunidad        | /catalogos/comunidad/{id}     | /catalogos/comunidad        | /catalogos/comunidad/{id}        | /catalogos/comunidad/{id}        |
| localidad               | /catalogos/localidad        | /catalogos/localidad/{id}     | /catalogos/localidad        | /catalogos/localidad/{id}        | /catalogos/localidad/{id}        |
| colonia                 | /catalogos/colonia          | /catalogos/colonia/{id}       | /catalogos/colonia          | /catalogos/colonia/{id}          | /catalogos/colonia/{id}          |

> Repite el patrón para los demás catálogos definidos en el backend (agronómicos, territoriales, etc.).

Todos los endpoints aceptan y devuelven datos en formato JSON. Consulta la documentación interactiva en `/docs` para ver los modelos y probar los endpoints.

---

**Contacto:**
Para dudas o soporte, contacta a los responsables del proyecto.

## Ejemplo de uso: Crear una localidad

```json
POST /catalogos/localidad
{
  "clave_inegi": "240010001",
  "nombre": "La Esperanza",
  "nombre_lengua_orig": null,
  "tipo": "rural",
  "categoria": "localidad",
  "poblacion_total": 1200,
  "num_viviendas": 300,
  "grado_marginacion": "alta",
  "indigena": false,
  "latitud": 21.12345,
  "longitud": -98.12345,
  "altitud_m": 120,
  "municipio_id": 1,
  "comunidad_id": 2,
  "fuente": "INEGI 2020"
}
```

## Ejemplo de respuesta
```json
{
  "id": 10,
  "clave_inegi": "240010001",
  "nombre": "La Esperanza",
  "nombre_lengua_orig": null,
  "tipo": "rural",
  "categoria": "localidad",
  "poblacion_total": 1200,
  "num_viviendas": 300,
  "grado_marginacion": "alta",
  "indigena": false,
  "latitud": 21.12345,
  "longitud": -98.12345,
  "altitud_m": 120,
  "municipio_id": 1,
  "comunidad_id": 2,
  "fuente": "INEGI 2020",
  "created_at": "2026-03-22T12:00:00",
  "updated_at": "2026-03-22T12:00:00"
}
```

Puedes consultar la documentación interactiva en `/docs` para ver todos los modelos y probar los endpoints directamente desde el navegador.
