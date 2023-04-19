import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.descriptions import ComposableNode
from ament_index_python import get_package_share_directory



def generate_launch_description():

    nav2_yaml = os.path.join(get_package_share_directory)

    # Nodes
    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'use_sim_time':True},
                    {'yaml_filename': 'map/Masterlabben.yaml'}
                    ]
    )
    amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[{'yaml_filename':'src/tb3_cpp/params/amcl_params.yaml'}]
    )


    # Launch Description
    ld = LaunchDescription()


    # Nodes
    ld.add_action(map_server)
    #ld.add_action(amcl)

    return ld
