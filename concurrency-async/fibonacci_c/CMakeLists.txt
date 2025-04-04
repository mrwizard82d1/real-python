cmake_minimum_required(VERSION 3.30)
project(fibonacci_c C)

set(CMAKE_C_STANDARD 11)

find_package(PythonInterp REQUIRED)
find_package(PythonLibs ${PYTHON_VERSION} REQUIRED)

include_directories(${PYTHON_INCLUDE_DIRS})

add_library(my_extension SHARED my_extension.c)

target_link_libraries(my_extension ${PYTHON_LIBRARIES})

set_target_properties(my_extension PROPERTIES PREFIX "" SUFFIX ".so") # For Linux/macOS
# set_target_properties(my_extension PROPERTIES PREFIX "" SUFFIX ".pyd") # For Windows
