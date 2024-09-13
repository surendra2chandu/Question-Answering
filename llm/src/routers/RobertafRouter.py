# Importing necessary classes
from fastapi import APIRouter
from llm.src.api.Roberta import roberta_question_answering
from pydantic import BaseModel
from llm.src.conf.Configurations import logger

# Initialize the router
router = APIRouter(
    prefix="/llm",
    tags=["core-llm-system"],
)


# Define the request body model
class Prompt(BaseModel):
    questions: list[str]    # List of questions
    context: str           # Context for the questions


@router.post("/roberta/")
async def question_answering(prompt: Prompt):
    """
    This function is used to perform question answering using the Roberta model
    :param prompt: Required data. It contains questions and context
    :return: List of responses. It contains the answers to the questions.
    """

    # Call the roberta_question_answering function from Roberta.py
    logger.info("Calling the roberta_question_answering function from Roberta.py")
    response = roberta_question_answering(prompt.questions, prompt.context)

    return response
