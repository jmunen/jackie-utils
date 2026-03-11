from pathlib import Path


def list_files(directory: str):
    """Return file paths for files directly inside a directory."""
    path = Path(directory)

    if not path.exists():
        raise FileNotFoundError(f"File {directory} does not exist")

    if not path.is_dir():
        raise NotADirectoryError(f" {directory} does not exist in directory")

    return [str(p) for p in path.iterdir() if p.is_file()]