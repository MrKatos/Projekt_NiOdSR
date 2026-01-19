from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Symulator żółwia (z biblioteki turtlesim)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # 2. Twój interfejs graficzny
        Node(
            package='camera_control',
            executable='interface_node',
            name='gui'
        ),
        # 3. Twoja logika sterowania
        Node(
            package='camera_control',
            executable='turtle_controller',
            name='logic'
        )
    ])