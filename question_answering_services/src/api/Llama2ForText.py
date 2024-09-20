# Importing necessary classes
from question_answering_services.src.conf.Configurations import logger
from question_answering_services.src.utilities.Llama2ServiceManager import process_llama2_request


def question_answering_for_text(context: str, question: str):
    """
    This function is used to perform question answering using the Llama2ChatGGUF model.
    :param context: The context in which to answer the question.
    :param question: The question to be answered based on the context.
    :return:
    """
    logger.info("Received a request to perform question answering using Llama2ChatGGUF model")

    # Call the llama2_chat_gguf function from Llama2.py
    response = process_llama2_request(context, question)

    return response


if __name__ == "__main__":
    # Sample context and question
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_question = "What is the capital of France?"

    # Perform question answering using the Llama2ChatGGUF model
    res = question_answering_for_text(sample_context, sample_question)

    # Print the response
    print(res)
