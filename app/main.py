from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os
from .schemas import ChatRequest, QueryRequest
from .openai_client import chat_completion
from .rag import upsert_document, query_similar
from .utils import save_upload_file

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
    

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = await save_upload_file(file)

    # Try to extract text (basic version)
    try:
        with open(path, "rb") as f:
            raw = f.read()
            try:
                text = raw.decode("utf-8")
            except:
                text = "[binary file uploaded]"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    doc_id = os.path.basename(path)
    upsert_document(doc_id=doc_id, text=text)
    return {"doc_id": doc_id}

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
