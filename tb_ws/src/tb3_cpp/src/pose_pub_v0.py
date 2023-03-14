#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped

from rclpy.node import Node



class odom(Node):
    def __init__(self):
        super().__init__('topic')
        self.publisher_ = self.create_publisher(PoseStamped, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = PoseStamped()
        nav = BasicNavigator()
        msg.header.frame_id = 'map'
        msg.header.stamp = nav.get_clock().now().to_msg()
        msg.pose.position.x = 2.0
        msg.pose.position.y = 0.5
        msg.pose.position.z = 0.0
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.7079509
        msg.pose.orientation.w = -0.7062616
        print(msg)
        self.publisher_.publish(msg)

def main(): 
    rclpy.init()

    publisher = odom()  
    rclpy.spin(publisher)   
            
    rclpy.shutdown()

if __name__ == '__main__' : 
    main()