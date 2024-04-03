#!/usr/bin/env python3
from time import sleep
from CustomMotorGroup import *

# -------------------------------------------------------------

# STRAIGHT LINE TEST
# Robot drives forward a set amount of inches

# ENTER DATA HERE

# Distance (in inches)
# Enter the distance to drive in the unit of inches
DISTANCE_INCHES = 24

# -------------------------------------------------------------

# Create motor set
motor_group = MotorGroup()

MIN_SPEED_FWD = 4
MAX_SPEED_FWD = 24

# Reset gyro rotation
motor_group.reset_encoders()

sleep(2)

# Drive away from origin
motor_group.move_distance_in(MIN_SPEED_FWD,MAX_SPEED_FWD,DISTANCE_INCHES,0,True)

sleep(2)