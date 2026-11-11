import os

from langchain_community.vectorstores import FAISS

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model

#build vector store

def build_vector_store(chunks):
    """
    Embed every chunk and build a searchable FAISS index in the memory.
    """ 
    embeddings_model = get_embeddings_model() ## here we are calling our embeddings model
    return FAISS.from_documents(chunks, embeddings_model) ## here we are converting chunks into embeddings

## save vector store

def save_vector_store(vector_store, path : str = config.Vector_Store_path)-> None: ##this func takes a vector store i.e vector_store and the second argument is path is where we cant to store the vector store and the path will be string.
    """save the FAISS index to disk so we don't have to rebuild it every time"""
    vector_store.save_local(path)


##loading the vector store

def load_vector_store(path:str = config.Vector_Store_path):
    """laod a previously saved FAISS index from disk"""
    embedding_model = get_embeddings_model()
    # allow_dangerous_serialization is safe here because we only ever load an index that this same app created and saved.
    return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True) #allow_dangerous_deserialization means we are allowing it to loading it from a file coz if not faiss do not allow from loading from a file. 

def vector_store_exist(path:str = config.Vector_Store_path) -> bool: ## checking if the vector store exists and it returns a bool value and if its true then the reamaining func is executed.
    """check if a saved FAISS index already exists on the disk."""
    return os.path.exists(os.path.join(path, "index.faiss"))

def get_retriever(vector_store, k: int = config.TOP_K_RESULTS):
    """Turn a vector store into a retriever that returns the top-k matching chunks"""
    return vector_store.as_retriever(search_kwargs={"k":k})