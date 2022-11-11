from pathlib import Path


class Song:
    def __init__(self, raw_lyrics_file: Path):

        self.raw_lyrics_file = raw_lyrics_file
        self.frontmatter, self.lyrics = raw_lyrics_file.read_text().split("---")

        self.__set_attributes()

    def __set_attributes(self):

        info = {
            e.strip().split(":")[0]: e.strip().split(":")[1]
            for e in self.frontmatter.split("\n")
            if e.strip() != ""
        }
        # info = dict()
        # for _e in self.frontmatter.split("\n"):
        #     e = _e.strip()
        #     if e == "":
        #         continue
        #     else:
        #         try:
        #             k, v = e.split(":")
        #             info[k] = v
        #         except ValueError:
        #             breakpoint()
        try:
            self.song = info["name"].strip()
        except KeyError:
            breakpoint()
        self.artist = info["artist"].strip()
        self.ccli = info["ccli"].strip()
        self.slug = (
            f"{self.song}.{self.artist}.{self.ccli}".lower()
            .replace(" ", "-")
            .replace('"', "")
            .replace("'", "")
            .replace(",", "")
        )

        self.stubbed_lyrics_file = Path(f"./lyrics/02-stubs/{self.slug}")
        self.stubbed_lyrics_exist = self.stubbed_lyrics_file.exists()

    def __repr__(self):
        import json

        return json.dumps({k: str(v) for k, v in self.__dict__.items()})

    def __str__(self):
        return self.__repr__()


class SongsRepository:
    def __init__(self):
        self.songs = [Song(f) for f in Path("./lyrics/01-raw").glob("*")]

    def save(self):
        Path("./ccli2.txt").write_text("\n\n".join([str(song) for song in self.songs]))
