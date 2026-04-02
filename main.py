from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth.router import router as auth_router

from routes.geo.router import router as geo_router
from routes.amb.router import router as amb_router

from routes.social.router import router as social_router
from routes.cultural.router import router as cultural_router

from routes.agro.router import router as agro_router
from routes.fenotipo.router import router as fenotipo_router

from routes.trazabilidad.router import router as trazabilidad_router

app = FastAPI(title="Agroplataforma Maíz API")

# Configuración de CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*","https://agromaiz.mx"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Rutas por módulo

app.include_router(auth_router, prefix="/api/auth", tags=["Autenticación"])

app.include_router(geo_router, prefix="/api/geo", tags=["Geoespacial"])
app.include_router(amb_router, prefix="/api/amb", tags=["Ambiental"])

app.include_router(social_router, prefix="/api/social", tags=["Social"])
app.include_router(cultural_router, prefix="/api/cultural", tags=["Cultural"])

app.include_router(agro_router, prefix="/api/agro", tags=["Agronómico"])
app.include_router(fenotipo_router, prefix="/api/fenotipo", tags=["Fenotipo"])

app.include_router(trazabilidad_router, prefix="/api/trazabilidad", tags=["Trazabilidad"])


@app.get("/")
def root():
    return {"message": "API Agroplataforma Maíz funcionando"}