# Import necessary classes
import requests


class Llama2ForPDFClient:
    def __init__(self):
        """
        This class is a client for the Custom Llama2ChatGGUF API endpoint.
        """

        # Define the URL for the API endpoint
        url = "http://localhost:8001/question_answering/llama2_pdf/"

        # Define the data to be sent in the request body
        data = {
            "questions": ["What is the capital of France?", "What is the tower name?", "Who is Modi?"]
        }
        # Define the file to be uploaded
        files = {
            'file': open(r'D:\example.pdf', 'rb')
        }

        # Send the POST request with JSON data and query parameter
        response = requests.post(url, files=files, data=data)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the CustomLlama2ChatGGUFClient class
    Llama2ForPDFClient()

