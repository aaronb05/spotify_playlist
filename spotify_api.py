import os
import requests
from dotenv import load_dotenv


load_dotenv()
URL = "https://api.spotify.com/v1"
client_id = os.getenv("client_id")
secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")


def authorize():
    params = {
                "client_id": client_id,
                "client_secret": secret,
                "redirect_uri": redirect_uri,
            }
    get = requests.get(url=f"https://api.spotify.com/v1/authorize", params=params)
    print(get.text)
    result = get.json()
    print(result)





