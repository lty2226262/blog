    rosbag record -O subset /turtle1/cmd_vel /turtle1/pose

The -O argument tells rosbag record to log to a file named subset.bag, and the topic arguments cause rosbag record to only subscribe to these two topics. Move the turtle around for several seconds using the keyboard arrow commands, and then Ctrl-C the rosbag record.

    rosbag play -r 2 <your bagfile>

 this is the trajectory that would have resulted had you issued your keyboard commands twice as fast.
