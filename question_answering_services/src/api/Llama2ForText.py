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
    sample_context = "In the solar system, there are eight primary planets that orbit the sun."
    sample_question = "Name the eight planets in the solar system?"

    # Perform question answering using the Llama2ChatGGUF model
    res = question_answering_for_text(sample_context, sample_question)

    # Print the response
    print(res)
