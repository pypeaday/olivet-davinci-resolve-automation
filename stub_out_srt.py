# NEED TO REFACTOR FOR LYRICS FOLDER CHANGE AND ALSO TRACKING BETTER!!!

from argparse import ArgumentParser
from pathlib import Path

from ccli import Song, SongsRepository

things_to_strip = [
    "[Verse 1]",
    "[Verse 2]",
    "[Verse 3]",
    "[Verse 4]",
    "[Verse 5]",
    "[Chorus]",
    "[Bridge]",
]


def strip_it(s: str) -> str:
    for t in things_to_strip:
        # first try it with new line
        s = s.replace(f"{t}\n", "")
        # s = s.replace(t, "")
    return s


def make_sure_paths_exist(filepath: str):
    Path(filepath.replace("01-raw", "02-stubs")).mkdir(parents=True, exist_ok=True)
    Path(filepath.replace("01-raw", "03-manual-wip")).mkdir(parents=True, exist_ok=True)


def subtitles_exist(filepath: str, date: str) -> bool:

    name = Path(filepath).stem

    print(f"checking if {name} was already done")

    done_directory = Path("lyrics", "04-done")
    done_files = [str(x) for x in list(done_directory.glob(f"**/*{name}*"))]

    # Check if the filename for raw subtitles/lyrics for the given date is in a historical folder
    if any([name in x for x in done_files]):
        old_filepath = Path([x for x in done_files if name in Path(x).name][0])
        old_date = old_filepath.parent.name
        new_filepath = Path(f"./lyrics/04-done/{date}/{Path(filepath).name}")

        # write to a log where the stubbed srt file would otherwise be as a hint to me
        Path(f"./lyrics/02-stubs/{date}/{name}.log").write_text(
            f"{name} was already processed on {old_date}.\nThe completed subtitles will be copied to {new_filepath} for convenience of importing and organizing in DaVinci"
        )
        print(f"Copying {str(old_filepath)} to {new_filepath}")
        new_filepath.write_text(old_filepath.read_text())
        return True

    return False


def stub_it_out(filepath: str):

    frontmatter, msg = Path(filepath).read_text().split("---")

    new_msg = ""
    for i, group in enumerate(msg.split("\n\n")):
        group = strip_it(group)
        start_minutes = str((15 * i) // 60).zfill(2)
        end_minutes = str((15 * (i + 1)) // 60).zfill(2)
        start_seconds = str((15 * i) % 60).zfill(2)
        end_seconds = str((15 * (i + 1)) % 60).zfill(2)
        start_time = f"00:{start_minutes}:{start_seconds},000"
        end_time = f"00:{end_minutes}:{end_seconds},000"
        srt_timecode = f"{start_time} --> {end_time}"
        new_msg += f"{i+1}\n{srt_timecode}\n{group}\n\n"
        # print(f"{new_msg}")
    return new_msg


if __name__ == "__main__":
    parser = ArgumentParser("Olivet automation for DaVinci workflow")

    # assuming that if I have a CCLI number that the song has been done before
    songs = SongsRepository()

    song: Song
    for song in songs.songs:
        if song.stubbed_lyrics_exist:
            continue
        if not song.raw_lyrics_file.exists():
            print(
                f"*** {song.song} has entry in ccli.txt but no lyric stubs reported here!"
            )
            breakpoint()
            continue
        filepath = str(song.raw_lyrics_file)
        new_msg = stub_it_out(f"{filepath}")

        Path(filepath.replace("01-raw", "02-stubs")).write_text(new_msg)
