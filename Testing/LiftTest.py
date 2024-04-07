#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent, OUTPUT_B,OUTPUT_D,OUTPUT_A
from time import sleep

liftMtr = MediumMotor(OUTPUT_B)
driveLMtr = LargeMotor(OUTPUT_D)
driveRMtr = LargeMotor(OUTPUT_A)

liftMtr.reset()
liftMtr.on_to_position(-100,550,True)
sleep(0.125)

driveLMtr.on(-20,True,False)
driveRMtr.on(-20,True,False)
sleep(1)
driveLMtr.on(20,True,False)
driveRMtr.on(20,True,False)
sleep(1.3)
driveLMtr.stop()
driveRMtr.stop()

liftMtr.on_to_position(100,100,True)
sleep(5)


# liftMtr.reset()
# liftMtr.on_to_position(-100,-550,False)
# sleep(0.125)

# liftMtr.on_to_position(30,-280,False)
# sleep(1)

# driveLMtr.on(-20,True,False)
# driveRMtr.on(-20,True,False)
# sleep(0.5)
# driveLMtr.on(20,True,False)
# driveRMtr.on(20,True,False)
# sleep(0.7)
# driveLMtr.stop()
# driveRMtr.stop()

# liftMtr.on_to_position(100,10,True)
# sleep(5)
