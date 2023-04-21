#!/usr/bin/env python3
from ev3dev.auto import *
import time
from ev3dev2.motor import LargeMotor,MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank,OUTPUT_B
from time import sleep


Claw = MediumMotor(OUTPUT_B)


Claw.on(SpeedRPS(-1))
Claw.wait_until_not_moving()