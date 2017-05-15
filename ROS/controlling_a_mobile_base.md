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
