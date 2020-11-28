import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Servo_motor(object):
    def __init__(self,servo1_pin,servo2_pin):
        self.servo1_pin = servo1_pin
        self.servo2_pin = servo2_pin
        self.angledown = 0
        self.angleup = 0
        self.initialize()
        self.pwm1 = GPIO.PWM(self.servo1_pin,50)
        self.pwm2 = GPIO.PWM(self.servo2_pin,50)
        self.pwm1.start(7.5)
        self.pwm2.start(7.5)
    
    def initialize(self):
        GPIO.setup(self.servo1_pin,GPIO.OUT)
        GPIO.setup(self.servo2_pin,GPIO.OUT)

    def setAngle(self, angledown, angleup):

        if angledown < -75 or angledown > 75 or angleup < -45 or angleup > 45:
            pass
        else:
            self.pwm1.ChangeDutyCycle(angledown/18+7.5) 
            self.pwm2.ChangeDutyCycle(angleup/18+7.5) 
            sleep(0.25)

    def changeAngle(self, angledown, angleup):
        if angledown == 1:
            self.angledown += 3
            
        elif angledown == -1:
            self.angledown -= 3
           
        if angleup == 1:
            self.angleup -= 3

        elif angleup == -1:
            self.angleup += 3

        self.setAngle(self.angledown,self.angleup)


    def stop(self):
        self.pwm1.stop()
        self.pwm2.stop()
        



