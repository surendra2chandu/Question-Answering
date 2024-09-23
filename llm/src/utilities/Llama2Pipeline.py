# Importing necessary classes
from llm.src.conf.Configurations import llama2_model_path
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import LlamaCpp


class Llama2Pipeline:
    def __init__(self):
        """
        This function initializes the GGUFModelLoader class with the specified model path.
        """
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

        # Load the GGUF model using the specified model path
        self.llm = LlamaCpp(model_path=llama2_model_path, temperature=0.01, max_tokens=512, top_p=0.98,
                            Callback_manager=callback_manager, verbose=True)

    def get_llm_model(self):
        """
        This function returns the GGUF model.
        :return: GGUF model
        """

        # Return the GGUF model
        return self.llm
