# Importing necessary classes
from transformers import pipeline
from llm.src.conf.Configurations import roberta_model_path


class RobertaPipeline:
    def __init__(self):
        """
        This function initializes the RobertaPipeline class with the specified model path.
        :param model_path: str - Path to the Roberta model
        """

        # Load the Roberta pipeline model using the specified model path
        self.nlp = pipeline("question-answering", model=roberta_model_path, tokenizer=roberta_model_path)

    def get_qa_model(self):
        """
        This function returns the Roberta pipeline model.
        :return: Roberta pipeline model
        """

        # Return the Roberta pipeline model
        return self.nlp

