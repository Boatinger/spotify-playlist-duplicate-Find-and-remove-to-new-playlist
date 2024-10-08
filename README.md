
# spotify-playlist-duplicate-find-and-remove-to-new-playlist

This Python script allows you to compare two Spotify playlists, find duplicate tracks that exist in both playlists, move those duplicates to a new playlist, and remove them from the source playlist.

## Features

- Fetches tracks from two Spotify playlists.
- Lists tracks from both playlists side by side with their names and URIs.
- Identifies duplicate tracks (present in both playlists).
- Moves duplicates to a new playlist.
- Removes duplicate tracks from the source playlist.

## Prerequisites

1. **Python 3.9 or later** should be installed.
2. Install the `spotipy` library:

   ```bash
   pip install spotipy
   ```

3. A Spotify Developer account with **API credentials**:
   - Create a [Spotify Developer account](https://developer.spotify.com/dashboard/applications).
   - Get the following from your app:
     - **Client ID**
     - **Client Secret**
     - **Redirect URI**

## Setup

### 1. Clone or Download the Repository

Download or clone this repository to your local machine.

### 2. Install Dependencies

Install the required `spotipy` library using the following command:

```bash
pip install spotipy
```

### 3. Spotify Developer Credentials

To use this script, you need to provide your **Spotify API credentials** in the script. Replace the placeholders (`Change_me`) in the script with your **Client ID**, **Client Secret**, and **Redirect URI**:

```python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="Change_me",
                                               client_secret="Change_me",
                                               redirect_uri="Change_me",
                                               scope="playlist-modify-public playlist-read-private"))
```

### 4. Playlist IDs

You need to provide the **Source Playlist ID**, **Comparison Playlist ID**, and a **New Playlist Name** for storing duplicates. Replace the placeholders where it says `Change_me`:

```python
source_playlist_id = "Change_me"
comparison_playlist_id = "Change_me"
new_playlist_name = "Change_me"
```

You can find a playlist ID in the URL of the playlist on Spotify. For example:

```
https://open.spotify.com/playlist/6g25SNucbeCjxAJXIZ5RSJ?si=f9bfc5e850c44615
```

Here, `6g25SNucbeCjxAJXIZ5RSJ` is the playlist ID.

## How to Use

1. Open a terminal and run the script:

   ```bash
   python3 your_script.py
   ```

2. The script will:

   - Fetch and display the tracks from both the **source** and **comparison** playlists side by side.
   - Identify the duplicate tracks present in both playlists.
   - Move the duplicates to a **new playlist** (with the name you provide).
   - Remove the duplicates from the **source playlist**.

### Example Output:

```
Source Playlist                                      | Comparison Playlist                                
---------------------------------------------------- | ------------------------------------------------
Track A                   spotify:track:1abcdefg1234567   | Track A                   spotify:track:1abcdefg1234567
Added 69 duplicate tracks to the playlist: Duplicates from Source
Removed 69 duplicate tracks from the source playlist.
```

### Important Notes

- Ensure that you have **access** to the playlists, especially if they are private.
- The **new playlist** will be created to store the duplicates.
- Duplicate comparison is done by comparing **Spotify track URIs**.

## License

This project is licensed under the **GNU General Public License v3.0**. Any modified versions of this project must also be distributed under the same license.
