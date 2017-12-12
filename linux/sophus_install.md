```
git clone https://github.com/strasdat/Sophus.git
cd Sophus
git checkout a621ff
```



```
mkdir build && cd build
cmake ..
make
sudo make install
```



```
find_package(Sophus REQUIRED)
include_directories(${Sophus_INCLUDE_DIRS})

add_executable(xxx xxx.cpp)
target_link_libraries(xxx ${Sophus_LIBRARIES})
```



