from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader


def data_ingestion():
    loader = PyPDFDirectoryLoader("Data")
    documents = loader.load()

    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size=10000, chunk_overlap=1000)

    docs = text_spliter.split_documents(documents)

    return docs
