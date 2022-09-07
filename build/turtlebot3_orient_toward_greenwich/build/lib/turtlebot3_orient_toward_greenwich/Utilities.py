import numpy as np
import math
import sys, select, termios, tty


init_msg = """
Main Menu
---------------------------
Please choose a Mode
For Manual control type: M/m
For Auto   Control type: A/a
---------------------------
Type: CTRL-C to terminate the program
"""

manual_msg = """
Manual Mode - Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
r/c : increase/decrease only angular speed by 10%
e / CTRL-C: to quit Manual Mode
"""
auto_msg = """
Auto Mode - orienting toward Greenwich
---------------------------
e / CTRL-C  to quit Auto Mode
"""

wrong_msg = """
Wrong Input - Please choose between
Auto:   A/a
Manual: M/m   
---------------------------

e / CTRL-C to terminate the program
"""


moveBindings = {
		'i':(1,0,0,0),
		'o':(1,0,0,-1),
		'j':(0,0,0,1),
		'l':(0,0,0,-1),
		'u':(1,0,0,1),
		',':(-1,0,0,0),
		'.':(-1,0,0,1),
		'm':(-1,0,0,-1),
		'O':(1,-1,0,0),
		'I':(1,0,0,0),
		'J':(0,1,0,0),
		'L':(0,-1,0,0),
		'U':(1,1,0,0),
		'<':(-1,0,0,0),
		'>':(-1,-1,0,0),
		'M':(-1,1,0,0),
		't':(0,0,1,0),
		'b':(0,0,-1,0),
	       }

  
speedBindings={				
		'q':(1.1,1.1),
		'z':(.9,.9),
		'w':(1.1,1),
		'x':(.9,1),
		'r':(1,1.1),
		'c':(1,.9),
	      }


def getKey():
    """
    Get input from keyboard
    """
    settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key



def euler_from_quaternion(quaternion): # source code from https://gist.github.com/salmagro/2e698ad4fbf9dae40244769c5ab74434
    """
    Converts quaternion (w in last place) to euler roll, pitch, yaw
    quaternion = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
    x = quaternion.x
    y = quaternion.y
    z = quaternion.z
    w = quaternion.w

    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.arcsin(sinp)

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw



def calculate_initial_compass_bearing(pointA, pointB): # source code from: https://gist.github.com/jeromer/2005586
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)
    
    return initial_bearing
