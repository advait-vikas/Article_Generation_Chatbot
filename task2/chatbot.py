from langchain.chains import RetrievalQA 
from langchain_community.llms import Ollama 
from utils import load_vector_store 

def get_qa_chain():
    llm = Ollama(model="mistral") 
    retriever = load_vector_store().as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever = retriever) 

def ask_question(question):
    qa_chain = get_qa_chain()
    return qa_chain.run(question)