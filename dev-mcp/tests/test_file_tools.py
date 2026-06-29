from pathlib import Path

from tools.file_tools import (
    read_file,
    write_file,
    list_files
)


def test_write_file():
    result = write_file(
        "pytest_test.txt",
        "Hello MCP"
    )

    assert result["success"] is True


def test_read_file():
    write_file(
        "read_test.txt",
        "Read Test"
    )

    result = read_file(
        "read_test.txt"
    )

    assert result["success"] is True
    assert result["content"] == "Read Test"


def test_missing_file():
    result = read_file(
        "does_not_exist.txt"
    )

    assert result["success"] is False


def test_path_traversal():
    result = read_file(
        "../secret.txt"
    )

    assert result["success"] is False


def test_list_files():
    write_file(
        "list_test.txt",
        "content"
    )

    result = list_files()

    assert result["success"] is True

    names = [
        item["name"]
        for item in result["entries"]
    ]

    assert "list_test.txt" in names