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

U and V are orthogonal array, <img src="http://latex.codecogs.com/gif.latex?\Sigma"> is the Singular value matrix. We know <img src="http://latex.codecogs.com/gif.latex?\Sigma=diag(\sigma,\sigma,0)"> from E's intrinsic property. Through the SVD decomposition, for any E, there may be 2 possible corresponding t,R:

<img src="http://latex.codecogs.com/gif.download?%5Cbegin%7Bmatrix%7D%20t_1%5E%5Cwedge%20%3D%20UR_Z%5Cfrac%7B%5Cpi%7D%7B2%7D%5CSigma%20U%5ET%2C%20R_1%20%3D%20UR%5ET_Z%28%5Cfrac%7B%5Cpi%7D%7B2%7D%29V%5ET%5C%5C%20t_2%5E%5Cwedge%20%3D%20UR_Z%28-%5Cfrac%7B%5Cpi%7D%7B2%7D%29%5CSigma%20U%2C%20R_2%20%3D%20UR%5ET_Z%28-%5Cfrac%7B%5Cpi%7D%7B2%7D%29V%5ET%20%5Cend%7Bmatrix%7D">

<img src="http://latex.codecogs.com/gif.download?R_Z(\frac{\pi)}{2}"> represent rotating 90 degree along Z axis. Because -E equals to E, so negate t will get the same result. There are 4 probable solutions.

The last problem: E may not fit its intrinsic property: Singular Value <img src="http://latex.codecogs.com/gif.download?\sigma,\sigma,0">. The normal deed is: SVD decomposition of E and get the Singular Matrix <img src="http://latex.codecogs.com/gif.download?\Sigma=diag(\sigma_1,\sigma_2,\sigma_3)">, suppose that <img src="http://latex.codecogs.com/gif.download?\sigma_1>\sigma_2>\sigma_3">, then:

<img src="http://latex.codecogs.com/gif.download?E=Udiag(\frac{\sigma_1+\sigma_2}{2},\frac{\sigma_1+\sigma_2}{2},0)V^T)">. It means projection on the flow E. Of course, the much easier deed is set Singular Value diag(1,0,0), because E has the sacale eqaualism.

### Homography matrix
If all of the points in the scene are on the same plane, we could use the homography property to do motion estimation.

### Discussion
E, F, H all can decompose the motion, but H needs all feature points stay on a plane. Its solved t and R are the same in scale, if we multiply a non-zero constant, the decomposition is fit. Hence, we usually nomarlize t, and let its length equal to 1.

#### scale amibiguity

The normalization leads to scale ambiguity, if we multiply a constant to t, the equation also holds. In monocular slam, we normalize the t, which means fixed scale.

Another normalization method is to set the average depth as 1. It has more stable values in computing.

#### pure rotation in initialization
If the camera is only rotation, then t becomes zero, and the E will also be 0, then we could not solve R. So in initialization, we could not only rotate but also translate.

#### More than 8 pairs of points

For 8 points method, we could get the coefficient matrix is A:

<img src="http://latex.codecogs.com/gif.download?Ae=0">

For 8 points method, the size of A is 8x9, if the count of the matched points pairs more than 8, there may be no e. Hence, we could minimize the quadric to solve this equation:

<img src="hhttp://latex.codecogs.com/gif.download?min_e%5Cleft%20%5C%7C%20Ae%20%5Cright%20%5C%7C%5E2_2%3Dmin_ee%5ETA%5ETAe">

This solves the E matrix, but when the mismatch exists, we might prefer the Ramdom Sample Concensus,RANSAC.

## Triangulation

When we have estimated the camera motion, we should estimate the feature points' spatial coordination through triangulation.

Because of noises, the two lines may not intersect, so we solve them by the method of Least Squares Method.

### Triangulation discussion

Triangulation is concluded by translation, if we only rotate the camera, we could not get the result. 2 ways to raise the accuration: 1. enhance the measure accuracy; 2. increase the translation value. But we could not increase the translation value as much as possible because the light and appearance will have significant changes.

