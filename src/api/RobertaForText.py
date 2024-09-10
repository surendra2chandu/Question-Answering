# Importing necessary classes
from src.conf.Configurations import logger, model_path
from src.utilities import InputValidations
from src.utilities.RobertaPipeline import RobertaPipeline


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
    nlp = RobertaPipeline(model_path).get_qa_model()
    logger.info("Initialized the RobertaPipeline class with the specified model path")

    # Perform question answering
    responses = nlp(question=questions, context=context)
    logger.info("Performed question answering")

    # Extract the answers from the responses
    answers = list(map(lambda x: x['answer'], responses))

    # Create a dictionary with questions as keys and answers as values
    res = dict(zip(questions, answers))

    # Return the response
    return res


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_text function")
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "what is tower name?"]

    # Call the question_answering_from_text function
    logger.info("Calling the question_answering_from_text function")
    result = question_answering_from_text(sample_questions, sample_context)

    # Print the result
    logger.info("Printing the result")
    print(result)
