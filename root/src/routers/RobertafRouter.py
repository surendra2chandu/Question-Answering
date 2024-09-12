# Importing necessary classes
from fastapi import APIRouter
from root.src.api import Roberta
from pydantic import BaseModel
from root.src.conf.Configurations import logger

# Initialize the router
router = APIRouter(
    prefix="/question_answering_roberta",
    tags=["question-answering-root"],
)


# Define the request body model
class Questions(BaseModel):
    questions: list[str]    # List of questions


@router.post("/")
async def question_answering(questions: Questions, context: str) -> list:

    # Call the roberta_question_answering function from Roberta.py
    logger.info("Calling the roberta_question_answering function from Roberta.py")
    response = Roberta.roberta_question_answering(questions.questions, context)

    return response