There is a depth filter if we decrease the variance of the mesurement.

## 3D-2D: PnP

Using 3D or rgbd sensor. Avoid solving initialization, pure ratation and scale problem.

Many solve method: P3P, DLT, EPnP, UPnP. Besides, we could use the nonlinear optimization to build the least squatrs problem, This is Bundle Adjustment.

###DLT:

a spatial point P, whose coordinate is <img src="hhttp://latex.codecogs.com/gif.download?P=(X,Y,Z,1)^T">. In image <img src="hhttp://latex.codecogs.com/gif.download?I_1">, its projection point <img src="hhttp://latex.codecogs.com/gif.download?x_1=(u_1,v_1,1)^T">. R and t is unknown. We define a matrix [R|t] whose size is 3x4, we expand it as followings:

<img src="http://latex.codecogs.com/gif.latex?s%5Cbegin%7Bpmatrix%7D%20u_1%5C%5C%20v_1%5C%5C%201%20%5Cend%7Bpmatrix%7D%3D%5Cbegin%7Bpmatrix%7D%20t_1%20%26%20t_2%20%26%20t_3%20%26%20t_4%5C%5C%20t_5%20%26%20t_6%20%26%20t_7%20%26%20t_8%5C%5C%20t_9%20%26%20t_%7B10%7D%20%26%20t_%7B11%7D%20%26%20t_%7B12%7D%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%20X%5C%5C%20Y%5C%5C%20Z%5C%5C%201%20%5Cend%7Bpmatrix%7D">

Eliminate s, we could get two constrians:

<img src="http://latex.codecogs.com/gif.latex?u_1%3D%5Cfrac%7Bt_1X&plus;t_2Y&plus;t_3Z&plus;t_4%7D%7Bt_9X&plus;t_%7B10%7DY&plus;t_%7B11%7DZ&plus;t_%7B12%7D%7D%2Cv_1%3D%5Cfrac%7Bt_5X&plus;t_6Y&plus;t_7Z&plus;t_8%7D%7Bt_9X&plus;t_%7B10%7DY&plus;t_%7B11%7DZ&plus;t_%7B12%7D%7D">

To simplify the expression, we define the row vector:

<img src="http://latex.codecogs.com/gif.latex?t_1%3D%28t_1%2Ct_2%2Ct_3%2Ct_4%29%5ET%2Ct_2%3D%28t_5%2Ct_6%2Ct_7%2Ct_8%29%5ET%2C%20t_3%3D%28t_9%2C%20t_%7B10%7D%2C%20t_%7B11%7D%2C%20t_%7B12%7D%29%5ET">

Then we have:

<img src="http://latex.codecogs.com/gif.latex?t_1%5ETP-t_3%5ETPu_1%3D0">

and

<img src="http://latex.codecogs.com/gif.latex?t_2%5ETP-t_3%5ETPv_1%3D0">

t is a variable to solve, and every key-point provide two linear constrains. Suppose we have N key-points, we could list the linear equations:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20P_1%5ET%20%26%200%20%26%20-u_1P_1%5ET%5C%5C%200%20%26%20P_1%5ET%20%26%20-v_1P_1%5ET%5C%5C%20%5Cvdots%20%26%20%5Cvdots%20%26%5Cvdots%20%5C%5C%20P_N%5ET%20%26%200%20%26%20-u_NP_N%5ET%5C%5C%200%20%26%20P_N%5ET%20%26%20-v_NP_N%5ET%20%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7D%20t_1%5C%5C%20t_2%5C%5C%20t_3%20%5Cend%7Bpmatrix%7D%3D0">

t has 12 dimensions in total, and we should have 6 pairs key-points at least. This method calls DLT. When we have more than 6 pairs points, we could solve the least squars solutions by SVD.

In DLT solution, we should project the matrix into SE(3) flow.

###P3P

