class AudioStrategy:
    group_name = "Audio"
    def accepts(self, file) -> bool:
        AudioList = [".mp3",".wav",".flac",".aac",".ogg",".m4a",".wma",".aiff",".opus"]
        return file.suffix in AudioList
