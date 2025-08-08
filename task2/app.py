import streamlit as st 
from ingest import ingest_new_text 
from chatbot import ask_question 

st.set_page_config(page_title = "Dynamic Knoeledge Chatbot")
st.title("Knowledge Updating Chatbot") 

menu = st.sidebar.radio("Select Action", ["Ask Question", "Add Knowledge"])

if menu == "Ask Question":
    query = st.text_input("Ask me anything:")
    if st.button("Get Answer") and query:
        st.markdown("**Answer:**")
        st.write(ask_question(query))

elif menu == "Add Knowledge":
    user_input = st.text_area("Paste text to add to chatbot knowledge:")
    if st.button("Ingest Text") and user_input:
        ingest_new_text(user_input)
        st.success("Knowledge added successfully!")