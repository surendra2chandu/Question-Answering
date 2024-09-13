
import requests


class RobertaForPDFClient:
    def __init__(self):
        """
        Initialize the RobertaForTextClient class
        """

        # Define the URL for the API endpoint
        url = "http://localhost:8001/question-answering-roberta_pdf/"

        # Define the form data (questions should be sent as a form field)
        data = {
            'questions': ["what is title of given file?", "who is author?", "what is file name?",
                          "What is the capital of France?", "what is tower name?", "who is modi?"]
        }

        # Define the file to be uploaded
        files = {
            'file': open(r'C:\CHANDU\work\example_data\examplefile.pdf', 'rb')
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
