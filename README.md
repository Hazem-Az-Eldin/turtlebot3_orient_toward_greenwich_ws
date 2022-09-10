# Goal:
Turtlebot3 should orient toward Greenwich Observatory from anywhere on earth

## Proposed Solution:

The robot is using GPS sensor to read its current Longitude and Latitude, with a given  Longitude and Latitude of the Greenwich Observatory. For measuring its  orientation, IMU sensor was chosen. Given these information, the robot should be able to calculate the bearing and adjust itself toward the goal.

Note: Turtlebot3 does not come with a pre-defined gps sensor, hence the gps sensor was added, this work was done by: https://github.com/cocodmdr/turtlebot3_robot_localization_ws

## Proposed Design:

There are Two main Classes that communicate with each other using ROS. 

The First class is the Turtlebot3 which is responsible for everything related to the robot. For example, controlling the motor, reading the sensor values and orient to the goal. 
The second class is the Robot-Interface, which is responsible for choosing the mode of operation and to drive the robot manually.

There are three modes supported by the robot: 
    1. Standby: default mode (mean the robot is ready to be used) 
    2. Manual: The robot is controlled through the Terminal from the Robot-Interface class ( based on teleop)
    3. Auto: The robot orient itself from anywhere toward Greenwich Observatory


Note: 

when designing the solution, there were two options for testing: 

1) use the different Test cases for different locations

2) switch robot to manual and drive anywhere and test.

Due to the time constraint the second option was chosen, since it allows infinity tests scenarios for anywhere, and it is more challenging to implement. In ideal case, both test should have been considered. 

## Known Limitation: 
   1) Using one sensor as the only source of information is not ideal, especially for outdoors. For real scenario, an sensor fusion can be used to get more reliable data from different sensors. 
   2) PID controller was chosen with value of 1 for P and 0 for both I and D, it still have a good performance since this is a simulated environment. For real application, these parameters needed to be carefully tuned, and for more complicated task such a trajectory following, an optimal controller or model predictive controller should be considered
   3)  For a real application, a more time should be dedicated to choose the appropriate quality of the server for each topic. 


## Requirements: 

* ROS2-Foxy
* Python3
* Gazebo

## How To Run: 

    1)  Download the Package & navigate to Package
    2)  Build the Package by Typing Colcon build 
    3)  open 3 Terminals:
    4)  source the workspace by typing source install/setup.bash (each Terminal)
    5)  In the First Terminal:  ros2 run turtlebot3_orient_toward_greenwich Robot_interface 
    6) In the Second Terminal: ros2 launch turtlebot3_orient_toward_greenwich turtlebot_launch.py 
    7) in The Third Terminal: 
        1. export TURTLEBOT3_MODEL=waffle
        2. export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_orient_toward_greenwich_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/
        3. ros2 launch turtlebot3_gazebo empty_world.launch.py


~~~
