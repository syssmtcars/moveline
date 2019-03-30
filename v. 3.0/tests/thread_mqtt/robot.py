#!/usr/bin/env python3

from Listener import *
import Listener as ls

import paho.mqtt.client as mqtt
from threading import Thread
from ev3dev.ev3 import *

sender = mqtt.Client()

pc_thread = ListenPC("Listen to PC")
pc_thread.start()

sender.connect("192.168.1.141",1883,1000)

try:
	while True:
		if ls.msgFromPC!='':
			print(ls.msgFromPC)
			#sender.publish("syssmtcars", 'ok')

finally:
	pass