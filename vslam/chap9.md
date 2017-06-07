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

Pairwise Structureless VO. Assume that the Reference frame to the world coordinate is <img src="http://chart.googleapis.com/chart?cht=tx&chl=T_{rw}">, the Current Frame to the world coordinate is <img src="http://chart.googleapis.com/chart?cht=tx&chl=T_{cw}">, The estimated frame form the left multiply relationship:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=T_{cr}, s.t. T_{cw}=T_{cr}T_{rw}">

We only care about the motion, but do not the structure.

Its flow shows below:

1. Extract the key-points and descriptors for the current frame.
2. This frame is the reference frame without initialization, return the 3D pose of the key-points, and return 1.
3. Estimate the motion between reference frame and current frame.
4. Judge if the above is successful.
5. If success, add the current frame as a new reference frame, return 1.
6. If fail, mark the continuous lost frame, and set the VO state as LOST, algorithm ends. If not exceed, return 1.

#### VO class

This class implement the above algorithm.

Some explanations:

1. VO have different states, it is a finite state machine. We consider the easiest three states: initialization, normal, lost.
2. We add some middle variables into the class to avoid value passing.
3. Feature extraction and parameter matching, load the parameters from the parameter files.
4. addFrame is for external call.

#### Discussion

This simple approach doesn't make sense. Reasons maybe:

1. We using RANSAC to solve the PnP solution. Due to RANSAC only uses a few points, so influenced strongly by noises. So we need to estimate the RANSAC solution as the initialized value. Then solve an optimized solution.

2. Because the VO is structureless, so the pose of 3D points are treated as the true value. But in actually, RGB-D depth image has some errors. So we need to optimize the key-points together with the VO.

3. If we only refer the reference frame and the current frame, the pose estimation depends the reference frame too strongly. When the estimation of the reference frame is not accurate, it could cause an obvious drift. One the other hand, we do not make full  use of information. The more useful method is to compare the current frame and the map, but not compare the current frame and the reference frame. Therefore, we need to care about how to match the current frame and the map, and how to optimize the map points.
