# <arg> tag

The <arg> tag allows you to create more re-usable and configurable launch files by specifying values that are passed via the command-line, passing in via an <include>, or declared for higher-level files. Args are not global. An arg declaration is specific to a single launch file, much like a local parameter in a method. You must explicitly pass arg values to an included file, much like you would in a method call. 

## Passing an argument to an included file

my_file.launch: 

		<include file="included.launch">
		  <!-- all vars that included.launch requires must be set -->
		  <arg name="hoge" value="fuga" />
		</include>

included.launch: 

		<launch>
		  <!-- declare arg to be passed in -->
		  <arg name="hoge" /> 

		  <!-- read value of arg -->
		  <param name="param" value="$(arg hoge)"/>
		</launch>

## Passing an argument via the command-line

roslaunch uses the same syntax as ROS remapping arguments to specify arg values. 

		$ roslaunch my_file.launch hoge:=my_value      (.launch file is available at the current dir)
		$ roslaunch %YOUR_ROS_PKG% my_file.launch hoge:=my_value

# <param> tag

The <param> tag defines a parameter to be set on the Parameter Server. Instead of value, you can specify a textfile, binfile or command attribute to set the value of a parameter. The <param> tag can be put inside of a <node> tag, in which case the parameter is treated like a private parameter.

You can also set private parameter across a group of nodes by using the ~param syntax (see ROS names) in a <param> tag. The declared parameter will be set as a local parameter in the <node> tags that follow that are in the same scope (i.e. group or ns tag). 

The rosparam command-line tool enables you to query and set parameters on the Parameter Server using YAML syntax. 

## Examples

		<param name="publish_frequency" type="double" value="10.0" />

# <include> tag

The <include> tag enables you to import another roslaunch XML file into the current file. It will be imported within the current scope of your document, including <group> and <remap> tags. All content in the include file will be imported except for the <master> tag: the <master> tag is only obeyed in the top-level file. 

