#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool

def callback(data):
    rospy.loginfo(data)

def listener():
    rospy.init_node('lis', anonymous=True)

    rospy.Subscriber('bool_ch', Bool, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
