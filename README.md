# Description

A simple python script that copies all songs in playlist into a playlist that you own.\
I created this because my Tastebreakers playlist from 2018 was so good that I wanted to keep it forever. Afraid that the playlist would change over time, I created a script to save the current snapshot of said playlist to save under my profile.

## Getting Started

After forking you'll need to `pip install spotipy`
 
You'll also need to create a `spotify_credentials.py` file.  
It is a simple file that only has your credentials held in an object that the script calls to verify your profile.
```
spotify = {
    'username': 'INSERT_USER_ID',
    'client_id': 'INSERT_CLIENT_ID',
    'client_secret': 'INSERT_CLIENT_SECRET',
    'redirect_uri':'https://localhost:8080'
}
```
The `username` can be found by:
- Navigating to your profile on the desktop app and clicking the `...` button and choosing `share` -> `Copy Spotify URI`. This copies a link such as `spotify:user:USER_ID` with `USER_ID` being a user's ID. Copy only the `USER_ID` portion and paste it into your `spotify_credentials.py` where `INSERT_USER_ID` is.

The `client_id` and `client_secret` can be found by:
- Navigate to `https://developer.spotify.com/dashboard/login` and log in using your account
- Create a new app with a name like `playlist_creator` to differentiate from your other apps
- Navigate to your new app (`playlist_creator` in this case)
- Your Client ID and Client Secret should be visible from this screen
- Copy your Client ID and Client Secret and paste them in their respective spots in `spotify_credentials.py` 

The `redirect URI` can be found by:
- From your new application's application page, click `Edit Settings`
- Scroll down until you find `Redirect URIs`
- This can be any URI, I chose `https://localhost:8080`, this just has to match in your `spotify_credentials.py` file.

## Usage

After running the script it will function through the command line.

It will authenticate through the `spotify_credentials.py` file and will ask you to enter where you've been redirected to on your browser. Simply copy the URL on your browser and paste it into the command line. After authentication, the script will continue running and:

1. Ask for the source playlist id.  
- This can easily be found by navigating to the chosen playlist's web page on the spotify web player and copy the id after */playlist/* i.e. in `https://open.spotify.com/playlist/37i9dQZF1EjiPmbQ8cXezO` you'd copy and paste `37i9dQZF1EjiPmbQ8cXezO`.
- You can also use the spotify desktop app and clicking the `...` button next to the play/pause button and choosing `Copy Spotify URI`. This copies the entire URI while only the playlist ID is needed so stripping everything except for the ending ID is necessary. 
2. Compile all songs from the source playlist into a list
3. Ask for a name to call your new playlist
4. Create a new playlist with that name
5. Populate the new playlist with all songs from source playlist  

Now you always have access to that precious playlist on your profile if you ever want it.