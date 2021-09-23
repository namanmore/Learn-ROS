#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('bool_ch', Bool, queue_size=10)
    rospy.init_node('tal', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    f=True
    c=0
    while not rospy.is_shutdown():
        c=c+1
        f=True
        if c%2!=0:
            f=False
        print(f)
        pub.publish(f)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass