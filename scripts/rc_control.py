# !/usr/bin/env python

import rospy
import time
from mavros_msgs.msg import OverrideRCIn
from mavros_msgs.srv import SetMode
throttle_channel = 3
steer_channel = 2

def talker():
  pub = rospy.Publisher('mavros/rc/override', OverrideRCIn, queue_size=10)
  r = rospy.Rate(10)
  msg = OverrideRCIn()
  start = time.time()
  speed='SLOW'
  direction='LEFT'
  exec_time=1
  flag=True
  if speed == 'SLOW':
    msg.channels[throttle_channel]=1558
  if direction == 'LEFT':
    msg.channel[steer_channel[=1300
  while not rospy.is_shutdown() and flag:
    sample_time = time.time()
  if ((sample_time - start) > exec_time):
    flag=False
  rospy.loginfo(msg)
  pub.publish(msg)
  r.sleep()

if __name__ = '__main__':
  rospy,wait_For_service('/mavros/set_mode')
  change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
  resp1 = change_mode(custom_mode='manual')
  print(resp1)
  if 'True' in str(resp1):
    try:
      talker()
    except rospy.ROSInterruptException: pass
  
