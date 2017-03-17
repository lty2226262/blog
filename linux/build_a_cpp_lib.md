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
