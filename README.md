# Automating Olive Bible Music & Slides production

## Workflow

1. Paste raw song lyrics into `./lyrics/{date}/{songname}.srt`
    * Lyric format doesn't super matter but having new lines in between what I think slides should be makes it easier in DaVinci
    * Name needs to be what I name the subtitle track in DaVinci - I'm using a Title case schema
2. Run python `stub_out_srt.py` which will create stubbed out subtitle files and will save each one to `./lyrics/02-stubs/{date}/{songname}.srt`
    * This script should check if the file with that name exists in `./lyrics/04-done` and if so alert me so that I don't redo work
3. The python script will also copy the stubbed srt file into `./lyrics/03-manual-wip/{date}/{songname}.srt` and this is what can be loaded into DaVinci and overwritten etc.
3. In DaVinci:
    * Some setup notes:
        * I created bins in the `Olivet Bible Church` project: 
            * `Initial Subtitles` for starting point files out of python script
            * `Individual Timelines` for putting per-song timelines in
            * `Songs` for the initial songs
            * `Completed Subtitles` for re-importing subtitles after matching up from the initial files
            * `Rendered Songs` for re-importing the rendered mp4 files that are song/lyrics/background
        * Naming schemes:
            * Prefix timelines with `TL - `
            * Prefix combined songs with `CTL - ` for "Combined Timeline"
    * Import all full songs, instrumentals, lyric files
    * For each song make a timeline out of the full song, the instrumental, and the lyric file
    * **Set the instrumental track as the first one so it plays by default**
    * **Make sure the timeline starts at 0 seconds...default is an hour for some reason - this messes up the exported subtitle files**
4. Tune in DaVinci then export subtitles to `./lyrics/04-done/{songname}.srt` (I don't think keeping dates in the done folder matters...)
5. Render each timeline/song and save to `./rendered-songs` as `{songname}.mp4`

6. Use mp4 files from step 5 to combine songs if necessary

## Workflow for reusing rendered song/lyric videos but changing background

1. Find the date it was done by looking for the srt file in `./lyrics-01-raw`
2. The timeline for that song should be in the DaVinci project in the `Individual Timelines` bin 
3. Create a duplicate timeline and change background
4. Save timeline with `BG - {N}` where `N` is the nth iteration of backgrounds for a given song
4. Re-render

## Subtitle settings

> TODO: Figure out setting these as deafult track style for subtitles

font: CMG Sans
size: 65
line spacing: 25
kerning: -5 to 10 depending on slide layout
alignment: center
y: 540



# Automation ideas

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