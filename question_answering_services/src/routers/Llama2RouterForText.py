# Importing necessary classes
from fastapi import APIRouter
from question_answering_services.src.api import CustomLlama2ChatGGUF
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/question_answering",
    tags=["question-answering-services"],
)


# Define the request body model
class Prompt(BaseModel):
    question: str   # Question to be answered
    context: str     # Context for the question


# Define the route
@router.post("/llama2/")
async def llama2_question_answering(prompt: Prompt):
    """
        This function is used to perform question answering using the Llama2ChatGGUF model
        :param prompt: Required data. It contains the prompt
        :return: List of responses. It contains the answers to the questions.
        """

    # Call the question_answering_from_text function from RobertaForText.py
    res = CustomLlama2ChatGGUF.question_answering(prompt.question, prompt.context)

    # Return the response
    return res
