#!/usr/bin/env python3
from ev3dev.auto import *
import time
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank
from time import sleep


tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)

tank_pair.on_for_seconds(SpeedRPS(1), SpeedRPS(1), seconds=8.5)   





