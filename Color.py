#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank 
from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import GyroSensor,ColorSensor
from ev3dev2.sound import Sound

test = True

tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)

gyro = GyroSensor(INPUT_1)
gyro.mode = GyroSensor.MODE_GYRO_ANG

Cl = ColorSensor(INPUT_2)
Cl.mode='COL-COLOR'

spkr = Sound()

tank_pair.on(SpeedRPS(.1), SpeedRPS(.1))

while test:
    if Cl.value() == 6:
        tank_pair.brake()
        spkr.speak("I see white").wait()
        test = False


tank_pair.on_for_seconds(SpeedRPS(.1), SpeedRPS(.1), seconds=0.145)
if Cl.value() == 6:
    num = num + '2'
else:
    num = num+ '3'
tank_pair.on_for_seconds(SpeedRPS(.1), SpeedRPS(.1), seconds=0.145)
if Cl.value() == 6:
    num = num + '4'
else:
    num = num + '5'
tank_pair.on_for_seconds(SpeedRPS(.1), SpeedRPS(.1), seconds=0.145)
if Cl.value() == 6:
    num = num + '6'
else:
    num = num + '7'

if num == '0347':
    spkr.speak('This is the correct output')
else:
    spkr.speak('This is not the correct output')
     
