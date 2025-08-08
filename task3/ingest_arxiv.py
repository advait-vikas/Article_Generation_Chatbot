import os
import json
import torch
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def ingest_document(text: str, title: str = "User Upload"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents([Document(page_content=text, metadata={"title": title})])

    device = "cuda" if torch.cuda.is_available() else "cpu"
    embed_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    index_dir = "faiss_index"
    if os.path.exists(index_dir):
        db = FAISS.load_local(index_dir, embed_model, allow_dangerous_deserialization=True)
        db.add_documents(docs)
    else:
        db = FAISS.from_documents(docs, embed_model)
    db.save_local(index_dir)

def bulk_ingest_arxiv():
    import kagglehub
    path = kagglehub.dataset_download("Cornell-University/arxiv")
    if path.endswith(".zip"):
        from zipfile import ZipFile
        extract_dir = os.path.splitext(path)[0]
        with ZipFile(path, "r") as zf:
            zf.extractall(extract_dir)
    else:
        extract_dir = path

    json_path = os.path.join(extract_dir, "arxiv-metadata-oai-snapshot.json")
    data = []
    with open(json_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))

    docs = []
    for paper in data[:500]:
        title = paper.get("title")
        abstract = paper.get("abstract")
        if title and abstract:
            docs.append(
                Document(
                    page_content=title + "\n\n" + abstract,
                    metadata={"title": title},
                )
            )
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    embed_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(split_docs, embed_model)
    db.save_local("faiss_index") 

    print("FAISS index created in faiss_index/ — ready for load_local()")
