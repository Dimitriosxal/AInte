import os
from chromadb import Client
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# Database directory
DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db")

# Initialize ChromaDB client
client = Client(
    settings=Settings(
        persist_directory=DB_DIR,
        allow_reset=True
    )
)

# Embedding function using OpenAI
emb_func = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
)

COLLECTION_NAME = "documents"


def get_collection():
    """Return the collection, create it if missing."""
    try:
        return client.get_collection(COLLECTION_NAME)
    except:
        return client.create_collection(
            name=COLLECTION_NAME,
            embedding_function=emb_func
        )


def upsert_document(doc_id: str, text: str, metadata: dict = None):
    """Add or update a document in vector DB."""
    col = get_collection()
    col.upsert(
        ids=[doc_id],
        documents=[text],
        metadatas=[metadata or {}]
    )
    client.persist()


def query_similar(query: str, n_results: int = 3):
    """Retrieve semantically similar documents."""
    col = get_collection()
    results = col.query(
        query_texts=[query],
        n_results=n_results
    )
    return results
