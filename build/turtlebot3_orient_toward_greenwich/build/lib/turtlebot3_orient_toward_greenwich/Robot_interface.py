#!/usr/bin/env python
import rclpy
import sys, select, termios, tty
from . import Utilities 
from std_msgs.msg import String
from turtlebot3_msgs.msg import CustomArray
import sys
from rclpy.node import Node


class RobotInterface(Node):
    """
     This class is an interface between the user and the robot, From this class you can 
     choose the mode of the robot from:
     Standby: Robot is stable and ready to be used 
     Manual:  Robot is controlled from the terminal, commands are sent using this class 
     Auto:    Robot is orienting Automatically Toward Greenwich Coordinates 
    """
    def __init__(self):
        super().__init__('Robot_Interface')
        self.mode_toggler_pub = self.create_publisher(String, 'mode_control', 1)
        self.speed_pub = self.create_publisher(CustomArray, 'manual_control',1 )

    def manual_mode_handler(self):
        """
        Read input keyboard for Manual-Mode 
        """ 
        x = 0
        th= 0
        speed = 0.5
        turn =0.5

        while(1):
            manual_key = Utilities.getKey()

            if manual_key in Utilities.moveBindings.keys():
                x = Utilities.moveBindings[manual_key][0]
                th = Utilities.moveBindings[manual_key][3]

            elif manual_key in Utilities.speedBindings.keys():
                speed = speed * Utilities.speedBindings[manual_key][0]
                turn  = turn * Utilities.speedBindings[manual_key][1]

            else:
                x  = 0.0
                th = 0.0

                if manual_key == '\x03' or manual_key =='e' or manual_key =='E' :	
                    self.set_mode("Standby")
                    break

            self.send_manual_commands(x,th,speed,turn)
    

    def auto_mode_handle(self):
        """
        To Keep within Auto mode in terminal, until terminated by user 
        """
        auto_key = Utilities.getKey()
        while(1):
            if auto_key == '\x03' or auto_key =='e' or auto_key =='E' :
                self.set_mode("Standby")
                break
                            

    def send_manual_commands(self,x,th,speed,turn):
        """
        send Manual commands to TurtleBot 
        """
        speed_msg = CustomArray()
        manual_command = [x*speed,th*turn]
        speed_msg.data = manual_command
        self.speed_pub.publish(speed_msg)

    
    def set_mode(self,mode):
         """
         Set TurtleBot's Mode 
         """
         mode_msg  = String()
         mode_msg.data = mode
         self.mode_toggler_pub.publish(mode_msg)

    
    def run(self):  
        """
        Run the Main code for Choosing Mode and send commands to Turtlebot 
        """
        print(Utilities.init_msg)
        try:

            while(1):
                key = Utilities.getKey()
                    
                if key == 'A' or key =='a':
                    print(Utilities.auto_msg) 
                    self.set_mode("Auto")
                    self.auto_mode_handle()
                    print(Utilities.init_msg)
                    
                elif key == 'M' or key =='m':
                    print(Utilities.manual_msg)
                    self.set_mode("Manual")
                    self.manual_mode_handler()          
                    print(Utilities.init_msg)

                else:

                    if (key == '\x03' or key == 'e' or key =='E'): 
                        break
                    
                    self.set_mode("Standby")
                    print(Utilities.wrong_msg)
        
        except:
            print("Error")
        
        finally:
            self.set_mode("Standby")




def main(args=None):
    rclpy.init(args=args)
    robot_interface = RobotInterface()
    robot_interface.run()





if __name__ == '__main__':
    main()
