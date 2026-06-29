def project_overview():
    return """
Developer Productivity MCP Server

Purpose:
This MCP server provides developer-focused tools for
working with source code repositories.

Available Tools:
- read_file
- write_file
- list_files
- search_code
- git_status
- git_log
- run_pytest
- run_single_test

Primary Use Cases:
- Code exploration
- Repository analysis
- Test execution
- Git history inspection
- Developer productivity workflows
"""

def coding_standards():
    return """
Coding Standards

1. Use type hints for all functions.
2. Handle exceptions gracefully.
3. Return structured JSON responses.
4. Restrict filesystem access to approved locations.
5. Write pytest test cases for all tools.
6. Avoid hardcoded paths.
7. Prefer pathlib over os.path.
"""

def project_architecture():
    return """
Project Structure

tools/
    file_tools.py
    search_tools.py
    git_tools.py
    test_tools.py

resources/
    project_resources.py

prompts/
    review_prompts.py

tests/

workspace/

Responsibilities

file_tools:
    File operations

search_tools:
    Source code search

git_tools:
    Git repository operations

test_tools:
    Test execution
"""

def tool_catalog():
    return """
Tool Catalog

read_file(path)
    Read a file.

write_file(path, content)
    Create or overwrite a file.

list_files(directory='')
    List files and directories.

search_code(query, directory='', file_pattern=None)
    Search source code.

git_status()
    Show git repository status.

git_log(max_commits=10)
    Show commit history.

run_pytest()
    Run all tests.

run_single_test(test_path)
    Run a specific test.
"""