#!/usr/bin/env python3

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("IP_ADDRESS_OF_BROKER", 1883, 60)
rc = client.publish("zikubes/test", "Hello World")
client.loop_start()
