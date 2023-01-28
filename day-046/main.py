import os
import time
import requests
from tqdm import tqdm
from pathlib import Path
from pprint import pprint
from spotipy import Spotify
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
from spotipy.oauth2 import SpotifyOAuth

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()
load_dotenv(DOTENV_PATH)


SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_SCOPE = "playlist-modify-private"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:9090"

date_input = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f'{BILLBOARD_URL}{date_input}')

soup = bs(response.text, "html.parser").find(name='div', class_='pmc-paywall')
classes = soup.select(
    "#title-of-a-story.c-title.u-letter-spacing-0021.a-font-primary-bold-s")
songs = [song.getText().strip()
         for song in tqdm(classes, desc="Getting top 100 songs...")]
song_uris = []


sp = Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
             client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope=SPOTIFY_SCOPE, show_dialog=True))


user_id = sp.current_user()["id"]
year = date_input.split("-")[0]

# songs = songs[:2]

for song in tqdm(songs, desc="Searching songs on Spotify..."):
    result = sp.search(q=f"track:{song} year:{year}",
                       type="track", market="US")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    time.sleep(2)


create_playlist = sp.user_playlist_create(
    user=user_id, name=f"{date_input} Billboard 100", public=False)
# pprint(create_playlist)
play_list_id = create_playlist["id"]
print(play_list_id)
print(create_playlist["external_urls"]["spotify"])

sp.user_playlist_add_tracks(
    user=user_id, playlist_id=play_list_id, tracks=song_uris)
