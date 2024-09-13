from fastapi import FastAPI
from question_answering_services.src.routers.RobertafRouterForPDF import router as roberta_pdf_router
from question_answering_services.src.routers.RobertaRouterForText import router as roberta_text_router


# Initialize the FastAPI app
app = FastAPI()

# Include the roberta_pdf_router
app.include_router(roberta_pdf_router)

# Include the roberta_text_router
app.include_router(roberta_text_router)
