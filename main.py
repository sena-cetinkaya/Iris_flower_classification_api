from fastapi import FastAPI
from models import create_db_and_tables
from routes import router

app = FastAPI()

# Uygulama başladığında tablo oluştur
@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(router)
