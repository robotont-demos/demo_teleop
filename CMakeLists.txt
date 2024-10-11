cmake_minimum_required(VERSION 3.5)
project(demo_teleop)

find_package(ament_cmake REQUIRED)
find_package(teleop_twist_joy REQUIRED)
find_package(teleop_twist_keyboard REQUIRED)

ament_package()

include_directories(
  ${teleop_twist_joy_INCLUDE_DIRS}
  ${teleop_twist_keyboard_INCLUDE_DIRS}
)

# If you have any executables or libraries, you would add them here
# add_executable(${PROJECT_NAME}_node src/${PROJECT_NAME}_node.cpp)
# ament_target_dependencies(${PROJECT_NAME}_node
#   teleop_twist_joy
#   teleop_twist_keyboard
# )

install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(teleop_twist_joy teleop_twist_keyboard)
ament_export_include_directories(include)

ament_package()
