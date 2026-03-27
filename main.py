from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#from agro.router import router as agro_router
from catalogo.router import router as catalogo_router
#from geo.router import router as geo_router
#from social.router import router as social_router

app = FastAPI(title="Agroplataforma Maíz API")

# Configuración de CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["https://agromaiz.mx"],
	#allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Rutas por módulo
#app.include_router(agro_router, prefix="/agro", tags=["Agronómico"])
app.include_router(catalogo_router, prefix="/api/catalogo", tags=["Catálogo"])
#app.include_router(geo_router, prefix="/geo", tags=["Geoespacial"])
#app.include_router(social_router, prefix="/social", tags=["Sociocultural"])

@app.get("/")
def root():
    return {"message": "API Agroplataforma Maíz funcionando"}