# Importing necessary classes
from fastapi import APIRouter
from question_answering_services.src.api.Llama2ForText import question_answering_for_text
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/question_answering",
    tags=["question-answering-services"],
)


# Define the request body model
class Prompt(BaseModel):
    questions: list[str]    # List of questions
    context: str           # Context for the questions


# Define the route
@router.post("/llama2_text/")
async def llama2_question_answering_for_text(prompt: Prompt):
    """
        This function is used to perform question answering using the Llama2ChatGGUF model
        :param prompt: Required data. It contains the prompt
        :return: List of responses. It contains the answers to the questions.
        """

    # Call the question_answering_from_text function from Llama2ForText.py
    res = question_answering_for_text(prompt.context, prompt.questions)

    # Return the response
    return res
