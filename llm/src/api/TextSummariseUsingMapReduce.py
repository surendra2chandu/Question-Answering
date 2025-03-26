# Import necessary modules
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Configurations import logger
from fastapi import HTTPException
from PyPDF2 import PdfReader
import re
from multiprocessing import Pool

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
    system_prompt = "Write a concise summary of the following context in paragraph format."

    # Construct the user prompt
    user_prompt = f"Context: {context}"

    # Format the complete prompt for model invocation
    prompt = (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        f"{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n"
        f"{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )

    try:
        logger.info("Invoking the model with the input prompt.")
        response = model.invoke(input=prompt, options={"num_ctx": 4000})
        logger.info("Response received from the model.")
        return response
    except Exception as e:
        logger.error(f"Error during model invocation: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")


def split_text(text, chunk_size=2000):
    """
    Splits the input text into smaller chunks.

    Args:
        text (str): The full context to be split.
        chunk_size (int): The size of each chunk.

    Returns:
        list: List of text chunks.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def map_reduce_summarization(text):
    """
    Processes the text using MapReduce and summarizes each chunk.

    Args:
        text (str): The context to be summarized.

    Returns:
        str: The final summary after MapReduce processing.
    """
    # Split the text into smaller chunks
    text_chunks = split_text(text)

    # Use multiprocessing to process chunks
    with Pool(processes=4) as pool:
        summaries = pool.map(summarize_with_ollama, text_chunks)

    # Combine the results into a final summary
    final_summary = " ".join(summaries)
    return final_summary


if __name__ == "__main__":
    # Read the PDF file
    pdf_path = r"C:\Docs\sample.pdf"
    reader = PdfReader(pdf_path)

    # Initialize the text
    text = ""

    # Iterate over the pages
    for page_number in range(len(reader.pages)):
        text += reader.pages[page_number].extract_text()

    # Clean up the extracted text
    text = re.sub(r'\s+', ' ', text.strip())
    text = re.sub(r'([^\w\s])\1+', r'\1', text)
    text = re.sub(r'[^\w\s.,?!]', '', text)
    text = ' '.join(re.sub(r'[^A-Za-z0-9\s]', '', text).split())

    l = len(text)

    # Generate the summary using MapReduce approach
    final_summary = map_reduce_summarization(text)
    print(final_summary)
