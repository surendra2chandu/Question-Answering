import requests


class RobertaForTextClient:
    def __init__(self):
        """
        Initialize the RobertaForTextClient class
        """

        url = "http://localhost:8000/question_answering_roberta_text/"

        # Define the data to be sent in the request body
        data = {
            "questions": ["What is the capital of France?", "What is the tower name?"]
        }

        # Send the POST request with JSON data and query parameter
        response = requests.post(url, json=data, params={
            "context": "The capital of France is Paris. The Eiffel Tower is located in Paris."})

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the RobertaForTextClient class
    RobertaForTextClient()

