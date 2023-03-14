#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator  import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

from rclpy.node import Node

from std_msgs.msg import String 
import time

def create_pose_stamped( nav , position_x , position_y , orientation_z): 
    q_x , q_y , q_z , q_w = tf_transformations.quaternion_from_euler( 0.0 , 0.0 , orientation_z )
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = nav.get_clock().now().to_msg()
    pose.pose.position.x = position_x
    pose.pose.position.y = position_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose



class odom(Node):
    def __init__(self,x,y,z , x_q,y_q,z_q,w_q):
        super().__init__('topic')
        self.publisher_ = self.create_publisher(PoseStamped, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.x = x ; self.y = y ; self.z = z ; 
        self.x_q= x_q; self.y_q= y_q; self.z_q= z_q; self.w_q= w_q; 


    def timer_callback(self):
        msg = PoseStamped()
        nav = BasicNavigator()
        print(nav.getFeedback() , '\nooooooooooooooooooooooooo\n')
        if not nav.isTaskComplete() or True: 
            print(nav.getFeedback() , '\nooooooooooooooooooooooooo\n')
        msg.header.frame_id = 'map'
        msg.header.stamp = nav.get_clock().now().to_msg()
        msg.pose.position.x = self.x
        msg.pose.position.y = self.y
        msg.pose.position.z = self.z
        msg.pose.orientation.x = self.x_q
        msg.pose.orientation.y = self.y_q
        msg.pose.orientation.z = self.z_q
        msg.pose.orientation.w = self.w_q
        self.publisher_.publish(msg)

def main(): 
    rclpy.init()
    nav = BasicNavigator()

    # --- Wait for Nav2 
    nav.waitUntilNav2Active()

    # --- Send Nav2 goal 
    goal_pose = create_pose_stamped(nav , 2.0 , 0.0 , 3.14)
    nav.goToPose(goal_pose)

    print(nav)
    print( nav.getFeedback() , '\n')
    if not nav.isTaskComplete() or True: 
        print(nav)
        print(nav.getFeedback() , '\n----------------------------\n\n')
    print(nav)
    print( nav.getFeedback() , '\n-------------------')

    while True : 
        # initiolice pose varibals 
        print(nav.getFeedback())
        #if not nav.isTaskComplete() or True:
        print( nav.getFeedback().current_pose.pose.position.x )
        x = nav.getFeedback().current_pose.pose.position.x
        y = nav.getFeedback().current_pose.pose.position.y
        z = nav.getFeedback().current_pose.pose.position.z
        orientation = nav.getFeedback().current_pose.pose.orientation
        x_q = orientation.x
        y_q = orientation.y
        z_q = orientation.z
        w_q = orientation.w
        print('publish')
        
        publisher = odom(x,y,z , x_q,y_q,z_q,w_q)  
        rclpy.spin_once(publisher)   

        print('\n---------------------------\n')
        


    rclpy.shutdown()

if __name__ == '__main__' : 
    main()