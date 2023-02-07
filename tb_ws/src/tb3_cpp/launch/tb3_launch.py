import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
#from launch.actions import DeclareLaunchArgument
#from launch_ros.actions import Node

#from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, Command, FindExecutable 
from launch_ros.substitutions import FindPackageShare

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([

        # export TURTLEBOT3_MODEL=waffle
        
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('turtlebot3_bringup'),
                    'launch/robot.launch.py')
                ),
                    
                launch_arguments={
                    'tb3_param_dir':'./src/tb3_cpp/params/tb3_param.yaml'
                    
                }.items()
        )

        
       
    ])
