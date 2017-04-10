sudo apt-get install build-essential
sudo apt-get install libgl1-mesa-dev
sudo apt-get install libglu1-mesa-dev
sudo apt-get install freeglut3-dev


PCL installation:

We will first install PCL 1.7.2. This can be done very easy, as Ubuntu is supported by PCL. You have to open a terminal and execute the following three commands as described here:
sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
sudo apt-get update
sudo apt-get install libpcl-all  

All dependencies of PCL are now installed, so we dont have to worry about them when installing PCL 1.8.0, which has not been released yet, so we have to compile by ourself. We install git, cmake and ccmake with one command:
sudo apt-get install git cmake cmake-curses-gui  

We use git to fetch the PCL source code from Github:
git clone https://github.com/PointCloudLibrary/pcl  

In our homefolder we have now a folder pcl. With the following commands we change the directory to the pcl folder, make a build folder in this directory and then change to the new created build folder:
cd pcl
mkdir build
cd build  

We use from there ccmake:
ccmake ..  

A commandline based editor opens and we should be able to press 'c' to configure and then 'g' to generate meta data and exit ccmake. You need to press two times 'c' to configure with no further changes made to enable the 'g' option. 
The next two commands to build pcl 1.8.0
cmake ..
make  

Now your C++ compiler has a lot of work for up to several hours.
If successful, you can now install the library finally:
sudo make install  
