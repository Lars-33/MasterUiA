import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace
from launch_ros.actions import Node
from launch_ros.actions import SetRemap






def generate_launch_description():

        #  ros2 launch slam_toolbox online_async_launch.py 
    SetRemap(src='/odom',dst='/tb/odom'),
    SetRemap(src='/cmd_vel',dst='/tb/cmd_vel'),
    slam = GroupAction(
        actions=[
            PushRosNamespace('tb'),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('slam_toolbox'),
                        'launch/online_async_launch.py'
                    )
                ),
                launch_arguments={
                'params_file':'src/tb3_cpp/params/mapper_params_lifelong.yaml',
                'use_sim_time':'false'
                }.items()
            ),
        ]
    )


    ld = LaunchDescription()

    ld.add_action(slam)

    return ld

