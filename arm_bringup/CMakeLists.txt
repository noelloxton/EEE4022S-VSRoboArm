cmake_minimum_required(VERSION 3.0.2)
project(arm_bringup)

## Compile as C++11, supported in ROS Kinetic and newer
 add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  actionlib
  control_msgs
  robot_state_publisher
  roscpp
  rospy
  std_msgs
  tf
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES arm_bringup
#  CATKIN_DEPENDS actionlib control_msgs robot_state_publisher roscpp rospy std_msgs tf
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME}_Pub_to_Arduino_Class src/pub_to_arduino_class.cpp)

## Rename C++ executable without prefix
## The above recommended prefix causes long target names, the following renames the
## target back to the shorter version for ease of user use
## e.g. "rosrun someones_pkg node" instead of "rosrun someones_pkg someones_pkg_node"

set_target_properties(${PROJECT_NAME}_Pub_to_Arduino_Class PROPERTIES OUTPUT_NAME Pub_to_Arduino_Class PREFIX "")

## Add cmake target dependencies of the executable


add_dependencies(${PROJECT_NAME}_Pub_to_Arduino_Class ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against

target_link_libraries(${PROJECT_NAME}_Pub_to_Arduino_Class
   ${catkin_LIBRARIES}
 )
