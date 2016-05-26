-- Description:
--  This script scans your iTunes library, then uses a python script to get your last.fm play count of each track.
--  it then sets the play count in iTunes to be equal to the playcount in Last.fm

set username to "bob"
set apikey to "0123456789"

tell application "Finder"
	set alias_path to container of (path to me) as alias
	set posix_path to POSIX path of alias_path
end tell

tell application "iTunes"
	set track_list to tracks of user playlist "All Music"
	--set track_list to (every file track of playlist "Library" whose artist contains "Pink Floyd")
	repeat with a_track in track_list
		
		set lastfm_plays to do shell script "python " & posix_path & "/get_lastfm_playcount.py --apikey=" & apikey & " --username=" & username & " --artist=\"" & artist of a_track & "\"" & " --song=\"" & name of a_track & "\""
		
		if lastfm_plays is greater than (played count of a_track) then do shell script "echo " & "\"" & artist of a_track & "\"" & "-" & "\"" & name of a_track & "\"" & "-Last.fm playcount is higher." & lastfm_plays & " vs. " & played count of a_track
		
		if lastfm_plays is greater than (played count of a_track) then set played count of a_track to lastfm_plays
		delay 0.5
	end repeat
end tell
 