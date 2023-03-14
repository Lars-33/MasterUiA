#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator


class PoseSub(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            PoseStamped,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('%s' % msg.header.frame_id)
        print(msg.header.frame_id)

        goal_pose = msg 
        BasicNavigator().goToPose(goal_pose) 


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = PoseSub()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()