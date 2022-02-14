import requests
from bs4 import BeautifulSoup
import connections
import spotify_api as api

user_date = input("Enter a date in the last 20 years to get a the Billboard top 100 songs added to a spotify playlist."
                  "Please use the format - YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url=f"{URL}/{user_date}")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
song_names = [song.getText().strip("\n") for song in soup.select("li h3")]
with open(file="song_names", mode="w") as song_file:
    for name in song_names[0:100]:
        song_file.write(f"{name}\n")
connections.load_spotipy()
spotify_list = []
for song in song_names[0:100]:
    song_uri = connections.search_for_song(song, user_date)
    spotify_list.append(song_uri)
number_of_songs = len(spotify_list)
name = f"{user_date} Billboard top 100"
description = "automatically created via python api"
playlist_id = connections.create_playlist(name, description)
for item in spotify_list:
    if item == "None":
        pass
    else:
        connections.add_track(playlist_id=playlist_id, track=item)

