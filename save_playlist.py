import spotify_credentials as cfg

# everything to log into spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


def create_playlist(source_name, new_name):
    # grab all credentials from a separate file
    username = cfg.spotify['username']
    client_id = cfg.spotify['client_id']
    client_secret = cfg.spotify['client_secret']
    redirect_uri = cfg.spotify['redirect_uri']

    scope = 'user-library-read playlist-modify-public playlist-read-private'

    # use credentials for spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    # creating the spotify object with credentials
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # creating a token, if possible, with user credentials
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    # login successful or unsuccessful
    if token:
        sp = spotipy.Spotify(auth=token)
        print("Login successful")
    else:
        print("Can't get token for ", username)

    # get all songs from one playlist and store in variable
    # spotify:user:spotify:playlist:ENTER_SOURCE_PLAYLIST_ID
    # my "tastebreakers" to get songs from
    source_playlist_id = source_name
    source_playlist = sp.user_playlist(username, source_playlist_id)
    print("Using '" + source_playlist['name'] + "' as source playlist.")
    tracks = source_playlist['tracks']
    songs = tracks["items"]

    # filling a list of track id's
    # and only track id's, apparently that's how "user_playlist_add_tracks()"
    # takes in tracks
    track_ids = []
    for i in range(0, len(songs)):
        track_ids.append(songs[i]['track']['id'])
        # print(track_ids[i])

    # put all songs into playlist I've created
    created_name = new_name
    my_playlist = sp.user_playlist_create(username, name=created_name)
    print("Playlist " + created_name + " has been created.")
    sp.user_playlist_add_tracks(
        username,
        playlist_id=my_playlist['id'],
        tracks=track_ids
    )
    print("We've added all the songs from the source playlist to your selected playlist")