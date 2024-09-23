# Importing necessary classes
from question_answering_services.src.conf.Configurations import logger
from question_answering_services.src.utilities.Llama2ServiceManager import process_llama2_request


def question_answering_for_text(context: str, questions: list[str]):
    """
    This function is used to perform question answering using the Llama2ChatGGUF model.
    :param context: The context in which to answer the question.
    :param questions: List of questions to answer.
    :return:
    """
    logger.info("Received a request to perform question answering using Llama2ChatGGUF model")

    # Call the llama2_chat_gguf function from Llama2.py
    response = process_llama2_request(context, questions)

    return response


if __name__ == "__main__":
    # Sample context and question
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "What is the tower name?", "Who is Modi?"]

    # Perform question answering using the Llama2ChatGGUF model
    res = question_answering_for_text(sample_context, sample_questions)

    # Print the response
    print(res)
