# 🚀 AI DuckDB RAG Chatbot

This repository contains a practical implementation of a **Retrieval-Augmented Generation (RAG) chatbot** built using:

- 🧠 LlamaIndex
- 🤖 OpenAI GPT-4o
- 🔎 OpenAI Embeddings
- 🗄 Local document indexing
- 📚 Source-aware answer generation

The system indexes local documents and generates grounded answers with references.

---

# 📦 Project Structure

AI-DuckDB-Analytics/
│
├── data/
│   └── notes.txt
│
├── assets/
│   └── image.png
│
├── rag_app.py
├── requirements.txt
├── .env
└── README.md

---

# 🧠 Project Overview

This project implements a **local Retrieval-Augmented Generation (RAG) system**.

Instead of relying only on a large language model’s internal knowledge, the system:

1. Loads local `.txt` documents
2. Converts them into embeddings
3. Builds a vector index
4. Retrieves relevant context
5. Generates grounded answers using GPT-4o
6. Displays source documents with similarity scores

This ensures responses are transparent and based on actual indexed data.

---

# ⚙️ How It Works

User Question  
↓  
Embedding Generation  
↓  
Vector Similarity Search  
↓  
Context Retrieval  
↓  
LLM Response Generation  
↓  
Answer + Source References

---

# ▶️ How to Run

## 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add OpenAI API Key

Create a .env file:

OPENAI_API_KEY=your_api_key_here
4️⃣ Run the Application
python rag_app.py
💬 Example Question
What is this project about?
✅ Example Response
This project builds a local RAG chatbot using LlamaIndex.
It indexes documents in the data folder and answers questions with source references.
🖼 Example Output

🏗 Tech Stack

Python 3.10+

LlamaIndex

OpenAI GPT-4o

OpenAI Embeddings

Local Vector Index

🎯 What This Project Demonstrates

✔ Retrieval-Augmented Generation
✔ Local document indexing
✔ Vector similarity search
✔ Source-aware AI responses
✔ Practical AI system design
