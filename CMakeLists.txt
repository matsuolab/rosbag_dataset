cmake_minimum_required(VERSION 3.0.2)
project(rosbag_dataset)

## Find catkin and any catkin packages
find_package(
  catkin REQUIRED COMPONENTS 
  roscpp 
  rospy 
  std_msgs
  message_generation 
)

## Declare a catkin package
catkin_package()
catkin_python_setup()

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

# Install

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS scripts/rosbag_handler.py 
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
