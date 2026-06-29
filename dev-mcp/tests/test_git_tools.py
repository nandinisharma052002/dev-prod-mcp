from tools.git_tools import (
    git_log,
    git_status
)


def test_git_status():

    result = git_status()

    assert result["success"] is True


def test_git_log():

    result = git_log()

    assert result["success"] is True
    assert "commits" in result


def test_git_log_limit():

    result = git_log(
        max_commits=5
    )

    assert result["success"] is True
    assert result["count"] <= 5