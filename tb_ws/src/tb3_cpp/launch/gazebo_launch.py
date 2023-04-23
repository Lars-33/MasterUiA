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

# fail at trying to make a launch file for tb gazebo 

os.environ["TURTLEBOT3_MODEL"] = "waffle"

def generate_launch_description():

    gazebo= GroupAction(
        actions= [
            IncludeLaunchDescription(          
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('gazebo_ros'),
                        'launch/gazebo.launch.py'
                    )
                ),
                launch_arguments={
                    #'x_pose':'-2.0',
                    #'y_pose':'0.5' 
                }.items()
            )
        ]
    )

    tb_waffle= GroupAction(
        actions=[
            # ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py 
            PushRosNamespace('tb'),            
            IncludeLaunchDescription(

                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory('turtlebot3_gazebo'),
                        'launch/turtlebot3_world.launch.py'
                    )
                ),
                launch_arguments={
                    'x_pose':'-1.0',
                    'y_pose':'0.0' 
                }.items()
            ),
        ]
    )

    tb_burger= GroupAction(
        actions=[
            #SetRemap(src='/odom',dst='follower/odom'),
            #SetRemap(src='/cmd_vel',dst='follower/cmd_vel'),
            #SetRemap(src='/scan',dst='follower/scan'),
            
            
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
    #ld.add_action(tb_burger)
    ld.add_action(gazebo)
    ld.add_action(tb_waffle)


    return ld