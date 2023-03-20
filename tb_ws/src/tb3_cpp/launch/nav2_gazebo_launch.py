import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.actions import SetRemap


os.environ["TURTLEBOT3_MODEL"] = "waffle"

print('hei')

def generate_launch_description():

   return LaunchDescription([
        #SetRemap(src='/odom',dst='follower/odom'),
        #SetRemap(src='/cmd_vel',dst='follower/cmd_vel'),
        
        # ros2 launch nav2_bringup rviz_launch.py 
        IncludeLaunchDescription(
            
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('turtlebot3_gazebo'),
                    'launch/spawn_turtlebot3.launch.py'
                )
            ),
            launch_arguments={
                'x_pose':'-2.0',
                'y_pose':'0.5' 
            }.items()
        )

   ])
