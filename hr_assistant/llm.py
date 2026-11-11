"""connect the llm to the brain of the assistant"""


from langchain_groq import ChatGroq

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def get_llm():
    """return a Chat groq model. Read GROQ_API_KEY from the environment."""
    logger.info("Initializing the LLM '%s' ", config.LLM_MODEL_NAME)
    return ChatGroq(model=config.LLM_MODEL_NAME, temperature=0)

    