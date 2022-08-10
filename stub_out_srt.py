from pathlib import Path

things_to_strip = [
    '[Verse 1]',
    '[Verse 2]',
    '[Verse 3]',
    '[Verse 4]',
    '[Verse 5]',
    '[Chorus]',
    '[Bridge]',
]


def strip_it(s: str) -> str:
    for t in things_to_strip:
        s = s.replace(t, '')
    return s


def stub_it_out(filepath: str):

    msg = Path(filepath).read_text()

    new_msg = ""
    for i, group in enumerate(msg.split("\n\n")):
        start_time = f"00:00:{5*(i)},000"
        end_time = f"00:00:{5*(i+1)},000"
        srt_timecode = f"{start_time} --> {end_time}"
        new_msg += f"{i} \n{srt_timecode} \n{group} \n\n"
        # print(f"{new_msg}")
    Path(filepath.replace("raw-lyrics", "song-subtitles")).write_text(new_msg)

if __name__ == "__main__":
    stub_it_out("./raw-lyrics/lord-i-need-you.srt")
    

# 22
# 00:05:35,291 --> 00:05:45,291