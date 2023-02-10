import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

import launch


base_path = os.path.realpath(get_package_share_directory('tb3_cpp'))
rviz_path=base_path+'/params/test.rviz'

def generate_launch_description():


   return LaunchDescription([

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d',str(rviz_path)]
            #arguments=['-d', str(.rviz2/lars.rviz)]
        )


   ])

