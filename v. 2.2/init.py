#!usr/bin/env python3

import paho.mqtt.client as mqtt
from time import sleep
from ev3dev.ev3 import *

speed = 450
delta = 0
m1 = 0  # -port D
m2 = 0  # -port A
mr = MediumMotor('outD')
ml = MediumMotor('outA')
ls = ColorSensor('in1')
rs = ColorSensor('in4')
ls.mode = 'COL-REFLECT'
rs.mode = 'COL-REFLECT'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("syssmtcars")


def on_message(client, userdata, msg):

    if str(msg.payload.decode()) == 'right':
        pass

    elif str(msg.payload.decode()) == 'left':
        pass

    elif str(msg.payload.decode()) == 'forward':


        a = rs.value()
        b = ls.value()
        c = 2.0
        delta = (a - b) * c
        if delta <= 0:
            ml.run_forever(speed_sp=speed * -1)
            mr.run_forever(speed_sp=speed + delta)
        else:
            mr.run_forever(speed_sp=speed)
            ml.run_forever(speed_sp=(speed - delta) * -1)




client = mqtt.Client()
client.connect("192.168.0.34", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()