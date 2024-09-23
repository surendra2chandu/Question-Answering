# Importing necessary classes
from fastapi import APIRouter, UploadFile, File, Form
from question_answering_services.src.api.Llama2ForPDF import question_answering_for_pdf


# Initialize the router
router = APIRouter(
    prefix="/question_answering",
    tags=["question-answering-services"],
)


# Define the route
@router.post("/llama2_pdf/")
async def llama2_question_answering_for_pdf(questions: list[str] = Form(...), file: UploadFile = File(...)):
    """"
    This function is used to perform question answering using the Llama2ChatGGUF model
    :param questions: Required list of questions
    :param file: Required pdf file
    :return:
    """
    # Call the question_answering_from_text function from Llama2ForPDF.py
    res = question_answering_for_pdf(questions, file)

    # Return the response
    return res
