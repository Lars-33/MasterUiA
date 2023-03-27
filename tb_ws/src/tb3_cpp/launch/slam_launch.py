import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

#from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, Command, FindExecutable 
from launch_ros.substitutions import FindPackageShare

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import SetRemap
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
import time



def generate_launch_description():

        #  ros2 launch slam_toolbox online_async_launch.py 
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
                #'map':'/home/lars/MasterUiA/tb_ws/map/Masterlabben.yaml'
                'params_file':'src/tb3_cpp/params/mapper_params_lifelong.yaml'
                }.items()
            ),
        ]
    ),

    ld = LaunchDescription()

    ld.add_action(slam)

    return ld

