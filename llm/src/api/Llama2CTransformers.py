from ctransformers import AutoModelForCausalLM
from llm.src.conf.Configurations import llama2_model_path, logger
# from llm.src.conf.Prompts import default_prompt2, default_prompt1, default_prompt3, default_prompt4

# Log loading message
logger.info("Loading Llama2 model")

# Load the Llama2 model
llm = AutoModelForCausalLM.from_pretrained(llama2_model_path, model_type='llama')

# Define the context and query
context = "The Eiffel Tower is located in Paris, France."
queries = ["What is the capital of france", "What is the capital of India?"]


# Log generation message
# Prepare the prompt for the model with clearer instructions
#prompt = f"{default_prompt3}" :\n\n{context}\n\n{query}
prompt = ( f"""Use the following pieces of information to answer the user's queries.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context}
Question: {queries}
Only return the helpful answers below and nothing else.
Helpful answer:
"""
)


# Log generation message
logger.info("Generating response from Llama2 model")

# Generate and print the model's response
response = llm(prompt=prompt, temperature=0.1, max_new_tokens=1024)
print("response : ", response)
