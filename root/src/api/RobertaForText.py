# Importing necessary classes
from client.src.conf.Configurations import logger, default_answer
from client.src.utilities import InputValidations
import requests


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

    url = "http://localhost:8000/question_answering_roberta/"

    # Define the data to be sent in the request body

    # Sen the POST request with JSON data and query parameter
    response = requests.get(url, json=questions, params={
        "context": context})

    print(response.json())

    # Extract answers from the responses
    answers = map(lambda x: x['answer'] if x['score'] > 0.1 else default_answer, response.json())

    # Create a dictionary with questions as keys and answers as values
    res = dict(zip(questions, answers))

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
