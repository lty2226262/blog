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

1. FAST conner extraction. Compute the FAST as well as the key-point oriention in order to increse rotation fixed property for computing the BRIEF.

2. BRIEF descriptors: to describe the surrounding environments.

### FAST key-point

FAST is a key-point which detects the place where the pixel gray scale changes significantly. It is famous for its computing speed. Its contain is that if a pixel's brightness is different from its neiber pixels, it might be a conner. Its detecting steps is as followings:

1. Pick a pixel p, its brightness is $I_p$.
2. Set a threshold T(20% of $I_p$ for example).
3. Treat p as the center of the cirble, pick the 16 surrounding pixels by the radius of 3.
4. Suppose the circle has continuous points whose brightness greater than $I_p+T$ or less than $I_p-T$, then we could treat the pixel p as a key-point(N is usually 12)
5. Cycle the above steps for every pixel.
 
To be faster: detect the 1,5,9,13 brightness. Besides, we use the Non-maximal suppression to keep the maximal responsing conner to avoid the conner focus problem.

Problems in FAST:
1. Number is large and uncertain, but we usually want fixed features. Therefore, in ORB, we fix the original FAST algorithm. Compute the Harris responcing value, and pick the former largest N conner, as the result conner set.
2. It has scale problem: some conner might be seen as a conner when you're far away from the target but no more a conner when you access to it. ORB attach the scale and rotation description. Scale invariance is constructed by the image pyramid. And the feature rotation is computed by the intensity centroid.

Centroid refers to the image block gray value as the center of the weight. The steps are shown as follows:
1. In a small image block $B$, the moment of the image block is:
$$m_{pq}=\sum_{x,y\in B}x^py^qI(x,y), p,q=\{0,1\}.$$
2. Through the moment we could get the centroid of the image block:
$$C=(\frac{m_{10}}{m_{00}},\frac{m_{01}}{m_{00}})$$
3. Connect the central $O$ and the centroid $C$, we could get a  $\overrightarrow{OC}$, we could define the direction of key-points:
$$\theta=arctan(m_{01}/m_{10})$$

###BRIEF descriptor
After extracting the Oriened FAST, we could compute the discriptor of every point. ORB uses improved BRIEF feature.

BRIEF is a binary descriptor, its description vector consists of many 0 and 1, the 0 and 1 represents the size relationship: if $p$ is larger than $q$, it sets 1, otherwise it sets 0. If we pick 128 such $p,q$ pairs, we could get a 128-dimension vector consist of $p,q$. They pick such pairs randomly following some probablity rule.

###Feature matching
Feature matching is a signicant step in the SLAM, it deals withe the data association problem, when we see the landmark and determine the relationship of the landmarks we have seen before. By accurate matching, we could reduce the burden on the pose estimation and the optimization. But the mismatch always limit the SLAM.

How to match these points? The easiest method is the Brute-Force Marcher. For every key-point $x_t^m$, compare its distance to every other key-points'. The distance is Hamming distance.

But as the amount of the key-points get larger, the brute-force matcher turns to be very slow. We use FLANN to compute the situation where there are a large of amount of key-points. 