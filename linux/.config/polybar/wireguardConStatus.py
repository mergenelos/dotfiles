#!/usr/bin/env python

import os
import sys
import subprocess

config = "/etc/wireguard/wg0-client-mak.conf"
confName = os.path.basename(config)
confName = confName[:-5]

def con_status():
	if config:
		connection = subprocess.getoutput("sudo wg show "+confName+" 2>/dev/null | head -n 1 | awk '{print $NF }'")

		if connection == confName:
			return 1
		else:
			return 2
	else:
		return 3


status = con_status()

if len(sys.argv) > 1:
	if sys.argv[1] == '--toggle':
		if status == 2:
			output = subprocess.getoutput("sudo wg-quick up "+confName)
			status = 1
		elif status == 1:
			output = subprocess.getoutput("sudo wg-quick down "+confName)
			status = 2


if status == 3:
	print("Invalid Config")
elif status == 2:
	#print("%{F#e60053}-WG%{F-}")
	print("-WG")
else:
	#print("%{F#55aa55}+WG%{F-}")
	print("+WG")
	
