# Importing necessary classes
from langchain.chains.question_answering.map_reduce_prompt import messages

from llm.src.conf.Configurations import logger, default_prompt
from langchain_core.prompts import PromptTemplate
from llama_cpp import Llama
from llm.src.utilities.Llama2Pipeline import Llama2Pipeline


def llama2_chat_ggu_question_answering(context: str, questions: list[str]):
    """
    Perform question answering using the Llama2ChatGGUF model.
    :param context: The context in which to answer the question.
    :param questions: List of questions to answer.
    :return: The answers generated by the Llama2ChatGGUF model.
    """
    logger.info("Received a request to perform question answering using Llama2ChatGGUF model")

    # Load the Llama2 GGUF model
    logger.info("Loading Llama2 GGUF model")
    #llm = Llama(model_path=r"D:\LLM\llama-2-7b-chat.Q2_K.gguf")

    llm = Llama2Pipeline().get_llm_model()

    # Enforcing that the model should strictly answer from context or say "I don't know"
    system_msg = f"{default_prompt}"

    # Format the prompt with context and the current question
    #user_msg = f"CONTEXT:{context} \n QUESTION:{questions}"
    user_msg = f"CONTEXT: {context} \n QUESTIONS: {' \n'.join(questions)}"

    logger.info(f"Generating response for questions: {questions}")

    # Generate the response using create_chat_completion
    """response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        max_tokens=100  # Adjust token limit as needed)"""

    prompts = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg}
    ]
    response = llm.invoke(input=prompts)

    return response


if __name__ == "__main__":
    # Sample context and question
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "Where Eiffel Tower is Located?"] #, "What is the capital of Germany?"]

    # Perform question answering using the Llama2ChatGGUF model
    res = llama2_chat_ggu_question_answering(sample_context, sample_questions)

    # Print the response
    print("res",res)
