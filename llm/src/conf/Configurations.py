# Import necessary libraries
import logging

# Define log format with date and time
log_format = "%(asctime)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"  # Custom date-time format

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    datefmt=date_format
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Define the Roberta model path
roberta_model_path = R"C:\llm\deepsetroberta-base-squad2"

# Define the Llama2 model path
llama2_model_path = r"C:\llm\llama-2-7b-chat.Q2_K.gguf"



