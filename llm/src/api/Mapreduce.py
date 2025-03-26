from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import Document
from PyPDF2 import PdfReader
import re
from llm.src.utilities.OllamaPipeline import OllamaPipeline

# Function to split text into chunks
def split_text(text, chunk_size=1000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Function to summarize using Map-Reduce
def map_reduce_summarization(text, llm):
    text_chunks = split_text(text)
    documents = [Document(page_content=chunk) for chunk in text_chunks]

    map_prompt = PromptTemplate.from_template("Summarize the following text:\n{context}")
    reduce_prompt = PromptTemplate.from_template("Combine the following summaries into a final, concise summary:\n{context}")

    # Map step
    map_chain = map_prompt | llm | StrOutputParser()

    # Reduce step

    reduce_chain = reduce_prompt | llm | StrOutputParser()

    # Map-Reduce execution
    map_results = list(map_chain.map([{"context": doc.page_content} for doc in documents]))
    final_summary = reduce_chain.invoke({"context": " ".join(map_results)})

    return final_summary

if __name__ == "__main__":
    llm = OllamaPipeline().get_model()
    pdf_path = r"C:\\Docs\\B.pdf"
    reader = PdfReader(pdf_path)
    text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    text = re.sub(r'\s+', ' ', text.strip())

    print(map_reduce_summarization(text, llm))
