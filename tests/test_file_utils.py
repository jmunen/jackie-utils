import pytest
from pathlib import Path
from jackie_utils.file_utils import list_files

def test_list_files(tmp_path: Path):
    (tmp_path / "a.txt").write_text("hello")
    (tmp_path / "b.txt").write_text("world")
    (tmp_path / "subdir").mkdir()

    files = sorted(list_files(str(tmp_path)))

    assert len(files) == 2
    assert files[0].endswith("a.txt")
    assert files[1].endswith("b.txt")

def test_list_files_missing_dir():
    with pytest.raises(FileNotFoundError):
        list_files("does-not-exist")