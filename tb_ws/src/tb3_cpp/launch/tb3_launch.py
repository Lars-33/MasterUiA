import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
#from launch_ros.actions import Node

#from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, Command, FindExecutable 
from launch_ros.substitutions import FindPackageShare

from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess

from launch_ros.actions import SetRemap

os.environ["TURTLEBOT3_MODEL"] = "waffle"

os.system('sudo chmod a+rw /dev/ttyACM0')

def generate_launch_description():

    return LaunchDescription([
        #GroupAction(
        #    actions=[
            
                SetRemap(src='/odom',dst='tb/odom'),

                IncludeLaunchDescription(
                    

                    PythonLaunchDescriptionSource(
                        os.path.join(
                            get_package_share_directory('turtlebot3_bringup'),
                            'launch/robot.launch.py'
                        )
                    ),
                            
                    launch_arguments={
                        'tb3_param_dir':'./src/tb3_cpp/params/tb3_param.yaml'
                            
                        }.items()
            )
        #    ]
        #)
    ])

