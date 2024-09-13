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
