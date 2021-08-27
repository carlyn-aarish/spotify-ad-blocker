# Spotify Ad Blocker

## About
Automatically mutes Spotify ads

## User Story
As a listener using Spotify, I want to avoid listenting to ads without paying for Premium

## How to Use
1. Go to https://developer.spotify.com/console/get-users-currently-playing-track/
1. Click `Get Token`
1. Check `user-read-currently-playing` box
1. Click `Request Token`
1. Copy the generated OAuth Token
1. Set `SPOTIFY_ACCESS_TOKEN` to the copied token in `main.py`
1. Open Spotify app and start playing something
1. In terminal, go to directory where program is saved
1. Run `python main.py`

## Steps
1. detect when an ad is playing
1. muting device while ad is playing

## Possible Future Iterations
1. close and reopening Spotify to skip ads 
1. mute Spotify app audio and playing a local song while ad is playing

## To Mute Device While Ad is Playing
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

## Possible Future Features
* instead of setting to a fixed volume when a track is playing, check the
current volume setting using osascript and set it to that
* automate getting the OAuth token when the script is run
* get it to work on a mobile device
* instead of muting device audio, close and reopen Spotify to skip ad
* instead of muting device audio, mute Spotify app audio and play a song saved locally


## Questions
* When does an OAuth token expire?
    * After one hour


