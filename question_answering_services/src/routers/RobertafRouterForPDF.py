# Importing necessary classes
from fastapi import APIRouter, UploadFile, File, Form
from question_answering_services.src.api import RobertaForPDF

# Initialize the router
router = APIRouter(
    prefix="/question_answering",
    tags=["question-answering-services"]
)


# Define the route
@router.post("/roberta_pdf/")
async def roberta_question_answering_from_pdf(questions: list[str] = Form(...), file: UploadFile = File(...)) -> dict:
    """
    This function is used to get the answers for the questions from the pdf file using Roberta model.
    :param questions: Required list of questions
    :param file: Required pdf file
    :return: Dictionary containing the answers for the questions
    """

    # Call the question_answering function from RobertaForPDF.py
    res = RobertaForPDF.question_answering_from_pdf(questions, file)

    # Return the res
    return res
