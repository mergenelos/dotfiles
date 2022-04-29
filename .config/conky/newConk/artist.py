#!/usr/bin/env python


import os
import subprocess
artist = subprocess.getoutput("playerctl metadata artist")
musicUrl = subprocess.getoutput("playerctl metadata xesam:url")



if artist=='' and musicUrl!='':
	artist="noArtistEnt"
elif "failed" in artist:
	artist=""
if len(artist)>15:
	artist=artist[:15]+"..."


print('{:^18}'.format(artist));
