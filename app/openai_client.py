import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_completion(messages, model=None, temperature=0.2):
    """
    Chat completion using the new OpenAI client API.
    """
    model = model or os.getenv("MODEL_CHAT", "gpt-4o-mini")

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content

def get_embeddings(texts, model=None):
    """
    Embedding generation using the new OpenAI client API.
    """
    model = model or os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    response = client.embeddings.create(
        model=model,
        input=texts
    )

    # extract vectors
    vectors = [item.embedding for item in response.data]
    return vectors
