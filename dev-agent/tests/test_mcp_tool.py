# tests/mcp_tool_test.py

from agent.llm import get_llm
from agent.tools import TOOLS

llm = get_llm()

llm_with_tools = llm.bind_tools(TOOLS)

response = llm_with_tools.invoke(
    "List all files in the project"
)

print(response)
print()
print("Tool Calls:")
print(response.tool_calls)