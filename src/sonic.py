# https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython
import os
import time

import RPi.GPIO as GPIO
import board
import adafruit_hcsr04

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance))
    except RuntimeError:
        print('Retrying')
    time.sleep(0.1)
