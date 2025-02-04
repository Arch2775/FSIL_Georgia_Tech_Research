import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from fun import embed_pdf, prompt_generator, extract_all_pages_as_images
import time


st.set_page_config(
    page_title="FSIL-RAG",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.subheader("🚀 PDF RAG-Ollama", divider="gray", anchor=False)
col1, col2 = st.columns([2, 2])

with col2:
    st.image("gt.jfif")

last_time = time.time()

file_upload = col1.file_uploader(
    "Upload PDF ↓", type="pdf", accept_multiple_files=False
)

if file_upload:
    # Save the uploaded file temporarily
    with open(file_upload.name, "wb") as f:
        f.write(file_upload.getbuffer())

    # Create embeddings
    embed_pdf(file_upload.name)

    # Extract and display PDF pages as images
    pdf_pages = extract_all_pages_as_images(file_upload)

    
    zoom_level = 650  
    with col1:
        with st.container():
            for page_image in pdf_pages:
                st.image(page_image, width=zoom_level)

    
    with col2:
        user_query = st.text_area("Ask your query:")
        if st.button("Submit"):
            if user_query:
                response = prompt_generator(user_query)
                st.write("**Answer:**", response["answer"])
            else:
                st.warning("Please enter a query.")

current_time = time.time()

elapsed_time = current_time - last_time
st.write(f"pipeline execution time: {elapsed_time:.2f} seconds")
