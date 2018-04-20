from subprocess import call
import random, os, math, json

call(["omxplayer","-o","local"])

##########################################################

lead=["Do","Mib","Fa","Sol","Sib","Do2"]
drum=["Kick","Snare"]

path="./samples/"
s_type=".wav"

###########################################################

def play(sound,vol=100):
	if type(sound) == int :
		if sound == 1:
			sound = random.choice(lead)
		elif sound == 2:
			sound = random.choice(drum)
		else:
			print ("invalid option")
			return False

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

prev=[-1,-1]

while True:
	f=open("./result.txt","rb")
	data=0
	for data in f:
		pass
	if data:
		data=str(data)[2:-2].split(':')
		data = [int(i.replace("\\","")) for i in data]
		if data[0:2] != prev:
			prev=data[0:2]
			data.append(json.load(open('config.json'))['vol'+str(data[0])])
			print ("data: ",data)
			play(data[1],data[2])
	f.close()
	continue
