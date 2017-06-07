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
from mavros_msgs.srv import SetMode

exec_time = 1

#DEFINE AVOIDANCE_RANGE
#AVOIDANCE_RANGE = 300
#avoiding = True
#timer = 0

def callback(data):
    print("call back activated")  


    needAvoidance = data.data
    print(str(needAvoidance))
#    if "True" in needAvoidance:
#    change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
#    if "True" in needAvoidance:
#    global avoiding
#    global timer
#    global AVOIDANCE_RANGE
    
#    objectRange = data.data
    
#    if(int(objectRange) <= 100):
 #       print("activating avoidance")
#        change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
  #      resp = change_mode(custom_mode="manual")
  #      if "True" in str(resp):
  #          try:
  #              avoidance()
   #         except rospy.ROSInterruptException: pass
 #   else:
  #      print("dont need to avoid")
   #     resp = change_mode(custom_mode="guided")
    rospy.spin()
def avoidance():

    msg = OverrideRCIn()
    start = time.time()
    flag = True
    msg.channels[0] = 1000
    msg.channels[2] = 1550
    while not rospy.is_shutdown():
        sample_time = time.time()
        if((sample_time - start) > exec_time):
            flag=False
            rospy.loginfo(msg)
            pub.publish(msg)
            r.sleep
    resp = change_mode(custom_mode="guided")
    rospy.spin()


if __name__ == '__main__':
    rospy.wait_for_service('/mavros/set_mode')
    rospy.init_node('simple_avoidance', anonymous = True)    
    rospy.Subscriber('object_detection_chatter', String, callback)
    pub = rospy.Publisher('mavros/rc/override',OverrideRCIn, queue_size=10)
    r = rospy.Rate(10)

















