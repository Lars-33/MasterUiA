from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


ARGUMENTS = [

    DeclareLaunchArgument('teleop_interactive_markers_params', default_value=PathJoinSubstitution([FindPackageShare("husky_control"),"config","teleop_interactive_markers.yaml"],),
                          description='Path to teleop_interactive_markers .yaml file. In order to add for example um7(set publish tf to false)'),

    DeclareLaunchArgument('twist_mux_params', default_value=PathJoinSubstitution([FindPackageShare("husky_control"),"config","twist_mux.yaml"],),
                          description='Path to twist_mux .yaml file. In order to add for example um7(set publish tf to false)'),

]

def generate_launch_description():

    filepath_config_twist_mux = PathJoinSubstitution(
        [FindPackageShare('husky_control'), 'config', 'twist_mux.yaml']
    )

    filepath_config_interactive_markers = PathJoinSubstitution(
        [FindPackageShare('husky_control'), 'config', 'teleop_interactive_markers.yaml']
    )

    teleop_interactive_markers_params = LaunchConfiguration("teleop_interactive_markers_params")
    twist_mux_params = LaunchConfiguration("twist_mux_params")


    node_interactive_marker_twist_server = Node(
        package='interactive_marker_twist_server',
        executable='marker_server',
        name='twist_server_node',
        remappings={('cmd_vel', 'twist_marker_server/cmd_vel')},
        parameters=[teleop_interactive_markers_params],
        output='screen',
    )

    node_twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        output='screen',
        remappings={('/cmd_vel_out', '/husky_velocity_controller/cmd_vel_unstamped')},
        parameters=[twist_mux_params]
    )

    ld = LaunchDescription(ARGUMENTS)

    ld.add_action(node_interactive_marker_twist_server)
    ld.add_action(node_twist_mux)
    return ld