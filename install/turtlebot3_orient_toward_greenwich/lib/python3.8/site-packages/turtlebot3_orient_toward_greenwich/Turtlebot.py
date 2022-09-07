from tkinter import E
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
import math 
from . import Utilities 
from .PID_controller import  PID
from std_msgs.msg import String
from turtlebot3_msgs.msg import CustomArray

class TurtleBot(Node):
    """
     This class represnts the robot, From reading sensor values to control the velocity. 
    """

    def __init__(self):
        super().__init__('Turtlebot')
        self.gps_sub = self.create_subscription(NavSatFix, 'gps/fix', self.gps_callback, 1) 
        self.imu_sub = self.create_subscription(Imu, 'imu/data', self.imu_callback, 1)
        self.subscription = self.create_subscription(String,'mode_control',self.mode_toggler_calleback,1) 
        self.manual_speed_controller_sub = self.create_subscription(CustomArray,'manual_control',self.manual_commands_callback,1)
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 1)
        self.declare_parameter('greenwich_longtitude')
        self.declare_parameter('greenwich_latitude')
        self.declare_parameter('max_velocity')
        self.declare_parameter('kp')
        self.declare_parameter('ki')
        self.declare_parameter('kd')
        self.kp, self.ki, self.kd = self.get_parameters(['kp', 'ki', 'kd'])
        self.pid_controller = PID( self.kp.value, self.ki.value ,self.kd.value)                                           
        self.robot_yaw = 0.0               
        self.mode = "Standby"

    def manual_commands_callback(self,msg): 
        """
        Linear and Angular velocities are set from the RobotInterface Script
        """
        if self.mode == "Manual":               
            self.set_velocityy(msg.data[0],msg.data[1])
      
        
    def mode_toggler_calleback(self, msg):
        """
        There are three Modes supported:
        Standby: Robot is ready to be used
        Manual:  Robot is  manually controlled 
        Auto:    Robot Rotate Toward Greewich 
        """
        self.mode = msg.data
        self.stop()

    def gps_callback(self,msg):
        """
        the GPS callback is used to get the latitude and longitude
        Note: rotating the robot is chosen here since it is based on the gps reading and there is no point of creating a seperate publisher callback
        """                             
        heading_angle = self.calculate_heading_angle(msg.latitude,msg.longitude)  
        if self.mode=="Auto":                                     
            self.auto_control(heading_angle)


    def auto_control(self,heading_angle):
        """
        orient Toward GreenWich
        """
        angle_error = self.calculate_error_angle(heading_angle)
        self.set_velocityy(0.0,angle_error)

    
    def imu_callback(self, msg):         # To make sure test use this website https://www.igismap.com/map-tool/bearing-angle for test scripts
        """
        the IMU callback is used to get the current orientation of the robot
        """   
        _ , _ , self.robot_yaw = Utilities.euler_from_quaternion(msg.orientation)            

        
    def set_velocityy(self,linear_vel,angular_vel):
        cmd_message = Twist() 
        cmd_message.linear.x  = self.limit_max_vel(linear_vel)
        cmd_message.angular.z = self.limit_max_vel(angular_vel)
        self.cmd_pub.publish(cmd_message)


    def stop(self): 
        self.set_velocityy(0.0,0.0)


    def calculate_heading_angle(self,Latitude,Longtitude):
        """
        Calculate the Angle to the Goal, based on the current Latitude and Longtitude of the robot
        """ 
        greenwich_longtitude,greenwich_latitude = self.get_parameters(['greenwich_longtitude','greenwich_latitude'])
        robot_coordinates = (Latitude,Longtitude)
        greenwich_coordinates = (greenwich_latitude.value,greenwich_longtitude.value)
        heading_angle = Utilities.calculate_initial_compass_bearing(robot_coordinates,greenwich_coordinates)
        return heading_angle

    def calculate_error_angle(self,heading_angle):
        """
        Calculate the error between the Bearing and the current robot's angle
        """  
        angle_error = heading_angle - self.robot_yaw
        angle_error = self.shortest_rotation(angle_error)
        angle_error = self.pid_controller.update_controller(angle_error)
        return angle_error

    def shortest_rotation(self,angle):
        """
        check which shorter: rotating from the left or the right
        """  
        if angle > math.pi:
            angle -= 2 * math.pi
        if angle < - math.pi:
            angle += 2 * math.pi
        return angle

    def limit_max_vel(self,velocity):
          """
           Limit the max veloicty  of the robot
          """ 
          max_velocity = self.get_parameter('max_velocity')
          if  velocity > 0.0:
            velocity = min(max_velocity.value, velocity) 
          elif velocity < 0.0:
            velocity = max(-max_velocity.value, velocity)

          return velocity


def main(args=None):

    rclpy.init(args=args)
    turtlebot = TurtleBot()
    rclpy.spin(turtlebot)
    turtlebot.destroy_node()    
    rclpy.shutdown()  
    
if __name__ == '__main__':
    main()