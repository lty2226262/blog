project(imageBasics)
cmake_minimum_required(VERSION 2.8)

#添加c++ 11标准文件
set (CMAKE_CXX_FLAG "-std=c++11" )



#寻找Opencv库
find_package( OpenCV REQUIRED)
#添加头文件
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable( imageBasics imageBasics.cpp)

#链接Opencv库
target_link_libraries( imageBasics ${OpenCV_LIBS})

#在kdevelop添加c++11支持
打开kdevelop -> project -> open configuration -> show advance -> show advance variables -> CMAKE_CXX_FLAGS -std=c++0x
