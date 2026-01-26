class Scanner:
    def __init__(self, recursive=False):
        self.recursive = recursive

    def scan_directory(self, path):
        files = self._scan_directory_recursive(path)
        return files

    def _scan_directory_recursive(self, path):
        files = []
        for fildir in path.iterdir():
            if fildir.is_file() and fildir.name not in ["organizer.py", "fsort.py"] and not fildir.name.startswith("."):
                files.append(fildir)

            if self.recursive and fildir.is_dir() and fildir.name not in ["Images", "Docs", "Others"] and not fildir.name.startswith("."):
                files.extend(self._scan_directory_recursive(fildir))
        return files



def scan_directory(path, recursive=False):
    scanner = Scanner(recursive=recursive)
    return scanner.scan_directory(path)
