# URDF 기반 TF만 퍼블리시
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # URDF 파일 경로
    urdf_file = PathJoinSubstitution([
        FindPackageShare('erp42_description_pkg'),
        'urdf',
        'erp42_robot.urdf.xacro'
    ])

    # xacro로 파싱해서 robot_description 파라미터에 전달
    robot_description = ParameterValue(
        Command(['xacro ', urdf_file]),
        value_type=str
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        )
    ])
