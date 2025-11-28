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
A simple API endpoint that communicates with OpenAI’s Chat models  
(default: `gpt-4o-mini`).

### **2. File Upload + Embeddings**
Users can upload documents which are then embedded and stored  
inside ChromaDB along with metadata.

### **3. RAG Query**
Ask a question → semantic search runs → the top-matched context is sent  
to the LLM for an enriched and accurate answer.

### **4. Frontend Demo**
A very small HTML interface used for testing:
- Chat
- Upload
- Ask (RAG)

---

## 📁 Project Structure

AInte/
│
├── app/
│ ├── main.py # API endpoints & routing
│ ├── openai_client.py # OpenAI API wrapper
│ ├── rag.py # RAG logic (ChromaDB + embeddings)
│ ├── schemas.py # Pydantic models (validation)
│ ├── utils.py # File upload helpers
│ └── static/
│ └── index.html # Minimal frontend demo
│
├── .env.example # Environment variables template
├── requirements.txt # Dependencies
├── .gitignore # Ignored files
└── README.md # Documentation


---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/AInte.git
cd AInte
```

  2. Create a virtual environment
```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
  3. Install Dependecies
```
pip install -r requirements.txt
```
  4. Create your environment file
```
cp .env.example .env
```
->Fill in your OpenAI API Key inside .env.

---

## ▶️ Running the Server

```
uvicorn app.main:app --reload
```

Then open your browser at:

```
http://localhost:8000
```

You will see:

- Chat section  
- Upload section  
- RAG Query section  

All inside the simple HTML interface.

---
✅📄 PDF Text Extraction (New Feature)
 
AInte now supports automatic text extraction from PDF documents using PyMuPDF (fitz).

When a user uploads a PDF:

The server reads the file

Extracts clean text from each page

Stores the extracted content inside ChromaDB

Makes it searchable via RAG queries

Supported formats:

✔ .pdf — full text extraction

✔ .txt — plain text read

✘ Other binary files return: "[unsupported file type]"

This enables real Retrieval-Augmented Generation (RAG), allowing the system to give accurate answers based on the actual content of the uploaded PDF.

## 🧠 API Usage

### **Chat**
POST → `/chat`

Body:
```
{
  "prompt": "Your message here"
}
```

---

### **Upload Document**
POST → `/upload`

Multipart form-data:
```
file: <your_file>
```

---

### **RAG Query**
POST → `/query`

Body:
```
{
  "query": "Your question",
  "top_k": 3
}
```

---

## 🏗 Future Improvements

- Chunking for large PDF files  
- Proper PDF parsing (PyMuPDF / pdfplumber)  
- Authentication (API key / JWT)  
- Dockerfile + container deployment  
- Move vector DB from local ChromaDB → Pinecone / Weaviate  
- Replace HTML with React or Next.js frontend  
- Add retry logic for OpenAI rate limits  
- Add tests with pytest  

