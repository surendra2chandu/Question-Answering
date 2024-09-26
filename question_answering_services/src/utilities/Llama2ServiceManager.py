# Import necessary classes
import requests
from question_answering_services.src.conf.Configurations import logger
from fastapi import HTTPException
import re


def process_llama2_request(context: str, questions: list[str]):
    # Define the URL for the Llama2ChatGGUF model
    url = "http://localhost:8000/llm/llama2/"

    # Define the data to be sent in the request body
    prompt = {
        "questions": questions,
        "context": context
    }

    # Sen the POST request with JSON data and query parameter
    logger.info("Sending the POST request with JSON data and query parameter")
    response = requests.post(url, json=prompt)

    if response.status_code == 200:
        try:
            # Get the answer from the response
            logger.info("Getting the answer from the response")
            res = response.json()
            answers = [line.split(":")[1].strip() for line in res.splitlines() if "Answer:" in line]
            return dict(zip(questions, answers))

        except ValueError as e:
            logger.error(f"Error occurred while parsing the response: {e}")
            raise HTTPException(status_code=500, detail=f"Error occurred while parsing the response{e},"
                                                        f" and the response is {response.json()}")

    else:
        logger.error(f"Error occurred while sending the request: {response.text}")
        raise HTTPException(status_code=500, detail=f"Error occurred while sending the request: {response.text}")




