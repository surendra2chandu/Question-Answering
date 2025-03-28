# Import necessary modules
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Configurations import logger
from fastapi import HTTPException
from llm.src.api.data import text

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
    system_prompt = "Write a concise summary of the following context use paragraph format."

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
        response = model.invoke(input=prompt, options={"num_ctx": 2000})
        logger.info("Response received from the model.")

        return response
    except Exception as e:
        logger.error(f"Error during model invocation: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")


if __name__ == "__main__":

    # Generate the summary using the Ollama model
    summary = summarize_with_ollama(text)
    print(summary)

