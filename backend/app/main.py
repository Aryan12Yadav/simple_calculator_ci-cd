from fastapi import FastAPI

from app.database.database import engine
from app.database.database import Base
from fastapi.middleware.cors import CORSMiddleware
from app.api.calculator import router as calculator_router

Base.metadata.create_all(bind = engine)

app = FastAPI(
    title = 'Calculator API',
    description="Calculator api using restapi",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        'http://localhost:5173',
        'http://127.0.0.1:5173',
        'https://calculator-api-7ntd.onrender.com'
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.include_router(calculator_router)

@app.get("/")
def root():
    return  {
        "message":"Calculator API  is running"
    }