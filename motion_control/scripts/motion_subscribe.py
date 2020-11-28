#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist  

import RPi.GPIO as GPIO          
from time import sleep
import MotionControl as mc

GPIO.setmode(GPIO.BCM)
car = mc.Car(24,23,4,21,20,17,5,6,13)

def callback(data):
    
    speed = data.linear.x*100
    turnspeed = data.angular.z*50
    print("Speed: ", speed)
    print("Turn speed: ", turnspeed)
    speed = 100 if speed > 100 else speed
    speed = -100 if speed < -100 else speed
    speed = 50 if 0 < speed < 50 else speed
    speed = -50 if -50 < speed < 0 else speed
    
    turnspeed = 100 if turnspeed > 100 else turnspeed
    turnspeed = -100 if turnspeed < -100 else turnspeed
    turnspeed = 60 if 0 < turnspeed < 60 else turnspeed
    turnspeed = -60 if -60 < turnspeed < 0 else turnspeed

    if speed > 0 and turnspeed ==0:
        car.forward(speed)  #go foward

    elif speed < 0 and turnspeed == 0:
        car.backward(-speed)

    elif turnspeed > 0 and speed == 0:
        car.turn(0,turnspeed)    #turn right

    elif turnspeed < 0 and speed == 0:
        car.turn(1,-turnspeed)

    elif turnspeed == 0 and speed == 0:
        car.stop()



    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('walle_move_listener', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    listener()

        

        
