#!/usr/bin/env python3

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("192.168.43.64", 1883, 60)
rc = client.publish("zikubes/test", "Hello World")
client.loop_start()
