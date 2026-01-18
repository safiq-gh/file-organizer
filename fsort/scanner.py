def scan_directory(path):
    files = []
    for fildir in path.iterdir():
        if fildir.is_file() and fildir.name not in ["organizer.py", "fsort.py"] and not fildir.name.startswith("."):
            files.append(fildir)
    return files

