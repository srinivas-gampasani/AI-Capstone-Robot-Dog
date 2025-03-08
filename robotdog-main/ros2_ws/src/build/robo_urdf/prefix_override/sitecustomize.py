import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/workspaces/bhanu mallik/PuppyPi/ros2_ws/src/install/robo_urdf'
