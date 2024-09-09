from fastapi import FastAPI
from src.routers.RobertaPdfRouter import router as roberta_router
from src.routers.RobertaTextRouter import router as roberta_text_router

app = FastAPI()

app.include_router(roberta_router)

app.include_router(roberta_text_router)
