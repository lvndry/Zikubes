from subprocess import call
import random,os,math

call(["omxplayer","-o","local"])
##########################################################

lead=["Do","Mib","Fa","Sol","Sib","Do2"]
drum=["Kick","Snare"]

path="./samples/"
s_type=".wav"

###########################################################

def play(sound,vol=100):
	if type(sound) == list :
		sound = random.choice(sound)

	elif type(sound) == str :
		pass

	else:
		print("invalid option")
		return False


	if __exists(sound) and __valideVol(vol) :
		call(["omxplayer","--vol",str(int(2000 * math.log10(vol/100.0))),path+sound+s_type])
		return True

	else:
		if __valideVol(vol) :
			print ("can't find "+sound+s_type)
		else:
			print ("invalid volume")
		return False

###########################################################

def __exists(sound):
	dirs = os.listdir(path)

	for file in dirs:
		if file == sound+s_type :
			return True

	return False


def __valideVol(vol):
	if type(vol) == int and vol<=100 and vol>=0 :
			return True

	return False

###################################################################


f=open("./result.txt","rb")
for data in f:
	pass

data=str(data)[2:-2]
data=data.split(':')
data[2]=data[2].replace("\\","")
print("data: ",data)

play(data[1],int(data[2]))
