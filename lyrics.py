import json
import requests

from pathlib import Path

import logging

from urllib3.util import parse_url

logger = logging.getLogger(__name__)

fh = logging.StreamHandler()

logger.addHandler(fh)


def extract_lyrics(artist: str, song: str):
    # link = 'https://api.lyrics.ovh/v1/'+artist+'/'+song
    link = 'https://api.lyrics.ovh/v1/'+artist+'/'+song

    req = requests.get(parse_url(link))
    json_data = json.loads(req.content)

    try:
        lyrics = json_data['lyrics']

        # exec("print(lyrics)")
        Path(f"{artist}_{song}.lyrics").write_text(lyrics)
            
        logger.info('Lyrics printed', 
            f'The lyrics to the song you wanted have been extracted, and have been printed on your command terminal.')
    except Exception:
        logger.error('No such song found', 'We were unable to find such a song in our directory. Please recheck the name of the artist and the song, and if it correct, we apologize because we do not have that song available with us.')
