import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory



os.environ["TURTLEBOT3_MODEL"] = "waffle"

print('hei')

def generate_launch_description():


   return LaunchDescription([

        #  ros2 launch slam_toolbox online_async_launch.py 
        IncludeLaunchDescription(
            
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('slam_toolbox'),
                    'launch/online_async_launch.py'
                )
            ),
        ),


        # ros2 launch nav2_bringup localization_launch.py 
        IncludeLaunchDescription(
            
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('nav2_bringup'),
                    'launch/bringup_launch.py'
                )
            ),
                    
            #launch_arguments={
            #    'map':'/home/lars/MasterUiA/tb_ws/map/Masterlabben.yaml'
            #        
            #    }.items()
        )

        # ros2 launch nav2_bringup rviz_launch.py 
        #IncludeLaunchDescription(
        #    
        #    PythonLaunchDescriptionSource(
        #        os.path.join(
        #            get_package_share_directory('nav2_bringup'),
        #            'launch/rviz_launch.py'
        #        )
        #    ),
        #)

   ])

