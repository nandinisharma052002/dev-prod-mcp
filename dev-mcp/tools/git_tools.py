from pathlib import Path
import subprocess


WORKSPACE = Path("workspace").resolve()


def _run_git_command(args: list[str]):
    """
    Execute a git command inside the workspace.
    """

    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=WORKSPACE,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr.strip()
            }

        return {
            "success": True,
            "output": result.stdout.strip()
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def git_status():
    """
    Get git repository status.
    """

    try:
        result = _run_git_command(["status", "--short"])

        if not result["success"]:
            return result

        return {
            "success": True,
            "status": result["output"]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def git_log(max_commits: int = 10):
    """
    Return recent commit history.
    """

    try:
        result = _run_git_command([
            "log",
            f"-{max_commits}",
            "--pretty=format:%H|%an|%ad|%s",
            "--date=short"
        ])

        if not result["success"]:
            return result

        commits = []

        if result["output"]:
            for line in result["output"].splitlines():
                commit_hash, author, date, message = line.split("|", 3)

                commits.append({
                    "hash": commit_hash,
                    "author": author,
                    "date": date,
                    "message": message
                })

        return {
            "success": True,
            "count": len(commits),
            "commits": commits
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }