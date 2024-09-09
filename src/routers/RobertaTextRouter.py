# Importing necessary classes
from fastapi import APIRouter
from src.api import RobertaForText

# Initialize the router
router = APIRouter(
    prefix="/question-answering-roberta",
    tags=["question-answering"],
)


# Define the route
@router.post("/text/")
async def roberta_question_answering_from_text(questions: list[str], context: str) -> dict:

    # Call the question_answering_from_text function from RobertaForText.py
    res = RobertaForText.question_answering_from_text(questions, context)

    # Return the response
    return res
