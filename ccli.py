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
        )

        self.stubbed_lyrics_exist = Path(f"./lyrics/02-stubs/{self.slug}").exists()

        # if not self.raw_lyrics_exist and self.old_raw_file.exists():
        #     # print(f"Migrating {self._song} raw and stub to new naming convention")
        #     # self.__migrate_lyric_file()
        #     print(f"Frontmattering {self._song} raw and stub to new naming convention")
        #     self.__frontmatter()
        # else:
        #     breakpoint()
        #     print(f"********{self.song} wasn't migrated")

    # def __frontmatter(self):
    # frontmatter = f"""
    # name: {self.song}
    # ccli: {self.ccli}
    # artist: {self.artist}
    # ---
    # """
    # new_text = frontmatter + self.old_raw_file.read_text()
    # self.raw_lyrics_file.write_text(new_text)

    # def __migrate_lyric_file(self):
    #     breakpoint("why is this happening")
    #     self.old_raw_file.rename(f"./lyrics/01-raw/{self.slug}")
    #     old_stub_file = Path(f"./lyrics/02-stubs/{self.song}")
    #     if old_stub_file.exists():
    #         old_stub_file.rename(f"./lyrics/02-stubs/{self.slug}")

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

    def add_song(self, song: str, artist: str, ccli_number: str):
        self.songs.append(Song("\n".join([song, artist, ccli_number])))
