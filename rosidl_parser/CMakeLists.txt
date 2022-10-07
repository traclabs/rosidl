cmake_minimum_required(VERSION 3.5)

project(rosidl_parser)


set(DEPS
  rospy
#  rosidl_adapter
)

find_package(catkin REQUIRED COMPONENTS ${DEPS})

catkin_package(
#  INCLUDE_DIRS ${CMAKE_CURRENT_BINARY_DIR}/..
  LIBRARIES 
  CATKIN_DEPENDS ${DEPS}
)

catkin_python_setup()

# Python stuff
catkin_install_python(PROGRAMS bin/idl2png
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
    



