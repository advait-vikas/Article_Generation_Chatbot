import streamlit as st
from langchain.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="Mistral Chatbot with Ollama", layout="wide")
st.title("🤖 Chat with Mistral (via Ollama + LangChain)")

llm = ChatOllama(model="mistral")  

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Give an article title ....")

prompt_template = f"""
You are a helpful and professional writing assistant. Your task is to generate a well-structured and detailed article based on the topic the user provides.

Guidelines:
- Use formal and informative language.
- Structure the article with headings and subheadings (if appropriate).
- Keep the response coherent and factually accurate.
- Ensure proper grammar and natural flow.

User Topic: {user_input}

Now write the article:
"""

if user_input:
    response = conversation.predict(input=prompt_template)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Mistral", response))

for speaker, message in st.session_state.chat_history:
    with st.chat_message(speaker):
        st.markdown(message)
