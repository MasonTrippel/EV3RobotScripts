#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,OUTPUT_B,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, SpeedPercent,MediumMotor,follow_for_ms
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import GyroSensor,ColorSensor
from ev3dev2.sound import Sound


test = True
target_num = "0101"
num = ""
repeat = 0
tank = MoveTank(OUTPUT_A, OUTPUT_D)

tank.gyro = GyroSensor()
tank.gyro.mode = GyroSensor.MODE_GYRO_ANG
tank.gyro.calibrate()

Claw = MediumMotor(OUTPUT_B)

Cl = ColorSensor(INPUT_2)
Cl.mode='COL-REFLECT'
Cl.calibrate_white()
print('calibrated')
time.sleep(3)
spkr = Sound()
tank.on(SpeedRPS(.1), SpeedRPS(.1)) 
start = time.perf_counter()
while test:
    

    if len(num) == 4 and num == target_num :
        test = False
    
    elif len(num) == 4 and num != target_num:
        print(num)
        num = ""    
    
    elif Cl.value()>70:
        print('White')
        time.sleep(1.45/2)
        num = num + '0'
    
    elif Cl.value() == 0:
        print('nothing')
        time.sleep(0.1)
        num = ""
    
    elif Cl.value()<10:
        print('black')
        time.sleep(1.45/2)
        num = num + '1'
