# Spotify Ad Blocker

######################
How to Use
######################
1) Go to https://developer.spotify.com/console/get-users-currently-playing-track/
2) Click Get Token
3) Check "user-read-currently-playing" box
4) Click Request Token
5) Copy the generated OAuth Token
6) Set SPOTIFY_ACCESS_TOKEN to the copied token in main.py
7) Open Spotify app and start playing something
8) In terminal, go to directory where program is saved
9) Run `python main.py`

######################
User Story
######################
As a listener using Spotify, I want to skip ads without paying for Premium

######################
Steps
######################
1) detect when an ad is playing
2) skip add by either:
  a) muting device while ad is playing
  b) closing and reopening Spotify to skip
  c) muting Spotify app audio and playing a local song while ad is playing

2a:
To mute MacOS speakers, need to be able to communicate with local processes on
my OS. Can do this using AppleScript
(https://wiki.python.org/moin/MacPython/AppleScript).
To execute AppleScript from Python 3.6, you can use osascript
(https://ss64.com/osx/osascript.html).

######################
Spotify API
######################
This is an example of a portion of what the Spotify API returns if an ad is playing. "item" is null and "currently_playing_type" is "ad"
(https://developer.spotify.com/console/get-users-currently-playing-track)

{
  "timestamp": 1625703306354,
  "context": {
    "external_urls": {
      "spotify": "https://open.spotify.com/playlist/123"
    },
    "href": "https://api.spotify.com/v1/playlists/123",
    "type": "playlist",
    "uri": "spotify:playlist:08MT3rlqhj9y3oiIdbAjx1"
  },
  "progress_ms": 14544,
  "item": null,
  "currently_playing_type": "ad",
  "actions": {
    "disallows": {
      "resuming": true,
      "seeking": true,
      "skipping_prev": true,
      "skipping_next": true,
      "interrupting_playback": true,
      "transferring_playback": true
    }
  },
  "is_playing": true
}

If a song is playing, then "item" has the song info, the "currently_playing_type" is "track", and the "actions" differ. Here is an example:


"currently_playing_type": "track",
"actions": {
  "disallows": {
    "resuming": true
  }
},

######################
Possible Future Features
######################
1) instead of setting to a fixed volume when a track is playing, check the
current volume setting using osascript and set it to that
2) automate getting the OAuth token when the script is run
3) get it to work on a mobile device
4) instead of muting device audio, close and reopen Spotify to skip ad
5) instead of muting device audio, mute Spotify app audio and play a song saved
locally

######################
Questions
######################
* How does an OAuth token expire? After a certain amount of time that Spotify is
idle?


