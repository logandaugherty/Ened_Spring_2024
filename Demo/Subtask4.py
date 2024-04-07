#!/usr/bin/env python3
from CustomMotorGroup import *
from ev3dev2.motor import MediumMotor, OUTPUT_B

# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE
# Did the Subtask 1 succeed? If so, set this to true
box_num = 9

# -------------------------------------------------------------

# ----- CONSTANTS
BOX_MARGIN_X = 0

# ---------- INITIALIZATION -----
drive = MotorGroup()
drive.init()
liftMtr = MediumMotor(OUTPUT_B)
liftMtr.reset()

liftMtr.reset()
liftMtr.on_to_position(-100,550,True)
sleep(0.125)

drive.m1.on(-20,True,False)
drive.m2.on(-20,True,False)
sleep(1)
drive.m1.on(20,True,False)
drive.m2.on(20,True,False)
sleep(1.3)
drive.m1.stop()
drive.m2.stop()

liftMtr.on_to_position(100,100,True)

drive.drive_in(-6)

drive.turn_ang_rel(-90)

to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6)
fwd = 54 - to_box_fwd
fwd -= 12
drive.drive_in(fwd)

liftMtr.on_to_position(-100,550,True)
drive.drive_in(-6)
