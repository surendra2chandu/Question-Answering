from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm.src.conf.Configurations import logger
from fastapi import HTTPException
from PyPDF2 import PdfReader
import re
import os
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Configurations import logger

# Function to summarize with LangChain and Ollama model
def summarize_with_langchain(summaries: str, llm):
    """
    Summarizes the given context using the Ollama model in a LangChain setup.
    """

    # System prompt for summarization
    system_prompt = "Summarize the following summary snippets into a final, consolidated summary:"

    # Construct the user prompt
    user_prompt = f"summaries: {summaries}"

    # Format the complete prompt for model invocation
    prompt = (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        f"{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n"
        f"{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )

    try:
        logger.info("Invoking the model with the input prompt.")
        response = llm.invoke(input=prompt, options={"num_ctx": 4000})
        logger.info("Response received from the model.")

        return response
    except Exception as e:
        logger.error(f"Error during model invocation: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")


# Function to split text into chunks
def split_text(text, chunk_size=1000):
    """Splits the text into smaller chunks of specified size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Function to summarize the document using Map-Reduce approach with LangChain
def map_reduce_summarization(text, llm):
    """
    Summarizes the text using a Map-Reduce approach with LangChain and Ollama.
    """
    text_chunks = split_text(text)

    map_template = """The following is a document:\n{context}\nSummarize the main themes concisely:"""
    map_prompt = PromptTemplate(template=map_template, input_variables=["context"])
    map_chain = map_prompt | llm | StrOutputParser()

    intermediate_summaries = [map_chain.invoke({"context": chunk}) for chunk in text_chunks]

    # # reduce_template = """The following are summary snippets:\n{summaries}\nCombine them into a final, consolidated summary:"""
    # # reduce_prompt = PromptTemplate(template=reduce_template, input_variables=["summaries"])
    # # reduce_chain = reduce_prompt | llm | StrOutputParser()
    # final_summary = reduce_chain.invoke({"summaries": "\n".join(intermediate_summaries)})

    final_summary = summarize_with_langchain("\n".join(intermediate_summaries), llm)

    return final_summary

if __name__ == "__main__":
    llm = OllamaPipeline().get_model()
    pdf_path = r"C:\Docs\B.pdf"
    reader = PdfReader(pdf_path)
    text = "".join([reader.pages[i].extract_text() for i in range(len(reader.pages))])
    text = re.sub(r'\s+', ' ', text.strip())
    final_summary = map_reduce_summarization(text, llm)
    print(final_summary)
