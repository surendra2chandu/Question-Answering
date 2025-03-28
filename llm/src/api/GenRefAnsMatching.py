# Import necessary libraries
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Prompts import llama3_prompt_for_qa
from llm.src.conf.Configurations import logger
from fastapi import HTTPException, UploadFile
from rouge import Rouge
from io import BytesIO
import pandas as pd
import re

class GenRefAnsMatching:
    """
    Class for performing question answering using the Ollama model and calculating similarity scores.
    """

    def __init__(self):
        self.model = OllamaPipeline().get_model()
        logger.info("Model initialized.")

    def process_questions(self, context: str, file: UploadFile):
        """
        Process the questions in the input file and generate answers using the Ollama model.
        :param context: The context from the user
        :param file: The file containing questions and reference answers
        :return: DataFrame containing input questions, generated answers, reference answers, and similarity scores
        """

        try:
            df = pd.read_csv(file.file)
            questions = df.iloc[:, 0].tolist()
            reference_answers = df.iloc[:, 1].tolist()

            # Length of questions and reference answers  should be not match
            if len(questions) != len(reference_answers):
                raise HTTPException(status_code=500, detail="The number of questions and reference answers do not match.")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while reading the input file: {e}")

        try:

            response = self.model.invoke(input=llama3_prompt_for_qa.format(context=context, questions=questions))

            responses = re.findall(r'A:\s*(.*)', response)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")

        # Calculate similarity scores between generated answers and reference answers
        scores = self.similarity_scores(responses, reference_answers)

        # Create a DataFrame and save the results to a CSV file
        res_df = pd.DataFrame({
            "Input Question": questions,
            "Generated Answer": responses,
            "Reference Answer": reference_answers,
            "Similarity Score": scores})

        return res_df

    def similarity_scores(self, generated_answers, reference_answers):
        """
        Calculate similarity scores between generated answers and reference answers using the ROUGE metric.
        :param generated_answers: List of generated answers
        :param reference_answers: List of reference answers
        :return: List of similarity scores
        """
        rouge = Rouge()
        scores = []
        for gen_ans, ref_ans in zip(generated_answers, reference_answers):
            if gen_ans.lower() == ref_ans.lower():
                scores.append(1)
            else:
                rouge_score = rouge.get_scores(gen_ans.lower(), ref_ans.lower())[0]['rouge-l']['f'] * 1
                scores.append(round(rouge_score, 2))
        return scores


if __name__ == "__main__":

    # Sample context text
    context_text = "India, the world's most populous country and the seventh-largest by land area, is a vibrant and diverse nation in South Asia, known for its rich history, cultural heritage, and booming economy, with a democratic parliamentary system governing 28 states and 8 union territories, a multilingual society featuring Hindi, English, and 21 other recognized languages, and a deeply rooted spiritual tradition encompassing Hinduism, Islam, Christianity, Sikhism, Buddhism, and Jainism, all set against a geographically diverse backdrop that includes the towering Himalayas, expansive plains, and vast coastlines along the Arabian Sea and the Bay of Bengal."

    # Take the sample file  from the local system
    sample_file = UploadFile(filename="example.csv",file=BytesIO(open(r"D:\CSV\questions.csv", 'rb').read()))

    # Initialize the GenRefAnsMatching class and call the process_questions method
    gen_ref_ans_matching = GenRefAnsMatching()
    res = gen_ref_ans_matching.process_questions(context_text, sample_file)
    print(res)




