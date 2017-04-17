<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# VO
## Feature points method
Feature points method is popular because it is quite steady and insensible to light and dynamic.

Features include corners, edges and blocks. The easiest feature to detect is corner, then edge, then block.

Corners also have problems. Maybe some feature are corners but when we are close to it, it's no more a corner. Or when we rotate the camera, we could not recognize the corner. For this, computer researchers build several corners such as SIFT, SURF and ORB. These good corners have these features:

1. Repeatability: we could get the same region from different images.
2. Distinctiveness: different regions have different expressions.
3. Efficiency: the feature corners are much less than the non-feature corners.
4. Locality: the features are only correspond with a small region.

The feature points consists of Key-points and Descriptors. Key-points are the key-points in the pictures, some of them have oriention and size. Descriptors are usually a vector that descript the surrounding information of these key-points. Hence, if two descriptors are close in spatial, we could treat them as the same descriptos.

SIFT is very accurate, but very compute cosuming. We usually use the less consuming orb.

## ORB feature

ORB feature consists of key-points and descriptors. Its key-points called "Oriented FAST". Therefore, Extracting the ORB feature needs two steps:

1. FAST corner extraction. Compute the FAST as well as the key-point oriention in order to increse rotation fixed property for computing the BRIEF.

2. BRIEF descriptors: to describe the surrounding environments.

### FAST key-point

FAST is a key-point which detects the place where the pixel gray scale changes significantly. It is famous for its computing speed. Its contain is that if a pixel's brightness is different from its neiber pixels, it might be a corner. Its detecting steps is as followings:

1. Pick a pixel p, its brightness is <img src="http://latex.codecogs.com/gif.latex?I_p">.
2. Set a threshold T(20% of <img src="http://latex.codecogs.com/gif.latex?I_p"> for example).
3. Treat p as the center of the cirble, pick the 16 surrounding pixels by the radius of 3.
4. Suppose the circle has continuous points whose brightness greater than <img src="http://latex.codecogs.com/gif.latex?I_p+T"> or less than <img src="http://latex.codecogs.com/gif.latex?I_p-T">, then we could treat the pixel p as a key-point(N is usually 12)
5. Cycle the above steps for every pixel.

To be faster: detect the 1,5,9,13 brightness. Besides, we use the Non-maximal suppression to keep the maximal responding corner to avoid the corner focus problem.

Problems in FAST:
1. Number is large and uncertain, but we usually want fixed features. Therefore, in ORB, we fix the original FAST algorithm. Compute the Harris responding value, and pick the former largest N corner, as the result corner set.
2. It has scale problem: some corner might be seen as a corner when you're far away from the target but no more a corner when you access to it. ORB attach the scale and rotation description. Scale invariance is constructed by the image pyramid. And the feature rotation is computed by the intensity centroid.

Centroid refers to the image block gray value as the center of the weight. The steps are shown as follows:
1. In a small image block <img src="http://latex.codecogs.com/gif.latex?B">, the moment of the image block is:
  <img src="http://latex.codecogs.com/gif.latex?m_{pq}=\sum_{x,y\in%20B}x^py^qI(x,y),%20p,q=\{0,1\}.">
2. Through the moment we could get the centroid of the image block:
  <img src="http://latex.codecogs.com/gif.latex?C=(\frac{m_{10}}{m_{00}},\frac{m_{01}}{m_{00}})">
3. Connect the central <img src="http://latex.codecogs.com/gif.latex?O"> and the centroid <img src="http://latex.codecogs.com/gif.latex?C">, we could get a <img src="http://latex.codecogs.com/gif.latex?\overrightarrow{OC}">, we could define the direction of key-points:
  <img src="http://latex.codecogs.com/gif.latex?\theta=arctan(m_{01}/m_{10})">

###BRIEF descriptor
After extracting the Oriented FAST, we could compute the discriptor of every point. ORB uses improved BRIEF feature.

BRIEF is a binary descriptor, its description vector consists of many 0 and 1, the 0 and 1 represents the size relationship: if <img src="http://latex.codecogs.com/gif.latex?p"> is larger than <img src="http://latex.codecogs.com/gif.latex?q">, it sets 1, otherwise it sets 0. If we pick 128 such <img src="http://latex.codecogs.com/gif.latex?p,q"> pairs, we could get a 128-dimension vector consist of <img src="http://latex.codecogs.com/gif.latex?p,q">. They pick such pairs randomly following some probability rule.

###Feature matching
Feature matching is a significant step in the SLAM, it deals with the data association problem, when we see the landmark and determine the relationship of the landmarks we have seen before. By accurate matching, we could reduce the burden on the pose estimation and the optimization. But the mismatch always limit the SLAM.

