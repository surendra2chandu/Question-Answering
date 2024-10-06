from llm.src.utilities.Llama2Pipeline import Llama2Pipeline
from llm.src.conf.Prompts import default_prompt2, default_prompt1, default_prompt3, default_prompt4, default_prompt
llm = Llama2Pipeline().get_llm_model()

def get_model_response(user_prompt, system_prompt):
    prompt = f"""
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        { system_prompt }
        <|eot_id|>
        <|start_header_id|>user<|end_header_id|>
        { user_prompt }
        <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
        """
    response = llm.invoke(prompt)
    return response


if __name__ == "__main__":
    # Enforcing that the model should strictly answer from context or say "I don't know"
    # Sample context and question
    sample_context = "The capital of France is Paris. The Eiffel Tower is located in Paris."
    sample_questions = ["What is the capital of France?", "Where Eiffel Tower is Located?",
                        "What is the capital of Germany?"]

    system_msg = f"{default_prompt}"

    # Format the prompt with context and the current question
    user_msg = f"CONTEXT:{sample_context} \n QUESTION:{sample_questions}"
    res = get_model_response(system_msg, user_msg)
    print("res",res)