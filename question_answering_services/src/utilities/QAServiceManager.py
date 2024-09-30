# Import necessary classes
import requests
from question_answering_services.src.conf.Configurations import logger, default_answer
from fastapi import HTTPException


def qa_processing_pipeline(questions: list[str], context: str):

    url = "http://localhost:8000/llm/roberta/"

    # Sen the POST request with JSON data and query parameter
    logger.info("Sending the POST request with JSON data and query parameter")
    response = requests.post(url, json={"questions": questions, "context": context})

    if response.status_code == 200:
        try:
            if len(questions) == 1:
                # Get the answer from the response
                logger.info("Getting the answer from the response")

                res = response.json()['answer'] if response.json()['score'] > 0.0001 else default_answer

                # Create a dictionary with questions as keys and answers as values
                return {questions[0]: res}

            answers = map(lambda x: x['answer'] if x['score'] > 0.0001 else default_answer, response.json())

            # Create a dictionary with questions as keys and answers as values
            logger.info("Creating a dictionary with questions as keys and answers as values")
            res = dict(zip(questions, answers))

            # Return the dictionary
            return res

        except ValueError as e:
            logger.error(f"Error occurred while parsing the response: {e}")
            raise HTTPException(status_code=500, detail=f"Error occurred while parsing the response{e},"
                                                        f" and the response is {response.json()}")

    else:
        logger.error(f"Error occurred while sending the request: {response.text}")
        raise HTTPException(status_code=500, detail=f"Error occurred while sending the request: {response.text}")


