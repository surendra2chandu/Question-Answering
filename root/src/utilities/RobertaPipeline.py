# Importing necessary classes
from transformers import pipeline


class RobertaPipeline:
    def __init__(self, model_path):
        """
        This function initializes the RobertaPipeline class with the specified model path.
        :param model_path: str - Path to the Roberta model
        """

        # Load the Roberta pipeline model using the specified model path
        self.nlp = pipeline("question-answering", model=model_path, tokenizer=model_path)

    def get_qa_model(self):
        """
        This function returns the Roberta pipeline model.
        :return: Roberta pipeline model
        """

        # Return the Roberta pipeline model
        return self.nlp

