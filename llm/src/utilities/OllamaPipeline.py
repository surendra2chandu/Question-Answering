from langchain_ollama.llms import OllamaLLM
from fastapi import HTTPException

class OllamaPipeline:
    def __init__(self):
        """
        This function initializes the OllamaPipeline class with the specified model path.
        """
        # Load the Ollama model
        try:
            self.model = OllamaLLM(base_url="http://127.0.0.1:11434", model="llama3.2:1b")


        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while initializing the model: {e}")


    def get_model(self):
        """
        This function returns the Ollama model.
        :return: Ollama model
        """

        # Return the Ollama model
        return self.model

    def get_model2(self):
        """
        This function returns the Ollama model.
        :return: Ollama model
        """

        # Return the Ollama model
        return self.model2


    def get_model3(self):
        """
        This function returns the Ollama model.
        :return: Ollama model
        """

        # Return the Ollama model
        return self.model3