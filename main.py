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
#MongoDB
from routes.mongo_media.router import router as mongo_media_router

#Productores
from routes.productores.router import router as productores_router

# Parcelas
from routes.parcelas.router import router as parcelas_router

# Ubicaciones
from routes.ubicaciones.router import router as ubicaciones_router

# Core
from routes.core.router import router as core_router

app = FastAPI(title="Agroplataforma Maíz API", redirect_slashes=False)

# Configuración de CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://pushchair-cobbler-storage.ngrok-free.dev",
        "https://agromaiz.mx",
        "https://www.agromaiz.mx",
        "https://agro-frontend-prueba-tau.vercel.app",
    ],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Rutas por módulo

app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])

# Productores
app.include_router(productores_router, prefix="/productores", tags=["Productores"])

# Parcelas
app.include_router(parcelas_router, prefix="/parcelas", tags=["Parcelas"])

# Ubicaciones
app.include_router(ubicaciones_router, prefix="/ubicaciones", tags=["Ubicaciones"])

# Core
app.include_router(core_router, prefix="/core")

# Default
app.include_router(social_router, prefix="/social")

#app.include_router(geo_router, prefix="/geo", tags=["Geoespacial"])

#app.include_router(amb_router, prefix="/amb", tags=["Ambiental"])

#app.include_router(cultural_router, prefix="/cultural", tags=["Cultural"])

#app.include_router(agro_router, prefix="/agro", tags=["Agronómico"])

#app.include_router(fenotipo_router, prefix="/fenotipo", tags=["Fenotipo"])

#app.include_router(trazabilidad_router, prefix="/trazabilidad", tags=["Trazabilidad"])

#MongoDB
app.include_router(mongo_media_router)

@app.get("/")
def root():
    return {"message": "API Agroplataforma Maíz funcionando"}