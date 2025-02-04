# FSIL_RAG

_preprocess.py_ :- converts the credit agreements in HTML format to PDF format for the RAG application.

**RAG-Ollama** 

_fun.py_ :- contains all the functions needed for the RAG pipeline - pdf upload, view pdf, creating and storing embeddings in chromaDB and finally generating prompts

_app.py_ :- contains streamlit elements to render the UI and to display the functionalities

need to work on the prompts as the results are not that accurate.

current pipeline execution time is ~240 secs, might run faster on a better GPU.










https://www.gpu-mart.com/blog/custom-llm-models-with-ollama-modelfile :- helps me modify the models on Ollama according the role, and create a new model. Will try it out next and see the results
