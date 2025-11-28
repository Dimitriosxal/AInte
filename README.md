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

AInte/
  app/
    main.py               # API endpoints & routing
    openai_client.py      # OpenAI API wrapper
    rag.py                # RAG logic (ChromaDB + embeddings)
    schemas.py            # Pydantic models
    utils.py              # File upload helpers
    static/
      index.html          # Minimal frontend demo
  .env.example            # Environment variables template
  requirements.txt        # Dependencies
  .gitignore
  README.md



---

INSTALLATION

Clone the repository
git clone https://github.com/YOUR-USERNAME/AInte.git

cd AInte

Create a virtual environment
python -m venv .venv
source .venv/bin/activate (Linux/Mac)
.venv\Scripts\activate (Windows)

Install dependencies
pip install -r requirements.txt

Create your environment file
cp .env.example .env
Fill in your OpenAI API Key inside .env.

RUNNING THE SERVER

uvicorn app.main:app --reload
Open: http://localhost:8000

You will see Chat, Upload, and RAG sections.

PDF TEXT EXTRACTION (NEW FEATURE)

AInte now supports automatic PDF text extraction using PyMuPDF (fitz).

When a user uploads a PDF:

The server reads the file

Extracts clean text from each page

Stores the extracted text in ChromaDB

Makes it searchable through RAG queries

Supported formats:

PDF (.pdf) full text extraction

TXT (.txt) plain text

Other files return: "[unsupported file type]"

This enables true Retrieval-Augmented Generation based on real document content.

HOW RAG WORKS

RAG improves LLM responses by combining vector search with generative reasoning.

Embeddings
Uploaded documents are converted to embeddings using text-embedding-3-small.

Vector Storage
Embeddings and metadata are saved locally in ChromaDB.

Semantic Search
When the user performs a query:

The question is embedded

ChromaDB finds the most similar document chunks

These chunks become context for the model

LLM Response
The system sends this prompt:

Use the following context to answer:
[matched document chunks]
Question: <user query>

The model uses both the context + its own knowledge for accurate answers.

API USAGE

CHAT
POST /chat
JSON body:
prompt: "Your message here"

UPLOAD DOCUMENT
POST /upload
Multipart form-data:
file: <your_file>

RAG QUERY
POST /query
JSON body:
query: "Your question"
top_k: 3

FUTURE IMPROVEMENTS

Chunking for large PDF files

Better PDF parsing (tables, layout preservation)

Authentication (API key / JWT)

Docker deployment

Move vector DB to Pinecone / Weaviate

Replace HTML frontend with React or Next.js

Retry logic for OpenAI rate limits

Add backend tests with pytest
