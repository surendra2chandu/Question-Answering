# Import necessary libraries from vllm
from vllm import LLM, SamplingParams
from llm.src.conf.Configurations import roberta_model_path

class RobertaPipelineVLLM:
    def __init__(self):
        """
        This function initializes the RobertaPipelineVLLM class with the specified model path.
        """

        # Initialize the LLM using vllm and load the model
        self.llm = LLM(model=roberta_model_path, device="cpu")

    def get_qa_model(self, question: str, context: str) -> str:
        """
        This function answers a question given a context using the loaded vllm model.
        :param question: str - The question to be answered
        :param context: str - The context in which to find the answer
        :return: str - The answer from the model
        """

        # Prepare the input prompt for the QA task
        prompt = f"Question: {question}\nContext: {context}\nAnswer:"

        # Define sampling parameters (adjust these based on your requirements)
        sampling_params = SamplingParams(n=1, max_tokens=50)

        # Generate a response from the model
        output = self.llm.generate(prompt, sampling_params=sampling_params)

        # Extract and return the answer
        return output[0].outputs[0].text.strip()
