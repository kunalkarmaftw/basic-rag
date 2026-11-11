"""building the agent that ties the LLM and the search tool together."""

from langchain.agents import create_agent

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

from .llm import get_llm

llm = get_llm()

print("LLM OBJECT:", llm)
print("LLM TYPE:", type(llm))
print("HAS bind_tools:", hasattr(llm, "bind_tools"))


def create_hr_agent(llm,tools):
    """return a langchain agent that can call our tools to answer questions."""
    logger.info("Creating HR agent with %d tools", len(tools))
    agent = create_agent(model=llm, tools=tools,system_prompt=config.system_prompt)
    logger.info("HR agent is ready")
    return agent

    # print("MODEL TYPE:", type(llm))
    # print("IS FUNCTION:", callable(llm))
    # print("HAS bind_tools:", hasattr(llm, "bind_tools")) ## for debugging purpose

    

