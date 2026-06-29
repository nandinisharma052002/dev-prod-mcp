from tools.file_tools import write_file
from tools.search_tools import search_code


def test_search_existing_text():

    write_file(
        "search_file.txt",
        "FastMCP is awesome"
    )

    result = search_code(
        query="FastMCP"
    )

    assert result["success"] is True
    assert result["count"] >= 1


def test_search_missing_text():

    result = search_code(
        query="this_should_not_exist"
    )

    assert result["success"] is True
    assert result["count"] == 0


def test_search_file_pattern():

    write_file(
        "example.py",
        "import fastmcp"
    )

    result = search_code(
        query="fastmcp",
        file_pattern=".py"
    )

    assert result["success"] is True


def test_search_invalid_directory():

    result = search_code(
        query="test",
        directory="does_not_exist"
    )

    assert result["success"] is False