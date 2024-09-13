# Importing necessary classes
from fastapi import APIRouter
from rag_service.src.api import RobertaForText
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/question-answering-roberta",
    tags=["question-answering-rag_service"],
)


# Define the request body model
class Questions(BaseModel):
    questions: list[str]    # List of questions
    context: str            # Context for the questions


# Define the route
@router.post("_text/")
async def roberta_question_answering_from_text(data: Questions) -> dict:

    # Call the question_answering_from_text function from RobertaForText.py
    res = RobertaForText.question_answering_from_text(data.questions, data.context)

    # Return the response
    return res
