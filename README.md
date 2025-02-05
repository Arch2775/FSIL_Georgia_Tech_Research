
# FSIL_Georgia_Tech_Research

This repository contains research and development work conducted during my internship as a Research Assistant at the Financial Services Innovation Lab, Georgia Tech University.


![Logo](https://imgs.search.brave.com/gkw4zS3LPa1oiuJPfD8Kw4rv-43xJnJPPyyGHZ67znU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5saWNkbi5jb20v/ZG1zL2ltYWdlL0Q1/NjNEQVFFRk1Bal9n/WVptT3cvaW1hZ2Ut/c2NhbGVfMTkxXzEx/MjgvMC8xNjcwNDQ2/MTU1NjAwL2dlb3Jn/aWFfaW5zdGl0dXRl/X29mX3RlY2hub2xv/Z3lfZmluYW5jaWFs/X3NlcnZpY2VzX2lu/bm92YXRpb25fbGFi/X2NvdmVyP2U9MjE0/NzQ4MzY0NyZ2PWJl/dGEmdD1jUUNlM0Fl/LTZCVkl1SGdndHo5/Q0RZUVc4WVVRUndH/Zm9Ca3ZpMXdDN1FB)


## Documentation 

### 1. Annotations:

round 1: Annotated 18 credit agreements to identify entities related to the types of loan offered, i.e, Term loan, Revolver, Line of credit. 

round 2: Annotated 26 credit agreements to identify entities that describe the deal terms of the agreements. Some of the entities were Deal class, Deal sub-class, Loan type, Loan Amount type, Spread index, Spread Type, Spread value, Spread condition etc.

### 2. Dataset stats:

contains information related to the no. of annotated tokens, annotated sentances, etc. 

### 3. FSIL_RAG:

RAG_Ollama: developed a RAG pipeline using Ollama to answer queries related Named-entites in the credit agreements.

### 4. NER_models:

IOB - converts the json file of my Annotations into IOB format for T-NER model. IOB format is inspired from the CoNLL-2003 dataset for NER tasks. Fine-tuned "roberta-base" on my Annotations to perform NER. 

based on https://github.com/asahi417/tner 

### 5. Papers:

All the papers related to the project along with the lit. review of some of them. Some were needed as pre-requisite for the project and some were used as inspiration for our project. 





