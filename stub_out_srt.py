from pathlib import Path

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
    Path(filepath.replace("01-raw", "02-stubs")).parent.mkdir(
        parents=True, exist_ok=True
    )
    Path(filepath.replace("01-raw", "03-manual-wip")).parent.mkdir(
        parents=True, exist_ok=True
    )
    Path(filepath.replace("01-raw", "02-stubs")).write_text(new_msg)
    return new_msg


if __name__ == "__main__":
    date = "20220814"
    files = [
        "lord-i-need-you",
        "how-great-is-your-love",
        "psalm-45-fairest-of-all",
        "let-the-nations-be-glad",
    ]
    for f in files:
        filepath = f"./lyrics/01-raw/{date}/{f}.srt"
        new_file = stub_it_out(f"{filepath}")
        manual_wip_file = Path(filepath.replace("01-raw", "03-manual-wip"))
        # if I haven't started working on it yet then stage the file for me to
        # start
        if not manual_wip_file.exists():
            manual_wip_file.write_text(new_file)
