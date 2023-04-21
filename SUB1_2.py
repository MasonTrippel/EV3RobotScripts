#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank,MediumMotor ,SpeedPercent,follow_for_ms
from time import sleep
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import GyroSensor



tank = MoveTank(OUTPUT_A, OUTPUT_D)

tank.gyro = GyroSensor()
tank.gyro.mode = GyroSensor.MODE_GYRO_ANG

tank.gyro.calibrate()

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.5),target_angle=0,follow_for=follow_for_ms,ms = ((5.22*2)*1000))

    
tank.turn_right(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.5),target_angle=90,follow_for=follow_for_ms,ms = ((6.1)*1000))
#tank.on_for_seconds(SpeedRPS(0.5),SpeedRPS(0.5),seconds=(13.9*2))
sleep(5)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.5),target_angle=90,follow_for=follow_for_ms,ms = (((13.9*2)-6.1)*1000))

tank.turn_right(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.5),target_angle=180,follow_for=follow_for_ms,ms = ((5.22*2)*1000))
#tank.on_for_seconds(SpeedRPS(0.5),SpeedRPS(0.5),seconds=(5.22*2))

sleep(10)

#tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(-0.5),target_angle=180,follow_for=follow_for_ms,ms = ((1.74)*1000))
tank.on_for_seconds(SpeedRPS(-0.5),SpeedRPS(-0.5),seconds=(1.74))   


tank.turn_right(speed=SpeedRPS(.3),degrees = 90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.5),target_angle=270,follow_for=follow_for_ms,ms = ((13.9*2)*1000))
#tank.on_for_seconds(SpeedRPS(0.5),SpeedRPS(0.5),seconds=(13.9*2))


tank.turn_left(speed=SpeedRPS(.3),degrees=90)

#tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.5),target_angle=0,follow_for=follow_for_ms,ms = ((1.74)*1000))
tank.on_for_seconds(SpeedRPS(0.5),SpeedRPS(0.5),seconds=(1.74))

tank.stop()