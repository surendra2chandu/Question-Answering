# Importing necessary classes
from fastapi import APIRouter
from root.src.api import Roberta

# Initialize the router
router = APIRouter(
    prefix="/question_answering_roberta",
    tags=["question-answering-root"],
)


@router.get("/")
async def question_answering(questions: list[str], context: str) -> list:

    responses = Roberta.roberta_question_answering(questions, context)

    return responses
