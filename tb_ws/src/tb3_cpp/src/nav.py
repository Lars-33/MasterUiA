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
    
    def __init__(self):
        super().__init__('wwwwwww')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        #self.feedback = BasicNavigator().getFeedback().current_pose.pose.position.x
        #feedback = BasicNavigator().getFeedback()
        #self.x_pos = feedback.current_pose.pose.position.x
        #self.y_pos = y_pos
        #self.z_eul = z_euler

    def timer_callback(self):
        msg = BasicNavigator()
        #msg.data = 'x: %f y: %f z: %f' %( self.x_pos , self.y_pos, self.z_eul)
        #msg.data = 'Hello World: %d' % self.i
        msg.get = BasicNavigator().getFeedback().current_pose.pose.position.x
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Pub: "%s"' % msg.data)
        self.i += 1
        

class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')
        self.publisher_ = self.create_publisher(Odometry, 'odometry', 10)

    def publish_odometry(self, x, y, z, quat_x, quat_y, quat_z, quat_w):
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = z
        msg.pose.pose.orientation.x = quat_x
        msg.pose.pose.orientation.y = quat_y
        msg.pose.pose.orientation.z = quat_z
        msg.pose.pose.orientation.w = quat_w
        self.publisher_.publish(msg)

def main(): 
    rclpy.init()
    nav = BasicNavigator()

    # --- Set initial pose 
    initial_pose = create_pose_stamped( nav , -1.997726 , -0.499904 , 0.091122)
    #nav.setInitialPose( initial_pose )

    # --- Wait for Nav2 
    nav.waitUntilNav2Active()

    # --- Send Nav2 goal 
    goal_pose = create_pose_stamped(nav , 2.0 , 0.0 , 3.14)
    nav.goToPose(goal_pose)

    #while not nav.isTaskComplete():
    #    pose = nav.getFeedback().current_pose.pose
    #    x_pos = pose.position.x
    #    y_pos = pose.position.y
    #    x_euler , y_euler , z_euler = tf_transformations.euler_from_quaternion( [pose.orientation.x , pose.orientation.y , pose.orientation.z , pose.orientation.w] )
    #    print ('x_pos = ',x_pos,'y_pos = ', y_pos ,'z_euler = ', z_euler, "\n \n")
    
    
    publisher = OdometryPublisher()   
    rclpy.spin(publisher)
                
    #x_pos = feedback.current_pose.pose.position.x 

    print(nav.getResult())
    # --- Shutdown

    rclpy.shutdown()

if __name__ == '__main__' : 
    main()