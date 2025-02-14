# Importing necessary classes
import requests
import PyPDF2


class OllamaClient:
    def __init__(self):
        """
        Initialize the OllamaClient class
        """

        # Define the URL for the API endpoint
        url = "http://localhost:8001/llm/ollama/question-answering/"

        pdf_text = ''
        with open(r"C:\Docs\Doc1.pdf", 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text += str(pdf_reader.metadata)
            for page_num in range(min(1, len(pdf_reader.pages))):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text()

        # Define the data to be sent in the request body
        data = {
            "questions": ["What is the title of the document?", "What is the creation date of the document?", "What is the version of the document?", "Does the document has CDRL number?", "Who is the authorizing agent of the document?"]
,
            "context": pdf_text
        }

        # Send the POST request with JSON data and query parameter
        response = requests.post(url, json=data)

        # Check if the response status code indicates success
        if response.ok:
            print(response.json())  # Print JSON response if successful
        else:
            print("Request failed with status code", response.status_code)


if __name__ == "__main__":
    # Create an instance of the OllamaClient class
    OllamaClient()

