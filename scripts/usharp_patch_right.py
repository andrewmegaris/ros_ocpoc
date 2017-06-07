#!/usr/bin/env python

#This is the publisher node for reading in usharp patch
#This driver reports data from the right usharp patch(right as the rover rolls)
# Author: Andrew Megaris
# Date: 5/16/2017
# Email: andrew@aerotenna.com
# Github: https://github.com/andrewmegaris

import roslib;
import rospy
from std_msgs.msg import String
import serial
import struct

radar = serial.Serial('/dev/ttyS0', 115200,8,'N',1,50)


def usharp_patch_right_talker():
  radar.flushInput()
  radar.flushOutput()
  while not rospy.is_shutdown():
    byte1 = struct.unpack('B',radar.read(1))[0]
    if(byte1 == 0xFE):
      byte2 = struct.unpack('B',radar.read(1))[0]
      byte3 = struct.unpack('B',radar.read(1))[0]
      byte4 = struct.unpack('B',radar.read(1))[0]
      byte5 = struct.unpack('B',radar.read(1))[0]
      byte6 = struct.unpack('B',radar.read(1))[0]
      distance = byte3 + (byte4<<8)

    if(distance < 200):
      print("Right: Object Close @ " + str(distance))
    elif(distance < 500):
      print("Right: Object Far")
    else:
      print("Right: No Object")

    rate.sleep()
      
if __name__ == '__main__':
  try:
    pub = rospy.Publisher('usharp_patch_right', String, queue_size = 20)
    rospy.init_node('usharp_patch_right_talker', anonymous=True)
    rate = rospy.Rate(500)
    usharp_patch_right_talker()    
  except rospy.ROSInterruptException:
    pass
