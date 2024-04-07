#!/usr/bin/env python3
from CustomMotorGroup import *
from ev3dev2.sound import Sound


speaker = Sound()

drive = MotorGroup()
drive.init()

drive.drive_in(10)
drive.drive_in(10)

drive.turn_ang_rel(90)

drive.drive_in(15)

drive.turn_ang_rel(90)

drive.drive_in(15)

drive.turn_ang_rel(90)

drive.drive_in(15)

drive.turn_ang_abs(0)
