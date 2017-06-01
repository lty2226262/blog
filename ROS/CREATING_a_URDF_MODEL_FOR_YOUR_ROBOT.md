# Transform configuration

From "base_link" to "base_laser" we must apply a translation of (x: 0.1m, y: 0.0m, z: 0.2m).

To build the lidar model, "base_link" is the parent frame while "base_laser" is the child frame. x:0.1 , y: 0.0, z:0.2

## One shape

    sudo apt-get install ros-indigo-urdf-tutorial

Going to explore one simple shape. Here's about as simple as a urdf as you can make.

    <?xml version="1.0"?>
    <robot name="myfirst">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>
    </robot>

 this is a robot with the name myfirst, that contains only one link (a.k.a. part), whose visual component is just a cylinder 0.6 meters long with a 0.2 meter radius.

 To examine the model, launch the display.launch file:

    roslaunch urdf_tutorial display.launch model:=urdf/01-myfirst.urdf

**Tips**: model path is based on current path.

A slightly modified argument allows this to work regardless of the current working directory:

    roslaunch urdf_tutorial display.launch model:='$(find urdf_tutorial)/urdf/01-myfirst.urdf'

## Multiple shapes

    <?xml version="1.0"?>
    <robot name="multipleshapes">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>

      <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
        </visual>
      </link>

      <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
      </joint>

    </robot>

Then examine it:

    roslaunch urdf_tutorial display.launch model:=urdf/02-multipleshapes.urdf

## Origins

 so we must offset the origin for the leg as well. We also rotate the leg so it is upright.

     <?xml version="1.0"?>
    <robot name="origins">
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.6" radius="0.2"/>
          </geometry>
        </visual>
      </link>

      <link name="right_leg">
        <visual>
          <geometry>
            <box size="0.6 0.1 0.2"/>
          </geometry>
          <origin rpy="0 1.57075 0" xyz="0 0 -0.3"/>
        </visual>
      </link>

      <joint name="base_to_right_leg" type="fixed">
        <parent link="base_link"/>
        <child link="right_leg"/>
        <origin xyz="0 -0.22 0.25"/>
      </joint>

    </robot>

## Building a movable robot model with URDF

### continuous joint: Head

    <joint name="head_swivel" type="continuous">
      <parent link="base_link"/>
      <child link="head"/>
      <axis xyz="0 0 1"/>
      <origin xyz="0 0 0.3"/>
    </joint>

The connection between the body and the head is a continuous joint, meaning that it can take on any angle from negative infinity to positive infinity. The wheels are also modeled like this, so that they can roll in both directions forever.

The only additional information we have to add is the axis of rotation, here specified by an xyz triplet, which specifies a vector around which the head will rotate. Since we want it to go around the z axis, we specify the vector "0 0 1".

### revolute joint: Gripper

    <joint name="left_gripper_joint" type="revolute">
      <axis xyz="0 0 1"/>
      <limit effort="1000.0" lower="0.0" upper="0.548" velocity="0.5"/>
      <origin rpy="0 0 0" xyz="0.2 0.01 0"/>
      <parent link="gripper_pole"/>
      <child link="left_gripper"/>
    </joint>

Both the right and the left gripper joints are modeled as revolute joints. This means that they rotate in the same way that the continuous joints do, but they have strict limits. Hence, we must include the limit tag specifying the upper and lower limits of the joint (in radians). We also must specify a maximum velocity and effort for this joint but the actual values don't matter for our purposes here.

### prismatic joint: Gripper Arm

    <joint name="gripper_extension" type="prismatic">
      <parent link="base_link"/>
      <child link="gripper_pole"/>
      <limit effort="1000.0" lower="-0.38" upper="0" velocity="0.5"/>
      <origin rpy="0 0 0" xyz="0.19 0 0.2"/>
    </joint>

The gripper arm is a different kind of joint...namely a prismatic joint. This means that it moves along an axis, not around it. This translational movement is what allows our robot model to extend and retract its gripper arm.

The limits of the prismatic arm are specified in the same way as a revolute joint, except that the units are meters, not radians.

### Other types of joints

