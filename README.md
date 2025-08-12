
# 🚀 LLM-Based Article Generation Chatbot

This repository contains the three main tasks completed during my **NullClass Data Science Internship (July 16 – August 16, 2025)**.  
All tasks involve building and deploying **LLM-powered applications** using tools such as **LangChain**, **Streamlit**, **FAISS**, and various open-source LLMs like **Mistral** (via Ollama).

---

## 📝 Task Overviews

### **Task 1 – Multi-Model Article Generator**
**Goal**: Generate high-quality articles using **three different open-source LLMs** (e.g., Mistral, LLaMA 2, Falcon) for comparison.  
**Tools**: LangChain, Streamlit, Ollama  

**Features**:
- Select from multiple models
- Enter custom prompts
- View & compare generated outputs  

**Example Output**:  
*"The Impact of AI in Education – Mistral vs LLaMA 3 vs Falcon"*

---

### **Task 2 – Chatbot with Dynamic Knowledge Updates**
**Goal**: Create a chatbot that can **update its knowledge base** instantly from newly provided articles or text.  
**Tools**: LangChain, FAISS Vector Store, Streamlit  

**Features**:
- Upload text/markdown files
- Extract embeddings & store them in FAISS
- Query the bot for context-aware answers
- Persistent local FAISS DB for fast retrieval

---

### **Task 3 – Domain Expert Chatbot (arXiv Scientific Data)**
**Goal**: Build a **scientific research assistant** trained on the **Cornell arXiv dataset**.  
**Dataset Source**: [Cornell University – arXiv (via KaggleHub)](https://www.kaggle.com/datasets/Cornell-University/arxiv)  
**Tools**: LangChain, FAISS, Streamlit, Ollama  

**Features**:
- Import scientific papers from Kaggle
- Store them as embeddings in FAISS
- Query the bot for detailed, paper-based scientific answers
- Supports **article generation** from the ingested scientific knowledge

---

### 2️⃣ Install dependencies

Each task has its own `requirements.txt`. Example for Task 1:

```bash
cd task1
pip install -r requirements.txt
```

---

## 🚀 Usage

### Task 1: Article Generator

```bash
cd task1
ollama run mistral (another terminal) 
streamlit run chatbot.py
```

### Task 2: Dynamic Knowledge Chatbot

```bash
cd task2
ollama run mistral (another terminal) 
streamlit run app.py
```

### Task 3: Domain Expert Chatbot

```bash
cd task3
ollama run mistral (another terminal)
python ingest_arxiv.py (to import the papers)
streamlit run chatbot_arxiv.py
```

---

## 📊 Learning Outcomes

* **LLM Integration**: Worked with Ollama and LangChain to interact with multiple LLMs.
* **Vector Databases**: Implemented FAISS for fast semantic search & retrieval.
* **Streamlit UI**: Built interactive UIs for non-technical users.
* **Data Ingestion**: Imported large datasets (arXiv) and converted them into searchable embeddings.
* **Prompt Engineering**: Designed prompts for both article generation and domain-specific Q\&A.

---

## 🏆 Internship Impact

These projects showcase the ability to design, build, and deploy intelligent AI-driven applications that combine:

* Real-time knowledge updates
* Multi-model output comparison
* Specialized domain expertise

---

## 👨‍💻 Author

**Advait Vikas**
📧 [advaitvikas13@gmail.com](mailto:advaitvikas13@gmail.com)

