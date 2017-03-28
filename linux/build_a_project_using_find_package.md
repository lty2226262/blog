project(eigengeometry)

include_directories(/usr/include/eigen3)

find_package(Sophus REQUIRED )
include_directories( ${Sophus_INCLUDE_DIRS})

add_executable(useSophus main.cpp)
target_link_libraries(useSophus ${Sophus_LIBRARIES})
