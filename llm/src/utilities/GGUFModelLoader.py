# Importing necessary classes
from llama_cpp import Llama
from llm.src.conf.Configurations import llama2_model_path


class GGUFModelLoader:
    def __init__(self):
        """
        This function initializes the GGUFModelLoader class with the specified model path.
        """

        # Load the GGUF model using the specified model path
        self.llm = Llama(model_path=llama2_model_path, verbose=True)

    def get_llm_model(self):
        """
        This function returns the GGUF model.
        :return: GGUF model
        """

        # Return the GGUF model
        return self.llm
