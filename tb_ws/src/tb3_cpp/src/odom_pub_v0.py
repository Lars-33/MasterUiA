#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator import BasicNavigator
from nav_msgs.msg import Odometry

from rclpy.node import Node

# script for me breaking down Odometry() msg 

class odom_pub(Node):
    def __init__(self):
        super().__init__('topic')
        self.publisher_ = self.create_publisher(Odometry, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Odometry()
        msg.header.stamp.sec = 1
        msg.header.stamp.nanosec=2
        msg.header.frame_id = 'lars'
        msg.child_frame_id = 'barn'
        msg.pose.pose.position.z = 3.3 # x y z 
        msg.pose.pose.orientation.w = 4.4 # x y z w
        msg.pose.covariance[0:36] = 5.5 # 0 to 36
        msg.twist.twist.linear.z = 6.6 # x y z 
        msg.twist.twist.angular.z = 7.7 # x y z 
        msg.twist.covariance[0:36] = 8.8 # 0 to 36
        print(msg,'\n')
        print(msg.twist.twist,'\n')
        self.publisher_.publish(msg)

def main(): 
    rclpy.init()
    publisher = odom_pub() 

    rclpy.spin(publisher) 

    rclpy.shutdown()

if __name__ == '__main__' : 
    main()
