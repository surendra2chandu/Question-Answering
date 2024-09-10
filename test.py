from transformers import RobertaTokenizer, RobertaForQuestionAnswering
import torch
from src.conf.Configurations import logger, model_path


def question_answering_from_text(questions: list[str], context: str):
    """
    This function is used to perform question answering from text using the Roberta model without using pipeline.
    :param questions: List of questions
    :param context: Text context
    :return: List of answers for each question
    """

    # Load the model and tokenizer
    tokenizer = RobertaTokenizer.from_pretrained(model_path)
    model = RobertaForQuestionAnswering.from_pretrained(model_path)
    logger.info("Loaded the model and tokenizer")

    # List to store responses
    responses = []

    # Iterate over each question
    for question in questions:
        # Tokenize the input (question and context)
        inputs = tokenizer(question, context, return_tensors="pt")

        # Perform inference (get start and end scores for the answer)
        with torch.no_grad():
            outputs = model(**inputs)
            start_scores = outputs.start_logits
            end_scores = outputs.end_logits

        # Get the most likely beginning and end of the answer span
        start_idx = torch.argmax(start_scores)
        end_idx = torch.argmax(end_scores) + 1

        # Convert token indices back to words
        answer = tokenizer.convert_tokens_to_string(
            tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_idx:end_idx])
        )

        # Store the answer
        responses.append(answer)
        logger.info(f"Performed question answering for question: '{question}'")

    # Return the list of responses
    return responses


if __name__ == "__main__":
    # Sample data
    logger.info("Starting the question_answering_from_text function")
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "what is tower name?"]

    # Call the question_answering_from_text function
    logger.info("Calling the question_answering_from_text function")
    result = question_answering_from_text(sample_questions, sample_context)

    print(result)
