# Importing necessary classes
from fastapi import APIRouter, UploadFile, File
from client.src.api import RobertaForPDF
from pydantic import BaseModel

# Initialize the router
router = APIRouter(
    prefix="/question-answering-roberta",
    tags=["question-answering-client"],
)


# Define the request body
class Questions(BaseModel):
    questions: list[str]


# Define the route
@router.post("_pdf/")
async def roberta_question_answering_from_pdf(questions: Questions, file: UploadFile = File(...)) -> dict:

    # Call the question_answering function from RobertaForPDF.py
    res = RobertaForPDF.question_answering_from_pdf(questions.questions, file)

    # Return the response
    return res



