# Design the frontend
## Determine the program frame
### How to arrange the documents:
1. bin to store the binary documents
2. include/myslam to store the headers, when include these headers, writing ***include"myslam/xxx.h"*** is necessary and will not bring confusions.
3. src to store the codes, mainly .cpp.
4. test to store the testing codes, mainly .cpp.
5. lib to store compiled files.
6. config to store configurations.
7. cmake_modules to store 3-rd party libraries' cmake.

### Some basic data structures

1. frame. How to select key-frames is always based on practice but no theoretical direction.
2. landmarks. The key-points in the image, We always store the landmarks into the map and match the coming frames with the landmarks in the map and then get the estimated pose.

the pose of frames and the landmarks location is as a local SLAM problem. Besides, we need some more tools to make program more efficient. Such as:

1. Configuration files. Design a configuration file and then load these parameters from the program.
2. Pose transformations. Define a class to bring these transformations together.

***A principle:***a class have a header and a source file itself and avoid putting many classes into a file. And put the definition into the header file and the implements into the sources files.

### camera class

Store the intrincs and outtrincs of camera, and complete the camera, world, pixel transformations.

### frame class

data save and interfaces, define the ID, time_stamp, pose, camera, image.

### mappoint class

we estimate the world position of it, and match the key-points extracted from the current frame and the landmark within the map to estimate the movement of the camera, and store its descriptors. Besides, we record the times of one observed point and its matched times by a standard of judge if it's good or bad.

### map class

it manage all the landmarks, and take charge of adding new landmarks and deleting bad landmarks.

### Config class

it takes charge of the load of a file, and provide the parameter if necessary. So we set Config as singleton. it only has a global object, when we set the parameter files, we create and load the parameter file, then visit it anywhere.

## Basic VO

### VO between 2 images

Pairwise Structureless VO.
