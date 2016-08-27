#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 树莓派控制四驱小车 '

import RPi.GPIO as GPIO
import time

' 控制左侧的A,C轮子 '
L298N_1_ENA = 11
L298N_1_IN1 = 16
L298N_1_IN2 = 18
L298N_1_IN3 = 22
L298N_1_IN4 = 13
L298N_1_ENB = 15

' 控制右侧的B,D轮子 '
L298N_2_ENA = 29
L298N_2_IN1 = 40
L298N_2_IN2 = 31
L298N_2_IN3 = 33
L298N_2_IN4 = 35
L298N_2_ENB = 37


class Wheel:

    def __init__(self, name, pin_en, pin_1, pin_2):
        self.name = name
        self.pin_en = pin_en
        self.pin_1 = pin_1
        self.pin_2 = pin_2
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_en, GPIO.OUT)
        GPIO.setup(self.pin_1, GPIO.OUT)
        GPIO.setup(self.pin_2, GPIO.OUT)
        self.stop()

    def forward(self):
        GPIO.output(self.pin_en, GPIO.HIGH)
        GPIO.output(self.pin_1, GPIO.HIGH)
        GPIO.output(self.pin_2, GPIO.LOW)

    def back(self):
        GPIO.output(self.pin_en, GPIO.HIGH)
        GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pin_en, GPIO.LOW)
        GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_2, GPIO.LOW)


class Car:

    wheels = [
        Wheel("A", L298N_1_ENA, L298N_1_IN1, L298N_1_IN2),
        Wheel("B", L298N_2_ENA, L298N_2_IN1, L298N_2_IN2),
        Wheel("C", L298N_1_ENB, L298N_1_IN3, L298N_1_IN4),
        Wheel("D", L298N_2_ENB, L298N_2_IN3, L298N_2_IN4)
    ]

    @staticmethod
    def init():
        GPIO.setmode(GPIO.BOARD)

    @staticmethod
    def forward():
        Car.stop()
        for wheel in Car.wheels:
            wheel.forward()

    @staticmethod
    def back():
        Car.stop()
        for wheel in Car.wheels:
            wheel.back()

    @staticmethod
    def turn_left():
        Car.stop()
        Car.wheels[0].back()
        Car.wheels[2].back()
        Car.wheels[1].forward()
        Car.wheels[3].forward()

    @staticmethod
    def turn_right():
        Car.stop()
        Car.wheels[0].forward()
        Car.wheels[2].forward()
        Car.wheels[1].back()
        Car.wheels[3].back()

    @staticmethod
    def stop():
        for wheel in Car.wheels:
            wheel.stop()



#~ if __name__ == '__main__':
#~ 
    #~ try:
        #~ car = Car()
        #~ car.forward()
        #~ time.sleep(2)
        #~ car.back()
        #~ time.sleep(2)
        #~ car.turn_left()
        #~ time.sleep(2)
        #~ car.turn_right()
        #~ time.sleep(2)
        #~ car.stop()
#~ 
    #~ except KeyboardInterrupt:
        #~ pass
#~ 
    #~ GPIO.cleanup()
