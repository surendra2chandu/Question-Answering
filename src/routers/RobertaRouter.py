from fastapi import APIRouter
from pypdf import PyPDF

# Initialize the router
router = APIRouter(
    prefix="/question-answering",
    tags=["question-answering"],
)


# Define the route
@router.post("/roberta/")
async def roberta_question_answering():
    return {"message": "Hello World"}



