# Autonomous_driving_robot_walle
In order to implement some of the current mainstream image recognition algorithms, and reinforcement learning algorithms, we built Walle, which is driven by a raspberry pi 3B+ and controlled by four wheel differentials for motion. It contains a monocular camera, and two ultrasonic sensors. Because of the computational limitations of Raspberry and latency. We chose to use IP/TCP protocols for bi-directional data transfer between the laptop and the Raspberry over LAN. The image recognition and neural networks that require more com puting power are performed on the laptop, while the motion control of the car and the camera angle shift are controlled by the Raspberry.
Subtasks:
- Lane recognition of German highways 
- Traffic Sign Recognition based on MobileNet SSD
- Depth Estimation using monocular camera

ROS Control Demo: https://www.youtube.com/watch?v=Z1_V9yEkl9s

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


