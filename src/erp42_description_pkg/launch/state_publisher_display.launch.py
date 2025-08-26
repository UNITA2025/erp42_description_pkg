# URDF 기반 TF + RViz2 시각화 (for test!, 실제 실행 할 때에는 state_publisher.launch.py만 실행)
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

    # URDF를 xacro로 파싱
    robot_description = ParameterValue(
        Command(['xacro ', urdf_file]),
        value_type=str
    )

    # RViz 설정 파일 경로 (없으면 그냥 rviz2 실행됨)
    rviz_config = PathJoinSubstitution([
        FindPackageShare('erp42_description_pkg'),
        'rviz',
        'model_view.rviz'
    ])

    return LaunchDescription([
        # Robot State Publisher (URDF → TF)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # RViz2 실행
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])
