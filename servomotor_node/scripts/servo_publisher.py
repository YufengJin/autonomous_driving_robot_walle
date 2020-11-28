import rospy
from servomotor_node.msg import Twoangle

pub = rospy.Publisher('set_camera_angle', Twoangle, queue_size=10)
rospy.init_node('camera_motor_talker')
r = rospy.Rate(5) # 10hz
angle = Twoangle()
angle.angledown = -45
angle.angledown = -45


while not rospy.is_shutdown():
	
	pub.publish(angle)
	r.sleep()