#!/usr/bin/env python3
from ev3dev.auto import *
import time
from ev3dev2.motor import LargeMotor,MediumMotor,follow_for_ms,SpeedPercent
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank
from time import sleep




tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)

gyro = GyroSensor(INPUT_1)
gyro.mode = GyroSensor.MODE_GYRO_ANG



tank_pair.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedPercent(30),target_angle=0,follow_for=follow_for_ms,ms=5000)



tank_pair.stop()