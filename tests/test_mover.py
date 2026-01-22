from fsort import mover

def test_file_mover(tmp_path):

    root = tmp_path / "test"
    Img1 = root / "T1.jpg"
    Doc1 = root / "T2.txt"
    Oth1 = root / "T3.md"

    root.mkdir(parents=True, exist_ok=True)

    Img1.touch()
    Doc1.touch()
    Oth1.touch()

    groups = {"Images" : [Img1],
              "Docs" : [Doc1],
              "Others": [Oth1]}

    assert Img1.exists()
    assert Doc1.exists()
    assert Oth1.exists()
    
    mover.apply_moves(groups, root)
    
    Img = root / "Images" / "T1.jpg"
    Doc = root / "Docs" / "T2.txt"
    Oth = root / "Others" / "T3.md"

    assert Img.exists()
    assert Doc.exists()
    assert Oth.exists()

    assert not Img1.exists() 
    assert not Doc1.exists()
    assert not Oth1.exists()


