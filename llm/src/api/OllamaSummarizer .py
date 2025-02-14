# Import necessary modules
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Configurations import logger
from fastapi import HTTPException
from PyPDF2 import PdfReader
import re

def summarize_with_ollama(context: str):
    """
    Summarizes the given context using the Ollama model.

    Args:
        context (str): The input text to summarize.

    Returns:
        str: The generated summary.

    Raises:
        HTTPException: If an error occurs during model invocation.
    """

    # Initialize the Ollama model
    model = OllamaPipeline().get_model()
    logger.info("Model initialized.")

    # System prompt for summarization
    system_prompt = "Write a concise summary of the following context."

    # Construct the user prompt
    user_prompt = f"Context: {context}"

    # Format the complete prompt for model invocation
    prompt = (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        f"{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n"
        f"{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )

    print(prompt)
    try:
        logger.info("Invoking the model with the input prompt.")
        response = model.invoke(input=prompt)
        logger.info("Response received from the model.")

        return response
    except Exception as e:
        logger.error(f"Error during model invocation: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")


if __name__ == "__main__":

    # Read the PDF file
    pdf_path = r"C:\Docs\sample_doc.pdf"
    # Read the PDF file
    reader = PdfReader(pdf_path)

    # Initialize the text
    text = ""

    # Iterate over the pages
    for page_number in range(len(reader.pages)):
        text += reader.pages[page_number].extract_text()

        # Remove extra spaces
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove all extra special characters, keeping only one
    text = re.sub(r'([^\w\s])\1+', r'\1', text)
    # Remove any characters that aren't alphanumeric, spaces, or single special characters
    text = re.sub(r'[^\w\s.,?!]', '', text)

    text = ' '.join(re.sub(r'[^A-Za-z0-9\s]', '', text).split())

    # Generate the summary using the Ollama model
    summary = summarize_with_ollama(text)
    print(summary)

