cmake_minimum_required(VERSION 3.30)
project(fibonacci_ffi C)

set(CMAKE_C_STANDARD 11)

add_library(fibonacci_ffi STATIC library.c)
