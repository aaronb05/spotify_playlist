
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
URL = "https://api.spotify.com/v1"
client_id = os.getenv("client_id")
secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")


def load_spotipy():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=secret,
            show_dialog=True,
            cache_path="token.txt"
        )

    )
    user_id = sp.current_user()["id"]
    return user_id


def search_for_song(song_name, year):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    try:
        date = year.split("-")[0]
        song = sp.search(q=f"track:{song_name}, year:{date}", type="track")
        return song['tracks']['items'][0]['uri']
    except IndexError:
        pass
    else:
        pass


def create_playlist(name, description):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(name=name, public=False, description=description, user=user_id)
    playlist_id = playlist['id']
    return playlist_id


def add_track(playlist_id, track):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    try:
        new_track = [track]
        add = sp.playlist_add_items(playlist_id=playlist_id, items=new_track)
        print(add)
    except AttributeError:
        pass
    else:
        pass



