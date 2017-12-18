cmake_minimum_required(VERSION 2.6)
project(ceres_study)

find_package(Ceres REQUIRED)
include_directories(${CERES_INCLUDE_DIRS})

add_executable(ceres_study main.cpp)
target_link_libraries(ceres_study ${CERES_LIBRARIES})

