import requests
import osascript
import time


GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = ''


def get_current_track(access_token):
    response = requests.get(
        GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
        }
    )
    response_json = response.json()
    current_track_type = response_json['currently_playing_type']
    return current_track_type


def main():
    while True:
        current_track = get_current_track(SPOTIFY_ACCESS_TOKEN)
        print(current_track)
        if current_track == 'ad':
            print('an ad is playing!')
            osascript.osascript('set volume output volume 0')
        else:
            print('a song is playing!')
            osascript.osascript('set volume output volume 50')
        time.sleep(1)


if __name__ == '__main__':
    main()
