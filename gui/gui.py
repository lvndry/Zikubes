from guizero import App, Text, Slider, Box
import time,json
from subprocess import call

conf = json.load(open('config.json'))
master = 100
bg_color = "#eeeeee"

def END():
    call(["killall","bash"])
    call(["killall","python3"])
    call(["killall","zikubes.sh"])

def setConfig():
    c=open('config.json','w')
    c.write('{"vol1":'+str(conf['vol1'])+',"vol2":'+str(conf['vol2'])+'}')
    c.close()

def change_volume1():
    conf['vol1'] = volume1_text.value = int(float(volume1_slider.value)*float(master_slider.value)/100)
    setConfig()

def change_volume2():
    conf['vol2'] = volume2_text.value = int(float(volume2_slider.value)*float(master_slider.value)/100)
    setConfig()

def change_master():
    change_volume1()
    change_volume2()
    master = master_text.value = master_slider.value

app = App(title="Zikubes", bg=bg_color, height=480, width=800)
app.on_close(END)

welcome_message = Text(app, text="Welcome to Zikubes", size=40, color="#4499ff", bg=bg_color)

box_slider = Box(app, layout="grid")

volume1_text = Text(box_slider, text=conf['vol1'], size=30, color="#44dd44", bg=bg_color, grid=[0,0])
volume2_text = Text(box_slider, text=conf['vol2'], size=30, color="red", bg=bg_color, grid=[1,0])
master_text = Text(box_slider, text=master, size=30, color="#dd00dd", bg=bg_color, grid=[2,0])

volume1_slider = Slider(box_slider, horizontal=False, command=change_volume1, start=100, end=0, grid=[0,1])
volume2_slider = Slider(box_slider, horizontal=False, command=change_volume2, start=100, end=0, grid=[1,1])
master_slider = Slider(box_slider, horizontal=False, command=change_master, start=100, end=0, grid=[2,1])

Text(box_slider, text="---", size=100, color=bg_color, bg=bg_color, grid=[0,2])
Text(box_slider, text="---", size=100, color=bg_color, bg=bg_color, grid=[1,2])
Text(box_slider, text="---", size=100, color=bg_color, bg=bg_color, grid=[2,2])

box_slider.width=500
volume1_slider.text_size = volume2_slider.text_size = master_slider.text_size = 1
volume1_slider.text_color = volume2_slider.text_color = master_slider.text_color = master_slider.bg = volume1_slider.bg = volume2_slider.bg = box_slider.bg = bg_color
volume1_slider.width = volume2_slider.width = master_slider.width = 220
volume1_slider.height = volume2_slider.height = master_slider.height = 30

master_slider.value = 100
volume1_slider.value = conf['vol1']
volume2_slider.value = conf['vol2']

app.display()
