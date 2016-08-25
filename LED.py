#!/usr/bin/env python3
# coding: utf8

import RPi.GPIO as GPIO
import time

PIN_NO = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NO, GPIO.OUT)

pwm = GPIO.PWM(PIN_NO, 50)
pwm.start(0)

try:
    while True:
        for i in xrange(0, 101, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.03)
        for i in xrange(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.03)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
