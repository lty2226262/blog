# Camera and images

## Pinhole model

we could get the physical imagine plane o-u-v, and the pixel coordination of P' : <img src="http://latex.codecogs.com/gif.latex?%5Bu%2Cv%5D%5ET">. The normal definition of pixel coordination is: origin is at the left-top point, u-axis is parallel to x-axis towards right, v-axis is parallel to y-axis downwards. The difference between pixel coordination and imagine coordination is a zoom and a transformation of origin. We suppose that the pixel scale alpha times on the u-axis, and v scales beta times on the v-axis. At the same time, the origin translate a distance of <img src="http://latex.codecogs.com/gif.latex?%5Bc_x%2Cc_y%5D%5ET">. Therefore, the relationship of P' and the pixel coordination is <img src="http://latex.codecogs.com/gif.latex?%5Bu%2Cv%5D%5ET">:

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20u%3D%5Calpha%20X%27%20&plus;%20c_x%5C%5C%20v%20%3D%20%5Cbeta%20Y%27%20&plus;%20c_y%20%5Cend%7Bmatrix%7D%5Cright.">

according to:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20X%27%3Df%5Cfrac%7BX%7D%7BZ%7D%5C%5C%20Y%27%3Df%5Cfrac%7BY%7D%7BZ%7D%20%5Cend%7Bmatrix%7D">

we could get:

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20u%3Df_x%5Cfrac%7BX%7D%7BZ%7D&plus;c_x%5C%5C%20v%3Df_y%5Cfrac%7BY%7D%7BZ%7D&plus;c_y%20%5Cend%7Bmatrix%7D%5Cright.">

the unit of f is meter, alpha and beta is pixel/meter, so the unit of <img src="http://latex.codecogs.com/gif.latex?f_x%2Cf_y"> is pixel. Express it with the matrix form:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20u%5C%5C%20v%5C%5C%201%20%5Cend%7Bpmatrix%7D%3D%5Cfrac%7B1%7D%7BZ%7D%5Cbegin%7Bpmatrix%7D%20f_x%20%260%20%26c_x%20%5C%5C%200%20%26%20f_y%20%26c_y%20%5C%5C%200%20%260%20%261%20%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7D%20X%5C%5C%20Y%5C%5C%20Z%20%5Cend%7Bpmatrix%7D%5Cequiv%20%5Cfrac%7B1%7D%7BZ%7DKP">

according to our traditional habit, translate Z to the left:

<img src="http://latex.codecogs.com/gif.latex?Z%5Cbegin%7Bpmatrix%7D%20u%5C%5C%20v%5C%5C%201%20%5Cend%7Bpmatrix%7D%3D%5Cbegin%7Bpmatrix%7D%20f_x%20%260%20%26c_x%20%5C%5C%200%20%26f_y%20%26c_y%20%5C%5C%200%20%260%20%261%20%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7D%20X%5C%5C%20Y%5C%5C%20Z%20%5Cend%7Bpmatrix%7D%5Cequiv%20KP">

In this matrix, we called the K camera intrinsics. we need calibration to get the K matrix, and we usually consider that the camera parameters are fixed.  

P is the global coordination. Because the camera is moving, so P should be transformed to the coordination P_w. The pose is described by its rotation matrix and its translation vector t. Then we could get:

<img src="http://latex.codecogs.com/gif.latex?ZP_uv%3DZ%5Cbegin%7Bbmatrix%7D%20u%5C%5C%20v%5C%5C%201%20%5Cend%7Bbmatrix%7D%3DK%28RP_w&plus;t%29%3DKTP_w">

The R,t called the camera extrinsics. Contrast by the fixed intrinsics, the extrinsics is always changing following the camera movement, and it's also the estimation of SLAM.

The both sides of the above formula are homogenous coordination. Because that the homogenous multiply a non-zero constant is also a homogenous coordination, we could delete the Z simply.

<img src="http://latex.codecogs.com/gif.latex?P_%7Buv%7D%3DKTP_w">

After the homogenous transformation, we should also do a normalize:

<img src="http://latex.codecogs.com/gif.latex?%5Ctilde%7BP%7D_c%3D%5Cbegin%7Bbmatrix%7D%20X%5C%5C%20Y%5C%5C%20Z%20%5Cend%7Bbmatrix%7D%3D%28TP_w%29_%7B%281%3A3%29%7D%2CP_c%20%3D%20%5Cbegin%7Bbmatrix%7D%20X/Z%5C%5C%20Y/Z%5C%5C%201%20%5Cend%7Bbmatrix%7D">

We call <img src="http://latex.codecogs.com/gif.latex?P_c"> normalized coordination, it is on the z=1 plane. And we call the plane normalized plane. Because we could get the pixel coordination from <img src="http://latex.codecogs.com/gif.latex?P_c"> and intrinsics, so we could treat pixel coordination as the result of measurement on the normalized plane.
