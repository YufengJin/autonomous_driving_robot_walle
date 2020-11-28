# autonomous_driving_robot_walle
A completely manual mobile robot for sign recognition and slam, and wraps bunches of other algorithms, such as A* algorithm

## Robot components requirement
- 2 servomotor e.g SG90
- raspberry pi 3B+ (here we recommend raspberry pi versions 3 and above, as our system is Ubuntu Mate and there are several sensors, choose the newer one.)
- raspberry camera v2 or v1 (here you can choose any camera you want, but in our repository only raspberry camera driver supported.)
- 2 motor driver, we use L298N, and 4 motor for sure
- wheels, bunches of wires and frame of car(here we build them by hand with wooden planks, but you can also choose 3D printing or other methods.)
- 2 distance sensor, we use ultrasonsic sensors(HC-SR04)

Here is a demonstration of our walle car.


## Installation overview
All our packages are dependent on the ROS(ros operating system), the entire control and calculation is done on the host computer(installed Ubuntu 16.04). raspberry sends image information, and distance information, to the host via tcp protocol. Depending on the state of your local area network, there may be some delays.　We have chosen to sacrifice the latency in favour of a higher, faster level of calculation.

**Let's create and build a workspace:**
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
Instead of catkin_ws, you can choose any other folder name. and put all packages in folder src, then check dependency. build and make. 
```
$ cd ~/catkin_ws
$ rosdep install --from-paths src --ignore-src -r -y
$ catkin_make
```
Some basic ros tutorials, which you can find [here](https://wiki.ros.org/ROS/Tutorials). Installation is [here](https://wiki.ros.org/ROS/Installation).


