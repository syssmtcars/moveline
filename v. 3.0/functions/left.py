#!usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

#Инициализация переменных
speed = 450 # Скорость
delta = 0 # Пустая переменная delta , которая будет использоваться в будущем.
m1 = 0 #-port D
m2 = 0 #-port A
#Инициализация моторов и датчиков
mr = MediumMotor('outD')
ml = MediumMotor('outA')
ls = ColorSensor('in1')
rs = ColorSensor('in4')
#Режим датчиков
ls.mode = 'COL-REFLECT'
rs.mode = 'COL-REFLECT'
#Калибровка
b = rs.value()
#ПИД регулятор

def move():
    try:
        while True:
            a = ls.value()# Считывание датчика
            c = 8 # Коэфицент
            delta = (a-b)*c #Разница покозаний датчиков , умноженная на коэфицент.
            if delta <= 0:
                mr.run_forever(speed_sp = speed)
                ml.run_forever(speed_sp = (speed+delta)*-1)
            else:
                mr.run_forever(speed_sp = speed-delta)
                ml.run_forever(speed_sp = speed*-1)
            sleep(50 / 1000)
    except KeyboardInterrupt:
        pass
    finally:
        mr.stop(stop_action = 'brake')
        ml.stop(stop_action = 'brake')