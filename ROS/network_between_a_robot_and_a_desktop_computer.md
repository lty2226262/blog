## Networking Between a Robot and a Desktop Computer

A fairly typical setup when using ROS is to mount a laptop or single board computer on the robot while monitoring its actions on a desktop machine. ROS makes it relatively easy for multiple machines to view the same set of topics, services and parameters. This is particularly useful when your robot's onboard computer is not very powerful since it allows you to run the more demanding processes such as RViz on your desktop. (Programs like RViz can also run down a laptop battery very quickly.)

### Time Synchronization

First, must do time synchronization.

Install,

    sudo apt-get install chrony

### ROS Networking using Zeroconf

Zeroconf: using local hostnames instead of IP address. When connect to same router on a home or office.

For an added check on time synchronization, we can run the ntpdate command to
synchronize the desktop with the robot.

    sudo ntpdate -b my_robot.local

### Start a fake robot

    roslaunch rbx1_bringup fake_turtlebot.launch

</br>

    <launch>
      <param name="/use_sim_time" value="false" />

      <!-- Load the URDF/Xacro model of our robot -->
      <arg name="urdf_file" default="$(find xacro)/xacro.py '$(find rbx1_description)/urdf/turtlebot.urdf.xacro'" />

      <param name="robot_description" command="$(arg urdf_file)" />
      <!-- motion control -->
      <node name="arbotix" pkg="arbotix_python" type="arbotix_driver" output="screen" clear_params="true">
          <rosparam file="$(find rbx1_bringup)/config/fake_turtlebot_arbotix.yaml" command="load" />
          <param name="sim" value="true"/>
      </node>

      <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher">
          <param name="publish_frequency" type="double" value="20.0" />
      </node>

    </launch>

</br>

bring up a Rviz so we can observe the simulated robot in action:

    rosrun rviz rviz -d `rospack find rbx1_nav`/sim.rviz
