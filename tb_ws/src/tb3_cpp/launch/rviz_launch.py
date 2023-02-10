import os

from launch import LaunchDescription
from launch_ros.actions import Node


os.environ["TURTLEBOT3_MODEL"] = "waffle"

print('hei')

def generate_launch_description():


   return LaunchDescription([

        Node(
            package='turtlesim',
            executable='turtlesim_node'
        ),

        Node( 
            package='turtlebot3_teleop',
            executable='teleop_keyboard',
            output='screen'  
        )

   ])

