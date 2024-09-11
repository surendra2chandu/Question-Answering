import requests


class RobertaForPDFClient:
    def __init__(self):
        """
        Initialize the RobertaForTextClient class
        """

        # Define the URL for the API endpoint
        url = "http://localhost:8001/question-answering-roberta_pdf/"

        # Define the data to be sent in the request body
        data = {
            "questions": ["What is the capital of France?", "What is the tower name?", "Who is Modi?"]
        }

        # Define the query parameters
        files = {
            'file': open(r'C:\CHANDU\work\example_data\examplefile.pdf', 'rb')
        }

        # Send the POST request with JSON data and query parameter

        response = requests.post(url, files=files, json=data)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the RobertaForTextClient class
    RobertaForPDFClient()

