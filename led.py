# -*- coding: utf-8 -*-  
import RPi.GPIO as GPIO  
import time
# BCM编号方式，基于插座引脚编号  
GPIO.setmode(GPIO.BCM)  
# 输出模式  
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
#GPIO.setup(12,GPIO.OUT)
num=(1,2,3,4,5,6,7,8,9)



for item in num:
    print (item)
    if item == 1 :
        while True:
            GPIO.output(13, GPIO.HIGH) 
            print("THE LED_GREEN IS ON NOW")
            time.sleep(3)
            GPIO.output(13,GPIO.LOW)
            print("THE LED_GREEN IS OFF NOW")
            time.sleep(1)
            break  
    if item == 2 :
        while True:
            GPIO.output(26, GPIO.HIGH) 
            print("THE LED_RED IS ON NOW")
            time.sleep(5)
            GPIO.output(26,GPIO.LOW)
            print("THE LED_RED IS OFF NOW")
            time.sleep(1)
            break  
    if item == 3 :
        while True:
            GPIO.output(19, GPIO.HIGH) 
            print("THE LED_YELLOW IS ON NOW")
            time.sleep(1)
            GPIO.output(19,GPIO.LOW)
            print("THE LED_YELLOW IS OFF NOW")
            time.sleep(5)
            break 



       

