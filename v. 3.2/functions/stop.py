#!usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

mr = MediumMotor('outD')
ml = MediumMotor('outA')

def move():
    mr.stop(stop_action = 'brake')
    ml.stop(stop_action = 'brake')