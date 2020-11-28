'''
Haar Cascade Face and Eye detection with OpenCV  
	Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  

Adapted by Marcelo Rovai - MJRoBot.org @ 22Feb2018 
'''

#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage
import matplotlib.pyplot as plt
from LaneDetectionFunction import *


bridge = CvBridge()


def process_video(image):
    imshape = image.shape
    gray = grayscale(image)

    kernel_size = 5
    low_threshold = 50
    high_threshold = 150
    blur_gray = gaussian_blur(gray,kernel_size)
    masked_edges = canny(blur_gray, low_threshold, high_threshold)

    vertices = np.array([[(0, imshape[0]), (465, 310), (475, 310), (imshape[1], imshape[0])]], dtype=np.int32)
    regioned_masked_edges = region_of_interest(masked_edges,vertices)

    rho = 2
    theta = np.pi / 180
    threshold = 45
    min_line_length = 40
    max_line_gap = 100

    line_image = np.copy(image)*0

    lines = cv2.HoughLinesP(regioned_masked_edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)

    color_edges = np.dstack((masked_edges, masked_edges, masked_edges))
    combo = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    return combo

def callback(data):

    try:
        img = bridge.compressed_imgmsg_to_cv2(data, desired_encoding = 'passthrough')
    except CvBridgeError as e:
        print(e)
          
    combo = process_video(img)

    cv2.imshow('Detected Lanes', combo)
    k = cv2.waitKey(1) 

     


    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('lane_detection_node', anonymous=True)

    rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()