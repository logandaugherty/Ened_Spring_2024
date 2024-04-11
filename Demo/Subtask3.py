#!/usr/bin/env python3
from CustomMotorGroup import *
from ev3dev2.sensor import INPUT_2
from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_B
from ev3dev2.sound import Sound
from Qrcodescanner import checkBox
from Subtask4 import Subtask4
from Subtask3b import Subtask3b

# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE
# Did the Subtask 1 succeed? If so, set this to true
box_id = "1010"

# -------------------------------------------------------------


# ----- CONSTANTS
BOX_MARGIN_X = 2.25

# ---------- INITIALIZATION -----
drive = MotorGroup()
drive.init()

# Drive towards box (15)
to_box_fwd = BOX_MARGIN_X + 15
drive.drive_in(to_box_fwd)

drive.turn_ang_rel(90)

Subtask3b(box_id,drive)