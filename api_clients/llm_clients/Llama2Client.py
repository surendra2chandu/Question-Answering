# Importing necessary classes
import requests


class Llama2ChatGGUFClient:
    def __init__(self):
        """
        This class is a client for the Llama2ChatGGUF API endpoint.
        """
        # Define the URL for the API endpoint
        url = "http://localhost:8000/llm/llama2/"

        # Define the data to be sent in the request body
        data = {
            "questions": ["What is the capital of France?", "What is the tower name?", "Who is Modi?"],
            "context": "The capital of France is Paris. The Eiffel Tower is located in Paris."
        }

        # Send the POST request with JSON data and query parameter
        response = requests.post(url, json=data)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the Llama2ChatGGUFClient class
    Llama2ChatGGUFClient()

