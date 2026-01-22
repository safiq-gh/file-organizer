def scan_directory(path, recursive=False):
    files = []
    if recursive:
        for fildir in path.iterdir():
            if fildir.is_file() and fildir.name not in ["organizer.py", "fsort.py", "README.md"] and not fildir.name.startswith("."):
                files.append(fildir)
            elif fildir.is_dir() and fildir.name not in ["Images", "Docs", "Others", "fsort"] and not fildir.name.startswith("."):
                files.extend(scan_directory(fildir, recursive=True))
    else:
        for fildir in path.iterdir():
            if fildir.is_file() and fildir.name not in ["organizer.py", "fsort.py", "README.md"] and not fildir.name.startswith("."):
                files.append(fildir)
    return files

