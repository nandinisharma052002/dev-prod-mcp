from pathlib import Path
from pydantic import BaseModel, Field


# =========================
# Workspace Configuration
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

WORKSPACE = BASE_DIR / "workspace"

# =========================
# Request Models
# =========================

class ReadFileRequest(BaseModel):
    path: str = Field(min_length=1)


class WriteFileRequest(BaseModel):
    path: str = Field(min_length=1)
    content: str


class ListFilesRequest(BaseModel):
    directory: str = ""


# =========================
# Helper Functions
# =========================

def _resolve_workspace_path(relative_path: str) -> Path:
    """
    Resolves a path inside the workspace and prevents path traversal.
    """
    path = (WORKSPACE / relative_path).resolve()

    if not str(path).startswith(str(WORKSPACE)):
        raise PermissionError("Access denied")

    return path


# =========================
# Tools
# =========================

def read_file(path: str):
    """
    Read a file from the workspace.
    """

    try:
        request = ReadFileRequest(path=path)

        file_path = _resolve_workspace_path(request.path)

        if not file_path.exists():
            return {
                "success": False,
                "error": f"File '{request.path}' does not exist"
            }

        if not file_path.is_file():
            return {
                "success": False,
                "error": f"'{request.path}' is not a file"
            }

        content = file_path.read_text(encoding="utf-8")

        return {
            "success": True,
            "path": request.path,
            "content": content
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def write_file(path: str, content: str):
    """
    Create or overwrite a file inside the workspace.
    """

    try:
        request = WriteFileRequest(
            path=path,
            content=content
        )

        file_path = _resolve_workspace_path(request.path)

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path.write_text(
            request.content,
            encoding="utf-8"
        )

        return {
            "success": True,
            "path": request.path,
            "bytes_written": len(
                request.content.encode("utf-8")
            )
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def list_files(directory: str = ""):
    """
    List files and directories inside workspace.
    """

    try:
        request = ListFilesRequest(
            directory=directory
        )

        dir_path = _resolve_workspace_path(
            request.directory
        )

        if not dir_path.exists():
            return {
                "success": False,
                "error": f"Directory '{request.directory}' does not exist"
            }

        if not dir_path.is_dir():
            return {
                "success": False,
                "error": f"'{request.directory}' is not a directory"
            }

        entries = []

        for item in dir_path.iterdir():
            entries.append({
                "name": item.name,
                "type": "directory" if item.is_dir() else "file"
            })

        return {
            "success": True,
            "directory": request.directory,
            "entries": entries
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }