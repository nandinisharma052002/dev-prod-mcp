from fastmcp import FastMCP

from tools.file_tools import (
    read_file,
    write_file,
    list_files
)
from tools.git_tools import (
    git_status,
    git_log
)

from tools.search_tools import search_code

from tools.test_tools import (
    run_pytest,
    run_single_test
)

from resources.project_resources import (
    project_overview,
    coding_standards,
    project_architecture,
    tool_catalog
)

from prompts.review_prompts import (
    review_code,
    security_review,
    summarize_changes,
    generate_test_cases,
    explain_code,
    refactor_code
)

mcp = FastMCP("DevProductivityServer")

# file tools
mcp.tool()(read_file)
mcp.tool()(write_file)
mcp.tool()(list_files)

# git tools
mcp.tool()(git_status)
mcp.tool()(git_log)

# search tools
mcp.tool()(search_code)

# register resources
@mcp.resource("project://overview")
def overview():
    return project_overview()


@mcp.resource("project://coding-standards")
def standards():
    return coding_standards()


@mcp.resource("project://architecture")
def architecture():
    return project_architecture()


@mcp.resource("project://tool-catalog")
def catalog():
    return tool_catalog()

# register prompts
@mcp.prompt()
def code_review():
    return review_code()


@mcp.prompt()
def code_security_review():
    return security_review()


@mcp.prompt()
def change_summary():
    return summarize_changes()


@mcp.prompt()
def test_case_generation():
    return generate_test_cases()


@mcp.prompt()
def code_explanation():
    return explain_code()


@mcp.prompt()
def code_refactoring():
    return refactor_code()

if __name__ == "__main__":
    mcp.run()