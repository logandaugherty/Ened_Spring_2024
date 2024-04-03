#!/usr/bin/env python3
# from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent, OUTPUT_B, Motor
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

speaker = Sound()

ultrasonic_sensor = UltrasonicSensor(INPUT_2)

distance_in = ultrasonic_sensor.distance_inches
while distance_in > 1.5:
    distance_in = ultrasonic_sensor.distance_inches
    sleep(0.02)
speaker.speak("Life is full of obstacles, its how you overcome them that matter")

# distance_in = ultrasonic_sensor.distance_inches
# while distance_in > 1.5:
#     distance_in = ultrasonic_sensor.distance_inches
#     speaker.speak("{0:0.2f} inches".format(distance_in))
#     sleep(3)
# speaker.speak("Life is full of obstacles, its how you overcome them that matter")

# while True:
#     distance_in = ultrasonic_sensor.distance_inches
#     speaker.speak("{0:0.2f} inches".format(distance_in))
#     sleep(3)
