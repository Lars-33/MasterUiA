#!/usr/bin/env python3
import rclpy 
from geometry_msgs.msg import Twist 
from rclpy.node import Node
import time 

# converts cmd_vel to tb/cmd_vel with a time delay

class subpub(Node):
    def __init__(self):
        super().__init__('subpub')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.subscription
        self.publisher_ = self.create_publisher(Twist, 'tb/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0
        self.delay = 9
        self.submsg = Twist()  # Initialize the submsg attribute to Twist() 
        self.array_linear_x = [0.25] * self.delay #set initial vel start here 
        self.array_angular_z = [0.0] * self.delay

    def listener_callback(self,submsg):
        self.submsg = submsg

    def timer_callback(self):
        pubmsg = Twist()

        pubmsg.linear.x = self.array_linear_x[self.i] 
        pubmsg.angular.z = self.array_angular_z[self.i]
        
        self.array_linear_x[self.i] = self.submsg.linear.x
        self.array_angular_z[self.i] = self.submsg.angular.z
        
        self.i = self.i + 1 

        print('sub = ', self.submsg, '\n')
        print('pub = ', pubmsg, '\n')
        self.publisher_.publish(pubmsg)
        if self.i == self.delay :
            self.i = 0

def main(): 
    rclpy.init()
    publisher = subpub()  
    rclpy.spin(publisher)   
            
    rclpy.shutdown()

if __name__ == '__main__' : 
    main()