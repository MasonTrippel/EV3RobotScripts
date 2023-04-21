#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,OUTPUT_B,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, SpeedPercent,MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import GyroSensor,ColorSensor
from ev3dev2.sound import Sound


test = True
target_num = "0101"
num = ""
tank = MoveTank(OUTPUT_A, OUTPUT_D)

tank.gyro = GyroSensor()
tank.gyro.calibrate()

Claw = MediumMotor(OUTPUT_B)

Cl = ColorSensor()
Cl.mode='COL-COLOR'

start = time.perf_counter()

while test:
    tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(.1),target_angle=0, follow_for_ms=150)

    if len(num) == 4 and num == target_num :
        test = False
    elif len(num) == 4 and num != target_num:
        print(num)
        num = ""    
    elif Cl.value() == 6:
        time.sleep(1.5)
        num = num + '0'
        print('White')

    elif Cl.value() == 1:
        time.sleep(1.5)
        num = num + '1'
        print('black')
    #elif Cl.value == 0:
     #   num = ""


tank.stop()
end = time.perf_counter()

total = (end - start)

feetTraveled = ((total/1.74))/10

feetTillEnd = 3 - feetTraveled

print(num)