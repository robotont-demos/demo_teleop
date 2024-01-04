cmake_minimum_required(VERSION 3.0.2)
project(demo_teleop)

find_package(catkin REQUIRED COMPONENTS
  teleop_twist_joy
  teleop_twist_keyboard
)
catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
