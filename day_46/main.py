import configparser

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

config = configparser.ConfigParser()
config.read("config.ini")
client_id = config["DEFAULT"]["key"]
client_secret = config["DEFAULT"]["news_api"]
display_name = config["DEFAULT"]["news_api"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=display_name,
    )
)

user_id = sp.current_user()["id"]
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False
)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
}

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(URL, headers=header)
the_list = []

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)
