Visual : from the camera to generate a "fake" laser scan. depthimage_to_laserscan: http://wiki.ros.org/depthimage_to_laserscan

* move_base: moving the robot to a goal pose within a given reference frame

* gmapping: creating a map from laser scan data

* amcl: localization using an existing map

http://wiki.ros.org/navigation/Tutorials/RobotSetup

http://wiki.ros.org/navigation/Tutorials

## path planning and obstacle avoidance using move_base

tf between the /odom frame and the /base_link frame to keep track of the distance traveled and the angles rotated. Using move_base is more elegant.

http://wiki.ros.org/move_base

move_base package incorporates the base_local_planner that combines odometry data with both global and local cost maps when selecting a path to follow.

the goal consists of a standard ROS header including a frame_id, a goal_id, and the goal itself which is given as a PoseStamped message. The PoseStamped message type in turn consists of a header and a pose which itself consists of a position and an orientation.

### Configuration Paramenters for path planning

The move_base node requires four configuration files before it can be run. These files define a number of parameters related to the cost of running into obstacles, the radius of the robot, how far into the future the path planner should look, how fast we want the robot to move and so on. The four configuation files can be found in the config subdirectory of the rbx1_nav package and are called:

* base_local_planner_params.yaml
* costmap_common_params.yaml
* global_costmap_params.yanl
* local_costmap_params.yaml

#### base_local_planner_params.yaml

* controller_frequency： 3.0 - 3~5 seems to work fairly well for a typical laptop.
* max_vel_x: 0.3, maximum linear vel m/s, <0.5
* min_vel_x: 0.05 minimum linear velocity of the robot.
* max_vel_theta: 1.0 The maximum rotational velocity of the robot in radians per second. Don't set this too high or the robot will overshoot its goal orientation.
* min_vel_theta: -1.0
* min_in_place_vel_theta: 0.5  The minimum in-place rotational velocity of the robot in radians per second.
* escape_vel: -0.1 Speed used for driving during escapes in meters per sec. Note that it must be negative in order for the robot to actually reverse.
* acc_lim_x: 2.5  The maximum linear acceleration in the x direction in m/s2
* acc_lim_y: 0.0 – The maximum linear acceleration in the y direction in m/s2. We set this to 0 for a differential drive (non-holonomic) robot since such a robot can only move linearly in the x direction (as well as rotate).
* acc_lim_theta: 3.2 – The maximum angular acceleration in rad/s2.
* holonomic_robot: false – Unless you have an omni-directional drive robot, this is always set to false
* yaw_goal_tolerance: 0.1 – How close to the goal orientation (in radians)
do we have to get? Setting this value to small may cause the robot to oscillate
near the goal.
* xy_goal_tolerance: 0.1 – How close (in meters) do we have to get to the goal? If you set the tolerance too small, your robot may try endlessly to make small adjustments around the goal location. NOTE: Do not set the tolerance less than the resolution of your map (described in a later section) or your robot will end up spinning in place indefinitely without reaching the goal.
* pdist_scale: 0.8 – The weighting for how much the controller should stay close to the path it was given, maximal possible value is 5. The relative importance of sticking to the global path as opposed to getting to the goal. Set this parameter larger than the gdist_scale to favor following the global path more closely.
* gdist_scale: 0.4 – The relative importance of getting to the goal rather than sticking to the global path. Set this parameter larger than the pdist_scale to favor getting to the goal by whatever path necessary.
* occdist_scale: 0.1 - The relative importance of avoiding obstacles.
* sim_time: 1.0 – How many seconds into the future should the planner look? This parameter together with the next (dwa) can greatly affect the path taken by your robot toward a goal.
* dwa: true – Whether or not to use the Dynamic Window Approach when simulating trajectories into the future. See the Base Local Planner Overview for more details.

#### costmap_common_params.yaml

There are only two parameters in this file that you might have to tweak right away for your own robot:

* robot_radius: 0.165 – For a circular robot, the radius of your robot in meters. For a non-circular robot, you can use the footprint parameter instead as shown next. The value here is the radius of the original TurtleBot in meters.
* footprint: [[x0, y0], [x1, y1], [x2, y2], [x3, y3], etc] – Each coordinate pair in the list represents a point on the boundary of the robot with the robot's center assumed to be at [0, 0]. The measurement units are meters. The points can be listed in either clockwise or counterclockwise order around the perimeter of the robot.
* inflation_radius: 0.3 – The radius in meters that obstacles will be inflated in the map. If your robot is having trouble passing through narrow doorways or other tight spaces, trying reducing this value slightly. Conversely, if the robot keeps running into things, try increasing the value.

