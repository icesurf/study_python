#!/usr/bin/python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

 #参阅树莓派引脚图
GPIO.setmode(GPIO.BCM)
motor1,motor2 = 18,23
GPIO.setup(18, GPIO.OUT)#物理引脚12对应的BCM编码为18
GPIO.setup(23, GPIO.OUT)#物理引脚16对应的BCM编码为23

pwm1 = GPIO.PWM(motor1, 50)
pwm2 = GPIO.PWM(motor2, 50)
pwm1.start(0)
pwm2.start(0)
while True:
    pwm1.ChangeDutyCycle(6)
    time.sleep(2)
    pwm2.ChangeDutyCycle(6)
    time.sleep(2)
    pwm1.ChangeDutyCycle(14)
    #time.sleep(2)
    pwm2.ChangeDutyCycle(14)
    time.sleep(2)
    pwm1.ChangeDutyCycle(3)
    time.sleep(2)
    pwm2.ChangeDutyCycle(3)
    time.sleep(2)
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
    break

        