from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Agronómico/Fenotípico Agroplataforma")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from routers import router as agronomico_router
app.include_router(agronomico_router)

@app.get("/health")
def health():
    return {"status": "ok"}