#### global_costmap_params.yaml

There are a few parameters in this file that you might experiment with depending on the power of your robot's CPU and the reliability of the network connection between the robot and your workstation:

* global_frame: /map – For the global cost map, we use the the map frame as the global frame.
* robot_base_fame: /base_footprint – This will usually be either /base_link or /base_footprint. For a TurtleBot it is /base_footprint.
* update_frequency: 1.0 – The frequency in Hz of how often the global map is updated with sensor information. The higher this number, the greater the load on your computer's CPU. Especially for the global map, one can generally get away with a relatively small value of between 1.0 and 5.0.
* publish_frequency: 0 – For a static global map, there is generally no need to continually publish it.
* static_map, true - This parameter and the next are always set to opposite values. The global map is usually static so we set static_map to true.
* rolling_window: false - The global map is generally not updated as the robot moves to we set this parameter to false.
* transform_tolerance: 1.0 – Specifies the delay in seconds that is tolerated between the frame transforms in the tf tree. For typical wireless connections between the robot and the workstation, something on the order of 1.0 seconds works OK.

#### local_costmap_params.yaml

* global_frame: /odom – For the local cost map, we use the odometry frame as the global frame
* robot_base_fame: /base_footprint – This will usually be either /base_link or /base_footprint. For a TurtleBot it is /base_footprint.
* update_frequency: 3.0 – How frequently (times per second) do we update the local map based on sensor data. For a really slow computer, you may have to reduce this value.
* publish_frequency: 1.0 – We definitely want updates to the local map published so we set a non-zero value here. Once per second should be good enough unless your robot needs to move more quickly.
* static_map: false – This parameter and the next are always set to opposite values. The local map is dynamically updated with sensor data so we set static_map to false.
* rolling_window: true – The local map is updated within a rolling window defined by the next few parameters.
* width: 6.0 – The x dimension in meters of the rolling map.
* height: 6.0 – The y dimension in meters of the rolling map.
* resolution: 0.01 – The resolution in meters of the rolling map. This should match the resolution set in the YAML file for your map (explained in a later section).
* transform_tolerance: 1.0 – Specifies the delay in seconds that is tolerated between the frame transforms in the tf tree or the mapping process will temporarily abort. On a fast computer connected directly to the robot, a value 1.0 should work OK. But on slower computers and especially over wireless connections, the tolerance may have to be increased. The tell-tale warning message you will see when the tolerance is set too low will look like the following:

      [ WARN] [1339438850.439571557]: Costmap2DROS transform
      timeout. Current time: 1339438850.4395, global_pose stamp:
      1339438850.3107, tolerance: 0.0001

## Testing move_base in the ArbotiX Simulator

The launch file for bringing up the move_base node and the blank map is called fake_move_base_blank_map.launch in the launch subdirectory.

    <launch>
     <!-- Run the map server with a blank map -->
      <node name="map_server" pkg="map_server" type="map_server" args="$(find rbx1_nav)/maps/blank_map.yaml"/>
     <!-- Launch move_base and load all navigation parameters -->
      <include file="$(find rbx1_nav)/launch/fake_move_base.launch" />
     <!-- Run a static transform between /odom and /map -->
      <node pkg="tf" type="static_transform_publisher" name="odom_map_broadcaster" args="0 0 0 0 0 0 /odom /map 100" />
    </launch>
To try it out in simulation, first fire up the ArbotiX simulator:


    roslaunch rbx1_bringup fake_turtlebot.launch
To launch the move_base node together with the blank map, run the command:

    roslaunch rbx1_nav fake_move_base_blank_map.launch
If you're not already running RViz, bring it up now with the included navigation configuration file:

    $ rosrun rviz rviz -d `rospack find rbx1_nav`/nav.rviz

Since our robot is starting off at coordinates (0, 0, 0) in both the /map frame and the /base_link frame

    rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{ header: { frame_id: "map" }, pose: { position: { x: 1.0, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } } }'
