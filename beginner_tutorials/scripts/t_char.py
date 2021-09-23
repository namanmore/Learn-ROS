#!/usr/bin/env python3
import rospy
from std_msgs.msg import Char

def talker():
    pub = rospy.Publisher('char_ch', Char, queue_size=10)
    rospy.init_node('tal', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    f='a'
    while not rospy.is_shutdown():
        print(f)
        t=ord(f[0])
        pub.publish(t)
        t=t+1
        f=chr(t)
        if(f=='z'):
            f='a'
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass