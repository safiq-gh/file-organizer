import os

def scan_directory(path):
    files = []
    for fildir in os.listdir(path):
        full_path = os.path.join(path, fildir)
        if os.path.isfile(full_path) and fildir not in ["organizer.py", "fsort.py"] and not fildir.startswith("."):
            files.append(full_path)
    return files

