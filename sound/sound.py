from subprocess import call
import random,os,math

##########################################################

lead=["Do","Mib","Fa","Sol","Sib","Do2"]
drum=["Kick","Snare"]

path="./samples/"
s_type=".wav"

###########################################################

def play(sound,vol):
	if type(sound) == list :
		sound = random.choice(sound)
	
	elif type(sound) == str :
		pass

	else:
		print("invalid option")
		return False


	if __exists(sound) and __valiodeVol(vol) :
		call(["omxplayer","--vol",2000 * math.log10(vol/100.0),path+sound+s_type])
		return True

	else:
		if __valiodeVol(vol) :
			print ("invalid volume")
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


def __valiodeVol(vol):
	if type(vol) == int and vol<=100 and vol>=0 :
			return True

	return False
