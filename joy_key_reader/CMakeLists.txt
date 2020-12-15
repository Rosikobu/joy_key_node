cmake_minimum_required(VERSION 3.0.2)
project(joy_key_reader)

find_package(catkin REQUIRED COMPONENTS
  joy
  rospy
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES joy_key_reader
#  CATKIN_DEPENDS joy rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/jkeyreader.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)