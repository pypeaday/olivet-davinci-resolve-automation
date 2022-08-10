from pathlib import Path
from argparse import ArgumentParser

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
    Path(filepath.replace("01-raw", "02-stubs")).mkdir(
        parents=True, exist_ok=True
    )
    Path(filepath.replace("01-raw", "03-manual-wip")).mkdir(
        parents=True, exist_ok=True
    )
    Path(filepath.replace("01-raw", "04-done")).mkdir(
        parents=True, exist_ok=True
    )


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

    msg = Path(filepath).read_text()

    new_msg = ""
    for i, group in enumerate(msg.split("\n\n")):
        group = strip_it(group)
        # todo: what if we go past 60 seconds
        start_seconds = str((5 * i)).zfill(2)
        end_seconds = str((5 * (i + 1))).zfill(2)
        start_time = f"00:00:{start_seconds},000"
        end_time = f"00:00:{end_seconds},000"
        srt_timecode = f"{start_time} --> {end_time}"
        new_msg += f"{i+1}\n{srt_timecode}\n{group}\n\n"
        # print(f"{new_msg}")
    Path(filepath.replace("01-raw", "02-stubs")).write_text(new_msg)
    return new_msg


if __name__ == "__main__":
    parser = ArgumentParser("Olivet automation for DaVinci workflow")
    parser.add_argument("--date", type=str, required=True)
    args = parser.parse_args()
    date = args.date
    raw_files_directory = f"./lyrics/01-raw/{date}"
    print("Don't forget to try and figure out how to check for songs already done BEFORE needing to copy lyrics into 01-raw/SONGNAME.srt")
    if not Path(raw_files_directory).exists():
        print(
            f"WARNING: {raw_files_directory} does not exist\nCheck your date syntax and folder name - it should follow YYYYMMDD format"
        )
        import sys

        sys.exit()

    else:
        files = list(Path(raw_files_directory).glob("**/*.srt"))

    make_sure_paths_exist(f"{raw_files_directory}")
    for f in files:
        filepath = str(f)

        if subtitles_exist(filepath, date):
            print(f"{f.name} already done")
            continue

        new_file = stub_it_out(f"{filepath}")

        # I think this wip directory is worthless since I'm not really iterating
        # on the file... I just make it right in DaVinci and export once
        manual_wip_file = Path(filepath.replace("01-raw", "03-manual-wip"))
        # if I haven't started working on it yet then stage the file for me to
        # start
        if not manual_wip_file.exists():
            manual_wip_file.write_text(new_file)
