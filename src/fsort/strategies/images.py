class ImagesStrategy:
    group_name = "Images"
    def accepts(self,file) -> bool:
        ImagesList = [".jpg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".heif"]
        return file.suffix in ImagesList
