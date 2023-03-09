cmake_minimum_required(VERSION 3.5)
project(tb3_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# install cpp
add_executable(my_node src/my_node.cpp)

target_include_directories(my_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
  
install(TARGETS my_node
  DESTINATION lib/${PROJECT_NAME}
)

# install launch and params
install(DIRECTORY
  launch
  params
  DESTINATION share/${PROJECT_NAME}/
)

# install python 
ament_python_install_package(src)

install(PROGRAMS 
  src/publisher.py
  src/node.py
  src/nav.py
  DESTINATION lib/${PROJECT_NAME}
)


ament_package()
