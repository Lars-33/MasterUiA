#!/usr/bin/env python3
import rclpy 
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

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

def main(): 
    rclpy.init()
    nav= BasicNavigator()

    # --- Set initial pose 
    initial_pose = create_pose_stamped( nav , -1.997726 , -0.499904 , 0.091122)
    nav.setInitialPose( initial_pose )

    # --- Wait for Nav2 
    nav.waitUntilNav2Active()

    # --- Send Nav2 goal 
    goal_pose = create_pose_stamped(nav , 2.0 , 0.0 , 1.57)
    nav.goToPose(goal_pose)

    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        print(feedback)
        
    print(nav.getResult())
    # --- Shutdown

    rclpy.shutdown()

if __name__ == '__main__' : 
    main()