3D points: A,B,C is in the world coordinate

2D points: a, b, c is the 2D point.

<img src="https://github.com/lty2226262/blog/blob/master/MarkdownPhotos/vslam_7_2.png?raw=true">

Consider Oab and OAB. Using the cosine theorem:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20OA%5E2&plus;OB%5E2-2OA%5Ccdot%20OB%20%5Ccdot%20cos%20%3Ca%2Cb%3E%20%3D%20AB%5E2%5C%5C%20OB%5E2&plus;OC%5E2-2OB%5Ccdot%20OC%20%5Ccdot%20cos%20%3Cb%2Cc%3E%20%3D%20BC%5E2%5C%5C%20OA%5E2&plus;OC%5E2-2OA%5Ccdot%20OC%20%5Ccdot%20cos%20%3Ca%2Cc%3E%20%3D%20AC%5E2%20%5Cend%7Bmatrix%7D"

divided by OC^2, and note x = OA/OC, y = OB/OC:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20x%5E2&plus;y%5E2-2xycos%3Ca%2Cb%3E%3DAB%5E2/OC%5E2%5C%5C%20y%5E2&plus;1%5E2-2ycos%3Cb%2Cc%3E%3DBC%5E2/OC%5E2%5C%5C%20x%5E2&plus;1%5E2-2xcos%3Ca%2Cc%3E%3DAC%5E2/OC%5E2%20%5Cend%7Bmatrix%7D">

note <img src="http://latex.codecogs.com/gif.latex?v%3DAB%5E2/OC%5E2%2Cuv%3DBC%5E2/OC%5E2%2Cwv%3DAC%5E2/OC%5E2">, we could conclude that:

Replace v with the form in the equation 1:

<img src="http://latex.codecogs.com/gif.download?%5Cbegin%7Bmatrix%7D%20%281-u%29y%5E2-ux%5E2-cos%3Cb%2Cc%3Ey+2uxycos%3Ca%2Cb%3E+1%3D0%5C%5C%20%281-w%29x%5E2-wy%5E2-cos%3Ca%2Cc%3Ex+2wxycos%3Ca%2Cb%3E+1%3D0%20%5Cend%7Bmatrix%7D">

Notice the known and unknown variables, because we know the 2D pictures in the imagine, so we know the cosine value of cos<a,b>, cos<b,c> and cos<a,c>. At the same time,  <img src="http://latex.codecogs.com/gif.latex?u%20%3D%20BC%5E2/AB%5E2%2C%20w%20%3D%20AC%5E2/AB%5E2"> could compute by the world coordination A,B,C. However, the x,y are unknown. Similar to E, we have 4 solutions. We could compute the most possible solution and get the 3D coordination. And get the R and t by the 3D-3D pair.

P3P's disadvantage:

1. only uses 3 points. Waste lots of data.
2. If influenced by the noises, then there will be mismatching, not available.

To solve these problems, we use EPnP or UPnP and so on. Throughout SLAM, we use P3P/EPnP first then Bundle Adjustment.

### Bundle Adjustment

Linear method introduced above: solve the pose of cameras, then compute the position of the spatial point, nonlinear optimization: treat them all as the optimizable variables, then optimize them. We could use PnP or ICP to optimize them. In PnP problem, this Bundle Adjustment problem is a reprojection error problem.

Consider there are n spatial points P and their projections p, we wish to compute the pose R,t of camera, its Lie Algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cxi">. Suppose a spatial point <img src="http://latex.codecogs.com/gif.latex?P_i%3D%5BX_i%2CY_i%2CZ_i%5D%5ET">, and its projected pixel coordinate <img src="http://latex.codecogs.com/gif.latex?u_i%3D%5Bu_i%2Cv_i%5D%5ET">.

