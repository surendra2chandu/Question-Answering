# Importing necessary classes
from fastapi import APIRouter
from llm.src.api import OllamaSummarizer

# Initialize the router
router = APIRouter(
    prefix="/llm",
    tags=["core-llm-system"],
)

# Define route for summarization
@router.post("/ollama/summarize/")
def summarize_text(context: str):
    """
    Summarizes the given context using the Ollama model.

    Args:
        context (str): The input text to summarize.

    Returns:
        str: The generated summary.
    """
    return OllamaSummarizer.summarize_with_ollama(context)