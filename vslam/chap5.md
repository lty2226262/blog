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

## Distortion model

Lens lead to distortion. Two types: barrel distortion and pincushion distortion. Express as follows:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20x_%7Bcorrected%7D%20%3D%20x%281&plus;k_1e%5E2&plus;k_2r%5E4&plus;k_3r%5E6%29%5C%5C%20y_%7Bcorrected%7D%20%3D%20y%281&plus;k_1r%5E2&plus;k_2r%5E4&plus;k_3r%5E6%29%20%5Cend%7Bmatrix%7D">

The <img src="http://latex.codecogs.com/gif.latex?%5Bx%2Cy%5D%5ET"> is an uncorrected point, and the <img src="http://latex.codecogs.com/gif.latex?%5Bx_%7Bcorrected%7D%2Cy_%7Bcorrected%7D%5D%5ET"> is a corrected point, they are all on the normalized plane, but no points on the plane.

For some small distortion images, <img src="http://latex.codecogs.com/gif.latex?k_1"> is enough to correct the distortion. For some edges, we need the <img src="http://latex.codecogs.com/gif.latex?k_2">, for some fisheye cameras, we need some <img src="http://latex.codecogs.com/gif.latex?k_3">.

As for tangential distortion, we should use another two parameters, <img src="http://latex.codecogs.com/gif.latex?p_1%2Cp_2"> to correct the distortion.

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20x_%7Bcorrected%7D%3Dx&plus;2p_1xy&plus;p_2%28r%5E2&plus;2x%5E2%29%5C%5C%20y_%7Bcorrected%7D%3Dy&plus;p_1%28r%5E2&plus;2y%5E2%29&plus;2p_2xy%20%5Cend%7Bmatrix%7D">

Through these five distortion parameters, we could get the corrected position of this point:

1. Map the 3D spatial point to the normalized image plane. Suppose its normalized coordination is <img src="http://latex.codecogs.com/gif.latex?%5Bx%2Cy%5D%5ET">.
2. Correct the distortion points on the normalized plane:</br><img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x_corrected%20%3D%20x%281&plus;k_1%20r%5E2&plus;k_2%20r%5E4&plus;k_3%20r%5E6%29&plus;2p_1xy&plus;p_2%28r%5E2&plus;2x%5E2%29%5C%5C%20y_corrected%20%3D%20y%281&plus;k_1%20r%5E2%20&plus;%20k_2%20r%5E4%20&plus;%20k_3%20r%5E6%29&plus;p_1%28r%5E2&plus;2y%5E2%29&plus;2p_2xy%20%5Cend%7Bmatrix%7D%5Cright.">
3. We could get the corrected position after map to the pixel panel:</br>
<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20u%3Df_xx_%7Bcorrected%7D&plus;c_x%5C%5C%20v%3Df_yy_%7Bcorrected%7D&plus;c_y%20%5Cend%7Bmatrix%7D%5Cright.">

There are two methods to correct the distortion: first is to correct the image firstly, then use the corrected image; second is to use the distortion equation to compute the corresponding point.

To conclude, we get the processing as follows:

1. first, suppose a fixed point P, its global position is <img src="http://latex.codecogs.com/gif.latex?P_w">

2. Suppose the camera is moving, its motion change from R, t to <img src="http://latex.codecogs.com/gif.latex?T%20%5Cin%20SE%283%29">. The coordination is <img src="http://latex.codecogs.com/gif.latex?%5Ctilde%7BP%7D_c%3DRP_w&plus;t">.

3. This <img src="http://latex.codecogs.com/gif.latex?%5Ctilde%7BP%7D_c"> has X,Y,Z three parameters, and when they projection to the normalized plane Z=1, we could get the normalized coordination: <img src="http://latex.codecogs.com/gif.latex?P_c%20%3D%20%5BX/Z%2C%20Y/Z.%201%5D%5ET">

4. Through the intrinsics, processing P, we could get the normalized coordination: <img src="http://latex.codecogs.com/gif.latex?P_%7Buv%7D%3DKP_c">

### stereo cameras

Suppose b is the baseline, f is focal length,

<img src="https://github.com/lty2226262/blog/blob/master/MarkdownPhotos/vslam_chap5_1.png?raw=true">

so:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7Bz-f%7D%7Bz%7D%3D%5Cfrac%7Bb-u_L&plus;u_R%7D%7Bb%7D">

after arraignment we could get:

<img src="http://latex.codecogs.com/gif.latex?z%3D%5Cfrac%7Bfb%7D%7Bd%7D%2Cd%3Du_L-u_R">

the farthest distance that the camera could measure is defined by the product of fb. But the corresponding point pairs are difficult to compute, so we also need GPU or FPGA to compute this.

### RGB-D camera

1. structure light: kinect 1, project tango 1, intel realsense

2. time-of-flight kinect 2
