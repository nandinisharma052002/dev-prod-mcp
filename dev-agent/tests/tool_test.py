from langchain_core.tools import tool

# from agent.llm import get_llm


# @tool
# def hello_tool(name: str) -> str:
#     """Say hello to someone."""
#     return f"Hello {name}"


# llm = get_llm()

# llm_with_tools = llm.bind_tools(
#     [hello_tool]
# )

# response = llm_with_tools.invoke(
#     "Use the hello_tool for Nandini"
# )

# print(response)
# print()
# print("Tool Calls:")
# print(response.tool_calls)

from agent.tools import TOOLS

for tool in TOOLS:
    print(type(tool))
    print(tool.name)
    print(tool.description)
    print("------")