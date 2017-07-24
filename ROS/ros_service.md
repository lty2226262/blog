# ros services

The idea is:
* A client node sends some data called a request to a server node and waits for a reply.
* The server takes some action and sends some data called a response back to the client.

## Finding and calling services from the command line

### Listing all services

    rosservice list

### Listing services by node

    rosnode info node-name

### Finding the node offering a service

    rosservice node service-name

### Finding the data type of a service

    rosservice info service-name

### Inspecting service data types

    rossrv show service-data-type-name

produces this output:

    float32 x
    float32 y
    float32 theta
    string name
    ---
    string name

***Be careful about the difference between rosservice and rossrv, rostopic is like rosservice, rosmsg is like rossrv.***

### Calling services from the command line

    rosservice call service-name request-content

## A client program

### Including the message type declaration

    #include <package_name/type_name.h>

### Creating a client object

    ros::ServiceClient client = node_handle.serviceClient<service_type>(service_name);

### Sample codes

    // This program spawns a new turtlesim turtle by calling
    // the appropriate service

    #include <ros/ros.h>
    #include <turtlesim/Spawn.h>

    int main(int argc, char ** argv) {
    	ros::init(argc, argv, "spawn_turtle");
    	ros::NodeHandle nh;

    	// create a client object for spawn service
    	ros::ServiceClient spawnClient = nh.serviceClient<turtlesim::Spawn>("spawn");

    	// create the req and res objects
    	turtlesim::Spawn::Request req;
    	turtlesim::Spawn::Response res;

    	// fill in the request data member
    	req.x = 2;
    	req.y = 3;
    	req.theta = M_PI / 2;
    	req.name = "Leo";

    	// call the service
    	bool success = spawnClient.call(req, res);

    	// check for success
    	if(success) {
    		ROS_INFO_STREAM("Spawned a turtle named " << res.name);
    	} else {
    		ROS_ERROR_STREAM("Failed to spawn");
    	}
    }

Tips:

    A common mistake is to fail to check the return value of pected problems if the service call fails. It takes only a minute call. This can lead to unex- or two to add code to
    check this value and call ROS_ERROR_STREAM when the service call fails. It’s
    quite likely that this investment of time will be repaid with easier debugging in the
    future.

### Declaring a dependency

CMakeLists.txt:

    find_package(catkin REQUIRED COMPONENTS roscpp turtlesim)

In package.xml:

    <build_depend>turtlesim</build_depend>
    <run_depend<turtlesim</run_depend>

## A server program

### Writing a service callback

    bool function_name(
      package_name::service_type::Request &req,
      package_name::service_type::Response &resp
    ）{}

### Sample codes

    // This program toggles between rotatation and translation
    // commands, based on calls to a service.
    #include <ros/ros.h>
    #include <std_srvs/Empty.h>
    #include <geometry_msgs/Twist.h>

    bool forward = true;
    bool toggleForward(
      std_srvs::Empty::Request &req,
      std_srvs::Empty::Response &resp
    ) {
      forward = !forward;
      ROS_INFO_STREAM("Now sending " << (forward ?
        "forward" : "rotate") << " commands.");
      return true;
    }

    int main(int argc, char **argv) {
      ros::init(argc, argv, "pubvel_toggle");
      ros::NodeHandle nh;

      // Register our service with the master.
      ros::ServiceServer server = nh.advertiseService(
        "toggle_forward", &toggleForward);

      // Publish commands, using the latest value for forward,
      // until the node shuts down.
      ros::Publisher pub = nh.advertise<geometry_msgs::Twist>(
        "turtle1/cmd_vel", 1000);
      ros::Rate rate(2);
      while(ros::ok()) {
        geometry_msgs::Twist msg;
        msg.linear.x = forward ? 1.0 : 0.0;
        msg.angular.z = forward ? 0.0 : 1.0;
        pub.publish(msg);
        ros::spinOnce();
        rate.sleep();
      }
    }

</br>

    #include "ros/ros.h"
    #include "beginner_tutorials/AddTwoInts.h"

    bool add(beginner_tutorials::AddTwoInts::Request  &req,
             beginner_tutorials::AddTwoInts::Response &res)
    {
      res.sum = req.a + req.b;
      ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
      ROS_INFO("sending back response: [%ld]", (long int)res.sum);
      return true;
    }

    int main(int argc, char **argv)
    {
      ros::init(argc, argv, "add_two_ints_server");
      ros::NodeHandle n;

      ros::ServiceServer service = n.advertiseService("add_two_ints", add);
      ROS_INFO("Ready to add two ints.");
      ros::spin();

      return 0;
    }

# Write a service description file

A service description file consists of a request and a response msg type, separated by '---'. Any two .msg files concatenated together with a '---' are a legal service description.

    #request constants
    int8 FOO=1
    int8 BAR=2
    #request fields
    int8 foobar
    another_pkg/AnotherMessage msg
    ---
    #response constants
    uint32 SECRET=123456
    #response fields
    another_pkg/YetAnotherMessage val
    CustomMessageDefinedInThisPackage value
    uint32 an_integer

# build service srv

    # Get the information about this package's buildtime dependencies
    find_package(catkin REQUIRED
      COMPONENTS message_generation std_msgs sensor_msgs)

    # Declare the message files to be built
    add_message_files(FILES
      MyMessage1.msg
      MyMessage2.msg
    )

    # Declare the service files to be built
    add_service_files(
      FILES
      MyService.srv
    )

    # Actually generate the language-specific message and service files
    generate_messages(DEPENDENCIES std_msgs sensor_msgs)

    # Declare that this catkin package's runtime dependencies
    catkin_package(
     CATKIN_DEPENDS message_runtime std_msgs sensor_msgs
    )

    # define executable using MyMessage1 etc.
    add_executable(message_program src/main.cpp)
    add_dependencies(message_program ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

    # define executable not using any messages/services provided by this package
    add_executable(does_not_use_local_messages_program src/main.cpp)
    add_dependencies(does_not_use_local_messages_program ${catkin_EXPORTED_TARGETS})
