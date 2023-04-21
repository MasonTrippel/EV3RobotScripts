#!/usr/bin/env python3
from ev3dev.auto import *
import time
from ev3dev2.motor import LargeMotor,MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank
from time import sleep


tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)

Claw = MediumMotor(OUTPUT_C)


Claw.on_for_seconds(SpeedRPS(1), seconds=3.5)

tank_pair.on_for_seconds(SpeedRPS(1), SpeedRPS(1), seconds=1.74)  

Claw.on(SpeedRPS(-0.5))
Claw.wait_until_not_moving()




