import requests
import json
from llm.src.conf.Prompts import default_prompt1
import PyPDF2


# define endpoint for ollama api
url = "http://localhost:11434/api/generate"

# define headers
headers = {
    'Content-Type': 'application/json',
}


# define function to generate response from ollama api
def generate_response(prompt):
    data = {
        "model": "llama3",
        "stream": False,
        "prompt": prompt,
    }

    # make a post request to the ollama api
    response = requests.post(url,
                             headers=headers,
                             data=json.dumps(data))

    # check if the response is successful
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        print("Response: ", actual_response)
    # if the response is not successful, print the error
    else:
        print("Error:", response.status_code, response.text)


examples = """
        Example format:
        Q: What is the title of the document?
        A: Sample Document Title

        Q: Who is the authorizing agent of the document?
        A: Dr. John Doe.

        Q. Does the document has CDRL number?
        A. Answer not found in the information provided.

        Please respond in a similar format.
        """

system_prompt = f"{default_prompt1} \n\n {examples}"
pdf_text = ''
with open(r"C:\Docs\Doc1.pdf", 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_text += str(pdf_reader.metadata)
    for page_num in range(min(1, len(pdf_reader.pages))):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()

QUESTIONS = ["What is the title of the document?", "What is the creation date of the document?",
                 "What is the version of the document?", "Does the document has CDRL number?",
                 "Who is the authorizing agent of the document?"]

# Define the user prompt with the question and context




user_prompt = f"The question is: {QUESTIONS} \n\n The information provided is: {pdf_text}"
# Define messages in the chat format with "system," "user," and "content"
message = """[
    {"role": "system",
     "content": system_prompt},
    {"role": "user", "content": user_prompt}]"""


prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

generate_response(prompt)

