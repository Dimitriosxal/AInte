# AInte – AI Integration with FastAPI, OpenAI & RAG

AInte is a complete demo project that showcases how to integrate  
LLM models, embeddings, and RAG  
into a FastAPI backend.

This project includes:

✅ Chat endpoint  
✅ File upload + embedding generation  
✅ Vector storage using ChromaDB  
✅ RAG queries with semantic search  
✅ Simple frontend (HTML/JS) for testing  

---

## 🚀 Features

### **1. Chat Endpoint**
Communicates directly with OpenAI Chat models (default: `gpt-4o-mini`).

### **2. File Upload + Embeddings**
Users upload documents → embeddings are generated → stored in ChromaDB.

### **3. RAG Query**
Semantic search retrieves relevant chunks → sent to the LLM for more accurate responses.

### **4. Frontend Demo**
Simple HTML page for:
- Chat  
- Upload  
- RAG queries  

---

## 📁 Project Structure
```
AInte/
│
├── app/
│   ├── main.py
│   ├── openai_client.py
│   ├── rag.py
│   ├── schemas.py
│   ├── utils.py
│   └── static/
│       └── index.html
│
├── .env.example
├── requirements.txt
├── .gitignore
└── README.md

```


##🔧 Installation
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/AInte.git
cd AInte

2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
.venv\Scripts\activate          # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create your environment file
cp .env.example .env


Fill in your OpenAI API Key inside .env.

##  ▶️ Running the Server
uvicorn app.main:app --reload


Then open in browser:

http://localhost:8000


You will see the Chat, Upload, and RAG interface.

##  📄 PDF Text Extraction

AInte supports automatic PDF text extraction using PyMuPDF (fitz).

When a PDF is uploaded:

The server loads the file

Extracts readable text from each page

Stores the text inside ChromaDB

Makes it searchable via RAG

Supported Formats

✔ PDF (.pdf) — full text extraction

✔ TXT (.txt) — plain text

✘ Others → "unsupported file type"

This enables real Retrieval-Augmented Generation based on actual document content.

##  🧠 How RAG Works

RAG (Retrieval-Augmented Generation) improves LLM responses using vector search + generation.

1. Embeddings

Documents are embedded using:

text-embedding-3-small

2. Vector Database

Embeddings + metadata are stored in ChromaDB.

3. Semantic Search

When the user asks a question:

The question is embedded

ChromaDB returns the most similar document chunks

These chunks become context

4. LLM Response

The system generates a prompt like:

Use the following context to answer:

[matched document chunks]

Question: <user query>


The model answers using both context + world knowledge.

##  🧠 API Usage
Chat
POST /chat
{
  "prompt": "Your message here"
}

Upload Document
POST /upload
file: <your_file>

RAG Query
POST /query
{
  "query": "Your question",
  "top_k": 3
}

##  🏗 Future Improvements

Chunking for large PDF files

More advanced PDF parsing (tables, layout)

Authentication (API key / JWT)

Docker container deployment

Move from local ChromaDB → Pinecone / Weaviate

Replace HTML interface with React or Next.js

Retry logic for OpenAI rate limits

Unit tests with pytest


##  🎯 Summary

AInte is a clean, modern, production-style AI integration template showing:

FastAPI backend

OpenAI models

Vector database

RAG flow

PDF extraction

Frontend interface
