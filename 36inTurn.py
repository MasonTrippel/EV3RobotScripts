#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank 
from time import sleep
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import GyroSensor



tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)

gyro = GyroSensor(INPUT_1)
gyro.mode = GyroSensor.MODE_GYRO_ANG

tank_pair.on_for_seconds(SpeedRPS(1), SpeedRPS(1), seconds=1.74) 

sleep(1)
gyro.calibrate()
while gyro.angle<80 and gyro.angle>-80:
    tank_pair.on_for_seconds(SpeedRPS(0.4), SpeedRPS(-.4), seconds=0.2) 
    sleep(0.1)   

while gyro.angle<=90 and gyro.angle>=-90:
    tank_pair.on_for_seconds(SpeedRPS(0.1), SpeedRPS(-.1), seconds=.2) 
    sleep(0.3)   
    

tank_pair.on_for_seconds(SpeedRPS(1), SpeedRPS(1), seconds=5)   

