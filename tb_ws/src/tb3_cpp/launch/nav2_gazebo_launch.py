import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.actions import SetRemap
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace
import time

print('hei')

os.environ["TURTLEBOT3_MODEL"] = "burger"

def generate_launch_description():

    tb_waffle= GroupAction(
        actions=[
            # ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py 
            IncludeLaunchDescription(
                
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('turtlebot3_gazebo'),
                        'launch/turtlebot3_world.launch.py'
                    )
                ),
                launch_arguments={
                    #'x_pose':'-2.0',
                    #'y_pose':'0.5' 
                }.items()
            ),
        ]
    )



    tb_burger= GroupAction(
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
                        'launch/spawn_turtlebot3.launch.py'
                    )
                ),
                launch_arguments={
                    'x_pose':'-2.0',
                    'y_pose':'0.5' 
                }.items()
            ),
        ]
    )

    ld = LaunchDescription()
    
    #os.environ["TURTLEBOT3_MODEL"] = "waffle"
    #ld.add_action(tb_waffle)
    #time.sleep(20)


    ld.add_action(tb_burger)

    return ld