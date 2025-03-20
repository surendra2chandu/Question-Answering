
# Import necessary libraries
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Configurations import logger
from fastapi import HTTPException
from llm.src.conf.Prompts import default_prompt1
from difflib import SequenceMatcher

class GenRefAnsMatching:
    """
    Class for performing question answering using the Ollama model.
    """
    def __init__(self):
        self.model = OllamaPipeline().get_model()
        logger.info("Model initialized.")

    def qa_with_ollama(self, context: str, questions: list[str]) -> list[str]:
        """
        Perform question answering using the Ollama model.
        """
        responses = []
        for question in questions:
            user_prompt = f"The question is: {question} \n\n The information provided is: {context}"
            prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            {default_prompt1}<|eot_id|><|start_header_id|>user<|end_header_id|>
            {user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""


            try:
                logger.info(f"Invoking the model with input message for question: {question}")
                response = self.model.invoke(input=prompt)
                logger.info("Response received from the model")
                responses.append(response.strip())
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")

        return responses


    def calculate_score(self, generated_answer: str, reference_answer: str) -> float:
        """
        Calculate score between generated and reference answers.
        :return: Similarity score between 0 and 100
        """
        if generated_answer.lower() == reference_answer.lower():
            return 100.0
        return round(SequenceMatcher(None, generated_answer.lower(), reference_answer.lower()).ratio() * 100, 2)


if __name__ == "__main__":

    text = "New Delhi is the capital of India. It is located in Asia. The population of India is 1.4 billion."

    questions = ["What is the capital of India?", "Where is India located?"]
    reference_answers = ["The capital of India is new delhi.", "India is located in Asia"]

    gen_ref_ans_matching =GenRefAnsMatching()
    generated_answers =  gen_ref_ans_matching.qa_with_ollama(text, questions)

    for question, generated_ans, reference_ans in zip(questions, generated_answers, reference_answers):
        score = gen_ref_ans_matching.calculate_score(generated_ans, reference_ans)
        print(f"Question: {question}")
        print(f"Generated Answer: {generated_ans}")
        print(f"Reference Answer: {reference_ans}")
        print(f"Similarity Score: {score}\n")
