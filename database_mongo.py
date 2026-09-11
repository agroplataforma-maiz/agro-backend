import os

from pymongo import MongoClient


MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://agro-mongodb:27017"
)

MONGO_DB = os.getenv(
    "MONGO_DB",
    "agroplataforma_nosql"
)


mongo_client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)

mongo_db = mongo_client[MONGO_DB]


# ==========================================================
# COLECCIONES
# ==========================================================

multimedia_collection = mongo_db[
    "trazabilidad_multimedia"
]

medios_parcela_collection = mongo_db[
    "medios_parcela"
]

medios_culturales_collection = mongo_db[
    "medios_culturales"
]

evidencias_fenotipicas_collection = mongo_db[
    "evidencias_fenotipicas"
]


def verificar_mongo():
    mongo_client.admin.command("ping")
    return True
