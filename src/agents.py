from langchain.tools import tool
from langchain.agents import create_agent
from tavily import TavilyClient

from prompts import RESEARCH_PROMPT, PLANNER_PROMPT


tavily_client = TavilyClient()

@tool
def search_recipe(query: str) -> dict:
    """Search for recipes on the web."""
    return tavily_client.search(query)

research_agent = create_agent(
    model="gpt-5-nano",
    system_prompt=RESEARCH_PROMPT,
    tools=[search_recipe]
)

planner_agent = create_agent(
    model="gpt-5-nano",
    system_prompt=PLANNER_PROMPT,
)
