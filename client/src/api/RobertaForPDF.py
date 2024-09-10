# Importing necessary classes
from fastapi import UploadFile, File
from client.src.conf.Configurations import logger
from PyPDF2 import PdfReader


def question_answering_from_pdf(questions: list[str], file: UploadFile = File(...)):
    """
    This function is used to perform question answering from PDF file using the Roberta model.
    :param questions: List of questions
    :param file: PDF file
    :return: Response from the question_answering function
    """
    logger.info("Received a request to perform question answering using Roberta model")

    # Read the PDF file
    pdf = PdfReader(file.file)
    # get data from the PDF file
    data = pdf.extract_text()


    return {"message": "Hello World"}