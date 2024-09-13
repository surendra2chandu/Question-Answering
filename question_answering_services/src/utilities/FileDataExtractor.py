# Importing necessary classes
import PyPDF2
from question_answering_services.src.conf.Configurations import logger, NUMBER_OF_PDF_PAGES_TO_READ
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
    for i in range(min(NUMBER_OF_PDF_PAGES_TO_READ, len(pdf.pages))):
        data += pdf.pages[i].extract_text().strip()

    # Remove special characters
    # data = re.sub(r'[^\w\s]', '', data)

    data = ' '.join(data.split())

    metadata_str = ""
    for key, value in pdf.metadata.items():
        metadata_str += key[1:] + ": " + value + "\n"
    metadata_str += "File metadata, File name: "+file.filename + "\n"

    # Return the pdf data
    return metadata_str + data