How to match these points? The easiest method is the Brute-Force Marcher. For every key-point <img src="http://latex.codecogs.com/gif.latex?x_t^m">, compare its distance to every other key-points'. The distance is Hamming distance.

But as the amount of the key-points get larger, the brute-force matcher turns to be very slow. We use FLANN to compute the situation where there are a large of amount of key-points.

Then we hope to estimate the camera's motion according to the paired points. This varies according to the cameras' types:

1. When the camera is monocular, we only know the 2D pixel coordinates. We estimate the cameras' motion according to two pairs of 2D points by using Epipolar Geometry.
2. When the camera is stereo, we know the distances. We estimate the cameras' motion according to two pairs of 3D points by using ICP.
3. If we have the 3D points and their projection position in the camera, we solve it by using PnP.

## 2D-2D: Epipole Geometry
### Epipole confinement
<img src="https://github.com/lty2226262/blog/blob/master/MarkdownPhotos/vslam_7_1.png?raw=true">

We hope to solve the motion between two frames <img src="http://latex.codecogs.com/gif.latex?I_1,I_2">, suppose the motion from the first frame to the second frame is <img src="http://latex.codecogs.com/gif.latex?R,t">, and the center of the camera is <img src="http://latex.codecogs.com/gif.latex?O_1,O_2">, <img src="http://latex.codecogs.com/gif.latex?p_1"> is a key-point in <img src="http://latex.codecogs.com/gif.latex?I_1">, while <img src="http://latex.codecogs.com/gif.latex?p_2"> is a key-point in <img src="http://latex.codecogs.com/gif.latex?I_2">. First of all, <img src="http://latex.codecogs.com/gif.latex?%5Coverrightarrow%7BO_1p_1%7D"> and <img src="http://latex.codecogs.com/gif.latex?%5Coverrightarrow%7BO_2p_2%7D"> intersect at the point <img src="http://latex.codecogs.com/gif.latex?P">. The point <img src="http://latex.codecogs.com/gif.latex?O_1">, <img src="http://latex.codecogs.com/gif.latex?O_2"> and <img src="http://latex.codecogs.com/gif.latex?P"> determine a plane Epipolar plane. The line <img src="http://latex.codecogs.com/gif.latex?O_1O_2"> intersects the plane <img src="http://latex.codecogs.com/gif.latex?I_1,I_2"> with <img src="http://latex.codecogs.com/gif.latex?e_1,e_2">. These points are called Epipoles, <img src="http://latex.codecogs.com/gif.latex?O_1O_2"> are called baseline. <img src="http://latex.codecogs.com/gif.latex?l_1"> and <img src="http://latex.codecogs.com/gif.latex?l_2"> are called Epipolar line.

Suppose the spatial coordinate of P in the first frame is:

 <img src="http://latex.codecogs.com/gif.latex?P=[X,Y,Z]^T">

 We know the pixel coordinate of <img src="http://latex.codecogs.com/gif.latex?p_1,p_2"> is:

 <img src="http://latex.codecogs.com/gif.latex?s_1p_1=KP,s_2p_2=K(RP+t)">

K here is the intrinsics of the camera, R, t shows the motion of this camera. But if we use the homogenous coordinate, we can write these formulas in the terms of multiplying a non-zero constant up to a scale:

  <img src="http://latex.codecogs.com/gif.latex?p_1=KP,p_2=K(RP+t)">

Now, suppose:

<img src="http://latex.codecogs.com/gif.latex?x_1=K^{-1}p_1,%20x_2=K^{-1}p_2">

<img src="http://latex.codecogs.com/gif.latex?x_1"> and <img src="http://latex.codecogs.com/gif.latex?x_2"> here are the normalized coordinate. Bring it into this formula, we could get:

<img src="http://latex.codecogs.com/gif.latex?x_2=Rx_1+t">

left multiply <img src="http://latex.codecogs.com/gif.latex?t^\wedge">:

<img src="http://latex.codecogs.com/gif.latex?t^\wedge%20x_2=t\wedge%20Rx_1">

Then left multiply <img src="http://latex.codecogs.com/gif.latex?x_2^T">:

<img src="http://latex.codecogs.com/gif.latex?x_2^Tt^\wedge%20x_2=x_2^Tt^\wedge%20Rx_1">

we could see from the left part of the equation that <img src="http://latex.codecogs.com/gif.latex?t^\wedge%20x_2"> is vertical to <img src="http://latex.codecogs.com/gif.latex?x_2">. So the product is 0. Then we could get:

