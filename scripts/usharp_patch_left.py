#!/usr/bin/env python

#This is the publisher node for reading in usharp patch
#This driver reports data from the left usharp patch(left as the rover rolls)
# Author: Andrew Megaris
# Date: 5/16/2017
# Email: andrew@aerotenna.com
# Github: https://github.com/andrewmegaris

import roslib;
import rospy
from std_msgs.msg import String
import serial
import struct
#Set the address of uSharp Patch
RADAR_ADDRESS = '/dev/ttyS6'


#Instantiate the radar object
radar = serial.Serial(RADAR_ADDRESS, 115200,8,'N',1,50)

def usharp_patch_left_talker():

    #Make sure we are getting clean fresh data.
    radar.flushInput()
    radar.flushOutput()
  
    #Instantiate flags and counters for object detection
    sCount = mCount = lCount = 0
    objectDetected = False
  
    while not rospy.is_shutdown():
    
        #Read a byte and check for header 
        byte1 = struct.unpack('B',radar.read(1))[0]
        
        #If a header byte is found continue processing the reading from radar
        if(byte1 == 0xFE):
            #Unpack bytes individualy
            byte2 = struct.unpack('B',radar.read(1))[0]
            byte3 = struct.unpack('B',radar.read(1))[0]
            byte4 = struct.unpack('B',radar.read(1))[0]
            byte5 = struct.unpack('B',radar.read(1))[0]
            byte6 = struct.unpack('B',radar.read(1))[0]
            #Assign bytes to their respective values
            versionID = byte2
            altitudeLSB = byte3
            altitudeMSB = byte4
            SNR = byte5
            checksum = byte6
            currentDistance = altitudeLSB + (altitudeMSB << 8)
            if(checksum == ((versionID + altitudeLSB + altitudeMSB + SNR) & 0xFF)):
                pub.publish(str(currentDistance))
        
        rate.sleep()
      
if __name__ == '__main__':
    try:
        pub = rospy.Publisher('usharp_left_chatter', String, queue_size = 20)
        rospy.init_node('usharp_patch_left_talker', anonymous=True)
        rate = rospy.Rate(500)
        usharp_patch_left_talker()    
    except rospy.ROSInterruptException: pass






