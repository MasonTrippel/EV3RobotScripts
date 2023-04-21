#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D,OUTPUT_B,SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, SpeedPercent,MediumMotor,follow_for_ms
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import GyroSensor,ColorSensor
from ev3dev2.sound import Sound


test = True
target_num = "0001"
num = ""

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
tank.on(SpeedRPS(.1), SpeedRPS(.1)) 
start = time.perf_counter()
while test:
    

    if len(num) == 4 and num == target_num :
        test = False
    
    elif len(num) == 4 and num != target_num:
        print(num)
        num = ""    
    
    elif Cl.value()>70:
        print('White')
        time.sleep(.7)
        num = num + '0'
    
    elif Cl.value() == 0:
        print('nothing')
        time.sleep(0.1)
        num = ""
    
    elif Cl.value()<10:
        print('black')
        time.sleep(.7)
        num = num + '1'


end = time.perf_counter()

total = (end - start)

feetTraveled = ((total/1.74))/10

feetTillEnd = 3 - feetTraveled

print(num)

#tank.on_for_seconds(SpeedRPS(-0.25),SpeedRPS(-0.25),seconds=(total/2.5))

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(-0.25),target_angle=0,follow_for=follow_for_ms,ms = ((total/2.5)*1000))

tank.turn_left(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=-90,follow_for=follow_for_ms,ms = ((6.95)*1000))

#tank.on_for_seconds(SpeedRPS(0.25),SpeedRPS(0.25),seconds=6.95)

tank.turn_right(speed=SpeedRPS(.3),degrees=90)

#tank.on_for_seconds(SpeedRPS(0.25),SpeedRPS(0.25),seconds=(total/2.5))

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=0,follow_for=follow_for_ms,ms = ((total/2.5)*1000))

tank.turn_right(speed=SpeedRPS(.3),degrees=90)

Claw.on_for_seconds(SpeedRPS(1), seconds=3.5)

#tank.on_for_seconds(SpeedRPS(0.25),SpeedRPS(0.25),seconds=(3.5*2))
tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=90,follow_for=follow_for_ms,ms = ((7.4)*1000))

Claw.on(SpeedRPS(-0.5))
Claw.wait_until_not_moving()

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(-0.25),target_angle=90,follow_for=follow_for_ms,ms = ((7.4-6.95)*1000))
#tank.on_for_seconds(SpeedRPS(-0.25),SpeedRPS(-0.25),seconds=(3.5*2))

tank.turn_left(speed=SpeedRPS(.3),degrees=90)

tank.follow_gyro_angle(kp=11.3, ki=0.05, kd=3.2,speed=SpeedRPS(0.25),target_angle=0,follow_for=follow_for_ms,ms = ((feetTillEnd*6.95))*1000)
#tank.on_for_seconds(SpeedRPS(0.25),SpeedRPS(0.25),seconds=((feetTillEnd*3.5/2)*12))


Claw.on_for_seconds(SpeedRPS(1), seconds=3.5)

time.sleep(10)

