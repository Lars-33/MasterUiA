import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
#from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, Command, FindExecutable 
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import SetRemap
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

os.environ["TURTLEBOT3_MODEL"] = "waffle"   # exporting "TURTLEBOT3_MODEL" is required by "robot.launch.py"
os.system('sudo chmod a+rw /dev/ttyACM0')
os.system('sudo chmod 666 /dev/ttyUSB0')    # opens acsess to LiDAR and OpenCR1.0 

def generate_launch_description():

    return LaunchDescription([
        #SetRemap(src='/odom',dst='/tb/odom'),
        #SetRemap(src='/cmd_vel',dst='/tb/cmd_vel'),
        #DeclareLaunchArgument("tb", default_value=TextSubstitution(text="tb")),
        GroupAction(
            actions=[
                PushRosNamespace('tb'),     # Pushing namespace to TB3 
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        os.path.join(
                            get_package_share_directory('turtlebot3_bringup'),
                            'launch/robot.launch.py'    # Finding and executing standard TB3 launch
                        )
                    ),
                            
                    launch_arguments={
                        'tb3_param_dir':'./src/tb3_cpp/params/tb3_param.yaml'   # Coustom params just for ns
                        #'__ns':'/tb'    
                        }.items()
                ),
            ]
        )
    ])
