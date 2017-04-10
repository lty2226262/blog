 一，下载PCL
 git clone https://github.com/PointCloudLibrary/pcl.git pcl-trunk  
 ln -s pcl-trunk pcl   
 
二，安装库
 sudo apt-get install cmake g++ libeigen3-dev libflann-dev python libusb-1.0-0-dev libudev-dev freeglut3-dev doxygen graphviz libpng12-dev libgtest-dev libxmu-dev libxi-dev libpcap-dev libqhull-dev libvtk5-qt4-dev python-vtk libvtk-java  libboost1.58-all-dev

三，编译库
 cd pcl-trunk  
 mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=None -DBUILD_GPU=ON -DBUILD_apps=ON -DBUILD_examples=ON ..   
 make  
 sudo make install  
 
四，测试PCL
1、HOME目录下  pcl-trunk->doc->tutorials->content->sources下有PCL例程：这里我选择的是cloud_viewer文件夹下的cloud_viewer.cpp
2、创建demo包
 cd catkin_ws/src/  
 catkin_create_pkg demo std_msgs rospy roscpp  
3、将cloud_viewer.cpp文件拷贝到demo文件下，同时用cloud_viewer文件夹下的CmakeList.txt代替demo文件夹下的CmakeList.txt文件
4、编译运行cloud_view.cpp源文件
 cd demo  
 sudo cmake .  
 sudo make  
 ./cloud_viewer  
