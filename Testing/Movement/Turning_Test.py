#!/usr/bin/env python3
from time import sleep
from CustomMotorGroup import MotorGroup

# -------------------------------------------------------------

# TURNING TEST
# Robot turns 90 degrees

# -------------------------------------------------------------
# Create motor set
motor_group = MotorGroup()

MIN_SPEED_FWD = 4
MAX_SPEED_FWD = 25

MIN_SPEED_TURN = 4
MAX_SPEED_TURN = 12
# MAX_SPEED_TURN = 25
# Store the amount of motor degrees to allot for speeding up or slowing down
SLOW_SPEED_DEG_TURN = 30
END_DEG_TURN = 179
END_DEG_TURN_SECOND = 0

# Reset gyro rotation
motor_group.reset_gryo()
motor_group.reset_encoders()

# Wait 2 seconds for gyro callibration
sleep(2)


# Reset motor rotation
counter = 0
while(True):
    offset = counter*90
    # Rotate back to the origin
    motor_group.on_to_gyro_rotation(MIN_SPEED_TURN,MAX_SPEED_TURN,offset + SLOW_SPEED_DEG_TURN)
    motor_group.on_to_gyro_rotation(MAX_SPEED_TURN,MAX_SPEED_TURN,offset + 90-SLOW_SPEED_DEG_TURN)
    motor_group.on_to_gyro_rotation(MAX_SPEED_TURN,MIN_SPEED_TURN,offset + 90,True)
    counter+=1
    sleep(5)


# Wait for motors to settle
sleep(2)