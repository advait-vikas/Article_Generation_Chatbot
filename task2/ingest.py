from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils import get_embeddings_model, load_vector_store, save_vector_store

def ingest_new_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    embeddings = get_embeddings_model()
    db = load_vector_store()
    db.add_texts(chunks)
    save_vector_store(db)
    