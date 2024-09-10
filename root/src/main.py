from fastapi import FastAPI
from root.src.routers.RobertafRouter import router as roberta_router


# Initialize the FastAPI app
app = FastAPI()

app.include_router(roberta_router)


