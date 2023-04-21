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
start = time.perf_counter()
while test:
    print(Cl.value())
    time.sleep(0.1)
    