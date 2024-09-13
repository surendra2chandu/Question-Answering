# Importing necessary classes
import PyPDF2
from rag_service.src.conf.Configurations import logger
from fastapi import UploadFile
import re


def extract_text_from_pdf(file: UploadFile):
    """
    This function is used to extract the data from the PDF file.
    :param file: PDF file
    :return: Data extracted from the PDF file
    """
    logger.info("Extracting data from the PDF file")

    # Read the PDF file
    pdf = PyPDF2.PdfReader(file.file)

    # Initialize the data and add the metadata
    data = ""

    # Iterate over the pages
    for i in range(len(pdf.pages)):
        data += pdf.pages[i].extract_text()

    # Remove special characters
    data = re.sub(r'[^\w\s]', '', data)

    # Return the pdf data
    return str(pdf.metadata) + data
