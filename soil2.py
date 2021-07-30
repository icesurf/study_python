#!/usr/bin/python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

 #参阅树莓派引脚图
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)#物理引脚12对应的BCM编码为18
GPIO.setup(4, GPIO.OUT)#物理引脚7对应的BCM编码为4

while True:
        if GPIO.input(18) == GPIO.LOW:
            GPIO.output(4, GPIO.LOW)
            print ("土壤：潮湿 \n信号灯灭 \n停止洒水")
            time.sleep(5) #检测结果潮湿，5秒钟后再次检测土壤湿度
        else:
            GPIO.output(4, GPIO.HIGH)
            print ("土壤：干燥 \n信号灯亮 \n开始洒水")
            time.sleep(1) #检测结果干燥，启动洒水，每隔1秒检测1次

