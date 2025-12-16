from fastapi import FastAPI

from app.database import Base, engine
from app.routers import book

app = FastAPI(title="Luz Sagrada API", version="1.0.0")

# Criar as tabelas e não existir
Base.metadata.create_all(bind=engine)


# Inclui as rotas
app.include_router(book.router)


@app.get("/")
def read_root():
    """End point raiz da API"""
    return {
        "message": "Luz Sagrada API",
        "status": "online",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "redoc",
    }


@app.get("/health")
def health_check():
    """End point de verificação da saúde a API"""
    return {"status": "health", "database": "connected"}
