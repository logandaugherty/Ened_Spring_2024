#!/usr/bin/env python3
from time import sleep
from CustomMotorGroup import MotorGroup

# -------------------------------------------------------------

# TURNING TEST
# Robot drives 12 inches forward, turns 90 degrees

# ENTER DATA HERE

# Distance (in inches)
# Enter the distance to drive after the turn
DISTANCE_2_INCHES = 12

# -------------------------------------------------------------
# Create motor set
motor_group = MotorGroup()

MIN_SPEED_FWD = 4
MAX_SPEED_FWD = 25

MIN_SPEED_TURN = 4
# MAX_SPEED_TURN = 12
MAX_SPEED_TURN = 25
# Store the amount of motor degrees to allot for speeding up or slowing down
SLOW_SPEED_DEG_TURN = 30
END_DEG_TURN = 179
END_DEG_TURN_SECOND = 0

# Reset gyro rotation
motor_group.reset_gryo()

# Wait 2 seconds for gyro callibration
sleep(2)


# Reset motor rotation
motor_group.reset_encoders()

# # Drive forward with speeding up and slowing down
# motor_group.move_distance_in(MIN_SPEED_FWD,MAX_SPEED_FWD,12,0,True)

# # Wait for motors to settle
# sleep(0.4)

# Rotate back to the origin
motor_group.on_to_gyro_rotation(MIN_SPEED_TURN,MAX_SPEED_TURN,SLOW_SPEED_DEG_TURN)
motor_group.on_to_gyro_rotation(MAX_SPEED_TURN,MAX_SPEED_TURN,180-SLOW_SPEED_DEG_TURN)
motor_group.on_to_gyro_rotation(MAX_SPEED_TURN,MIN_SPEED_TURN,180,True)

# # Wait for motors to settle
# sleep(0.4)

# motor_group.move_distance_in(MIN_SPEED_FWD,MAX_SPEED_FWD,DISTANCE_2_INCHES,0,True)

# Wait for motors to settle
sleep(2)