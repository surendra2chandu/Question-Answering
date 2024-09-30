
import requests


class RobertaForPDFClient:
    def __init__(self):
        """
        Initialize the RobertaForTextClient class
        """

        # Define the URL for the API endpoint
        url = "http://localhost:8001/question_answering/roberta_pdf/"

        # Define the form data (questions should be sent as a form field)
        data = {
            'questions': ["what is title of given document?", "who is author of the document?", "What is the version of the document?",
                          "What is the capital of France?"]
        }

        # Define the file to be uploaded
        files = {
            'file': open(r'D:\doc1.pdf', 'rb')
        }

        # Send the POST request with form data and file
        response = requests.post(url, files=files, data=data)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Initialize the RobertaForTextClient class
    RobertaForPDFClient()