<img src="http://latex.codecogs.com/gif.latex?s_i%5Cbegin%7Bbmatrix%7D%20u_i%5C%5C%20v_i%5C%5C%201%20%5Cend%7Bbmatrix%7D%3DKexp%28%5Cxi%20%5E%5Cwedge%29%5Cbegin%7Bbmatrix%7D%20X_i%5C%5C%20Y_i%5C%5C%20Z_i%5C%5C%201%20%5Cend%7Bbmatrix%7D">

Despite of Lie Algebra using <img src="http://latex.codecogs.com/gif.latex?%5Cxi">. Writing in the form of matrix:

<img src="http://latex.codecogs.com/gif.latex?s_iu_i%3DKexp%28%5Cxi%5E%5Cwedge%29P_i">

Because the pose of cameras and noises, we could sum the noises, and construct the least squares problem. Then minimize the error:

<img src="http://latex.codecogs.com/gif.latex?%5Cxi%20%5E*%20%3D%20argmin_%5Cxi%20%5Cfrac%7B1%7D%7B2%7D%5Csum%20%5En%20_%7Bi%3D1%7D%5Cleft%20%5C%7C%20u_i-%5Cfrac%7B1%7D%7Bs_i%7DKexp%28%5Cxi%20%5E%5Cwedge%29%20P_i%20%5Cright%20%5C%7C%5E2_2">

The error is an error between the pixel coordinate and the 3D point projection following the current pose, it means reprojection error. Using the homogenous coordinates, the error have 3 dimensions. But due to the last dimension u is 1, the error of this dimension is always zero, so we often use inhomogeneous coordinates because the there are only 2 errors components. We know the p_1 and p_2 is the projection from the same point P through feature matching, however, we do not know the pose of cameras. So we adjust the pose of camera to make this error to zero. Becuase that we must consider many points throughout the adjustment process, the error might unable to down to 0.

By Lie Algebra, we could build the unrestraint optimization problem. Then we could use G-N or L-M to solve this problem. Before we use G-N or L-M, we should know the derivative of every error, this is linearization:

<img src="http://latex.codecogs.com/gif.latex?e%28x&plus;%5CDelta%20x%29%5Capprox%20e%28x%29&plus;J%5CDelta%20x">

If e is the pixel coordinate error(2 dimensions), x is the pose of camera(6 dimensions), J will be a 2x6 matrix. We now deduce the form of J.

Remember the content of Lie Algebra, we introduce how to solve the Lie Algebra's derivative using perturbation model. Firstly, note the spatial point coordinate is P', and withdraw the former 3 dimensions of it:

<img src="http://latex.codecogs.com/gif.latex?P%27%3D%28exp%28%5Cxi%20%5E%5Cwedge%29P%29_%7B1%3A3%7D%3D%5BX%27%2CY%27%2CZ%27%5D%5ET">

The camera projection model that's relative to P' is:

<img src="http://latex.codecogs.com/gif.latex?su%3DKP%27">

expand it we could get:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20su%5C%5C%20sv%5C%5C%20s%20%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%20f_x%20%26%200%20%26%20c_x%20%5C%5C%200%20%26%20f_y%20%26%20c_y%5C%5C%200%20%26%200%20%26%201%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20X%27%5C%5C%20Y%27%5C%5C%20Z%27%20%5Cend%7Bbmatrix%7D">

eliminate s with the 3rd line:

<img src="http://latex.codecogs.com/gif.latex?u%3Df_x%5Cfrac%7BX%27%7D%7BZ%27%7D&plus;c_x%2C%20v%20%3D%20f_y%5Cfrac%7BY%27%7D%7BZ%27%7D%20&plus;c_y">

