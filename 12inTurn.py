#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,SpeedDPS, SpeedRPM, SpeedRPS,SpeedPercent, SpeedDPM, MoveTank 
from time import sleep
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import GyroSensor


#initialize motor setup and gyro
tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)
gyro = GyroSensor(INPUT_1)
gyro.mode = GyroSensor.MODE_GYRO_ANG

#move forwrd
tank_pair.on_for_seconds(SpeedRPS(1), SpeedRPS(1), seconds=1.74) 
sleep(1)
#calibrate gyro
gyro.calibrate()

tank_pair.turn_degrees(
    speed=SpeedPercent(5),
    target_angle=30
)

#turn
while gyro.angle<80 and gyro.angle>-80:
    tank_pair.on_for_seconds(SpeedRPS(0.4), SpeedRPS(-.4), seconds=0.2) 
    sleep(0.1)   
#increment to turn
while gyro.angle<=90 and gyro.angle>=-90:
    tank_pair.on_for_seconds(SpeedRPS(0.1), SpeedRPS(-.1), seconds=.2) 
    sleep(0.3)   
    
#move forward again
tank_pair.on_for_seconds(SpeedRPS(1), SpeedRPS(1), seconds=1.74)     

