#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped

from rclpy.node import Node



class odom(BasicNavigator): # mabye this needs to be changed with BasicNavigator
    def __init__(self):
        super().__init__('topic')
        self.publisher_ = self.create_publisher(getFeedback, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        
    def timer_callback(self):
        msg = BasicNavigator().getFeedback()
        print(msg)
        self.publisher_.publish(msg)

def main(): 
    rclpy.init()

    publisher = odom()  
    rclpy.spin(publisher)   
            
    rclpy.shutdown()

if __name__ == '__main__' : 
    main()