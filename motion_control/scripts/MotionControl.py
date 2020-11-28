import RPi.GPIO as GPIO          
from time import sleep,time


def set_dc(channel,frequence,duty_cycle):
    p=GPIO.PWM(channel,frequence)
    p.start(duty_cycle)
    return p


def initialize(car):
    
    GPIO.setup(car.ml_in1,GPIO.OUT)
    GPIO.setup(car.ml_in2,GPIO.OUT)
    GPIO.setup(car.ml_en,GPIO.OUT)

    GPIO.setup(car.mr_in1,GPIO.OUT)
    GPIO.setup(car.mr_in2,GPIO.OUT)
    GPIO.setup(car.mr_en,GPIO.OUT)

    GPIO.output(car.ml_in1,GPIO.LOW)
    GPIO.output(car.ml_in2,GPIO.LOW)   
    GPIO.output(car.mr_in1,GPIO.LOW)   
    GPIO.output(car.mr_in2,GPIO.LOW)   



class Car():
    def __init__(self, pin1, pin2, pin3, pin4, pin5, pin6, flpin,frpin,bpin):
        self.ml_in1 = pin1
        self.ml_in2 = pin2
        self.ml_en  = pin3
        self.mr_in1 = pin4
        self.mr_in2 = pin5
        self.mr_en  = pin6
        self.flpin = flpin
        self.frpin = frpin
        self.bpin = bpin
        self.initialize()
        self.p1 = set_dc(self.ml_en,1000,50)
        self.p2 = set_dc(self.mr_en,1000,50)  

    def initialize(self):
    
        GPIO.setup(self.ml_in1,GPIO.OUT)
        GPIO.setup(self.ml_in2,GPIO.OUT)
        GPIO.setup(self.ml_en,GPIO.OUT)

        GPIO.setup(self.mr_in1,GPIO.OUT)
        GPIO.setup(self.mr_in2,GPIO.OUT)
        GPIO.setup(self.mr_en,GPIO.OUT)

        GPIO.setup(self.flpin,GPIO.OUT)
        GPIO.setup(self.frpin,GPIO.OUT)
        GPIO.setup(self.bpin,GPIO.OUT)

        GPIO.output(self.ml_in1,GPIO.LOW)
        GPIO.output(self.ml_in2,GPIO.LOW)   
        GPIO.output(self.mr_in1,GPIO.LOW)   
        GPIO.output(self.mr_in2,GPIO.LOW) 


    def turn_light(self,direction=1,LEDon=False):
    	# direction 1 is turn right
		while LEDon:
			if direction:
				GPIO.output(self.frpin,GPIO.HIGH)
				sleep(0.5)
				GPIO.output(self.frpin,GPIO.LOW)
				sleep(0.5)
			else:
				GPIO.output(self.flpin,GPIO.HIGH)
				sleep(0.5)
				GPIO.output(self.flpin,GPIO.LOW)
				sleep(0.5)
				
		GPIO.output(self.flpin,GPIO.LOW)
		GPIO.output(self.frpin,GPIO.LOW)

    def stop(self):
        GPIO.output(self.ml_in1,GPIO.LOW)
        GPIO.output(self.ml_in2,GPIO.LOW)
        GPIO.output(self.mr_in1,GPIO.LOW)
        GPIO.output(self.mr_in2,GPIO.LOW)
        GPIO.output(self.bpin,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(self.bpin,GPIO.LOW)
     
    def forward(self, speed = 50):
        GPIO.output(self.ml_in1,GPIO.HIGH)
        GPIO.output(self.ml_in2,GPIO.LOW)
        GPIO.output(self.mr_in1,GPIO.HIGH)
        GPIO.output(self.mr_in2,GPIO.LOW)
        GPIO.output(self.bpin,GPIO.LOW)
        GPIO.output(self.flpin,GPIO.LOW)
        GPIO.output(self.frpin,GPIO.LOW)
    
        #print("Forward  Speed: {} Time: {}".format(speed, time))
        self.p1.ChangeDutyCycle(speed)   
        self.p2.ChangeDutyCycle(speed)
        
        
    
    def backward(self, speed=50 ):
        GPIO.output(self.ml_in1,GPIO.LOW)
        GPIO.output(self.ml_in2,GPIO.HIGH)
        GPIO.output(self.mr_in1,GPIO.LOW)
        GPIO.output(self.mr_in2,GPIO.HIGH)
        GPIO.output(self.bpin,GPIO.HIGH)
        GPIO.output(self.flpin,GPIO.LOW)
        GPIO.output(self.frpin,GPIO.LOW)

    
        #print("Forward  Speed: {} Time: {}".format(speed, time))
        self.p1.ChangeDutyCycle(speed)   
        self.p2.ChangeDutyCycle(speed)    
    
    
    def turn(self, direction, speed):
        self.p1.ChangeDutyCycle(speed)
        self.p2.ChangeDutyCycle(speed)
        

        if direction:
            GPIO.output(self.ml_in1,GPIO.HIGH)
            GPIO.output(self.ml_in2,GPIO.LOW)
            GPIO.output(self.mr_in1,GPIO.LOW)
            GPIO.output(self.mr_in2,GPIO.HIGH)
            

        else:
            GPIO.output(self.ml_in1,GPIO.LOW)
            GPIO.output(self.ml_in2,GPIO.HIGH)
            GPIO.output(self.mr_in1,GPIO.HIGH)
            GPIO.output(self.mr_in2,GPIO.LOW)

    
    
  


      




