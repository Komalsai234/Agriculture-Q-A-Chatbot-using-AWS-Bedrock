import boto3
from langchain_community.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from src.data_ingestion import *
from src.vector_embeddings import *

bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock)


if __name__ == "__main__":
    docs = data_ingestion()

    get_vector_store(docs,bedrock_embeddings)
