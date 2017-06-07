#!/usr/bin/env python
import rospy
import time
from mavros_msgs.msg import OverrideRCIn
from mavros_msgs.srv import SetMode

exec_time=1

print("hello?")
def talker():
    pub = rospy.Publisher('mavros/rc/override', OverrideRCIn, queue_size=10)
    rospy.init_node('pwm_talker', anonymous=True)
    r = rospy.Rate(10)
    msg = OverrideRCIn()
    start = time.time()
    flag=True
    msg.channels[0] = 1000
    msg.channels[2] = 1550
    while not rospy.is_shutdown():
        sample_time = time.time()
        if((sample_time - start) > exec_time):
            flag=False
            rospy.loginfo(msg)
            pub.publish(msg)
            r.sleep()
    resp = change_mode(custom_mode="guided")


if __name__ == '__main__':
    rospy.wait_for_service('/mavros/set_mode')
    change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
    resp = change_mode(custom_mode="manual")
    print (resp)
    if "True" in str(resp):
        try:
            print("t2")
            talker()
        except rospy.ROSInterruptException: pass


