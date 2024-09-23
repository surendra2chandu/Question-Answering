# Importing necessary classes
from fastapi import UploadFile, File
from question_answering_services.src.conf.Configurations import logger
from question_answering_services.src.utilities import InputValidations, FileDataExtractor, QAServiceManager
from io import BytesIO


def question_answering_from_pdf(questions: list[str], file: UploadFile = File(...)):
    """
    This function is used to perform question answering from PDF file using the Roberta model.
    :param questions: List of questions
    :param file: PDF file
    :return: Response from the question_answering function
    """

    logger.info("Received a request to perform question answering using Roberta model")

    # Validate the PDF file
    logger.info("Validating the PDF file")
    InputValidations.validate_pdf(file)

    # Validate the list of questions
    InputValidations.validate_list_obj(questions)

    # Extract text from the PDF file
    logger.info("Extracting text from the PDF file")
    context = FileDataExtractor.extract_text_from_pdf(file)

    # Perform question answering
    logger.info("Performing question answering")
    res = QAServiceManager.qa_processing_pipeline(questions, context)
    logger.info("Performed question answering")

    # Return the response
    return res


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_pdf function")
    sample_questions = ["what is title of given file?", "who is author?", "what is file name?",
                        "What is the capital of France?", "what is tower name?", "who is modi?"]
    sample_file = UploadFile(filename="examplefile.pdf",
                             file=BytesIO(open(r'D:\example.pdf', 'rb').read()))

    # Call the question_answering_from_pdf function
    logger.info("Calling the question_answering_from_pdf function")
    result = question_answering_from_pdf(sample_questions, sample_file)

    # Print the result
    logger.info("Printing the result")
    print(result)
