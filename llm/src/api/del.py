from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from llm.src.utilities.OllamaPipeline import OllamaPipeline


class DocumentSummarizer:
    """
    A class for summarizing large documents using a Map-Reduce approach.
    """

    def __init__(self, chunk_size=1000, chunk_overlap=0, token_max=4000):
        """
        Initializes the summarizer with text splitting and LLM model.

        :param chunk_size: Size of text chunks for processing.
        :param chunk_overlap: Overlapping characters between chunks.
        :param token_max: Maximum token limit for reduction.
        """
        self.llm = OllamaPipeline().get_model()
        self.text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        self.map_chain = self._create_map_chain()
        self.reduce_chain = self._create_reduce_chain()
        self.combine_documents_chain = self._create_combine_documents_chain()
        self.reduce_documents_chain = self._create_reduce_documents_chain(token_max)
        self.map_reduce_chain = self._create_map_reduce_chain()

    def _create_map_chain(self):
        """Creates the mapping step for extracting themes from documents."""
        map_prompt = PromptTemplate.from_template(
            """The following is a set of documents:
            {docs}
            Based on this list of docs, please identify the main themes.
            Helpful Answer:"""
        )
        return LLMChain(llm=self.llm, prompt=map_prompt)

    def _create_reduce_chain(self):
        """Creates the reduction step for consolidating summaries."""
        reduce_prompt = PromptTemplate.from_template(
            """The following is a set of summaries:
            {docs}
            Take these and distill them into a final, consolidated summary of the main themes.
            Helpful Answer:"""
        )
        return LLMChain(llm=self.llm, prompt=reduce_prompt)

    def _create_combine_documents_chain(self):
        """Creates a chain to combine documents into a single summary."""
        return StuffDocumentsChain(
            llm_chain=self.reduce_chain, document_variable_name="docs"
        )

    def _create_reduce_documents_chain(self, token_max):
        """Creates a chain to reduce document summaries into a final summary."""
        return ReduceDocumentsChain(
            combine_documents_chain=self.combine_documents_chain,
            collapse_documents_chain=self.combine_documents_chain,
            token_max=token_max,
        )

    def _create_map_reduce_chain(self):
        """Creates a Map-Reduce chain combining the mapping and reducing steps."""
        return MapReduceDocumentsChain(
            llm_chain=self.map_chain,
            reduce_documents_chain=self.reduce_documents_chain,
            document_variable_name="docs",
            return_intermediate_steps=False,
        )

    def summarize(self, text):
        """
        Summarizes a large text by splitting it into chunks, processing it, and reducing it to key themes.

        :param text: A long text string to summarize.
        :return: A consolidated summary string.
        """
        split_docs = self.text_splitter.create_documents([text])
        summary = self.map_reduce_chain.run(split_docs)
        return summary

# Example Usage:
# summarizer = DocumentSummarizer()
# large_text = """Your long document text goes here."""
# summary = summarizer.summarize(large_text)
# print(summary)
