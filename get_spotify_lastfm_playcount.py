import pylast
import subprocess
from time import sleep
import argparse

# Description:
#   This script will retrieve the play count of a song that currently playing in the Spotify Desktop app.
#   This script currently ONLY works on Mac OS X
#
# Usage:
#   Run this script from command line, supplying the required arguments. control+c to exit
#
# Example:
#   python get_spotify_lastfm_playcount.py --apikey=1234567890 --username=bob

parser = argparse.ArgumentParser(description='Gets your Last.fm play count of the currently playing Spotify song')
parser.add_argument('--apikey', help='Last.fm API Key')
parser.add_argument('--username', help='Last.fm username')
args = vars(parser.parse_args())
lastfm_username = args['username']
lastfm_apikey = args['apikey']

artist_name_cmd = "/usr/bin/osascript -e 'tell application \"Spotify\" to artist of current track as string'"
track_name_cmd = "/usr/bin/osascript -e 'tell application \"Spotify\" to name of current track as string'"
current_track = ""

print
while True:
    artist_name = subprocess.Popen(artist_name_cmd,shell=True,stdout=subprocess.PIPE).stdout.read()
    artist_name = artist_name.rstrip()
    track_name = subprocess.Popen(track_name_cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    track_name = track_name.rstrip()

    if current_track == track_name:
        sleep(5)
    else:
        current_track = track_name
        try:
            lastfm = pylast.LastFMNetwork(api_key=lastfm_apikey,
                                          api_secret="",
                                          username=lastfm_username,
                                          password_hash="")

            track = pylast.Track(artist=artist_name,
                                 title=track_name,
                                 network=lastfm,
                                 username=lastfm_username)

            plays = track.get_userplaycount()
        except:
            plays = 0
        print artist_name + " - " + track_name + " - Plays: " + plays.__str__()
        print