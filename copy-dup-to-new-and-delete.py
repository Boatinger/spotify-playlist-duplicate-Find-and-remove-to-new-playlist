import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up the authentication using your provided Client ID and Client Secret
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="Change_me",
                                               client_secret="Change_me",
                                               redirect_uri="Change_me",
                                               scope="playlist-modify-public playlist-read-private"))

def get_tracks_from_playlist(playlist_id):
    """Retrieve all track names and URIs from a playlist."""
    tracks = []
    results = sp.playlist_items(playlist_id)
    tracks.extend([(item['track']['name'], item['track']['uri']) for item in results['items']])
    
    # Handle pagination
    while results['next']:
        results = sp.next(results)
        tracks.extend([(item['track']['name'], item['track']['uri']) for item in results['items']])
    
    return sorted(tracks, key=lambda x: x[0].lower())  # Sort alphabetically by track name

def get_playlist_name(playlist_id):
    """Retrieve the playlist name."""
    return sp.playlist(playlist_id)['name']

def print_side_by_side(source_tracks, comparison_tracks, source_playlist_name, comparison_playlist_name):
    """Print two lists side by side with playlist names."""
    max_len = max(len(source_tracks), len(comparison_tracks))
    
    print(f"{source_playlist_name:<60} {'|'} {comparison_playlist_name:<60}")
    print(f"{'-'*60} {'|'} {'-'*60}")
    
    for i in range(max_len):
        source_track = source_tracks[i] if i < len(source_tracks) else ('', '')
        comparison_track = comparison_tracks[i] if i < len(comparison_tracks) else ('', '')
        
        print(f"{source_track[0]:<40} {source_track[1]:<20} {'|'} {comparison_track[0]:<40} {comparison_track[1]:<20}")

def move_duplicates_to_new_playlist(source_playlist_id, comparison_playlist_id, new_playlist_name):
    """Find duplicates between two playlists, move them to a new playlist, and remove from the source playlist."""
    source_tracks = get_tracks_from_playlist(source_playlist_id)
    comparison_tracks = get_tracks_from_playlist(comparison_playlist_id)

    # Convert track lists into sets for easier comparison using URIs
    source_track_uris = set([track[1] for track in source_tracks])
    comparison_track_uris = set([track[1] for track in comparison_tracks])

    # Find duplicate tracks by URI
    duplicates = list(source_track_uris.intersection(comparison_track_uris))

    if duplicates:
        # Create a new playlist for the duplicates
        user_id = sp.me()['id']
        new_playlist = sp.user_playlist_create(user_id, new_playlist_name)
        new_playlist_id = new_playlist['id']
        
        # Add duplicates to the new playlist
        sp.playlist_add_items(new_playlist_id, duplicates)
        print(f"Added {len(duplicates)} duplicate tracks to the playlist: {new_playlist_name}")
        
        # Remove duplicates from the source playlist
        sp.playlist_remove_all_occurrences_of_items(source_playlist_id, duplicates)
        print(f"Removed {len(duplicates)} duplicate tracks from the source playlist.")
    else:
        print("No duplicates found between the playlists.")

# Example usage:
source_playlist_id = "Change_me"
comparison_playlist_id = "Change_me"
new_playlist_name = "Change_me"

# Print side-by-side lists with playlist names
source_tracks = get_tracks_from_playlist(source_playlist_id)
comparison_tracks = get_tracks_from_playlist(comparison_playlist_id)

source_playlist_name = get_playlist_name(source_playlist_id)
comparison_playlist_name = get_playlist_name(comparison_playlist_id)

print_side_by_side(source_tracks, comparison_tracks, source_playlist_name, comparison_playlist_name)

# Move duplicates from the source to the new playlist and remove from source
move_duplicates_to_new_playlist(source_playlist_id, comparison_playlist_id, new_playlist_name)