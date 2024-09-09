# Importing necessary classes
from fastapi import UploadFile, File
from src.conf.Configurations import logger


def question_answering_from_pdf(questions: list[str], file: UploadFile = File(...)):
    """
    This function is used to perform question answering from PDF file using the Roberta model.
    :param questions: List of questions
    :param file: PDF file
    :return: Response from the question_answering function
    """

    logger.info("Received a request to perform question answering using Roberta model")

    return {"message": "Hello World"}