import os
import torch
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

device = "cuda" if torch.cuda.is_available() else "cpu"
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True,
)
retriever = vectordb.as_retriever(search_kwargs={"k": 5})

llm = Ollama(model="mistral")
prompt_template = PromptTemplate(
    input_variables=["context", "query"],
    template=(
        "Use the following context to write a detailed article on the given topic. "
        "The article should have a clear, informative title (display the title first), "
        "and the body should be at least three paragraphs long.\n\n"
        "Context:\n{context}\n\n"
        "Topic: {question}\n\n"
        "Format:\n"
        "Title: <title>\n\n"
        "<article body>"
    ),
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template}
)

def generate_article(topic: str) -> str:
    return qa_chain.run({"query": topic})
