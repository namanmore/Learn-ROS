#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include <sstream>
int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::Int16>("chatter", 1000);
  ros::Rate loop_rate(10);
  int count= 0;
  std_msgs::Int16 msg;
  msg.data=0;
  while (ros::ok())
  {
    //int count=0;
    
    std::stringstream ss;
    //ss  << count;
    msg.data+=1;
    //int count.data=0;
    //msg.data = ss.str();
    ROS_INFO("%d", msg.data);
    chatter_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
    //f.data=f.data+1;
  }
  return 0;
}