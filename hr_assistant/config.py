import os

from dotenv import load_dotenv

load_dotenv()

## ENV VAR / SECRET

groq_key = os.getenv("GROQ_API_KEY")
jina_key = os.getenv("JINA_API_KEY")

## LANGSMITH TRACING
LANGSMITH_TRACING=os.getenv("LANGSMITH_TRACING")
LANGSMITH_ENDPOINT=os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY=os.getenv("LANGSMITH_API_KEY")
LANGSMITH_AGENT_ID=os.getenv("LANGSMITH_AGENT_ID")


## define path - data / vector store

Data_File_path = os.path.join("data", "hr_policy.txt")
Vector_Store_path = os.path.join("data","faiss_index")

## models

LLM_MODEL_NAME = 'openai/gpt-oss-120b'
EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

## CHUNK / TEXT SPLITTING CONFIG

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

## RETRIVAL RESULTS

TOP_K_RESULTS = 3

## SYSTEM INSTRUCTIONS

system_prompt=(

    "You are friendly HR assistant working for Acme crop."
    "Always use the search_hr_policy tool to look up facts before answering."
    "If the answer isn't in the search result, say you don't know, instead of guessing."
    )

def check_api_key()-> None:
    """Stop early with a clear message if a required API key is missing"""
    if not groq_key:
        raise ValueError("missing GROQ_API_KEY")
    if not jina_key:
        raise ValueError("missing JINA_API_KEY")