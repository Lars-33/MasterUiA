#!/usr/bin/env python3
import rclpy 
from geometry_msgs.msg import Twist 
from rclpy.node import Node

# just for me testing Twist() msg 

class odom(Node):
    def __init__(self):
        super().__init__('twist')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x=1.1 # x y z
        msg.angular.x=2.2 # x y z 
        print(msg)
        self.publisher_.publish(msg)

def main(): 
    rclpy.init()

    publisher = odom()  
    rclpy.spin(publisher)   
            
    rclpy.shutdown()

if __name__ == '__main__' : 
    main()