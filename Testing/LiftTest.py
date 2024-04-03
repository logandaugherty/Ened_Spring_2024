#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent, OUTPUT_B,OUTPUT_D,OUTPUT_C
from time import sleep

liftMtr = MediumMotor(OUTPUT_B)
driveLMtr = LargeMotor(OUTPUT_D)
driveRMtr = LargeMotor(OUTPUT_C)

liftMtr.reset()
liftMtr.on_to_position(-30,-550,False)
sleep(0.125)

liftMtr.on_to_position(-30,-170,False)
sleep(3)

driveLMtr.on(-20,True,False)
driveRMtr.on(-20,True,False)
sleep(0.5)
driveLMtr.on(20,True,False)
driveRMtr.on(20,True,False)
sleep(0.5)
driveLMtr.stop()
driveRMtr.stop()

liftMtr.on_to_position(-100,-360,False)
sleep(5)