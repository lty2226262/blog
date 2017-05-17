## Units and coordinate systems

A linear velocity of 0.5 m/s is actually quite fast for an indoor robot, while an angular speed is 1.0 rad/s.

### The ROS Base Controller

The driver and PID controller are usually combined inside a single ROS node called the base controller. The base controller must always run on a computer attached directly to the motor controller and is typically one of the first nodes launched when bringing up the robot.

base_controller publishes odometry data on the /odom and listens for motion commands on the /cmd_vel topic. At the same time, the controller node typically (but not always) publishes a transform from the /odom frame to the base frame--either /base_link or /base_footprint.

We could also use the robot_pose_ekf package to combine wheel encoder and IMU to get a more accurate pose. It is robot_pose_ekf node that publishes the transform from /odom to /base_footprint.

http://ros.org/wiki/robot_pose_ekf

### Frame-Base Motion using the move_base ROS Package

move_base: specify a target pose with respect to some frame of reference. Then attempt to move the robot to the goal while avoiding obstacles.

It combines odom data with both local and global cost maps. And it also controls the linear and angular velocities and accelerations automatically.

### SLAM using the gmapping and amcl ROS Package

amcl: (adaptive Monte Carlo localization) automatically localizing the robot based on its current scan and odometry data.

### Sematic Goals

Using smach, behavior trees, executive_teer, and knowrob.

GOAL -> AMCL -> Path Planner-> move_base -> /cmd_vel & /odom -> Base Controller -> Motor Speeds.

### Monitoring Robot Motion using rviz

    rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0, z: 0}, angular: {x: 0, y: 0, z: -0.5}}'

We use the -r parameter to publish the Twist message continually at 10Hz.

    rostopic pub -1 /cmd_vel geometry_msgs/Twist '{}'

the "-1" option means "publish once"

## Calibrating Your Robot's Odometry

    sudo apt-get install ros-indigo-orocos-kdl \
    ros-indigo-python-orocos-kdl

### Linear Calibration

lay out at least 1 meter of tape of the floor and align the starting end of the tape with some identifiable mark on your robot.

    roslaunch rbx1_bringup turtlebot_minimal_create.launch

Next, run the linear calibration node:

    rosrun rbx1_nav calibrate_linear.py

Finally, run rqt_reconfigure:

    rosrun rqt_reconfigure rqt_reconfigure

## Odometry

odometry measurements in ROS use /odom as the parent frame id and /base_link (or /base_footprint) as the child frame id.

/base_link: corresponds to a real physical part of the robot

/odom: defined by the translations and rotations encapsulated in the odometry data.

***transform_utils*** library is a small module that you can find in the rbx1_nav/src/rbx1_nav directory and contains a couple of handy functions borrowed from the Turtlebot package. The function ***quat_to_angle*** converts a quaternion to an Euler angle(yaw) while the ***normalize_angle*** function removes the ambiguity between 180 and -180 degrees as well as 0 and 360 degrees.

### The /odom topic versus the /odom frame

/odom topic is not always the full story. Turtlebot uses a single-axis gyro to provide an additional estimate of the robot's rotation. This is combined with the data from the wheel encoders by the robot_pose_ekf node.

robot_pose_ekf doesn't publish back on the /odom topic which is reserved for the wheel encoder data. Instead, it publishes it on the /odom_combined topic. It is published not as an Odometry message but a PoseWithCovarianceStamped message.

### The Trouble with Dead Reckoning

small errors in odometry accumulate over time.

### TurtleBot Teleoperation Using Interactive Markers

To try it out with the fake TurtleBot, run the following commands:

    $ roslaunch rbx1_bringup fake_turtlebot.launch
Bring up RViz with the pre-configured interactive_markers.rviz config file:

    $ rosrun rviz rviz -d `rospack find rbx1_nav`/interactive_markers.rviz
Finally, bring up the interactive_markers.launch file in the rbx1_nav package:

    $ roslaunch rbx1_nav interactive_markers.launch
