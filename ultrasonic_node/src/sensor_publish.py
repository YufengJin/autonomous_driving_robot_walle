# license removed for brevity
import rospy
from std_msgs.msg import Float64
import RPi.GPIO as GPIO
import time
import ultrasonic as ul
GPIO.setmode(GPIO.BCM)

ul.initialize(18,25)  #front
ul.initialize(16,12)  #back

def talker():
    pub = rospy.Publisher('distance_front', Float64, queue_size=10)
    pub = rospy.Publisher('distance_back', Float64, queue_size=10)
    rospy.init_node('UltraSonic', anonymous=True)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        dist_f = ul.entfernung(18,25)
        dist_b = ul.entfernung(16,12)
        rospy.loginfo("distance front: %s", dist_f)
        rospy.loginfo("distance back: %s", dist_b)
        pub.publish(dist_f)
        pub.publish(dist_b)
        rate.sleep()

if __name__ == '__main__':


    try:
        talker()
    except rospy.ROSInterruptException:
        pass
