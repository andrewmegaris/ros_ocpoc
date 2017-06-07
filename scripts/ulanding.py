#!/usr/bin/env python

#This is the publisher node for reading in ulanding readings
# Author: Andrew Megaris
# Date: 5/16/2017
# Email: andrew@aerotenna.com
# Github: https://github.com/andrewmegaris

import roslib;
import rospy
from std_msgs.msg import String
import serial
import struct

leftRadar = serial.Serial('/dev/ttyS6', 115200,8,'N',1,50)
rightRadar = serial.Serial('/dev/ttyS0',115200,8,'N',1,50) 

def ulanding_talker():
  leftRadar.flushInput()
  leftRadar.flushOutput()
  while not rospy.is_shutdown():
    byte1 = struct.unpack('B',leftRadar.read(1))[0]
    if(byte1 == 0xFE):
      readLeft = True
      byte2 = struct.unpack('B',leftRadar.read(1))[0]
      byte3 = struct.unpack('B',leftRadar.read(1))[0]
      byte4 = struct.unpack('B',leftRadar.read(1))[0]
      byte5 = struct.unpack('B',leftRadar.read(1))[0]
      byte6 = struct.unpack('B',leftRadar.read(1))[0]
      distanceLeft = byte3 + (byte4<<8)

    byte1 = struct.unpack('B',rightRadar.read(1))[0]
    if(byte1 == 0xFE):
      readRight = True
      byte2 = struct.unpack('B',rightRadar.read(1))[0]
      byte3 = struct.unpack('B',rightRadar.read(1))[0]
      byte4 = struct.unpack('B',rightRadar.read(1))[0]
      byte5 = struct.unpack('B',rightRadar.read(1))[0]
      byte6 = struct.unpack('B',rightRadar.read(1))[0]
      distanceRight = byte3 + (byte4<<8)

    if(readLeft & readRight):
      print("L-Dist : " + str(distanceLeft) + " R-Dist: " + str(distanceRight))

    rate.sleep()
      
if __name__ == '__main__':
  try:
    pub = rospy.Publisher('ulanding_chatter', String, queue_size = 20)
    rospy.init_node('ulanding_talker', anonymous=True)
    rate = rospy.Rate(500)
    ulanding_talker()    
  except rospy.ROSInterruptException:
    pass
