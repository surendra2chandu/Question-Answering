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
        prompt = {
            "question": "What is the capital of france?"
        }
        # Define the file to be uploaded
        files = {
            'file': open(r'C:\CHANDU\work\example_data\example.pdf', 'rb')
        }

        # Send the POST request with JSON data and query parameter
        response = requests.post(url, json=prompt, files=files)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the CustomLlama2ChatGGUFClient class
    Llama2ForPDFClient()

