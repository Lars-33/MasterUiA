from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

ARGUMENTS = [

    DeclareLaunchArgument('localization_params', default_value=PathJoinSubstitution([FindPackageShare("husky_control"),"config","localization.yaml"],),
                          description='Path to Localization .yaml file. In order to add for example um7(set publish tf to true)'),

]

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_node',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("husky_control"), 'config', 'localization.yaml')],
           ),
    ])