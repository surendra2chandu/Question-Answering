# Importing necessary classes
from fastapi import FastAPI
from question_answering_services.src.routers.RobertafRouterForPDF import router as roberta_pdf_router
from question_answering_services.src.routers.RobertaRouterForText import router as roberta_text_router
from question_answering_services.src.routers.Llama2RouterForText import router as llama2_chat_gguf_router
from question_answering_services.src.routers.Llama2RouterForPDF import router as llama2_pdf_router


# Initialize the FastAPI app
app = FastAPI()

# Include the roberta_pdf_router
app.include_router(roberta_pdf_router)

# Include the roberta_text_router
app.include_router(roberta_text_router)

# Include the llama2_pdf_router
app.include_router(llama2_pdf_router)

# Include the llama2_chat_gguf_router
app.include_router(llama2_chat_gguf_router)
