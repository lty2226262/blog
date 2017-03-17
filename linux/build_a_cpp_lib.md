libHelloSLAM.cpp:

    //这是一个库文件
    #include <iostream>
    using namespace std;
    void printHello()
    {
      cout<<"Hello SLAM"<<endl;
    }

CMakeList.txt

    add_library( hello libHelloSLAM.cpp)

Then generate a static link library named libhello.a

If we want to build a shared library: then we need to

    add_library( hello SHARED libHelloSLAM.cpp)

library is a binary file, so when should offer a header to declare what functions are in this library.

libHelloSLAM.h:

    #ifndef LIBHELLOSLAM_H_
    #define LIBHELLOSLAM_H_
    void printHello();
    #endif

then we create a file to use this library:

useHello.cpp

    #include "libHelloSLAM.h"
    int main( int argc, char** argv){
      printHello();
      return 0;
    }

Then add these commands into CMakeLists.txt

    add_executable( useHello useHello.cpp)
    target_link_libraries( useHello hello)

## ide: kdevelop

1. write a CMakeLists.txt
2. set in the CMakeLists.txt

        set( CMAKE_BUILD_TYPE "Debug")

3. Run->Launch configurations->add mew->ok
4. F8 compile, F9 debug
