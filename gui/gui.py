from guizero import App, Text, Slider, Box
import time

volume1 = 0
volume2 = 0
cubes = 0

def change_volume1(slider_value):
    volume1 = slider_value
    volume1_text.value = slider_value

def change_volume2(slider_value):
    volume2 = slider_value
    volume2_text.value = slider_value

app = App(title="Zikubes", bg="white", height=480, width=800, layout="grid")
header = Box(app, layout="grid")
box_slider = Box(app, layout="grid")

welcome_message = Text(app, text="Welcome to Zikubes", size=40, color="lightblue", bg="white")
cubes_num = Text(app, text="You have " + str(cubes) + " cubes open")

volume1_text = Text(app, text=volume1, size=30, color="green", bg="white")
volume2_text = Text(app, text=volume2, size=30, color="red", bg="white")

volume1_slider = Slider(box_slider, horizontal=False, command=change_volume1, start=100, end=0, grid=[0,0])
volume1_slider.bg = "white"
volume2_slider = Slider(box_slider, horizontal=False, command=change_volume2, start=100, end=0, grid=[2,0])
volume2_slider.bg = "white"

app.display()
