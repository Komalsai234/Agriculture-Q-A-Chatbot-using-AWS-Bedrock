import os
import json
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

import boto3
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS

from src.data_ingestion import *
from src.llm_bedrock import *
from src.vector_embeddings import *


bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v1", client=bedrock)


prompt_template = """

Human: Use the following pieces of context to provide a 
concise answer to the question at the end. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"])



def get_response_llm(llm,vectorstore_faiss,query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_faiss.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
    answer=qa({"query":query})
    return answer['result']



def main():
    st.title("Agriculture Bot")

    user_question = st.text_input("Ask your Question regarding Organic Farming")

    if st.button("Answer"):
        with st.spinner("Processing..."):
            
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            llm=get_llama2_llm(bedrock)

            st.write(get_response_llm(llm,faiss_index,user_question))
            st.success("Done")


if __name__ == "__main__":
    main()