import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([
        
        
        
        
        
	 #ros2 launch turtlebot3_bringup robot.launch.py
        
        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource(
        #        os.path.join(
        #            get_package_share_directory('demo_nodes_cpp'),
        #            'launch/topics/talker_listener.launch.py'))
        #),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('turtlebot3_bringup'),
                    'launch/robot.launch.py'))
        )


    ])
