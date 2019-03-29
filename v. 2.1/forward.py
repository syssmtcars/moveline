#!usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

#ISREADY

#Инициализация переменных
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
#ПИД регулятор
def move():
    try:
        a = rs.value()
        b = ls.value()
        c = 2.0
        delta = (a-b)*c
        if delta <= 0:
            ml.run_forever(speed_sp = speed*-1)
            mr.run_forever(speed_sp = speed+delta)
        else:
            mr.run_forever(speed_sp = speed)
            ml.run_forever(speed_sp = (speed-delta)*-1)
    except KeyboardInterrupt:
        pass

    finally:
        mr.stop(stop_action = 'brake')
        ml.stop(stop_action = 'brake')
