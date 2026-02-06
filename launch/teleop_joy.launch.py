from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    gamepad_conf_decl = DeclareLaunchArgument('gamepad_conf', default_value='ipega.yaml')
    namespace_decl = DeclareLaunchArgument('namespace', default_value='')
    namespace = LaunchConfiguration('namespace')


    config = PathJoinSubstitution([
        get_package_share_directory('demo_teleop'),
        'config',
        'joy',
        LaunchConfiguration('gamepad_conf')
    ])

    return LaunchDescription([
        gamepad_conf_decl,
        namespace_decl,
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            namespace=namespace,
            output='screen'
        ),
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy',
            namespace=namespace,
            parameters=[config],
            output='screen'
        )
    ])
