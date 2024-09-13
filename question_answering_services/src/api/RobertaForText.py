# Importing necessary classes
from question_answering_services.src.conf.Configurations import logger
from question_answering_services.src.utilities import InputValidations, QAServiceManager


def question_answering_from_text(questions: list[str], context: str):
    """
    This function is used to perform question answering from text using the Roberta model.
    :param questions: List of questions
    :param context: Text context
    :return: Response from the question_answering function
    """
    logger.info("Received a request to perform question answering using Roberta model")

    # Validate that 'questions' is a list and not empty
    InputValidations.validate_list_obj(questions)
    logger.info("Validated that 'questions' is a list and not empty")

    res = QAServiceManager.qa_processing_pipeline(questions, context)

    # Return the response
    return res


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_text function")
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "what is tower name?", "who is modi?"]

    # Call the question_answering_from_text function
    logger.info("Calling the question_answering_from_text function")
    result = question_answering_from_text(sample_questions, sample_context)

    # Print the result
    logger.info("Printing the result")
    print(result)
