from launch import LaunchDescription
from launch_ros.actions import Node

#ros2 run turtlebot3_teleop teleop_keyboard 
def generate_launch_description():
    return LaunchDescription([
        #Node(
        #    package='turtlesim',
        #    namespace='turtlesim1',
        #    executable='turtlesim_node',
        #    name='sim'
        #),
        Node(
            package='turtlebot3_teleop',
            #namespace='tbtelop',
            executable='teleop_keyboard',
        )

    ])