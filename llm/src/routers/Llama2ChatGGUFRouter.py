# Importing necessary classes
from fastapi import APIRouter
from llm.src.api.Llama2ChatGGUF import llama2_chat_ggu_question_answering
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/llm",
    tags=["core-llm-system"],
)


# Define the prompt structure
class Prompt(BaseModel):
    """
    This class is used to define the prompt structure
    """
    context: str    # The context in which to answer the question
    question: str   # The question to be answered based on the context


@router.post("/llama2/")
async def llama2_chat_gguf(prompt: Prompt):
    """
    This function is used to perform question answering using the Llama2ChatGGUF model
    :param prompt: Required data. It contains the prompt
    :return: List of responses. It contains the answers to the questions.
    """

    # Call the llama2chat_gguf function from Llama2ChatGGUF.py
    response = llama2_chat_ggu_question_answering(prompt.context, prompt.question)

    return response
