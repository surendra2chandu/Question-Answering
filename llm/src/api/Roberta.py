# Import necessary classes
from llm.src.conf.Configurations import logger
from llm.src.utilities.RobertaPipeline import RobertaPipelineVLLM
from llm.src.utilities import InputValidations


def roberta_question_answering(questions: list[str], context: str) -> list:
    """
    This function performs question answering using the vllm Roberta model.
    :param questions: List of questions
    :param context: Text context
    :return: List of responses
    """
    logger.info("Received a request to perform question answering using Roberta model")

    # Validate that 'questions' is a list and not empty
    InputValidations.validate_list_obj(questions)

    # Initialize the RobertaPipelineVLLM class
    nlp = RobertaPipelineVLLM()
    logger.info("Initialized the RobertaPipelineVLLM class")

    # Perform question answering for each question
    responses = []
    for question in questions:
        response = nlp.get_qa_model(question=question, context=context)
        responses.append(response)
        logger.info(f"Performed question answering for question: {question}")

    return responses


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_text function")
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "What is the tower name?", "Who is Modi?"]

    # Call the question_answering_from_text function
    logger.info("Calling the question_answering_from_text function")
    result = roberta_question_answering(sample_questions, sample_context)

    # Print the result
    logger.info("Printing the result")
    print(result)
