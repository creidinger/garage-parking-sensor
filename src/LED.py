import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)

print(GPIO.getmode())
print(GPIO.RPI_INFO)
print(GPIO.VERSION)

for _ in range(1000):
    # print('LED On')
    GPIO.output(3, GPIO.HIGH)

    time.sleep(1)

    # print('LED Off')
    GPIO.output(3, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup(3)
