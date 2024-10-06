# Importing necessary classes
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Get the llm logger
logger = logging.getLogger()

# Specify text to be used as default answer
default_answer = "Sorry, I don't have precise information to provide an answer."

# Default no of pages to read from pdf
NUMBER_OF_PDF_PAGES_TO_READ = 2
