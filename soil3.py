#!/usr/bin/python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

 #参阅树莓派引脚图
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)#物理引脚12对应的BCM编码为18,humidity
GPIO.setup(4, GPIO.OUT)#物理引脚7对应的BCM编码为4,red
GPIO.setup(17, GPIO.OUT)#物理引脚11对应的BCM编码为17,green
GPIO.setup(27, GPIO.OUT)#物理引脚对13应的BCM编码为27,Water

humidity=18
red=4
green=17
water=27


while True:
        if GPIO.input(humidity) == GPIO.LOW:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(water, GPIO.LOW) 
            print ("土壤：潮湿 \n绿色信号灯亮 \n停止洒水 \n-------------")
            time.sleep(1) #检测结果潮湿，1秒钟后再次检测土壤湿度
        else:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(water, GPIO.HIGH)
            print ("土壤：干燥 \n红色信号灯亮 \n开始洒水 \n-------------")
            time.sleep(1) #检测结果干燥，启动洒水，每隔1秒检测1次

