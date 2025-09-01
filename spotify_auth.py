import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")

scope = "user-library-read"

# Create an OAuth object --> gives us access to the Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, 
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))