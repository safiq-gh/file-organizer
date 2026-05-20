class DocsStrategy:
    group_name = "Docs"
    def accepts(self,file) -> bool:
        DocsList = [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".odt", ".csv", ".rtf"]
        return file.suffix in DocsList
