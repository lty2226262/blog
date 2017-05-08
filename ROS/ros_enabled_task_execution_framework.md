# task controller

often called the task executive and are included at least one of these key features:

* task priorities

* pause and resume

* task hierarchy: tasks can often be broken down into subtasks to handle the details. For instance, recharging needs:
  1. navigate to the docking station
  2. dock the robot
  3. charge the battery

  the docking could be broken down into:
  1. align with beacon
  2. drive forward
  3. stop when docked

* conditions: in ROS, these variables often take the form of messages being published by various nodes. For example, the battery monitoring task will subscribe to a diagnostics topic that includes the current battery level.

* concurrency: multiple tasks can run in parallel.

# SMACH

using state machines and pronounced "smash"

# PI_TREES

behavior trees

# Example: a fake battery simulator

The node takes three parameters:

* rate(default 1Hz): how often publish battery level

* battery_runtime(default 60 seconds): how long in seconds it takes the battery to run down to 0

* initial_battery_level: (default 100) the initial charge level of the  battery when we first start the node

launch the executes:

    roslaunch rbx2_utils battery_simulator.launch

verify the simulator is working:

    rostopic echo /battery_level

set the battery level:

    rosservice call /battery_simulator/set_battery_level 100

configure the parameters with rqt_reconfigure

    rosrun rqt_reconfigure rqt_reconfigure

Then click on battery_simulator node to see the options.
