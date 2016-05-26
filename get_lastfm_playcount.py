import pylast
import argparse

# Description:
#   This script will retrieve the play count of a song that is supplied as a command line argument.
#
# Usage:
#   Run this script from command line, supplying the required arguments.
#
# Example:
#   python get_lastfm_playcount.py --apikey=1234567890 --username=bob --artist=Tycho --song=Melanine


parser = argparse.ArgumentParser(description='Gets your Last.fm play count of the supplied song')
parser.add_argument('--apikey', help='Last.fm API Key')
parser.add_argument('--username', help='Last.fm username')
parser.add_argument('--artist', help='Name of artist')
parser.add_argument('--song', help='Name of song')
args = vars(parser.parse_args())
lastfm_username = args['username']
lastfm_apikey = args['apikey']
artist = args['artist']
song = args['song']


try:
    lastfm = pylast.LastFMNetwork(api_key=lastfm_apikey,
                                  api_secret="",
                                  username=lastfm_username,
                                  password_hash="")

    track = pylast.Track(artist=artist,
                         title=song,
                         network=lastfm,
                         username=lastfm_username)

    print track.get_userplaycount()
except:
    print 0