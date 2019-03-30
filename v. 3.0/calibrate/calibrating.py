#!usr/bin/env python3

#TODO

from ev3dev.ev3 import *
from time import sleep


ls = ColorSensor('in1')
rs = ColorSensor('in4')
ls.mode = 'COL-REFLECT'
rs.mode = 'COL-REFLECT'

while True:
    print(str(ls.value()),str(rs.value()))
