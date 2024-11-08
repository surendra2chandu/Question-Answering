# Importing necessary classes
from llm.src.utilities.OllamaPipeline import OllamaPipeline
from llm.src.conf.Configurations import logger
from fastapi import HTTPException
from llm.src.conf.Prompts import default_prompt1
import PyPDF2

def qa_with_ollama(context: str, questions: list[str]):
    """
    Perform question answering using the Ollama model
    :param context: The context in which to answer the question.
    :param questions: The questions to answer.
    :return: The answer generated by the Ollama model.
    """

    # Load the Ollama model
    model = OllamaPipeline().get_model()
    logger.info("Model initialized.")

    responses = []



    user_prompt = f"The question is: {questions} \n\n The context is: {context}"
    # Define messages in the chat format with "system," "user," and "content"
    message = [
        {"role": "system",
            "content": default_prompt1},
        {"role": "user", "content": user_prompt}]

    # Invoke the model with the chat structure
    try:
        # Directly invoke the model with the formatted prompt
        logger.info("invoking the model with input message")
        response = model.invoke(input=message)
        logger.info("response received from the model")

        responses.append(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during invocation: {e}")

    return responses



if __name__ == "__main__":

    pdf_text = ''
    with open(r"C:\Docs\Doc1.pdf", 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_text += str(pdf_reader.metadata)
        for page_num in range(min(1, len(pdf_reader.pages))):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

    QUESTIONS = ["What is the title of the document?", "What is the creation date of the document?", "What is the version of the document?", "Does the document has CDRL number?", "Who is the authorizing agent of the document?"]


    res = qa_with_ollama(pdf_text, QUESTIONS)

    for answer, Question in zip(res, QUESTIONS):
        print(f"Question: {Question}\nAnswer: {answer}\n")


