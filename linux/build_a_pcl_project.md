project(joinMap)
cmake_minimum_required(VERSION 2.8)

set (CMAKE_CXX_FLAG "-std=c++11" )

#寻找Opencv库
find_package( OpenCV REQUIRED)
#添加头文件
include_directories(${OpenCV_INCLUDE_DIRS})

#Eigen
include_directories("/usr/include/eigen3/")

#pcl
find_package(PCL REQUIRED COMPONENT common io)
include_directories(${PCL_INCLUDE_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable( joinMap joinMap.cpp)

#链接Opencv库,PCL库
target_link_libraries( joinMap ${OpenCV_LIBS} ${PCL_LIBRARIES})



#显示点云图片
pcl_viewer map.pcd
