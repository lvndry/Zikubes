from subprocess import call
import random

lead=["Do","Mib","Fa","Sol","Sib","Do2"]
drum=["Kick","Snare"]

for i in range(0,3):
	call(["omxplayer",random.choice(lead)+".wav"])
	call(["omxplayer",random.choice(drum)+".wav"])
