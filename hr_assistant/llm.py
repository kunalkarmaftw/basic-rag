"""connect the llm to the brain of the assistant"""


from langchain_groq import ChatGroq

from hr_assistant import config


def get_llm():
    """return a Chat groq model. Read GROQ_API_KEY from the environment."""
    return ChatGroq(model=config.LLM_MODEL_NAME, temperature=0)

    