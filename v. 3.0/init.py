#!usr/bin/env python3

import paho.mqtt.client as mqtt
from time import sleep
from ev3dev.ev3 import *

speed = 450
delta = None

mr = MediumMotor('outD')
ml = MediumMotor('outA')
ls = ColorSensor('in1')
rs = ColorSensor('in4')
ls.mode = 'COL-REFLECT'
rs.mode = 'COL-REFLECT'

msgFlag = False
message = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("syssmtcars")


def on_message(client, userdata, msg):

    if str(msg.payload.decode()) == 'right':
        pass

    elif str(msg.payload.decode()) == 'left':
        print('l')

    elif str(msg.payload.decode()) == 'forward':
        print('f')




client = mqtt.Client()
client.connect("192.168.1.141", 1883, 60)


client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()