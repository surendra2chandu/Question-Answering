from ctransformers import AutoModelForCausalLM
from llm.src.conf.Configurations import llama2_model_path, logger

# Log loading message
logger.info("Loading Llama2 model")
# Load the Llama2 model
llm = AutoModelForCausalLM.from_pretrained(llama2_model_path, model_type='llama')

# Define the context and query
context = """
The Eiffel Tower is one of the most iconic landmarks in the world, located in Paris, France.
It was completed in 1889 for the World's Fair. Standing at 324 meters, it was the tallest structure in the world until 1930.
Millions of people visit it every year.

"""
queries = ["Where is the Eiffel Tower located", "what is capital of india?"]

# Log generation message
logger.info("Generating response from Llama2 model")

# Prepare the prompt for the model
#prompt = f"""Answer based on context:\n\n{context}\n\n{query}"""
prompt = f"""Answers based on context. If answer is beyond the context, respond with "Sorry, I don't have precise information to provide an answer":\n\n{context}\n\n{queries}"""
# Generate and print the model's response
print(llm(prompt=prompt, temperature=0.1, max_new_tokens=1024))
