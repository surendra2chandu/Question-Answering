# Importing necessary classes
from fastapi import APIRouter, UploadFile, File, Form
from client.src.api import RobertaForPDF

# Initialize the router
router = APIRouter(
    prefix="/question-answering-roberta",
    tags=["question-answering-client"]
)


# Define the route
@router.post("_pdf/")
async def roberta_question_answering_from_pdf(questions: list[str] = Form(...), file: UploadFile = File(...)) -> dict:

    # Call the question_answering function from RobertaForPDF.py
    res = RobertaForPDF.question_answering_from_pdf(questions, file)

    # Return the response
    return res



