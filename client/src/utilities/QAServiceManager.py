# Import necessary classes
import requests
from client.src.conf.Configurations import logger, default_answer


def qa_processing_pipeline(questions: list[str], context: str):

    url = "http://localhost:8000/question_answering_roberta/"

    # Sen the POST request with JSON data and query parameter
    logger.info("Sending the POST request with JSON data and query parameter")
    response = requests.post(url, json={"questions": questions}, params={
        "context": context})

    # Extract answers from the responses
    logger.info("Extracting answers from the responses")
    answers = map(lambda x: x['answer'] if x['score'] > 0.1 else default_answer, response.json())

    # Create a dictionary with questions as keys and answers as values
    logger.info("Creating a dictionary with questions as keys and answers as values")
    res = dict(zip(questions, answers))

    return res
