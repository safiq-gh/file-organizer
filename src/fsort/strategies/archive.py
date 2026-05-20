class ArchiveStrategy:
    group_name = "Archive"
    def accepts(self, file) -> bool:
        ArchiveList = [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".iso", ".xz"]
        return file.suffix in ArchiveList