After the definition of the middle component, we could left multiply the perturbation component to the <img src="http://latex.codecogs.com/gif.latex?%5Cdelta%20%5Cxi"> to the <img src="http://latex.codecogs.com/gif.latex?%5Cxi%20%5E%5Cwedge">. According to chain principle:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20e%7D%7B%5Cpartial%20%5Cdelta%20%5Cxi%7D%20%3D%20lim%20_%7B%5Cdelta%5Cxi%5Crightarrow%200%7D%5Cfrac%7Be%28%5Cdelta%5Cxi%20%5Coplus%20%5Cxi%29%7D%7B%5Cdelta%20%5Cxi%7D%3D%5Cfrac%7B%5Cpartial%20e%7D%7B%5Cpartial%20P%27%7D%5Cfrac%7B%5Cpartial%20P%27%7D%7B%5Cpartial%20%5Cdelta%20%5Cxi%7D">

The <img src="http://latex.codecogs.com/gif.download?%5Coplus"> here represent left multiply the perturbation in the Lie Algebra. The first component is the derivative of the projection point, we could conclude:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20e%7D%7B%5Cpartial%20P%27%7D%3D-%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20X%27%7D%20%26%20%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20Y%27%7D%20%26%20%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20Z%27%7D%20%5C%5C%20%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20X%27%7D%20%26%20%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20Y%27%7D%20%26%20%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20Z%27%7D%20%5Cend%7Bbmatrix%7D%20%3D%20-%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7Bf_x%7D%7BZ%27%7D%20%26%200%20%26%20-%5Cfrac%7Bf_xX%27%7D%7BZ%27%5E2%7D%5C%5C%200%20%26%20%5Cfrac%7Bf_y%7D%7BZ%27%7D%20%26%20-%5Cfrac%7Bf_yY%27%7D%7BZ%27%5E2%7D%20%5Cend%7Bbmatrix%7D">

Leaving many steps out, we could get:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20e%7D%7B%5Cpartial%20P%7D%20%3D%20-%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7Bf_x%7D%7BZ%27%7D%20%26%200%20%26%20-%5Cfrac%7Bf_xX%27%7D%7BZ%27%5E2%7D%20%5C%5C%200%20%26%20%5Cfrac%7Bf_y%7D%7BZ%27%7D%20%26%20-%5Cfrac%7Bf_yY%27%7D%7BZ%27%5E2%7D%20%5Cend%7Bbmatrix%7DR">

### Using BA optimization

g2o vertex: the pose <img src="latex.codecogs.com/gif.download?%5Cxi%20%5Cin%20%5Cmathfrak%7Bse%7D%283%29">, and all of the spatial positions <img src="http://latex.codecogs.com/gif.download?P%20%5Cin%20R%5E3">

g2o edges: every 3D point in the second camera's projection, described in the observation equation: <img src="http://latex.codecogs.com/gif.download?z_j%3Dh%28%5Cxi%2C%20P_j%29">

After we optimize the pose using BA, we could find out that there are some changes in the R mattrix.

## 3D-3D:ICP

Since we have a paired 3D point:

<img src="http://latex.codecogs.com/gif.download?P={p_1,...,p_n}">

Now, we find a Euclidean transformation R,t, leads to:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=\forall%20i,p_i=Rp_p'%2Bt">

It can be solved by the method of Iterative Closest Point (ICP). We could notice that there is no camera module in the 3D-3D transformation. In laser, we could not get the match relationship. To solve this problem, we could use two kinds of problems: SVD and nonlinear optimization.

### SVD method

We now define the error between the ith pair points:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=e_i=p_i-(Rp_i'+t)">

Then we construct the LSP, and minimize the error:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7BR%2Ct%7DJ%3D%5Cfrac%7B1%7D%7B2%7D%5Csum%5En_%7Bi%3D1%7D%5Cleft%20%5C%7C%20%28p_i-%28Rp_i%27%2Bt%29%29%20%5Cright%20%5C%7C%5E2_2">

### Nonlinear optimization method

When we represent the pose using Lie Algebra, we could write the function:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_\xi=\frac{1}{2}\sum_{i=1}^n\left \| p_i-exp(\xi^\wedge)p_i') \right \|">

We could use the PnP and ICP together. For the depth known key-points, we could compute the 3D-3D error; for the deep unknown key-points, we could use the 3D-2D remap error.
