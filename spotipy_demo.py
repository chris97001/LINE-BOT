import json
import random
import string
import difflib
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv
import os

load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID", None)
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", None)

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))

# text = '鞋子特大號V ((((Live)'
# text = re.sub(r'Version|Ver|ver|Live|[\(\)\ ]', '', text)
# print(text)


# results = sp.search(q='genre:k-pop-girl-group',limit=1,offset=999)
# print(results['tracks']['total'])
# print([d['name'] for d in results['tracks']['items']])

s1 = "lifes too short".lower()
s2 = "Life's too short(English Version)".lower()

s1 = re.sub(r'Version|Ver|ver|Live|[\(\)\ \']', '', s1)
s2 = re.sub(r'Version|Ver|ver|Live|[\(\)\ \']', '', s2)

seq = difflib.SequenceMatcher(None, s1, s2)
ratio = seq.ratio()
seq = seq.find_longest_match(0,len(s1),0,len(s2))
isAnswer = ratio>=0.8 or (ratio>=0.7 and seq.size == len(s1) and seq.b == 0)
print(ratio, seq)
print(seq.size)
print(isAnswer)

'''
results:
    tracks:
        href
        items:
            [0]:
                album:
                    album_type
                    artists
                    available_markets
                    external_urls
                    href
                    id
                    images:
                        [0]:
                            height  300
                            width   640
                            url     
                        [1] 
                            300
                            300
                        [2]
                            64
                            64
                    name
                    release_date
                    release_date_precision
                    total_tracks
                    type
                    uri
                artists:
                    [0]:
                        name
                    .
                    .
                available_markets
                disc_number
                duration_ms
                explicit
                external_ids
                external_urls:
                    spotify:
                        https:...
                href
                id
                is_local
                name
                popularity
                preview_url
                track_number
                type
                uri
            [1]
            .
            .
        limit
        next
        offset
        previous
        total
'''