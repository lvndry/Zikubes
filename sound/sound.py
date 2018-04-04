from subprocess import call
import random,os

##########################################################

lead=["Do","Mib","Fa","Sol","Sib","Do2"]
drum=["Kick","Snare"]

path="./samples/"
s_type=".wav"

###########################################################

def play(sound):
	if type(sound) == list :
		sound = random.choice(sound)
	
	elif type(sound) == str :
		pass

	else:
		print("invalid option")
		return False

	if __exists(sound) :
		call(["omxplayer",path+sound+s_type])
		return True

	else:
		print ("can't find "+sound+s_type)
		return False

###########################################################

def __exists(sound):
	dirs = os.listdir(path)

	for file in dirs:
		if file == sound+s_type :
			return True

	return False
