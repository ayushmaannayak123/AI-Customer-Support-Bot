# rag.py

import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


DOCUMENT_FOLDER = "documents"


def load_documents(file_names):
    """
    Loads only the requested text files.
    """

    documents = []

    for file_name in file_names:

        loader = TextLoader(
            os.path.join(DOCUMENT_FOLDER, file_name),
            encoding="utf-8"
        )

        documents.extend(loader.load())

    return documents


def retrieve_context(query, department):
    """
    Retrieves relevant context based on department.
    """

    if department == "Sales":

        files = [
            "pricing.txt"
        ]

    elif department == "Technical":

        files = [
            "technical.txt"
        ]

    elif department == "Billing":

        files = [
            "policy.txt",
            "faq.txt"
        ]

    elif department == "Account":

        files = [
            "faq.txt"
        ]

    else:

        files = [
            "pricing.txt",
            "policy.txt",
            "technical.txt",
            "faq.txt"
        ]

    documents = load_documents(files)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    docs = vectorstore.similarity_search(
        query,
        k=2
    )

    context = ""

    for doc in docs:

        context += doc.page_content
        context += "\n\n"

    return context