#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    i = 1
    while not rospy.is_shutdown():
        hello_str = "1711457 %s" % i
        #rospy.loginfo(hello_str)
        pub.publish(hello_str)
        i = i + 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
