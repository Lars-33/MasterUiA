#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

from rclpy.node import Node

from std_msgs.msg import String

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

class MinimalPublisher(Node):
    
    def __init__(self,x_pos):
        super().__init__('minimal_publisher2')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.x_pos = x_pos #BasicNavigator().getFeedback().current_pose.pose.position.x 

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d x_pos: %f' %(self.i , self.x_pos )
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(): 
    rclpy.init()
    
    nav = BasicNavigator()
    
    # --- Set initial pose 
    initial_pose = create_pose_stamped( nav , -1.997726 , -0.499904 , 0.091122)
    #nav.setInitialPose( initial_pose )

    # --- Wait for Nav2 
    nav.waitUntilNav2Active()

    # --- Send Nav2 goal 
    goal_pose = create_pose_stamped(nav , 2.0 , 0.0 , 1.57)
    nav.goToPose(goal_pose)

    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        print( feedback , "\n")
        #print( feedback.navigation_time , "\n")
        #print ( feedback.distance_to_goal , "\n")
        print ( feedback.current_pose.pose.position , "\n")
        x_pos = nav.getFeedback().current_pose.pose.position.x 
        print ( x_pos, "\n")
        publisher = MinimalPublisher(x_pos)      
        rclpy.spin(publisher)
            
    
    #x_pos = feedback.current_pose.pose.position.x 

    
    

    print(nav.getResult())
    # --- Shutdown

    rclpy.shutdown()

if __name__ == '__main__' : 
    main()