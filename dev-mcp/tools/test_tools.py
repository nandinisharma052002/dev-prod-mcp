from pathlib import Path
import subprocess


REPO_ROOT = Path.cwd()


def _run_command(command: list[str]):
    """
    Execute a command and return structured output.
    """

    try:
        result = subprocess.run(
            command,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=120
        )

        return {
            "success": True,
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Command timed out"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def run_pytest():
    """
    Run the entire pytest suite.
    """

    try:
        result = _run_command([
            "pytest",
            "-v"
        ])

        if not result["success"]:
            return result

        return {
            "success": True,
            "passed": result["return_code"] == 0,
            "return_code": result["return_code"],
            "output": result["stdout"],
            "errors": result["stderr"]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def run_single_test(test_path: str):
    """
    Run a specific pytest test file or test function.

    Examples:
        tests/test_file_tools.py
        tests/test_file_tools.py::test_read_file
    """

    try:
        result = _run_command([
            "pytest",
            test_path,
            "-v"
        ])

        if not result["success"]:
            return result

        return {
            "success": True,
            "test": test_path,
            "passed": result["return_code"] == 0,
            "return_code": result["return_code"],
            "output": result["stdout"],
            "errors": result["stderr"]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }