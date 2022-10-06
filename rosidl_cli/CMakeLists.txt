cmake_minimum_required(VERSION 3.0.2)
project(rosidl_cli)

set(DEPS
  rospy
)


find_package(catkin REQUIRED COMPONENTS ${DEPS})

catkin_package(
#  INCLUDE_DIRS ${CMAKE_CURRENT_BINARY_DIR}/..
  LIBRARIES 
  CATKIN_DEPENDS ${DEPS}
)

catkin_python_setup()

#file(GLOB python_scripts_DIR "scripts/*.py")
    
## Python stuff
#catkin_install_python(PROGRAMS ${python_scripts_DIR}
#    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

