from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS


def get_vector_store(docs,bedrock_embeddings):
    vectorstore_faiss = FAISS.from_documents(docs, bedrock_embeddings)
    vectorstore_faiss.save_local("faiss_index")
