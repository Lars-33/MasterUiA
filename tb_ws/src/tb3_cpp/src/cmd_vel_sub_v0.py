#!/usr/bin/env python3
import rclpy 
from geometry_msgs.msg import Twist 
from rclpy.node import Node

# just for me testing Twist() msg 

class odom(Node):
    def __init__(self):
        super().__init__('twist')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.subscription
        
    def listener_callback(self):
        print(msg)

def main(): 
    rclpy.init()

    publisher = odom()  
    rclpy.spin(publisher)   
            
    rclpy.shutdown()

if __name__ == '__main__' : 
    main()