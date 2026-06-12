from fastapi import FastAPI

from app.database.database import engine
from app.database.database import Base

from app.api.calculator import router as calculator_router

Base.metadata.create_all(bind = engine)

app = FastAPI(
    title = 'Calculator API',
    description="Calculator api using restapi",
    version="1.0.0"
)

app.include_router(calculator_router)

@app.get("/")
def root():
    return  {
        "message":"Calculator API  is running"
    }