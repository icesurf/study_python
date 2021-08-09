import time
from apscheduler.schedulers.background import BackgroundScheduler
import RPi.GPIO as GPIO
import time

 #参阅树莓派引脚图
GPIO.setmode(GPIO.BCM)
motor1,motor2 = 18,23
GPIO.setup(18, GPIO.OUT)#物理引脚12对应的BCM编码为18
GPIO.setup(23, GPIO.OUT)#物理引脚16对应的BCM编码为23



def fish():
    print('干活时间到:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("开始喂鱼")  
    pwm1 = GPIO.PWM(motor1, 50)
    pwm2 = GPIO.PWM(motor2, 50)
    pwm1.start(0)
    pwm2.start(0)
    pwm1.ChangeDutyCycle(6)
    time.sleep(1)
    pwm2.ChangeDutyCycle(6)
    time.sleep(1)
    #pwm1.ChangeDutyCycle(14)
    time.sleep(1)
    pwm2.ChangeDutyCycle(14)
    time.sleep(1)
    pwm1.ChangeDutyCycle(3)
    time.sleep(1)
    pwm2.ChangeDutyCycle(3)
    time.sleep(1)
    pwm1.stop()
    pwm2.stop()
    #GPIO.cleanup()
    #break
if __name__ == '__main__':
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用date的方式，在特定时间里执行一次
    #scheduler.add_fish(fish, 'date', run_date='2021-08-10 02:03:00')
    
    #采用interval的方式，每隔多长时间执行一次
    scheduler.add_job(fish, 'interval', seconds=10)

    # 采用cron的方式，固定时间循环:hour = '+时'，minute = ‘+分’ ，cecond = ‘+秒
    #scheduler.add_job(job, 'cron', second = '00')
    # 这是一个独立的线程
    scheduler.start()
