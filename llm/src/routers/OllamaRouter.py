# Importing necessary classes
from fastapi import APIRouter
from llm.src.api import OllamaQA
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/llm",
    tags=["core-llm-system"],
)


# Define the request body model
class Prompt(BaseModel):
    questions: list[str]    # List of questions
    context: str           # Context for the questions
    #prompt: Optional[str] = default_prompt  # Prompt for the questions


# Define the request body model
@router.post("/ollama/question-answering/")
async def ollama_qa(prompt: Prompt):
    """
    Perform question answering using the Ollama model
    :param prompt: The prompt containing the context and questions.
    :return: The answer generated by the Ollama model.
    """


    # Call the qa_with_ollama function from OllamaPromptTemplate.py
    # response = OllamaPromptTemplate.qa_with_ollama(context, questions)

    # Call the qa_with_ollama function from OllamaQA.py
    response = OllamaQA.qa_with_ollama(prompt.context, prompt.questions)


    return response
