#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Num

def talker():
    pub = rospy.Publisher('custom_chatt', Num)
    rospy.init_node('custom_talk', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Num()
    #msg.name = "ROS User"
    msg.num = 2
    msg.f="Task"
    msg.l="was good"
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        #pub.publish("hello")
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass