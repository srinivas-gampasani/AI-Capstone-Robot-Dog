import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Determine the path to your URDF file
    pkg_share = get_package_share_directory('puppy_urdf')
    urdf_file = os.path.join(pkg_share, 'urdf', 'quad_robo.urdf')

    return LaunchDescription([
        # Launch Gazebo with the ROS factory (which enables entity spawning)
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        # Spawn your URDF into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'quad_robo', '-file', urdf_file, '-x', '0', '-y', '0', '-z', '0.2'],
            output='screen'
        )
    ])
