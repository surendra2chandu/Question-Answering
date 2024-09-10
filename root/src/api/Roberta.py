# Importing necessary classes
from root.src.conf.Configurations import logger, model_path
from root.src.utilities.RobertaPipeline import RobertaPipeline


def roberta_question_answering(questions: list[str], context: str):
    # Initialize the RobertaPipeline class with the specified model path
    logger.info("Loaded the model")
    nlp = RobertaPipeline(model_path).get_qa_model()
    logger.info("Initialized the RobertaPipeline class with the specified model path")

    # Perform question answering
    responses = nlp(question=questions, context=context)
    logger.info("Performed question answering")

    return responses
