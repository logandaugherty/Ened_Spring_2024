#!/usr/bin/env python3
from CustomMotorGroup import *

# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE
# Did the Subtask 1 succeed? If so, set this to true
Continuing_subtask1_program = False

# -------------------------------------------------------------

# ---------- INITIALIZATION -----
drive = MotorGroup()

if not Continuing_subtask1_program:
    drive.init()

drive.drive_in(-12)

drive.turn_ang_rel(90)

drive.drive_in(96)

drive.turn_ang_rel(-90)

drive.drive_in(12)

drive.turn_ang_abs(180)
