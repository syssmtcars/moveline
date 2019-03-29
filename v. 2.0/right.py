#!usr/bin/env python3

#TODO


'''''        _____     _
   _____   _|___ /  __| | _____   __
  / _ \ \ / / |_ \ / _` |/ _ \ \ / /
 |  __/\ V / ___) | (_| |  __/\ V /
  \___| \_/ |____/ \__,_|\___| \_/
'''''
from ev3dev.ev3 import *
from time import sleep

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
b = ls.value()
#ПИД регулятор
def move():
    try:
        while True:
            a = rs.value()
            c = 8
            delta = (a-b)*c
            if delta <= 0:
                ml.run_forever(speed_sp = speed*-1)
                mr.run_forever(speed_sp = speed+delta)
            else:
                ml.run_forever(speed_sp = (speed-delta)*-1)
                mr.run_forever(speed_sp = speed)

            sleep(50 / 1000)
    except KeyboardInterrupt:
        pass
    finally:
        mr.stop(stop_action = 'brake')
        ml.stop(stop_action = 'brake')