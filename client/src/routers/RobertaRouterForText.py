# Importing necessary classes
from fastapi import APIRouter
from client.src.api import RobertaForText
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/question-answering-roberta",
    tags=["question-answering-client"],
)


# Define the request body model
class Questions(BaseModel):
    questions: list[str]    # List of questions


# Define the route
@router.post("_text/")
async def roberta_question_answering_from_text(questions: Questions, context: str) -> dict:

    # Call the question_answering_from_text function from RobertaForText.py
    res = RobertaForText.question_answering_from_text(questions.questions, context)

    # Return the response
    return res
