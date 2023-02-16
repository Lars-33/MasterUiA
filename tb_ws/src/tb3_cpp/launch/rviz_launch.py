import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node

os.environ["TURTLEBOT3_MODEL"] = "waffle"

print('hei')

def generate_launch_description():

   return LaunchDescription([

        Node(
            package='rqt_graph',
            executable='rqt_graph'
        ),

        # ros2 launch nav2_bringup rviz_launch.py 
        IncludeLaunchDescription(
            
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('nav2_bringup'),
                    'launch/rviz_launch.py'
                )
            ),
        )

   ])

