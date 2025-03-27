
# Importing necessary classes
from fastapi import FastAPI
from llm.src.routers.GenRefAnsMatchingRouter import router as gen_ref_ans_matching_router

# Initialize the FastAPI app
app = FastAPI()

# Include the gen_ref_ans_matching_router
app.include_router(gen_ref_ans_matching_router)






