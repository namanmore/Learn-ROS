#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Num

def callback(data):
    rospy.loginfo("%s %d %s"%(data.f , data.num,data.l))
    #rospy.loginfo(data.num)

def listener():
    rospy.init_node('custom_list', anonymous=True)
    rospy.Subscriber("custom_chatt", Num, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()