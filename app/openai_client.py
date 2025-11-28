import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_KEY

def chat_completion(messages, model=None, max_tokens=500, temperature=0.2):
    model = model or os.getenv("MODEL_CHAT", "gpt-4o-mini")

    response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature
)
    )
    return response

def get_embeddings(texts, model=None):
    model = model or os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    response = openai.Embedding.create(
        model=model,
        input=texts
    )
    vectors = [item["embedding"] for item in response["data"]]
    return vectors
