import spotify_auth
import youtube_auth


def get_playlist_tracks(playlist_id):
    """Put the names of the songs in our playlist into an array"""
    names = []

    results = spotify_auth.sp.playlist(playlist_id)
    
    tracks = results['tracks']['items']
    
    for item in tracks:
        names.append(item['track']['name'])
    
    return names


def search_song(query):
    """Search for a song on YouTube and return the result"""
    result = youtube_auth.youtube.search().list(part="snippet", q=query, type="video", maxResults=1).execute()
    # result['items'][0]['snippet']['title'] --> title of song
    return result


def ids_slowed_version(spotify_playlist):
    """Return an array of youtube-video ids of slowed-reverb version of songs"""
    slowed_version = []
    for song in spotify_playlist:
        slowed_version.append(search_song(song + " Slowed Reverb"))

    ids = [video['items'][0]['id']['videoId'] for video in slowed_version]
    
    return ids


def create_playlist(title, description=None, privacyStatus='private', defaultLanguage=None):
    """Creates a playlist for you"""
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
    return youtube_auth.youtube.playlists().insert(part="snippet,status", body=snippet_body).execute()


def add_songs(videoId, playlistId):
    """Add songs to a YouTube playlist"""
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
    return youtube_auth.youtube.playlistItems().insert(part="snippet", body=snippet_body).execute()
