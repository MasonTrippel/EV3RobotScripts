#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank,SpeedRPS, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_1

# Instantiate the MoveTank object
tank = MoveTank(OUTPUT_A, OUTPUT_D)

# Initialize the tank's gyro sensor
tank.gyro = GyroSensor(INPUT_1)

# Calibrate the gyro to eliminate drift, and to initialize the current angle as 0
tank.gyro.calibrate()


    # Follow the target_angle for 4500ms
tank.follow_gyro_angle(
kp=11.3, ki=0.05, kd=3.2,
speed=SpeedRPS(.5),
target_angle=0,
follow_for=follow_for_ms,
ms=4500)

tank.stop()