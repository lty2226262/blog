    #include "ros/ros.h"
    #include "std_msgs/String.h"

    class Listener
    {
    public:
      void callback(const std_msgs::String::ConstPtr& msg);
    };

    void Listener::callback(const std_msgs::String::ConstPtr& msg)
    {
      ROS_INFO("I heard: [%s]", msg->data.c_str());
    }

    int main(int argc, char **argv)
    {
      ros::init(argc, argv, "listener_class");
      ros::NodeHandle n;

      Listener listener;
      ros::Subscriber sub = n.subscribe("chatter", 1000, &Listener::callback, &listener);

      ros::spin();

      return 0;
    }

</br>

    #include "ros/ros.h"
    #include "std_msgs/String.h"

    void chatterCallback(const std_msgs::String::ConstPtr& msg)
    {
      ROS_INFO("I heard: [%s]", msg->data.c_str());
    }

    int main(int argc, char **argv)
    {
      ros::init(argc, argv, "listener");

      ros::NodeHandle n;

      ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

      ros::spin();

      return 0;
    }
