from pathlib import Path


WORKSPACE = Path("workspace").resolve()


def _resolve_workspace_path(relative_path: str = "") -> Path:
    """
    Resolve path within workspace and prevent path traversal.
    """

    path = (WORKSPACE / relative_path).resolve()

    if not str(path).startswith(str(WORKSPACE)):
        raise PermissionError("Access denied")

    return path


def search_code(
    query: str,
    directory: str = "",
    file_pattern: str | None = None,
    max_results: int = 20
):
    """
    Search for text within files inside workspace.

    Args:
        query: Text to search for.
        directory: Subdirectory inside workspace.
        file_pattern: Optional file extension filter (e.g. ".py")
        max_results: Maximum matches returned.
    """

    try:
        search_root = _resolve_workspace_path(directory)

        if not search_root.exists():
            return {
                "success": False,
                "error": f"Directory '{directory}' does not exist"
            }

        if not search_root.is_dir():
            return {
                "success": False,
                "error": f"'{directory}' is not a directory"
            }

        results = []

        for file_path in search_root.rglob("*"):

            if not file_path.is_file():
                continue

            if file_pattern and file_path.suffix != file_pattern:
                continue

            try:
                lines = file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines()

                for line_number, line in enumerate(lines, start=1):

                    if query.lower() in line.lower():

                        relative_path = str(
                            file_path.relative_to(WORKSPACE)
                        )

                        results.append({
                            "file": relative_path,
                            "line_number": line_number,
                            "match": line.strip()
                        })

                        if len(results) >= max_results:
                            return {
                                "success": True,
                                "query": query,
                                "count": len(results),
                                "results": results
                            }

            except Exception:
                continue

        return {
            "success": True,
            "query": query,
            "count": len(results),
            "results": results
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }