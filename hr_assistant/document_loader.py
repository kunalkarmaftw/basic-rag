"""Step 1: read the raw document from the data folder."""

from langchain_community.document_loaders import TextLoader

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__) # this name func will share the name of particual file to logger


def load_document(file_path:str = config.Data_File_path):
    """Load a .txt file and return it as a list of Langchain Document"""
    logger.info("loading documents from '%s' ", file_path)
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load
    logger.info("Loaded documents %d document(s)", len(documents))
    return documents.load()