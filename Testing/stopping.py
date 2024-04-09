#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor, largemoter
from ev3dev2.sensor import INPUT_1
from time import sleep
sensor = UltrasonicSensor(INPUT_1)
motor = LargeMotor(OUTPUT_D)
distance_in = ultrasonic_sensor.distance_inches

if distance_in < 4:
    motor.stop_action = 'brake'
    motor.stop()