<img src="http://latex.codecogs.com/gif.latex?x_2^Tt^\wedge%20Rx_1=0">

Bring into <img src="http://latex.codecogs.com/gif.latex?p_1,p_2">, we could get:

<img src="http://latex.codecogs.com/gif.latex?p_2^TK^{-T}t^\wedge%20RK^{-1}p_1=0">

These two equations are called epipole confinement. Its geometric meaning is that <img src="http://latex.codecogs.com/gif.latex?O_1,P,O_2"> are in the same plane. We mark the middle matrix into two: fundamental matrix F and essential matrix E, and simplify the epipole refinement:

<img src="http://latex.codecogs.com/gif.latex?E=t^\wedge%20R,F=K^{-T}EK^{-1},x^T_2Ex_1=p_2^TFp_1=0">

The camera pose estimate problem turns into the following two steps:

1. solve E or F through the paired points pixel position.

2. solve R,t according to E or F.

### Essential matrix

According to the definition, the essential matrix <img src="http://latex.codecogs.com/gif.latex?E=t^\wedge%20R"> is a 3x3 matrix, its property shows as followings:

1. when it multiply with a non-zero constant, it also obeys the epipole refinement. This is called scale equivalence.
2. the singular value must be in the form of <img src="http://latex.codecogs.com/gif.latex?[\sigma,\sigma,0]^T">.
3. according to scale equivalence.  <img src="http://latex.codecogs.com/gif.latex?E=t^\wedge%20R"> have 6-1 =5 freedom degree.

We could use eight-point-algorithm to estimate E.

Suppose a paired matching points: <img src="http://latex.codecogs.com/gif.latex?x_1=[u_1,v_1,1]^T,x_2=[u_2,v_2,1]^T">. According to epipole refinement:

<img src="http://latex.codecogs.com/gif.latex?%28u_1%2Cv_1%2C1%29%5Cbigl%28%5Cbegin%7Bpmatrix%7D%20e_1%20%26%20e_2%20%26e_3%20%5C%5C%20e_4%20%26%20e_5%20%26%20e_6%20%5C%5C%20e_7%20%26%20e_8%20%26%20e_9%20%5Cend%7Bpmatrix%7D%5Cbigr%29%5Cbegin%7Bpmatrix%7D%20u_2%5C%5C%20v_2%5C%5C%201%20%5Cend%7Bpmatrix%7D%3D0">

expand the matrix E into vector:

<img src="http://latex.codecogs.com/gif.latex?[e_1,e_2,e_3,e_4,e_5,e_6,e_7,e_8,e_9]^T">

Write into the form of e:

<img src="http://latex.codecogs.com/gif.latex?[u_1u_2,u_1v_2,u_1,v_1u_2,v_1v_2,u_2,v_2,1]\cdot%20e=0">

Put all these points into a equation:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20u_1%5E1u_2%5E1%20%26%20u_1%5E1v_2%5E1%20%26%20u_1%5E1%20%26v_1%5E1u_2%5E1%20%26v_1%5E1v_2%5E1%20%26%20v_1%5E1%20%26%20u_2%5E1%20%26%20v_2%5E1%20%26%201%5C%5C%20u_1%5E2u_2%5E2%20%26%20u_1%5E2v_2%5E2%20%26%20u_1%5E2%20%26v_1%5E2u_2%5E2%20%26%20v_1%5E2v_2%5E2%20%26v_1%5E2%20%26u_2%5E2%20%26%20v%5E2_2%20%26%201%5C%5C%20%5Cvdots%20%26%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%5Cvdots%20%5C%5C%20u_1%5E8u_2%5E8%20%26%20u_1%5E8v_2%5E8%20%26%20u_1%5E8%20%26v_1%5E8u_2%5E8%20%26v_1%5E8v_2%5E8%20%26%20v_1%5E8%20%26%20u_2%5E8%20%26%20v_2%5E8%20%26%201%20%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7D%20e_1%5C%5C%20e_2%5C%5C%20e_3%5C%5C%20e_4%5C%5C%20e_5%5C%5C%20e_6%5C%5C%20e_7%5C%5C%20e_8%5C%5C%20e_9%20%5Cend%7Bpmatrix%7D%3D0">

If there're eight pairs of points which could solve E, and then solve R,t. This process is solved through SVD:

<img src="http://latex.codecogs.com/gif.latex?E=U\Sigma%20V^T">

U and V are orthogonal array, <img src="http://latex.codecogs.com/gif.latex?\Sigma"> is the Singular value matrix. We know <img src="http://latex.codecogs.com/gif.latex?\Sigma=diag(\sigma,\sigma,0)"> from E's intrinsic property.
