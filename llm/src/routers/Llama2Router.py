# Importing necessary classes
from fastapi import APIRouter
from llm.src.api.Llama2PromptTemplate import llama2_chat_ggu_question_answering
from pydantic import BaseModel

#from llm.src.conf.Configurations import default_prompt

# Initialize the router
router = APIRouter(
    prefix="/llm",
    tags=["core-llm-system"],
)


# Define the request body model
class Prompt(BaseModel):
    questions: list[str]    # List of questions
    context: str           # Context for the questions
    #prompt: Optional[str] = default_prompt  # Prompt for the questions


@router.post("/llama2/")
async def llama2_chat_gguf(prompt: Prompt):
    """
    This function is used to perform question answering using the Llama2ChatGGUF model
    :param prompt: Required data. It contains the prompt
    :return: List of responses. It contains the answers to the questions.
    """

    # Call the llama2chat_gguf function from Llama2PromptTemplate.py
    response = llama2_chat_ggu_question_answering(prompt.context, prompt.questions)

    return response
