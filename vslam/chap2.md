# slam

## sensor
* **on the robot**: wheel encoder, camera, laser, inertial measurement unit;
* **off the robot**: lead rail; tags.

camera
* monocular,
* stereo
* RGB-D
* panorama
* event

monocular camera: a scene is a projection of the fact, obviously, it loses depth. when we move the camera, we could estimate the motion, then we can call them structure. The parallax error reflects the distance from the camera to the target. We can multiply the measurement distance with a constant to get the true distance. This constant calls Scale. However, we could not define the scale when we use the monocular camera. This means the uncertain of the scale.

stereo camera: we can measure the distance by the difference between the two cameras. the distance between the cameras calls baseline. The larger the baseline are, the deeper it could measure. The consumes a lot computing resource, always need GPU or FPGA.

depth camera: range is rare, noise is big, view is little, be sensitive to sun light, cannot measure  transmission medium.

## classical slam framework
It can be divided into such 5 parts:

1. sensor data: include encoder, imu or photos.
2. visual odometry. estimate the motion of the camera. also named front end.
3. backend optimization. receive the visual odometry data and the loop closing messages.
4. loop closing. judge if the robot have arrived the former position. If yes, submit to the backend optimization.
5. mapping. estimate the track, and establish the map.

## VO

VO could estimate the motion of camera by the adjacent image. It would lead to accumulating drift. So we need backend optimization and loop closing to decrease this estimation errors.

## backend optimization

because the camera has some errors, so the backend optimization need to estimate the state through these noisy data. We estimate the position as well as the noises, our confidence about these estimations. These three parts constitute the Maximum-a-Posteriori.

## loop closing

this part can deal with the drift. a QRcode is an example.

## mapping

2 types maps: metric map and topological map.

metric map: It includes sparse and dense maps. Sparse maps are abstract. They represent the relationship of items in a map. we don't need to express all items and only choose some landmarks. Oppositely, dense maps includes all things we percept. 2d maps are built in GRID, while 3D maps are built in VOXEL. This type of map is large memory resource consumed. Consensus problem could make maps unavailable.

topological map: a graph, consist of plot and edge.

## problem description

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x_k%3Df%28x_%7Bk-1%7D%2C%20u_k%2C%20w_k%29%5C%5C%20z_%7Bk%2Cj%7D%20%3D%20h%28y_j%2C%20x_k%2C%20v_%7Bk%2Cj%7D%29%20%5Cend%7Bmatrix%7D%5Cright." >

so we know the measurement u and z to solve the localization x and mapping y is the key problem.

Linear Gussian System: Kalman Filter.

Non-Linear Non-Gaussian System: EKF or PF or Graph Optimization.

----------------------------
