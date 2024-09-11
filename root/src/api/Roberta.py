# Importing necessary classes
from root.src.conf.Configurations import logger, model_path
from root.src.utilities.RobertaPipeline import RobertaPipeline


def roberta_question_answering(questions: list[str], context: str) -> list:
    """
    This function is used to perform question answering using the Roberta model
    :param questions: List of questions
    :param context: Text context
    :return: List of responses
    """
    logger.info("Received a request to perform question answering using Roberta model")

    # Initialize the RobertaPipeline class with the specified model path
    logger.info("Loaded the model")

    # Initialize the RobertaPipeline class with the specified model path
    nlp = RobertaPipeline(model_path).get_qa_model()
    logger.info("Initialized the RobertaPipeline class with the specified model path")

    # Perform question answering
    responses = nlp(question=questions, context=context)
    logger.info("Performed question answering")

    return responses


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_text function")
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "what is tower name?", "who is modi?"]

    # Call the question_answering_from_text function
    logger.info("Calling the question_answering_from_text function")
    result = roberta_question_answering(sample_questions, sample_context)

    # Print the result
    logger.info("Printing the result")
    print(result)
