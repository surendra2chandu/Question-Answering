from fastapi import FastAPI
from llm.src.routers.RobertafRouter import router as roberta_router


# Initialize the FastAPI app
app = FastAPI()

# Include the roberta_router
app.include_router(roberta_router)


