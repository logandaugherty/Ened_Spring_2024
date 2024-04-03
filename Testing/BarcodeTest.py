#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent, OUTPUT_B
from time import sleep

liftMtr = MediumMotor(OUTPUT_B)

liftMtr.reset()

# while True:
#     liftMtr.on_to_position(-30,-550,False)
#     sleep(3)
#     liftMtr.on_to_position(30,0,False)
#     sleep(3)

while True:
    liftMtr.on_to_position(-30,-550,False)
    sleep(3)    
    liftMtr.on_to_position(30,0,False)
    sleep(3)    
    liftMtr.on_to_position(-30,-550,False)
    sleep(3)    
    liftMtr.on_to_position(30,0,False)
    sleep(3)        
    liftMtr.on_to_position(-30,-550,False)
    sleep(3)
    liftMtr.on_to_position(50,-170,False)
    sleep(3)
    liftMtr.on_to_position(-100,-360,False)
    sleep(3)    
