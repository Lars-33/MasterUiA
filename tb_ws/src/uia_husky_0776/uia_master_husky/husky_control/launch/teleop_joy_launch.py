from launch import LaunchContext, LaunchDescription
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

ARGUMENTS = [

    DeclareLaunchArgument('teleop_logitech_params', default_value=PathJoinSubstitution([FindPackageShare("husky_control"),"config","teleop_logitech.yaml"],),
                          description='Path to teleop_logitech .yaml file. In order to add for example um7(set publish tf to false)'),
]


def generate_launch_description():
    lc = LaunchContext()
    joy_type = EnvironmentVariable('CPR_JOY_TYPE', default_value='logitech')


    filepath_config_joy = PathJoinSubstitution(
        [FindPackageShare('husky_control'), 'config', ('teleop_logitech.yaml')]
    )
    teleop_logitech_params = LaunchConfiguration("teleop_logitech_params")


    node_joy = Node(
        namespace='joy_teleop',
        package='joy',
        executable='joy_node',
        output='screen',
        name='joy_node',
        parameters=[teleop_logitech_params]
    )

    node_teleop_twist_joy = Node(
        namespace='joy_teleop',
        package='teleop_twist_joy',
        executable='teleop_node',
        output='screen',
        name='teleop_twist_joy_node',
        parameters=[teleop_logitech_params]
    )


    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(node_joy)
    ld.add_action(node_teleop_twist_joy)
    return ld