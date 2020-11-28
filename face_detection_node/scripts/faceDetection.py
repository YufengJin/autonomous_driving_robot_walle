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
from servomotor_node.msg import Twoangle
import time

bridge = CvBridge()
angle = Twoangle()


def callback(data):
    
    try:
        img = bridge.compressed_imgmsg_to_cv2(data, desired_encoding = 'bgr8')
    except CvBridgeError as e:
        print(e)
    
    img = cv2.flip(img, -1)
    img_shape = img.shape
    resized_img = cv2.resize(img,(img_shape[1]*2,img_shape[0]*2))



    ### face detection


    faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml') 
    
    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(30, 30)
    )
    #154,205

    for (x,y,w,h) in faces:
 
        servo_pub.publish(angle)
        cv2.rectangle(img,(x/2,y/2),((x+w)//2,(y+h)//2),(255,0,0),1)
        font = cv2.FONT_HERSHEY_COMPLEX
        txt1 = 'W: ' + str(w) + ',' + 'H: ' + str(h)
        cv2.putText(img, txt1, (x, y-5), font, 0.5, (255,255,255), 1, cv2.LINE_AA)
        
        angle_x = np.arctan2((x+w/2-2*img_shape[1])*0.9, 2*img_shape[1])

        angle_y = np.arctan2((y+h/2-2*img_shape[0])*0.6, 2*img_shape[0])
        
        angle.angledown = -angle_x/3.14*180
        angle.angleup = angle_y/3.14*180

        angle.angledown = 0 if abs(angle.angledown)< 5 else angle.angledown
        angle.angleup = 0 if abs(angle.angleup)< 5 else angle.angleup



    
        #servo_pub.publish(angle)


    
    """

    ### green detection



    #image = cv2.flip(image, -1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform a series of dilations and erosions to remove any small blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was
    if len(cnts) > 0:
        # find the largest contour in the mask, then use it to compute the minimum enclosing circle
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if (radius < 300) & (radius > 2) :
            # draw the circle and centroid on the image, then update the list of tracked points
            cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(image, center, 5, (0, 0, 255), -1)
            print(image[int(x),int(y),0],image[int(x),int(y),1],image[int(x),int(y),2])

        else:
        	x = 200
        	y = 154
        if x > 205:
            angle.angledown = 1
        elif x < 195:
            angle.angledown = -1    # turn left
        else:
            angle.angledown = 0 

        if y > 158:
            angle.angleup = -1
        elif y < 150:
            angle.angleup = 1     # turn down
        else:
            angle.angleup = 0

        servo_pub.publish(angle)

    #   print(int(x), int(y))    # print (x, y) center of the ball
    #print(0.21*(320-int(x)), 0.21*(int(y)-240))    # print (x, y) of image
    
    """
    

    ### circle detection

    # center_point, image_output = circle_detection(image)

    # x = center_point[0] if center_point[0] != 200 else 200
    # y = center_point[1] if center_point[1] != 154 else 154
    # servo_publish(x,y)


    
    try:
        image_message = bridge.cv2_to_compressed_imgmsg(img)
        image_pub.publish(image_message)
    except CvBridgeError as e:
        print(e)


    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('walle_Face_Detection', anonymous=True)
    rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    servo_pub = rospy.Publisher('set_camere_angle', Twoangle, queue_size=10)
    image_pub = rospy.Publisher('face_detection/image/compressed', CompressedImage, queue_size=10)
    listener()





