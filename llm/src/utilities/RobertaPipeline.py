# Importing necessary classes
from transformers import pipeline
from llm.src.conf.Configurations import roberta_model_path

class RobertaPipeline:
    def __init__(self):
        """
        This function initializes the RobertaPipelineVLLM class with the specified model path.
        """

        # Initialize the LLM using vllm and load the model
        self.nlp = pipeline("question-answering", model=roberta_model_path, tokenizer=roberta_model_path)

    def get_qa_model(self):
        """
        This function returns the LLM model.
        :return: LLM model
        """
        return self.nlp