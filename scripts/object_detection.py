#!/usr/bin/env python

#Simple object detection node taking in data from uSharp patch
# Author: Andrew Megaris
# Date: 5/16/2017
# Email: andrew@aerotenna.com
# Github: https://github.com/andrewmegaris

import roslib;
import rospy
from std_msgs.msg import String

#Define you close / medium / long ranges
#Ranges are in CM
SHORT_RANGE = 300  #maximum distance for a short range classification
MEDIUM_RANGE = 550 #maximum distance for a medium range classification
LONG_RANGE = 1000  #minimum distance for a long range classification

sCount = mCount = lCount = 0
objectDetected = False

def callback(data):

    global sCount
    global mCount
    global lCount
    global objectDetected
    global SHORT_RANGE
    global MEDIUM_RANGE
    global LONG_RANGE

    currentDistance = int(data.data)
   
    
    if(currentDistance > LONG_RANGE):
        sCount = 0
        mCount = 0
        lCount = lCount + 1
    elif(currentDistance > MEDIUM_RANGE):
        sCount = 0
        mCount = mCount + 1
        lCount = 0
    elif(currentDistance < SHORT_RANGE ):
        sCount = sCount + 1
        mCount = 0
        lCount = 0

    #after 10 readings within the same range classification flag object detection.
    if(sCount == 10):  
        objectRange = "SHORT"
        print("ding")
        objectDetected = True 
        talker()
    elif(mCount == 10):
        objectRange = "MEDIUM"
        talker()
    elif(lCount == 10):
        objectRange = "FAR"
        talker()



def listener():
    rospy.Subscriber("usharp_left_chatter",String,callback)
    rospy.spin()

def talker():
    pub = rospy.Publisher('object_detection_chatter', String, queue_size = 10)
    global objectDetected
    global sCount
    global mCount
    global lCount
    #Process an object detection
    if(objectDetected):
        objectDetected = False
        sCount = mCount = lCount = 0
        pub.publish("True")
    else:
        pub.publish("False")



if __name__ == '__main__':
    try:
        rospy.init_node('listener', anonymous=True)
        rate = rospy.Rate(10)
        listener()
    except rospy.ROSInterruptException: pass



























