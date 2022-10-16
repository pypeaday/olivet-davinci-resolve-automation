from pathlib import Path


class Song:
    def __init__(self, entry: str):
        self._entry = entry.split("\n")
        self._entry = [x for x in self._entry if x != ""]

        self._song = self._entry[0]
        self._artist = self._entry[1]
        self._ccli = self._entry[2]
        self.song = self._song.replace('"', "")
        self.artist = self._artist
        self.ccli = self._ccli.replace("#", "").replace("-", "").replace(" ", "")
        self.slug = (
            f"{self.song}.{self.artist}.{self.ccli}".lower()
            .replace(" ", "-")
            .replace('"', "")
        )

        self.raw_lyrics_exist = Path(f"./lyrics/01-raw/{self.slug}").exists()
        self.stubbed_lyrics_exist = Path(f"./lyrics/02-stubs/{self.slug}").exists()

        self.old_raw_file = Path(f"./lyrics/01-raw/{self.song}")

        if not self.raw_lyrics_exist and self.old_raw_file.exists():
            print(f"Migrating {self._song} raw and stub to new naming convention")
            self.__migrate_lyric_file()

    def __migrate_lyric_file(self):
        breakpoint("why is this happening")
        self.old_raw_file.rename(f"./lyrics/01-raw/{self.slug}")
        old_stub_file = Path(f"./lyrics/02-stubs/{self.song}")
        if old_stub_file.exists():
            old_stub_file.rename(f"./lyrics/02-stubs/{self.slug}")

    def __repr__(self):
        import json

        return json.dumps({k: str(v) for k, v in self.__dict__.items()})

    def __str__(self):
        return self.__repr__()


class SongsRepository:
    def __init__(self):
        self.songs = [
            Song(song) for song in Path("./ccli.txt").read_text().split("\n\n")
        ]

    def save(self):
        Path("./ccli.txt").write_text("\n\n".join([str(song) for song in self.songs]))

    def add_song(self, song: str, artist: str, ccli_number: str):
        self.songs.append(Song("\n".join([song, artist, ccli_number])))
