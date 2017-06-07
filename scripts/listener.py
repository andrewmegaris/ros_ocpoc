#!/usr/bin/env python

#This is the subscriber node for the ulanding publisher node
#It will calculate if avoidance should be called
#Eventually this node will read in two radars for multi directional avoidance.
# Author: Andrew Megaris
# Date: 5/16/2017
# Email: andrew@aerotenna.com
# Github: https://github.com/andrewmegaris

import rospy
from std_msgs.msg import String

#DEFINE AVOIDANCE_RANGE
AVOIDANCE_RANGE = 300

#Init timer and flags
avoiding = Flase
timer = 0

def process_data(data):
    objectRange = data.data
    print("processing data")    
    #first check if currently avoiding. 
    if(avoiding):
    print("currently avoiding")
        #if object is in the way, continue avoiding
        if(objectRange <= AVOIDANCE_RANGE):
            timer = timer + 1
            #TODO STEER RIGHT
            print("steering right %s", timer)
        #Object has been avoided, get back onto path.
        else:
            while(timer != 0):
                timer = timer - 1
                print("Returning %s", timer)
                #TODO STEER LEFT
            avoiding = False
            print("object passed")
    #if not currently avoiding
    else:
        if(objectRange <= AVOIDANCE_RANGE):
            print("activating avoidance")
            #if an object is within specified range, enable avoidance.
            #JUMP OUT OF MISSION MODE
            avoiding = True
        else:
            print("dont need to avoid")
            #RETURN TO MISSION MODE
            avoiding = False
            timer = 0

def ulanding_listener():
    rospy.init_node('ulanding_listener', anonymous=True)
    rospy.Subscriber('ulanding_chatter', String, process_data)
    rospy.spin()

if __name__ == '__main__':
    ulanding_listener()
