#!/usr/bin/env python

import os
import subprocess


colorFile = open("/home/mak/.config/conky/newConk/playRingColor.txt", "r+")
color = colorFile.readline()
colorFile.close()
print(color,end='')
