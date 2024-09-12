# Importing necessary classes
from fastapi import UploadFile, HTTPException


# Validate that 'questions' is a list and not empty
def validate_list_obj(data: list[str]):
    """
    This function validates the data format and raises an HTTP 422 error if it is not a list.
    :param data: The data to be validated.
    :return: None
    """

    if not isinstance(data, list) or not data:
        raise HTTPException(status_code=422, detail=f"data must be a non-empty list of strings: {data}")


async def validate_pdf(file: UploadFile):
    """
    This function validates the file extension and raises an HTTP 400 error if it is not a PDF file.
    :param file: The file to be validated.
    :return: None
    """

    # Check the file extension
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file extension. Only PDF files are allowed.")

    try:
        # reading the uploaded file
        await file.read()

    # Handling the fIle not found error
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

    # Handling the file read error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"internal  server error as {str(e)}")


