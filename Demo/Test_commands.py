#!/usr/bin/env python3
from Support.CustomMotorGroup import *

drive = MotorGroup()
drive.init()

drive.drive_in(20)

drive.turn_ang_rel(90)

drive.drive_in(20)

drive.turn_ang_rel(90)

drive.drive_in(20)

drive.turn_ang_abs(0)