#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(data.data+2)

def listener():
    rospy.init_node('lis', anonymous=True)

    rospy.Subscriber('int_ch', Int16, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
