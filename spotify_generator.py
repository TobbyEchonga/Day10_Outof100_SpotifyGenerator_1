import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

def generate_playlist(sp, playlist_name, track_count=10):
    # Get the user's Spotify username
    user_info = sp.current_user()
    user_id = user_info['id']

    # Create a new playlist
    playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
    playlist_id = playlist['id']

    # Search for random tracks and add them to the playlist
    for _ in range(track_count):
        # Generate a random search query (you can customize this)
        search_query = random.choice(["pop", "rock", "hip hop", "indie", "electronic"])
        
        # Search for tracks
        results = sp.search(q=search_query, type='track', limit=1)
        
        # Add the first track found to the playlist
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.playlist_add_items(playlist_id, [track_uri])

    print(f"Playlist '{playlist_name}' created successfully!")

if __name__ == "__main__":
    # Set up Spotify API credentials
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'
    REDIRECT_URI = 'your_redirect_uri'

    # Set up Spotify authentication
    sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope='playlist-modify-private playlist-modify-public user-library-read user-read-private')
    token_info = sp_oauth.get_access_token()

    # Create a Spotify client
    sp = spotipy.Spotify(auth=token_info['access_token'])

    # Generate a playlist with a specified name and track count
    generate_playlist(sp, "My Random Playlist", track_count=10)
