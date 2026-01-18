def apply_moves(groups, base_path):
    for directory, files in groups.items():
        full_path = base_path / directory
        full_path.mkdir(parents=True,exist_ok=True)
        for src in files:
            dst = full_path / src.name
            if dst.exists():
                continue
            src.rename(dst)


