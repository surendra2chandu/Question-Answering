from fastapi import FastAPI
from src.routers.RobertaRouter import router as roberta_router

app = FastAPI()

app.include_router(roberta_router)
