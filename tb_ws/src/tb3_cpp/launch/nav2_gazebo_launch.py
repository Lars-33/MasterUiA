import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.actions import SetRemap
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

os.environ["TURTLEBOT3_MODEL"] = "waffle"

print('hei')

def generate_launch_description():

    return LaunchDescription([

        GroupAction(
            actions=[
                #SetRemap(src='/odom',dst='follower/odom'),
                #SetRemap(src='/cmd_vel',dst='follower/cmd_vel'),
                #SetRemap(src='/scan',dst='follower/scan'),
                PushRosNamespace('tb'),
                
                # ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py 
                IncludeLaunchDescription(
                    
                    PythonLaunchDescriptionSource(
                        os.path.join(
                            get_package_share_directory('turtlebot3_gazebo'),
                            'launch/turtlebot3_world.launch.py'
                        )
                    ),
                    launch_arguments={
                        'x_pose':'-2.0',
                        'y_pose':'0.5' 
                    }.items()
                ),
            ]
        )
   ])
