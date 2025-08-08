import time
import streamlit as st
from generate_article import generate_article
from ingest_arxiv import ingest_document

st.set_page_config(page_title="arXiv Article Generator")
st.title("Article Generator")

st.header("Expand Knowledge Base")
uploaded_file = st.file_uploader("Upload a text file to add to the knowledge base", type=["txt"])
if uploaded_file is not None:
    file_text = uploaded_file.read().decode("utf-8")
    title = uploaded_file.name
    with st.spinner("Adding document to knowledge base..."):
        ingest_document(file_text, title=title)
    st.success(f"Document '{title}' added to knowledge base!")

st.header("Generate Article")
topic = st.text_input("Enter your topic:")

if st.button("Generate Article"):
    if topic:
        start = time.time()
        with st.spinner("Generating article..."):
            article = generate_article(topic)
        elapsed = time.time() - start
        st.subheader(f"Generated Article (took {elapsed:.1f}s)")
        st.write(article)
    else:
        st.warning("Please enter a topic first.")
