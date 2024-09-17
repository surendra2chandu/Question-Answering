# Importing necessary classes
from fastapi import FastAPI
from llm.src.routers.RobertafRouter import router as roberta_router
from llm.src.routers.Llama2ChatGGUFRouter import router as llama2_router


# Initialize the FastAPI app
app = FastAPI()


# Include the roberta_router
app.include_router(roberta_router)


# Include the llama2_router
app.include_router(llama2_router)



