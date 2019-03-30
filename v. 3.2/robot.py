#!/usr/bin/env python3

from Listener import *
import Listener as listen
from time import sleep
import paho.mqtt.client as mqtt
from threading import Thread
from ev3dev.ev3 import *

speed = 450
delta = 0
m1 = 0 #-port D
m2 = 0 #-port A

mr = MediumMotor('outD')
ml = MediumMotor('outA')
ls = ColorSensor('in1')
rs = ColorSensor('in4')
ls.mode = 'COL-REFLECT'
rs.mode = 'COL-REFLECT'
sender = mqtt.Client()

pc_thread = ListenPC("Listen to PC")
pc_thread.start()

sender.connect("192.168.1.141",1883,1000)

try:
	b_right = ls.value()
	b_left = rs.value()
	while True:
		if listen.msgFromPC == 'forward':
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

		elif listen.msgFromPC == 'left':
			a = ls.value()  # Считывание датчика
			c = 8  # Коэфицент
			delta = (a - b_left) * c  # Разница покозаний датчиков , умноженная на коэфицент.
			if delta <= 0:
				mr.run_forever(speed_sp=speed)
				ml.run_forever(speed_sp=(speed + delta) * -1)
			else:
				mr.run_forever(speed_sp=speed - delta)
				ml.run_forever(speed_sp=speed * -1)

			sleep(50 / 1000)

		elif listen.msgFromPC == 'right':

			a = rs.value()
			c = 8
			delta = (a - b_right) * c
			if delta <= 0:
				ml.run_forever(speed_sp=speed * -1)
				mr.run_forever(speed_sp=speed + delta)
			else:
				ml.run_forever(speed_sp=(speed - delta) * -1)
				mr.run_forever(speed_sp=speed)

			sleep(50 / 1000)
finally:
	pass