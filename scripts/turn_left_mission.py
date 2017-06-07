#!/usr/bin/env python

#This is the subscriber node for the ulanding publisher node
#It will calculate if avoidance should be called
#Eventually this node will read in two radars for multi directional avoidance.
# Author: Andrew Megaris
# Date: 5/16/2017
# Email: andrew@aerotenna.com
# Github: https://github.com/andrewmegaris

import rospy
import time
from std_msgs.msg import String
from mavros_msgs.msg import OverrideRCIn
#from mavros_msgs.srv import SetMode

#exec_time = 1
release = False

def callback(data):
    global release
    turnLeft = str(data.data)
    print(turnLeft)
    if "True" in turnLeft:
        try:
            turn_left()
        except rospy.ROSInterruptException: pass
    elif(release):
        straighten_out()
 
def straighten_out():
    global release
    release = False
    msg.channels[0] = 0
    msg.channels[2] = 0
    rospy.loginfo
    pub.publish(msg)

    
def turn_left():
    global release
#    start = time.time()
    release = True
    msg.channels[0] = 1000
    rospy.loginfo(msg)
    pub.publish(msg)


def listener():
    rospy.Subscriber("object_detection_chatter", String, callback)
    rospy.spin()

    
if __name__ == '__main__':
    try:
        pub = rospy.Publisher('mavros/rc/override', OverrideRCIn, queue_size=10)
        msg = OverrideRCIn()
#        rospy.wait_for_service('/mavros/set_mode')
#        change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        rospy.init_node('simple_avoidance', anonymous = True)    
        rate = rospy.Rate(10)
        listener()   
    except rospy.ROSInterruptException: pass
















