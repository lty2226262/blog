
## how to create a cpp file and build it with g++

    vim helloSLAM.cpp
    g++ helloSLAM.cpp
    ./a.out

## build it with cmake

    vim CMakeLists.txt
CMakeLists.txt:

    # 声明要求的cmake最低版本
    cmake_minimum_required( VERSION 2.8)

    # 声明一个cmake工程
    project( HelloSLAM)

    # 添加一个可执行程序
    # 语法： add_executable(程序名源代码和文件)
    add_executable( helloSLAM helloSLAM.cpp)
<br/>

    cmake .

this command generate a MakeFile, then type:

    make

this is more convenient to maintenance a CMakeLists than type a series of g++ command, but it leaves us some temporaries.

    mkdir build
    cd build
    cmake ..
    make
