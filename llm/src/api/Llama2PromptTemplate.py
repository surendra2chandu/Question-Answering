# Importing necessary classes
from llm.src.conf.Configurations import logger
from llm.src.conf.Prompts import default_prompt2, default_prompt1, default_prompt3, default_prompt4
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
    pre_prompt = f"""<s>[INST] \n<<SYS>>{default_prompt1} <</SYS>>\n"""

    # Create a template for the prompt
    template = pre_prompt + "###CONTEXT:\n{context}\n" + "###QUESTIONS:\n{questions}\n" + "[/INST]"

    template = pre_prompt + "CONTEXT:\n\n{context}\n" + "Questions : {questions}" + "[\INST]"


    # Create a prompt template
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    #print(prompt)
    # Load the Llama2 model
    logger.info("Loading Llama2 model")
    llm = Llama2Pipeline().get_llm_model()

    # Generate the response from the model
    logger.info("Generating response from Llama2 model")
    response = llm.invoke(prompt.format(context=context, questions=questions)).strip()

    return response


if __name__ == "__main__":
    # Sample context and question
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris. India is a country in Asia."
    sample_questions = [ "What is the capital of Germany?", "What is the capital of France?", "Where Eiffel Tower is Located?"]

    # Perform question answering using the Llama2ChatGGUF model
    res = llama2_chat_ggu_question_answering(sample_context, sample_questions)

    # Print the response
    print(res)
