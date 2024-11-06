# Importing necessary classes
from fastapi import APIRouter
from llm.src.api import OllamaPromptTemplate, OllamaRoles

# Initialize the router
router = APIRouter(
    prefix="/llm",
    tags=["core-llm-system"],
)

# Define the request body model
@router.post("/ollama/")
async def ollama_qa(context: str, question: str):
    """
    Perform question answering using the Ollama model
    :param context: The context in which to answer the question.
    :param question: The question to answer.
    :return: The answer generated by the Ollama model.
    """

    # Call the qa_with_ollama function from OllamaPromptTemplate.py
    response = OllamaPromptTemplate.qa_with_ollama(context, question)

    # Call the qa_with_ollama function from OllamaRoles.py
    #response = OllamaRoles.qa_with_ollama(context, question)


    return response
