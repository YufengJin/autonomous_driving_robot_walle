#!/usr/bin/env python
import rospy
from servomotor_node.msg import Twoangle  
import RPi.GPIO as GPIO          
from time import sleep
from servo_motor import Servo_motor

servo_pin1 = 19
servo_pin2 = 26

GPIO.setmode(GPIO.BCM)
servo = Servo_motor(servo_pin1,servo_pin2)


def callback(data):
    servo.changeAngle(data.angledown, data.angleup)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('camera_motor_listener', anonymous=True)

    rospy.Subscriber("set_camere_angle", Twoangle , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()