from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os
from .schemas import ChatRequest, QueryRequest
from .openai_client import chat_completion
from .rag import upsert_document, query_similar
from .utils import save_upload_file
import fitz

load_dotenv()
app = FastAPI(title="AI Integration - FastAPI RAG Demo")

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def index():
    html = open("app/static/index.html", "r", encoding="utf-8").read()
    return HTMLResponse(content=html)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: ChatRequest):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": req.prompt}
    ]

    resp = chat_completion(messages)
    return {"answer": resp}
    

import fitz  # PyMuPDF

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # 1. Save file locally
    path = await save_upload_file(file)
    doc_id = os.path.basename(path)

    # 2. Extract text
    text = ""

    if file.filename.lower().endswith(".pdf"):
        # PDF extraction
        try:
            pdf = fitz.open(path)
            for page in pdf:
                text += page.get_text()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"PDF extraction failed: {e}")

    elif file.filename.lower().endswith(".txt"):
        # TXT extraction
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except:
            text = "[could not read .txt file]"
    else:
        text = "[unsupported file type]"

    # 3. Validate extracted text
    if not text.strip():
        text = "[empty document or unreadable text]"

    # 4. Store into ChromaDB
    upsert_document(
        doc_id=doc_id,
        text=text,
        metadata={"filename": file.filename}
    )

    return {
        "doc_id": doc_id,
        "text_preview": text[:300]  # send first 300 chars back for debugging
    }

@app.post("/query")
async def query(req: QueryRequest):
    results = query_similar(req.query, req.top_k)

    # Extract matched text chunks
    contexts = results.get("documents", [[]])[0]

    # Build RAG prompt
    prompt = f"Use the following information to answer the question:\n\n{contexts}\n\nQuestion: {req.query}"

    messages = [
        {"role": "system", "content": "You are a RAG assistant."},
        {"role": "user", "content": prompt}
    ]

    rag_answer = chat_completion(messages)

    return {
        "matches": results,
        "answer": rag_answer
    }
