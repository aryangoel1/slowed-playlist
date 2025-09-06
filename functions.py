import spotify_auth
import youtube_auth
import json
import os 
youtube_quota = 0 

def get_playlist_tracks(playlist_id):
    """Put the names of the songs in our playlist into an array"""
    names = []

    results = spotify_auth.sp.playlist(playlist_id)
    
    tracks = results['tracks']['items']
    
    for item in tracks:
        names.append(item['track']['name'])
    
    return names

def get_youtube_quota():
    return youtube_quota

def search_song(query):
    """Search for a song on YouTube and return the result"""
    global youtube_quota
    try:
        result = youtube_auth.youtube.search().list(part="snippet", q=query, type="video", maxResults=1).execute()
        save_search_result(query, result)
        youtube_quota += 100
        return result
    except Exception as e:
        youtube_quota += 100
        raise e 
    
def save_search_result(query, result):
    file_path = 'saved_songs.json'
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"searches": []}
    
    # Add new search result (no timestamp)
    new_entry = {
        "query": query,
        "video_id": result['items'][0]['id']['videoId'],
        "title": result['items'][0]['snippet']['title']
    }
    data["searches"].append(new_entry)
    
    # Write everything back
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
        
def ids_slowed_version(spotify_playlist):
    """Return an array of youtube-video ids of slowed-reverb version of songs"""
    slowed_version = [] # Add video data of the slowed_version of songs in an array 
    for song in spotify_playlist[:50]:
        slowed_version.append(search_song(song + " Slowed Reverb"))

    ids = [video['items'][0]['id']['videoId'] for video in slowed_version]
    
    return ids

def ids_slowed_version(spotify_playlist):
    # Modified
    # Check if the ID already exists inside of the JSON File 
    


def create_playlist(title, description=None, privacyStatus='private', defaultLanguage=None):
    """Creates a playlist for you"""
    global youtube_quota
    snippet_body = {
        'snippet': {
            'title': title,
            'description': description,
            'defaultLanguage': defaultLanguage
        },
        'status': {
            'privacyStatus': privacyStatus
        }
    }
    try:
        result = youtube_auth.youtube.playlists().insert(part="snippet,status", body=snippet_body).execute()
        youtube_quota += 50
        return result
    except Exception as e:
        youtube_quota += 50  # Still count quota even if it failed
        raise e  # Re-raise the error so caller knows it faile

def add_songs(videoId, playlistId):
    """Add songs to a YouTube playlist"""
    global youtube_quota
    snippet_body = {
        "snippet": {
            "playlistId": playlistId,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": videoId
            }
        }
    }
    # This makes a POST request to the YouTube API
    
    try: 
        result = youtube_auth.youtube.playlistItems().insert(part="snippet", body=snippet_body).execute()
        youtube_quota += 50 
        return result 
    except Exception as e:
        youtube_quota += 50
        raise e 