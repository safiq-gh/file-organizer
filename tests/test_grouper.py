import pytest
from fsort import grouper

def test_grouper(tmp_path):
    directory = tmp_path / "test"
    directory.mkdir(parents=True, exist_ok = True)
    f1 = directory / "f1.jpg"
    f1.touch()
    f2 = directory / "f2.docx"
    f2.touch()
    f3 = directory / "f3.tar.gz"
    f3.touch()

    files = []
    for i in directory.iterdir():
        files.append(i)

    g_f = grouper.group_files(files)
    assert f1 in g_f["Images"]
    assert f2 in g_f["Docs"]
    assert f3 in g_f["Others"]