There are two other kinds of joints that move around in space. Whereas the prismatic joint can only move along one dimension, a planar joint can move around in a plane, or two dimensions. Furthermore, a floating joint is unconstrained, and can move around in any of the three dimensions. These joints cannot be specified by just one number, and therefore aren’t included in this tutorial.

## Adding physical and collision properties to a URDF model

### collision
### inertia
### Others

## Using Xacro to Clean Up a URDF File

### Using Xacro

As its name implies, xacro is a macro language. The xacro program runs all of the macros and outputs the result. Typical usage looks something like this:

    rosrun xacro xacro model.xacro > model.urdf

You can also automatically generate the urdf in a launch file.

    <param name="robot_description" command="$(find xacro)/xacro '$(find pr2_description)/robots/pr2.urdf.xacro'" />

At the top of the URDF file, you must specify a namespace in order for the file to parse properly. For example, these are the first two lines of a valid xacro file:

    <?xml version="1.0"?>
    <robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="firefighter">

### Constants

Let’s take a quick look at our base_link in R2D2.

    <link name="base_link">
      <visual>
        <geometry>
          <cylinder length="0.6" radius="0.2"/>
        </geometry>
        <material name="blue"/>
      </visual>
      <collision>
        <geometry>
          <cylinder length="0.6" radius="0.2"/>
        </geometry>
      </collision>
    </link>

 a little redundant. xacro allows you to specify properties which act as constants. Instead, of the above code, we can write this.

    <xacro:property name="width" value="0.2" />
    <xacro:property name="bodylen" value="0.6" />
    <link name="base_link">
        <visual>
            <geometry>
                <cylinder radius="${width}" length="${bodylen}"/>
            </geometry>
            <material name="blue"/>
        </visual>
        <collision>
            <geometry>
                <cylinder radius="${width}" length="${bodylen}"/>
            </geometry>
        </collision>
    </link>

This code will generate the same code shown above.

The value of the contents of the \$\{\} construct are then used to replace the \$\{\}. This means you can combine it with other text in the attribute.

    <xacro:property name=”robotname” value=”marvin” />
    <link name=”${robotname}s_leg” />

### Math

You can build up arbitrarily complex expressions in the \$\{\} construct using the four basic operations (+,-,*,\/), the unary minus, and parenthesis. Examples:

    <cylinder radius="${wheeldiam/2}" length="0.1"/>
    <origin xyz="${reflect*(width+.02)} 0 0.25" />

All of the math is done using floats, hence

    <link name="${5/6}"/>

evaluates to

    <link name="0.833333333333"/>

### Macros

#### Simple macros

Let’s take a look at a simple useless macro.

    <xacro:macro name="default_origin">
        <origin xyz="0 0 0" rpy="0 0 0"/>
    </xacro:macro>
    <xacro:default_origin />

(This is useless, since if the origin is not specified, it has the same value as this.) This code will generate the following.

    <origin rpy="0 0 0" xyz="0 0 0"/>

#### Parameterized Macro

You can also parameterize macros so that they don’t generate the same exact text every time. When combined with the math functionality, this is even more powerful.

First, let’s take an example of a simple macro used in R2D2.

    <xacro:macro name="default_inertial" params="mass">
        <inertial>
                <mass value="${mass}" />
                <inertia ixx="1.0" ixy="0.0" ixz="0.0"
                     iyy="1.0" iyz="0.0"
                     izz="1.0" />
        </inertial>
    </xacro:macro>

This can be used with the code

    <xacro:default_inertial mass="10"/>

The parameters act just like properties, and you can use them in expressions

You can also use entire blocks as parameters too.

    <xacro:macro name="blue_shape" params="name *shape">
        <link name="${name}">
            <visual>
                <geometry>
                    <xacro:insert_block name="shape" />
                </geometry>
                <material name="blue"/>
            </visual>
            <collision>
                <geometry>
                    <xacro:insert_block name="shape" />
                </geometry>
            </collision>
        </link>
    </xacro:macro>

    <xacro:blue_shape name="base_link">
        <cylinder radius=".42" length=".01" />
    </xacro:blue_shape>
