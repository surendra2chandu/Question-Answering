from llm.src.utilities.Llama2Pipeline import Llama2Pipeline
from llm.src.conf.Prompts import default_prompt2, default_prompt1, default_prompt3, default_prompt4, default_prompt
llm = Llama2Pipeline().get_llm_model()

def get_model_response(user_prompt, system_prompt, context, questions):
    examples = """As an AI assistant. Please provide simple and precise answer, you will answer question based strictly on the given information.
     If the answer cannot be found in the given information, respond with "Answer not found in context

            Example format:
            Q: What is the title of the document?
            A: Sample Document Title

            Q: Who is the authorizing agent of the document?
            A: Dr. John Doe.

            Q. Does the document has CDRL number?
            A. Answer not found in the information provided.

            Please respond in a similar format.
            """

    system_prompt = f"{default_prompt1} \n\n {examples}"

    # Define the user prompt with the question and context
    # user_prompt = f"The question is: {questions} \n\n The information provided is: {context}"
    # prompt = f"""
    #     <|begin_of_text|>
    #     <|start_header_id|>system<|end_header_id|>
    #     { system_prompt }
    #     <|eot_id|>
    #     <|start_header_id|>user<|end_header_id|>
    #     { user_prompt }
    #     <|eot_id|>
    #     <|start_header_id|>assistant<|end_header_id|>
    #     """

    # Define the user prompt with the question and context
    user_prompt = f"The questions are: {questions} \n\n The information provided is: {context}"

    prompt = f"""<s>[INST] <<SYS>>
             {examples}
             <</SYS>>
           {user_prompt} [/INST]"""

    response = llm.invoke(prompt)
    return response


if __name__ == "__main__":
    # Enforcing that the model should strictly answer from context or say "I don't know"
    # Sample context and question
    # sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    # sample_questions = ["What is the capital of France?", "Where Eiffel Tower is Located?",
    #                     "What is the capital of Germany?"]
    #
    # sample_questions = ["What is surendra role?", "Where  surendra works?"]
    #
    # sample_context = "Surendra is a data scientist and works in amex"

    sample_questions = ["What is Surendra's role?", "Where does Surendra work?"]

    sample_context = "Surendra is a data scientist and works at Amex."

    system_msg = f"{default_prompt}"

    # Format the prompt with context and the current question
    user_msg = f"CONTEXT:{sample_context} \n QUESTION:{sample_questions}"
    res = get_model_response(system_msg, user_msg, sample_context, sample_questions)
    print("res",res)