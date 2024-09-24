# Importing necessary classes
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Get the llm logger
logger = logging.getLogger()

# Define the Roberta model path
roberta_model_path = r"D:\LLM\deepsetroberta-base-squad2"

# Define the Llama2 model path
llama2_model_path = r"D:\LLM\llama-2-7b-chat.Q2_K.gguf"

# Define the default prompt for the Llama2 model
default_prompt = "Use the following pieces of information to answer the user's queries. If you don't know the answer, just say that you don't know, don't try to make up an answer."