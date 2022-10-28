# ros_tasks

<h3><u>Task-1</u></h3>
<ul>
  <li>Create package with std-msgs roscpp and rospy as dependencies</li>
  <li>write subscribe.py and publish.py and add them to scripts directory inside the package</li>
  <li>edit Cmake file </li>
  <li>run roscore </li>
  <li>run chmod -x for both nodes </li>
  <li>source the devel/setup.bash file and run catkin-make </li>
  <li>rosrun for both nodes </li>
</ul>
<h4>Problems Faced</h4>
<ul>
<li>first tried with c++ instead of python and could not get it to work(must have missed something) </li>
<li>forgot to roscore and source the setup.bash file</li>
</ul>

<h3><u>Task-2</u></h3>
Site used:-https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/
<ul>
<li>followed instructions on above site to install ros</li>
<li>use teleop launch file to control bot and store readings in a bag file<\li>
<li>wrote a node that subscribes to the cmd_vel topic of the bag file, adds noise and publishes to a another topic noise_add<\li>
  <h4>Problems faced:</h4>
  unmet dependencies when installing turtlebot
  had to delete multiple packages and reinstall everything to make turtlebot work
  
<h6>Note: publishing to cmd_vel, starting the simulation and playin g the rosbag would have given us the path with noise added</h6>
