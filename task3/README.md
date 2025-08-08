# Task 3

This directory contains code for Task 3.

## Contents

- `chat_arxiv.py`: Script for interacting with arXiv data via chat.
- `ingest_arxiv.py`: Script for ingesting arXiv documents into the FAISS index.
- `generate_article.py`: Generates detailed articles using retrieved context and LLM.
- `faiss_index/`: Directory containing the FAISS vector database files.
- `requirements.txt`: Python dependencies for Task 3.

## Usage

1. Install dependencies from `requirements.txt`.
2. Run `ingest_arxiv.py` to add arXiv documents to the FAISS index.
3. Use `streamlit run chat_arxiv.py` for chat-based interaction with the ingested arXiv data or to add data 
from a .txt file and generating an article.

## Requirements

See `requirements.txt` for all dependencies.
