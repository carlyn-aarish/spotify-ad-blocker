# Spotify Ad Muter

## About
Automatically mutes Spotify ads

## User Story
As a listener using Spotify, I want to avoid listenting to ads while using the free version

## How to Use
1. Go to https://developer.spotify.com/console/get-users-currently-playing-track/
1. Click `Get Token`
1. Check `user-read-currently-playing` box
1. Click `Request Token`
1. Copy the generated OAuth Token
1. Set `SPOTIFY_ACCESS_TOKEN` to the copied token in `main.py`
1. Open Spotify app and start listening
1. In terminal, go to directory where program is saved
1. Run `python main.py`
2. Enjoy music without ads
3. Token expires after 1 hour
