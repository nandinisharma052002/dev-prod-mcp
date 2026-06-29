import sys

sys.path.append("../dev-mcp")

from tools.file_tools import (
    list_files as actual_list_files,
    read_file as actual_read_file
)

from tools.search_tools import (
    search_code as actual_search_code
)

from langchain_core.tools import tool


@tool
def list_files() -> str:
    """
    List all files in the project workspace.
    """

    result = actual_list_files("")

    if not result["success"]:
        return result["error"]

    return "\n".join(
        item["name"]
        for item in result["entries"]
    )


@tool
def read_file(path: str) -> str:
    """Read a file from the workspace."""

    result = actual_read_file(path)

    if result["success"]:
        return result["content"]

    return f"Error: {result['error']}"


@tool
def search_code(
    query: str,
    directory: str = "",
    file_pattern: str | None = None,
    max_results: int = 20
):
    """
    Search the local codebase.

    Use this tool whenever a question asks:
    - where something is implemented
    - how a feature works
    - where a function is defined
    - security mechanisms
    - configuration values

    Do not answer such questions from memory.
    Search the code first.
    """
    return actual_search_code(
        query=query,
        directory=directory,
        file_pattern=file_pattern,
        max_results=max_results
    )

# @tool
# def hello_tool(name: str) -> str:
#     """
#     Search the local project source code.

#     Use this tool whenever you need to find:
#     - functions
#     - classes
#     - variables
#     - file locations

#     Do NOT use web search.
#     This tool searches the developer workspace.
#     """
#     return f"Hello {name}"

TOOLS = [
    list_files,
    read_file,
    search_code
    # hello_tool
    
]