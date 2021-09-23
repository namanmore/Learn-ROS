#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('int_ch', Int16, queue_size=10)
    rospy.init_node('tal', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    f=0
    while not rospy.is_shutdown():
        f=f+2
        print(f)
        pub.publish(f)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass