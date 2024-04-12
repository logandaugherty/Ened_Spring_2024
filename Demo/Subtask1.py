#!/usr/bin/env python3
from time import sleep
from CustomMotorGroup import *

# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE
# Box Number
# Numbered like the guide on canvas
# 7-12 on top
box_num = 12

# -------------------------------------------------------------

# ----- CONSTANTS
BOX_MARGIN_X = 0

# ---------- INITIALIZATION -----
drive = MotorGroup()
drive.init()

# ---- GET TO BOX 
# Exit home and drive to correct Y level of target
leave_home_fwd = 12 + 24 * bool(box_num >= 7)
drive.drive_in(leave_home_fwd)

drive.turn_ang_rel(90)

# Drive towards box
to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6)
drive.drive_in(to_box_fwd)

# drive.turn_ang_rel(90)

sleep(5)

# drive.turn_ang_rel(-90)

# Drive towards side aisle of home
fwd = 96 - to_box_fwd
drive.drive_in(fwd)

drive.turn_ang_rel(90)

# Drive towards home B
drive.drive_in(leave_home_fwd)