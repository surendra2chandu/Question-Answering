# Importing necessary classes
from fastapi import APIRouter
from question_answering_services.src.api import RobertaForText
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/question_answering",
    tags=["question-answering-services"],
)


# Define the request body model
class Prompt(BaseModel):
    questions: list[str]    # List of questions
    context: str            # Context for the questions


# Define the route
@router.post("/roberta_text/")
async def roberta_question_answering_from_text(prompt: Prompt) -> dict:
    """
    This function is used to perform question answering from text using the Roberta model.
    :param prompt: Required request body with questions and context
    :return: Response from the question_answering function.
    """

    # Call the question_answering_from_text function from RobertaForText.py
    res = RobertaForText.question_answering_from_text(prompt.questions, prompt.context)

    # Return the response
    return res
