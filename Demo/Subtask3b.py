#!/usr/bin/env python3
from CustomMotorGroup import *
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_2
from time import sleep
from Qrcodescanner import checkBox
from Subtask4 import Subtask4
from ev3dev2.sound import Sound


# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE
# Did the Subtask 1 succeed? If so, set this to true
box_id_3b = "0011"

# -------------------------------------------------------------

def Subtask3b(box_id, drive):
    # ---------- INITIALIZATION -----
    ultrasonic_sensor = UltrasonicSensor(INPUT_2)

    time_s = 0.5
    target_speed = 4

    # delta_t = 0.05
    # n = time_s/delta_t
    # increment = target_speed/n
    # for i in range(int(n)):
    #     # start_rotation = drive.m1.position
    #     drive.m1.on(i*increment,True,False)
    #     drive.m2.on(i*increment,True,False)
    #     sleep(delta_t)
    drive.m1.on(target_speed,True,False)
    drive.m2.on(target_speed,True,False)

    while ultrasonic_sensor.distance_inches > 1.3:
        sleep(0.02)

    drive.m1.stop()
    drive.m2.stop()

    sleep(1)

    if checkBox(box_id):
        sleep(5)
        Subtask4(drive)
    else:
        speaker = Sound()
        speaker.speak('Wrong Box!')

# Main logic
if __name__ == "__main__":
    drive = MotorGroup()
    drive.init()
    Subtask3b(box_id_3b, drive)
