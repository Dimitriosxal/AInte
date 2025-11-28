from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3
