#!/usr/bin/env python3
import rospy
from std_msgs.msg import Char
def callback(data):
    rospy.loginfo('Got %c',data.data)

def listener():
    rospy.init_node('lis', anonymous=True)
    rospy.Subscriber('char_ch', Char, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
