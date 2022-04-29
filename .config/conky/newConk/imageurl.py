#!/usr/bin/env python


import os
import subprocess

colorFile = open("/home/mak/.config/conky/newConk/playRingColor.txt", "r+")
color = colorFile.readline()
colorFile.close()

imageurl = subprocess.getoutput("playerctl metadata mpris:artUrl")
imageurl = imageurl[7:]
#print(imageurl)
musicId = subprocess.getoutput("playerctl metadata mpris:trackid")
#print(musicId)
preMusic = open("/home/mak/.config/conky/newConk/preMusic.txt", "r+")
preMusicId = preMusic.readline()
preMusicId = preMusicId.rstrip("\n")
#print(preMusicId)
preImageurl = preMusic.readline()
preImageurl = preImageurl.rstrip("\n")
#print(preImageurl)

if preMusicId==musicId and preImageurl==imageurl:
	preMusic.close()
	#print('here')
	#nop
else:
	color = 'pink' if color=='blue' else 'blue'
	colorFile = open("/home/mak/.config/conky/newConk/playRingColor.txt", "w")
	colorFile.write(color)
	colorFile.close()

	preMusic.close()
	preMusic = open("/home/mak/.config/conky/newConk/preMusic.txt", "w")
	preMusic.write(musicId+'\n'+imageurl)
	preMusic.close()

	dst="~/.config/conky/newConk/imageurl.jpg"
	circle_imageurl="~/.config/conky/newConk/circle_imageurl.png"
	if_playing="~/.config/conky/newConk/makonplay.png"
	mak="~/.config/conky/newConk/mak.png"
	overlay = "~/.config/conky/newConk/overlay.png"

	if imageurl=='' or ("failed" in imageurl):
		#os.system('rm ' + dst)
		os.system('rm ' + if_playing)
		os.system('cp '+mak+' '+circle_imageurl)
	else:
		os.system('ln -sf '+mak+' '+if_playing)
		#os.system('ln -sf ' +'\"' + imageurl + '\"' + ' ' + dst)
		os.system('convert '+'\"'+imageurl+'\"'+' -resize 500x500 '+circle_imageurl)
		os.system('convert '+circle_imageurl+' '+overlay+' -composite '+circle_imageurl)
		os.system('convert -size 500x500 xc:none -fill '+circle_imageurl+' -draw "circle 250,250 250,1" '+circle_imageurl)
