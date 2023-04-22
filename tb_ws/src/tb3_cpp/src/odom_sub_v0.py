#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator import BasicNavigator
from nav_msgs.msg import Odometry

from rclpy.node import Node



class odom_sub(Node):
    def __init__(self):
        super().__init__('topic')
        self.subscription = self.create_subscription(Odometry, 'topic', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        print(msg)

def main(): 
    rclpy.init()

    publisher = odom_sub()  
    rclpy.spin(publisher)   
            
    rclpy.shutdown()

if __name__ == '__main__' : 
    main()