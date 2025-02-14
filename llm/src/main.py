# Importing necessary classes
from fastapi import FastAPI
from llm.src.routers.RobertafRouter import router as roberta_router
from llm.src.routers.Llama2Router import router as llama2_router
from llm.src.routers.OllamaRouter import router as ollama_router
from llm.src.routers.OllamaSummarizerRouter import router as ollama_summarizer_router


# Initialize the FastAPI app
app = FastAPI()


# Include the roberta_router
app.include_router(roberta_router)


# Include the llama2_router
app.include_router(llama2_router)

# Include the ollama_router
app.include_router(ollama_router)

# Include the ollama_summarizer_router
app.include_router(ollama_summarizer_router)




