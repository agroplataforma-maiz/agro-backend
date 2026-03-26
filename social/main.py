from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.social import router as social_router
from routers.cultural import router as cultural_router


app = FastAPI(title="API Sociocultural Agroplataforma")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Se incluyen ambos routers: social y cultural
app.include_router(social_router)
app.include_router(cultural_router)
