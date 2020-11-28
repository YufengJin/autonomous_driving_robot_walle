#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
      
import RPi.GPIO as GPIO          
from time import sleep
import MotionControl as mc


GPIO.setmode(GPIO.BCM)
car = mc.Car(24,23,4,21,20,17,5,6,13)


def callback_front(data):
    if data < 10:
        car.stop()



def callback_back(data):
    if data <10:
        car.stop()   


    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('obstacle_detection', anonymous=True)

    rospy.Subscriber("distance_front", Float64, callback_front)
    rospy.Subscriber("distance_back", Float64, callback_back)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()