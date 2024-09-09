# Importing necessary classes
from fastapi import APIRouter, UploadFile, File
from src.conf.Configurations import logger
from src.api import RobertaForPDF

# Initialize the router
router = APIRouter(
    prefix="/question-answering-roberta",
    tags=["question-answering"],
)


# Define the route
@router.post("/pdf/")
async def roberta_question_answering_from_pdf(questions: list[str], file: UploadFile = File(...)) -> dict:

    # Call the question_answering function from RobertaForPDF.py
    res = RobertaForPDF.question_answering_from_pdf(questions, file)

    # Return the response
    return res



