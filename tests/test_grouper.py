import pytest
from fsort import grouper

def test_grouper(tmp_path):
    directory = tmp_path / "test"
    directory.mkdir(parents=True, exist_ok = True)
    f1 = directory / "f1.jpg"
    f1.touch()
    f2 = directory / "f2.docx"
    f2.touch()
    f3 = directory / "f3.mp3"
    f3.touch()
    f4 = directory / "f4.mp4"
    f4.touch()
    f5 = directory / "f5.tar.gz"
    f5.touch()
    f6 = directory / "f6.bin"
    f6.touch()

    files = []
    for i in directory.iterdir():
        files.append(i)

    g_f = grouper.group_files(files)
    assert f1 in g_f["Images"]
    assert f2 in g_f["Docs"]
    assert f3 in g_f["Audio"]
    assert f4 in g_f["Video"]
    assert f5 in g_f["Archive"]
    assert f6 in g_f["Others"]




