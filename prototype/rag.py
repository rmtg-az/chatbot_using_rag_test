from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
FAISS_DIR = "faiss_index"


def create_vectorstore(pdf_path: Path) -> FAISS:
    """ Load a PDF, split it into chunks,generate embeddings,
    and save a FAISS vector store. """

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    vectorstore.save_local(FAISS_DIR)

    return vectorstore