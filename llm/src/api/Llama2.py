# Importing necessary classes
from llm.src.conf.Configurations import logger
from langchain_core.prompts import PromptTemplate
from llm.src.utilities.Llama2Pipeline import Llama2Pipeline


def llama2_chat_ggu_question_answering(context: str, questions: list[str]):
    """
    Perform question answering using the Llama2ChatGGUF model
    :param context: The context in which to answer the question.
    :param questions: List of questions to answer.
    :return: The answer generated by the Llama2ChatGGUF model.
    """

    logger.info("Received a request to perform question answering using Llama2ChatGGUF model")

    # Enforcing that the model should strictly answer from context or say "I don't know"
    pre_prompt = f"""[INST] <<SYS>>f"Use the following pieces of information to answer the user's queries.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    
    Context: {context}
    Question: {questions}
    Only return the helpful answer below and nothing else.
    Helpful answer:" <<SYS>>"""


    # Create a template for the prompt
    template = pre_prompt + f"CONTEXT:\n{context}\n" + f"QUESTION:\n{questions}\n" + "[INST]"

    # Create a prompt template
    prompt = PromptTemplate(template=template)

    #print(prompt)
    # Load the Llama2 model
    logger.info("Loading Llama2 model")
    llm = Llama2Pipeline().get_llm_model()

    # Generate the response from the model
    logger.info("Generating response from Llama2 model")
    response = llm.invoke(prompt.format(context=context, question=questions)).strip()

    return response


if __name__ == "__main__":
    # Sample context and question
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "Where Eiffel Tower is Located?"]

    # Perform question answering using the Llama2ChatGGUF model
    res = llama2_chat_ggu_question_answering(sample_context, sample_questions)

    # Print the response
    print(res)
