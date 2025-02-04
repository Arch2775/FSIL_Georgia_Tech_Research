from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
import streamlit as st 
import pdfplumber



def embed_pdf(file_path):
    folder_path = "db"
    embedding = FastEmbedEmbeddings()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2048, chunk_overlap=300, length_function=len, is_separator_regex=False
    )
    loader = PDFPlumberLoader(file_path)
    docs = loader.load_and_split()

    chunks = text_splitter.split_documents(docs)


    vector_store = Chroma.from_documents(
        documents=chunks, embedding=embedding, persist_directory=folder_path
    )
    vector_store.persist()
    st.success("embedding successful")

def prompt_generator(user_query):
    cached_llm = Ollama(model='llama3')
    folder_path = "db"
    raw_prompt = PromptTemplate.from_template("""
    <s>[INST] You are a technical assistant skilled in searching and analyzing documents, particularly legal and financial agreements (credit agreements in this case), with a strong focus on recognizing and extracting relevant entities. 
    When presented with a user query, create a rsponse using key named entities such as company names, dates, monetary values, legal clauses, and other significant terms. 
    Ensure that your response is concise, based solely on the context provided, and explicitly identifies these entities in relation to the user's query. If the provided information does not directly answer the query, clearly state that the answer is not found. [/INST] </s>

    [INST] {input}
   Context: {context}
   Answer:
    [/INST]
    """)

    embedding = FastEmbedEmbeddings()
    vector_store = Chroma(persist_directory=folder_path, embedding_function=embedding)
    
    retriever = vector_store.as_retriever(
        search_type = "similarity_score_threshold",
        search_kwargs={
            "k": 10,
            "score_threshold":0.65
        },
    )

    document_chain = create_stuff_documents_chain(cached_llm, raw_prompt)
    chain = create_retrieval_chain(retriever, document_chain)

    result = chain.invoke({"input": user_query})

    response_answer={"answer":result["answer"]}
    return response_answer 

@st.cache_data
def extract_all_pages_as_images(file_upload, dpi=300):
    pdf_pages = []
    with pdfplumber.open(file_upload) as pdf:
        for page in pdf.pages:
            pdf_pages.append(page.to_image(resolution=dpi).original)
    return pdf_pages

