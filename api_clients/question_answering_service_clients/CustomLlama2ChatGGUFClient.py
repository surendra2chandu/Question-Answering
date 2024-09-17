# Import necessary classes
import requests


class CustomLlama2ChatGGUFClient:
    def __init__(self):
        """
        This class is a client for the Custom Llama2ChatGGUF API endpoint.
        """

        # Define the URL for the API endpoint
        url = "http://localhost:8001/question_answering/llama2chat_gguf/"

        # Define the data to be sent in the request body
        prompt = {
            "context": "In the solar system, there are eight primary planets that orbit the sun.",
            "question": "Name the eight planets in the solar system?"
        }

        # Send the POST request with JSON data and query parameter
        response = requests.post(url, json=prompt)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the CustomLlama2ChatGGUFClient class
    CustomLlama2ChatGGUFClient()

