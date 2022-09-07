from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_orient_toward_greenwich',
            executable='Turtlebot',
            parameters=[
            {"greenwich_longtitude": -0.001545 },
            {"greenwich_latitude": 51.477928 },
            {"max_velocity": 1.0},
            {"kp": 1.0 },
            {"ki": 0.0 },
            {"kd": 0.0 }
            ],
            output="screen", 
        ),

    ])