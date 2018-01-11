cmake_minimum_required( VERSION 2.8 )
project( yam_write_and_read )

set( CMAKE_BUILD_TYPE "Release" )
set( CMAKE_CXX_FLAGS "-std=c++11 -O3" )

# OpenCV
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS})
message(STATUS"what "${OpenCV_INCLUDE_DIRS})

add_executable( naive_write naive_write.cpp )
target_link_libraries( naive_write 
    ${OpenCV_LIBRARIES}
)
add_executable( naive_read naive_read.cpp )
target_link_libraries( naive_read 
    ${OpenCV_LIBRARIES}
)
