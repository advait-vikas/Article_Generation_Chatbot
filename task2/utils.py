import os
import torch
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import faiss

DB_PATH = "vector_db"


def get_embeddings_model():
    # Determine the device to use (GPU if available, otherwise CPU)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2", model_kwargs={"device": device}
    )


def load_vector_store():
    embedding = get_embeddings_model()
    if os.path.exists(DB_PATH):
        return FAISS.load_local(DB_PATH, embedding, allow_dangerous_deserialization=True)
    else:
        return FAISS.from_texts(["This is a sample document"], embedding)


def save_vector_store(db):
    db.save_local(DB_PATH)