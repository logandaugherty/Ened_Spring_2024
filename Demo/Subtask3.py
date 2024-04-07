#!/usr/bin/env python3
from CustomMotorGroup import *
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_2
from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_B
from ev3dev2.sound import Sound

# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE
# Did the Subtask 1 succeed? If so, set this to true
box_num = 9

# -------------------------------------------------------------


# ----- CONSTANTS
BOX_MARGIN_X = 2.25

# ---------- INITIALIZATION -----
drive = MotorGroup()
ultrasonic_sensor = UltrasonicSensor(INPUT_2)
drive.init()
speaker = Sound()
liftMtr = MediumMotor(OUTPUT_B)
liftMtr.reset()

# Drive towards box
to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6)
drive.drive_in(to_box_fwd)

drive.turn_ang_rel(90)

start_rotation = drive.m1.position
drive.m1.on(20,True,False)
drive.m2.on(20,True,False)
while ultrasonic_sensor.distance_inches > 1.5:
    sleep(0.02)
drive.m1.stop()
drive.m2.stop()

sleep(1)

liftMtr.on_to_position(100,100,True)

scan_success = True
if scan_success:
    speaker.speak('This box is correct')
else:
    speaker.speak('This box is not correct')