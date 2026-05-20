class VideoStrategy:
    group_name = "Video"
    def accepts(self, file) -> bool:
        VideoList = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".mpeg", ".webm"]
        return file.suffix in VideoList
