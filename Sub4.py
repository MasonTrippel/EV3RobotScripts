#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,OUTPUT_B,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, SpeedPercent,MediumMotor,follow_for_ms
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import GyroSensor,ColorSensor
from ev3dev2.sound import Sound


tank = MoveTank(OUTPUT_A, OUTPUT_D)

tank.gyro = GyroSensor()
tank.gyro.mode = GyroSensor.MODE_GYRO_ANG
tank.gyro.calibrate()

Claw = MediumMotor(OUTPUT_B)

#tank.on_for_seconds(SpeedRPS(0.25),SpeedRPS(0.25),seconds=(3.5*2))
tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=0,follow_for=follow_for_ms,ms = ((7.4)*1000))

Claw.on(SpeedRPS(-0.5))
Claw.wait_until_not_moving()

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(-0.25),target_angle=0,follow_for=follow_for_ms,ms = ((7.4-6.95)*1000))
#tank.on_for_seconds(SpeedRPS(-0.25),SpeedRPS(-0.25),seconds=(3.5*2))

tank.turn_left(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=-90,follow_for=follow_for_ms,ms = ((2.9))*1000)
#tank.on_for_seconds(SpeedRPS(0.25),SpeedRPS(0.25),seconds=((feetTillEnd*3.5/2)*12))

tank.turn_left(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=-180,follow_for=follow_for_ms,ms = ((13.92)*1000)

tank.turn_left(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=-270,follow_for=follow_for_ms,ms = ((15.66)*1000)

tank.turn_right(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=-180,follow_for=follow_for_ms,ms = ((2.5)*1000)


Claw.on_for_seconds(SpeedRPS(1), seconds=3.5)

time.sleep(10)

