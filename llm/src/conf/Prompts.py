# Define the default prompt for the Llama2 model
default_prompt = "Use the following pieces of information to answer the user's queries. If you don't know the answer, just say that you don't know, don't try to make up an answer."

default_prompt0 = "Use the following pieces of information to answer the user's queries. If you don't know the answer, just say that you don't know, don't try to make up an answer.Only return the helpful answers below and nothing else.Helpful answer:"

default_prompt1 = """As an AI assistant. Please provide simple and precise answer, you will answer question based strictly on the given information. If the answer cannot be found in the given information, respond with "Answer not found in context"."""

default_prompt11 = """As an AI assistant. Please provide simple and precise answers, you will answer questions based strictly on the given context. If the answer cannot be found in the context, respond with "Answer not found in context"."""



default_prompt2 = """As an AI assistant, please provide simple, accurate and precise answers. You will answer questions based strictly on the given context. If the answer cannot be found in the context, respond with "I don't know". Don't try to make up an answer"""

default_prompt3 =  """Use the following pieces of information to answer the user's queries.
If you don't know the answer, just say that you don't know, don't try to make up an answer"""

default_prompt4 = """Use the given context to answer the question. If you don't find the answer in given context, just say you "I don't know". Keep the answer concise and accurate."""


examples = """
        Example format:
        Q: What is the title of the document?
        A: Sample Document Title

        Q: Who is the authorizing agent of the document?
        A: Dr. John Doe.

        Q. Does the document has CDRL number?
        A. Answer not found in the information provided.

        Please respond in a similar format.
        """

system_prompt_for_qa = f"{default_prompt1} \n\n {examples}"

# Define the user prompt with the question and context
user_prompt_for_qa = "The questions are: {questions} \n\n The information provided is: {context}"

llama3_prompt_for_qa = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt_for_qa}<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_prompt_for_qa}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""