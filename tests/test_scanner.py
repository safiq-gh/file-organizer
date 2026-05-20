from fsort import scanner

def test_scanner_non_recursive(tmp_path):
    rdir = tmp_path / "test"
    rdir.mkdir(parents=True, exist_ok = True)
    f1 = rdir / "a.txt"
    f1.touch()
    sub_dir = rdir / "sub_test"
    sub_dir.mkdir(parents=True, exist_ok=True)
    f2 = sub_dir / "b.txt"
    f2.touch()

    test = scanner.scan_directory(rdir, recursive = False)
    assert f1 in test
    assert f2 not in test

def test_scanner_recursive(tmp_path):
    rdir = tmp_path / "test"
    rdir.mkdir(parents=True, exist_ok = True)
    f1 = rdir / "a.txt"
    f1.touch()
    sub_dir = rdir / "sub_test"
    sub_dir.mkdir(parents=True, exist_ok=True)
    f2 = sub_dir / "b.txt"
    f2.touch()

    test = scanner.scan_directory(rdir, recursive = True)
    assert f1 in test
    assert f2 in test

def test_scanner_recursive_excludes_forbidden_dirs(tmp_path):

    rdir = tmp_path / "test"

    Imgdir = rdir / "Images"
    Docdir = rdir / "Docs"
    Othdir = rdir / "Others"
    Hiddir = rdir / ".Cred"
    smpldir = rdir / "smpl"
    

    rdir.mkdir(parents=True, exist_ok=True)
    Imgdir.mkdir(parents=True, exist_ok=True)
    Docdir.mkdir(parents=True, exist_ok=True)
    Othdir.mkdir(parents=True, exist_ok=True)
    Hiddir.mkdir(parents=True, exist_ok=True)
    smpldir.mkdir(parents=True, exist_ok=True)

    Img1 = Imgdir / "T1.jpg"
    Doc1 = Docdir / "T1.docx"
    Oth1 = Othdir / "T1.txt"
    Hid1 = Hiddir / ".hidd"
    Smp1 = smpldir / "sample.gif"

    Img1.touch()
    Doc1.touch()
    Oth1.touch()
    Hid1.touch()
    Smp1.touch()

    test = scanner.scan_directory(rdir, recursive = True)

    # Allowed files included
    assert Smp1 in test
    # Forbidden files excluded
    assert Img1 not in test
    assert Doc1 not in test 
    assert Oth1 not in test
    assert Hid1 not in test
