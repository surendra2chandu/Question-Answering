# Importing necessary classes
from llm.src.conf.Configurations import logger
from llm.src.utilities import InputValidations
from llm.src.utilities.RobertaPipeline import RobertaPipeline


def question_answering_from_text(questions: list[str], context: str):
    """
    This function is used to perform question answering from text using the Roberta model.
    :param questions: List of questions
    :param context: Text context
    :return: Response from the question_answering function
    """
    logger.info("Received a request to perform question answering from text using Roberta model")

    # Validate that 'questions' is a list and not empty
    InputValidations.validate_list_obj(questions)
    logger.info("Validated that 'questions' is a list and not empty")

    # Initialize the RobertaPipeline class with the specified model path
    logger.info("Loaded the model")
    nlp = RobertaPipeline().get_qa_model()
    logger.info("Initialized the RobertaPipeline class with the specified model path")

    # Perform question answering
    res = nlp(question=questions, context=context)
    logger.info("Performed question answering")

    # Return the response
    return res


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_text function")
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "what is tower name?"]

    sample_context = "RELEASE/REVISION: 1.1 22 September 2021"

    sample_questions = ["What is the date of the document?(Just give  date)", "WHAT IS THE DATE OF THE DOCUMENT?", "What is the date of the document?"]

    #sample_questions = ["What is the date of the document?"]



    # Call the question_answering_from_text function
    logger.info("Calling the question_answering_from_text function")
    result = question_answering_from_text(sample_questions, sample_context)

    # Print the result
    logger.info("Printing the result")
    print(result)