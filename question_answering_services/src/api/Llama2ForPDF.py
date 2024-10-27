# Importing necessary classes
from question_answering_services.src.conf.Configurations import logger
from question_answering_services.src.utilities.Llama2ServiceManager import process_llama2_request
from fastapi import UploadFile, File
from question_answering_services.src.utilities import InputValidations, FileDataExtractor
from io import BytesIO


def question_answering_for_pdf(questions: list[str], file: UploadFile = File(...)):
    """
    This function is used to perform question answering using the Llama2ChatGGUF model.
    :param questions: Required list of questions
    :param file: Required pdf file
    :return:
    """
    logger.info("Received a request to perform question answering using Llama2ChatGGUF model")

    # Validate the PDF file
    logger.info("Validating the PDF file")
    InputValidations.validate_pdf(file)

    # Extract text from the PDF file
    logger.info("Extracting text from the PDF file")
    context = FileDataExtractor.extract_text_from_pdf(file)

    # print("context",context)

    # Call the question_answering_from_pdf function from Llama2ForPDF.py
    response = process_llama2_request(context, questions)

    return response


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_for_pdf function")
    sample_questions = ["what is title of given file?", "who is author of the document?", "what is file name?", "What is the version of the file?"]
    sample_file = UploadFile(filename="doc2.pdf",
                             file=BytesIO(open(r'D:\doc2.pdf', 'rb').read()))

    # Call the question_answering_for_pdf function
    logger.info("Calling the question_answering_for_pdf function")
    result = question_answering_for_pdf(sample_questions, sample_file)

    # Print the result
    logger.info("Printing the result")
    print(result)
