# Spotify Ad Blocker

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

## About the Script

### Script Functions
1. detect when an ad is playing
1. mute device while ad is playing

### Notes on muting on MacOS
To mute MacOS speakers, need to be able to communicate with local processes on
my OS.
Can do this using [Applescript](https://wiki.python.org/moin/MacPython/AppleScript).
To execute AppleScript from Python 3.6, use [osascript](https://ss64.com/osx/osascript.html).

## Spotify API
This is an example of a portion of what the [Spotify API](https://developer.spotify.com/console/get-users-currently-playing-track) returns if an ad is playing. `"item"` is `"null"` and `"currently_playing_type"` is `"ad"`

```json
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
```

If a song is playing, then `"item"` has the song info, the `"currently_playing_type"` is `"track"`, and the `"actions"` differ. Here is an example:

```json
"currently_playing_type": "track",
"actions": {
  "disallows": {
    "resuming": true
  }
}
```

### Possible Future Iterations of Scripts
1. close and reopen Spotify to skip ads, rather than mute them 
1. mute Spotify app audio and play a local song while ad is playing

### Possible Future Features
* instead of setting to a fixed volume when a track is playing, check the
current volume setting using osascript and set it to that
* automate getting the OAuth token when the script is run
* get it to work on a mobile device
* instead of muting device audio, close and reopen Spotify to skip ad
* instead of muting device audio, mute Spotify app audio and play a song saved locally


### Questions
* When does an OAuth token expire?
    * After one hour


