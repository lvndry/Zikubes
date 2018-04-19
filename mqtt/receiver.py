#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber
def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("zikubes/test")

def on_message(client, userdata, msg):
    print ("Message")
    print('Message: ' + msg.payload)
    client.disconnect()

client = mqtt.Client()
client.connect("192.168.43.64", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
