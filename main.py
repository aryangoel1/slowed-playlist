#!/usr/bin/env python3
"""
Main script that demonstrates the functionality of the slowed playlist generator.
Contains all the executable code that was originally in test.ipynb.
"""

import pprint
from functions import get_playlist_tracks, ids_slowed_version, create_playlist, add_songs


def main():
    
    # Crack playlist ID: 3xWx987zAhFtL1r5kPhtpr
    crack = get_playlist_tracks("3xWx987zAhFtL1r5kPhtpr")
    
    # Get YouTube video IDs for slowed versions
    print("Getting YouTube video IDs for slowed versions ...")
    video_ids = ids_slowed_version(crack)
    print("Video IDs:")
    pprint.pprint(video_ids)
    print()
    
    # Create playlist
    print("Creating playlist...")
    playlist_result = create_playlist(title="Crack (Slowed)")
    print("Created playlist:")
    
    # Add songs to the playlist
    print("Adding songs to the playlist...")
    playlist_id = playlist_result['id']
    
    for video_id in video_ids:
        try:
            add_songs(videoId=video_id, playlistId=playlist_id)
            print(f"Added video {video_id} to playlist")
        except Exception as e:
            print(f"Error adding video {video_id}: {e}")
    
    print("Process completed!")


if __name__ == "__main__":
    main()
