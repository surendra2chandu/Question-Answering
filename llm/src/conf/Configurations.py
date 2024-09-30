# Importing necessary classes
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Get the llm logger
logger = logging.getLogger()

# Define the Roberta model path
roberta_model_path = "D:\LLM\deepsetroberta-base-squad2"

# Define the Llama2 model path
llama2_model_path = r"D:\LLM\llama-2-7b-chat.Q2_K.gguf"

# Define the default prompt for the Llama2 model
#default_prompt = "Use the following pieces of information to answer the user's queries. If you don't know the answer, just say that you don't know, don't try to make up an answer."

default_prompt1 = "Use the following pieces of information to answer the user's queries. If you don't know the answer, just say that you don't know, don't try to make up an answer.Only return the helpful answers below and nothing else.Helpful answer:"

default_prompt2 = """As an AI assistant. Please provide simple answers, you will answer questions based strictly on the given context. If the answer cannot be found in the context, respond with "Answer not found in context"."""

default_prompt3 =  """Use the following pieces of information to answer the user's queries.
If you don't know the answer, just say that you don't know, don't try to make up an answer"""