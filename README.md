# Automating Olive Bible Music & Slides production

## Ideal workflow

1. Get song lyrics
2. Script or something to create SRT files
3. Load SRT files with Python API into Davinci
4. Manually verify
5. Render

### Getting lyrics
1. Index all song files
2. Get details of those files which should have artist and song name - maybe something with `os`?
3. Get all lyrics to just text files to be used for probably manually created srt

### Getting Lyrics 2
1. api.lyrics.ovh doesn't make it easy to get Christian/worship stuff so hand copying from genius seems ok
2. I can probably use the genius api...

## SRT files
0. Decide on standard format - 2 or 4 lines per slide?
1. Set vim config for max length of line
2. Make rough draft srt files manually PER SONG
3. Load multiple files and they _should_ match multiple songs as long as I start the subtitle at the right spot
4. When rendering a service the subtitles can be exported as one separate file, but not multiple files per track - that's one reason to make srt files per song first
4b. Actually looks like I can only export a fle _or_ embed in video, and for formatting for subtitles to look big in the center then it needs to be embedded... not a big deal if we have srt files per song

## TODOs

1. Database of songs, instrumentals, etc.
2. Database of songs with lyrics and backgrounds (or no background) which could hopefully be used with Presenter

## NOTES

1. pysrt can probably be used to shift subtitles in srt if they're off when imported into Davinci