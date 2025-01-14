#include "ros/ros.h"
#include "std_msgs/Int16.h"

void chatterCallback(const std_msgs::Int16 msg)
{
  ROS_INFO("%d", msg.data);
}
int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  ros::spin();
  return 0;
}