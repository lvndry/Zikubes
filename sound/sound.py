from playsound import playsound
import random

lead=['Do','Mib','Fa','Sol','Sib','Do2']
drum=['Kick','Snare']

playsound(str(random.choice(lead)) + '.wav')
playsound(str(random.choice(lead)) + '.wav')
playsound(str(random.choice(lead)) + '.wav')
playsound(str(random.choice(drum)) + '.wav')
playsound(str(random.choice(drum)) + '.wav')