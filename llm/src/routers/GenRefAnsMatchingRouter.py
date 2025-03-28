# Import necessary libraries
from llm.src.api.GenRefAnsMatching import GenRefAnsMatching
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, UploadFile, File
import io
import os

# Initialize the router
router = APIRouter(tags=["GenRefAnsMatching"])

# Define the route for the root endpoint
@router.post("/Gen/Ref/Similarity_Score/")

# Define the function to calculate similarity scores between generated answers and reference answers
async def get_ans(context: str, file: UploadFile = File(...)):

    """
    Function to calculate similarity scores between generated answers and reference answers
    :param context: The context for the questions
    :param file: The file containing questions and reference answers`
    :return: The response from the service
    """

    # Calculate similarity scores between generated answers and reference answers
    res_df = GenRefAnsMatching().process_questions(context, file)

    # Convert the resulting DataFrame to a CSV format in memory
    csv_buffer = io.StringIO()
    res_df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Return the CSV content as a streaming response for download
    return StreamingResponse(csv_buffer, media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=similarity-scores.csv"})


