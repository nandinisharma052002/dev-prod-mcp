from langgraph.prebuilt import create_react_agent

from agent.llm import get_llm
from agent.tools import TOOLS


def build_graph():

    llm = get_llm()

    agent = create_react_agent(
        llm,
        TOOLS,
        prompt="""
You are a helpful assistant.

When a tool returns a result:
1. Use the result.
2. Do not call the same tool again unless absolutely necessary.
3. Provide the final answer to the user.
"""
    )

    return agent