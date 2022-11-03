# Automating Olive Bible Music & Slides production

## TODOs

<!-- 1. Track songs that are done better so that I don't have to make a raw lyric file to find out if I have already done the song -->
<!--     * I think naming with <song name>.<artist> in the raw folder would be good, maybe even with ccli number? -->
2. Look for ways to automate at least getting the lyrics - I can manually format the "raw lyrics" files for the stubbed out srt files
3. Database of songs, instrumentals, etc.
4. Database of songs with lyrics and backgrounds (or no background) which could hopefully be used with Presenter

`:set colorcolumn=35` will put the vertical bar at a nice spot for max width of a line

## Workflow

1. Paste raw song lyrics into `./lyrics/{songname}`
    * Break up lyrics with new lines where slide breaks should be 
    * Frontmatter (top of the file) 
        ```yaml 
        name: SONG NAME
        artist: ARTIST
        ccli: # CCLI NUMBER
        ---
        ```
2. Run python `stub_out_srt.py` which will create stubbed out subtitle files and will save each one to `./lyrics/02-stubs/{song-name}.{artist}.{ccli}`
3. In DaVinci:
    * Some setup notes:
        * I created bins in the `Olivet Bible Church` project: 
            * `Backgrounds` for backgrounds that are used
            * `Initial Subtitles` for starting point files out of python script
            * `Individual Timelines` for putting per-song timelines in
            * `Songs` for the initial songs
            * `Completed Subtitles` for re-importing subtitles after matching up from the initial files
            * `Rendered Songs` for re-importing the rendered mp4 files that are song/lyrics/background
            * `Combined Timelines` for putting rendered songs in for meshing them together
        * Naming schemes:
            * Prefix timelines with `TL - `
            * Prefix combined songs with `CTL - ` for "Combined Timeline"
    * Import all full songs, instrumentals, lyric files
    * For each song make a timeline out of the full song, the instrumental, and the lyric file
    * **2 audio tracks, 2 videos**
    * **Set the instrumental track as the first one so it plays by default**
    * **Make sure the timeline starts at 0 seconds...default is an hour for some reason - this messes up the exported subtitle files**
    * **WHEN RENDERING THE SONGS THE OTUPUT TRACK 1 NEEDS SET TO TIMELINE TRACK FOR EACH AUDIO TRACK FOR THEM TO BE SEPARATE OTHERWISE BUS 1 (STEREO) FOR COMBINING INTO ONE AUDIO TRACK**

4. Add licensing slide from `Edit` Tab then click `Effect` next to `Media Pool` and insert a slide -> I'm using Titles: Right Lower Third then putting the information in the Rich Text section of the slide.
    * CMG Sans
    * Size 40
    * Align right
5. Tune in DaVinci then export subtitles as `{songname}.srt` 
6. Render each timeline/song and save to `./rendered-songs` as `{songname}.mp4`
    * Audio -> Out Track 1 -> set to Bus 1 (Stereo) to combine the tracks... but to All Timeline Tracks for separate tracks... feels backwards to me

7. Use mp4 files from step 5 to combine songs if necessary
    * Import mp4 files into `Rendered Songs` bin
    * Create timeline with songs to combine
    * **Might need to import the instrumental tracks again? I don't know why but I can just bring them into the timeline as the first audio track no problem**
    * **Overlap the songs for transistion to make the music and background flow nice - then in `Deliever` when it's time to render change the Audio settings for `Output Track 1` as `All Timeline Tracks` which will combine them into one for Presenter**

8. Upload rendered media as well as subtitle files to Olivet Bible space in Nextcloud
9. Upload to [presenter](https://auth.worshiptools.com/login)

## Workflow for reusing rendered song/lyric videos but changing background

1. Find the date it was done by looking for the srt file in `./lyrics-01-raw`
2. The timeline for that song should be in the DaVinci project in the `Individual Timelines` bin 
3. Create a duplicate timeline and change background
4. Save timeline with `BG - {N}` where `N` is the nth iteration of backgrounds for a given song
4. Re-render

## Subtitle settings

> TODO: Figure out setting these as deafult track style for subtitles

font: CMG Sans
size: 88
line spacing: 25
kerning: -5 to 10 depending on slide layout
alignment: center
y: 540



# Automation ideas

## Getting lyrics
1. Index all song files
2. Get details of those files which should have artist and song name - maybe something with `os`?
3. Get all lyrics to just text files to be used for probably manually created srt

## Getting Lyrics 2
1. api.lyrics.ovh doesn't make it easy to get Christian/worship stuff so hand copying from genius seems ok
2. I can probably use the genius api...

## SRT files
0. Decide on standard format - 2 or 4 lines per slide?
1. Set vim config for max length of line
2. Make rough draft srt files manually PER SONG
3. Load multiple files and they _should_ match multiple songs as long as I start the subtitle at the right spot
4. When rendering a service the subtitles can be exported as one separate file, but not multiple files per track - that's one reason to make srt files per song first
4b. Actually looks like I can only export a fle _or_ embed in video, and for formatting for subtitles to look big in the center then it needs to be embedded... not a big deal if we have srt files per song

## NOTES

1. pysrt can probably be used to shift subtitles in srt if they're off when imported into Davinci
