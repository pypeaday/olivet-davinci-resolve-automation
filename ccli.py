from pathlib import Path


class CCLI:
    def __init__(self, entry: str):
        self._entry = entry.split("\n")
        self.song = self._entry[0].replace('"', "")
        self.artist = self._entry[1]
        self.ccli = self._entry[2]

    def __repr__(self):
        return "\n".join(self._entry)

    def __str__(self):
        return self.__repr__()


class CCLIRepository:
    def __init__(self):
        self.songs = [
            CCLI(song) for song in Path("./ccli.txt").read_text().split("\n\n")
        ]

    def save(self):
        Path("./ccli.txt").write_text("\n\n".join([str(song) for song in self.songs]))

    def add_song(self, song: str, artist: str, ccli_number: str):
        self.songs.append(CCLI("\n".join([song, artist, ccli_number])))
