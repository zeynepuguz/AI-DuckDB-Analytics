# 🚀 AI DuckDB Analytics

This repository contains **two practical AI + Data Engineering projects** built around DuckDB and LlamaIndex.

The goal is to demonstrate:

- 🧠 Retrieval-Augmented Generation (RAG)
- 🗄 DuckDB as a local analytics engine
- 🔎 Natural Language → SQL query generation
- 📚 Document indexing and source-aware responses
- 💬 Memory-enabled conversational AI

---

# 📦 Project Structure

AI-DuckDB-Analytics/
│
├── data/
│   ├── bank-marketing.csv
│   └── notes.txt
│
├── assets/
│   └── image.png
│
├── rag_app.py          → Project 1 (RAG chatbot)
├── analysis.py         → DuckDB analytics queries
├── db_setup.py         → Database initialization
├── datacamp.duckdb     → DuckDB database file
├── requirements.txt
└── README.md

---

# 🧠 Project 1 — Local RAG Chatbot (LlamaIndex + OpenAI)

This project builds a **Retrieval-Augmented Generation system** using:

- LlamaIndex
- OpenAI GPT-4o
- OpenAI Embeddings
- Local documents
- Optional conversational memory

## What It Does

- Loads `.txt` documents from `/data`
- Converts them into embeddings
- Builds a vector index
- Retrieves relevant context
- Generates grounded answers
- Displays similarity scores and sources

## Run It

```bash
python rag_app.py
```
## Example question:

- What is this project about?

## Example response:

- This project builds a local RAG chatbot using LlamaIndex.
- It indexes documents in the data folder and answers questions with source references.
