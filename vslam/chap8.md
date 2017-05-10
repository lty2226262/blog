# VO
## Direct method

1. Key-points extraction is time consuming.
2. Ignore the other information if using key-points method.
3. The key-points will be too little if going to few featured position.

The way of solving this problem:

1. Using optical flow to avoid the time computing descriptors and matching.
2. Using Direct method to avoid the time computing descriptors.
3. Using gray variation to compute the camera movement directly.

when we using key-points, we often compute the reprojection error. However, in direct method, we do not need to compute the relationship between point pairs, we usually minimize the photometric error to compute them.

## Optical Flow

 Compute part of optical flows called sparse flow, compute all of the pixels are called dense flow. Sparse optical flows take Lucas-Kanade optical flows for representation.

### Lucas-Kanade optical flow

In LK optical flow, we assume that the image of cameras changes by the time being. The image could be treat as a time function: I(t). Therefore, when at t, the position (x, y), its gray value could be written as I(x, y, t)

Basic assumption:

* Gray invariant: it is not always true. But we assume it.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=I(x%2Bdx,y%2Bdy,t%2Bdt)=I(x,y,t)">

Then Taylor expansion:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=I(x%2Bdx,y%2Bdy,t%2Bdt)\approx%20I(x,y,t)%2B\frac{\partial%20I}{\partial%20x}dx%2B\frac{\partial%20I}{\partial%20y}dy%2B\frac{\partial%20I}{\partial%20t}dt">

Therefore,

<img src="http://chart.googleapis.com/chart?cht=tx&chl=\frac{\partial%20I}{\partial%20x}dx%2B\frac{\partial%20I}{\partial%20y}dy%2B\frac{\partial%20I}{\partial%20t}dt=0">

divide by dt, we could get:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=\frac{\partial%20I}{\partial%20x}\frac{dx}{dt}%2B\frac{\partial%20I}{\partial%20y}\frac{dy}{dt}=-\frac{\partial%20I}{\partial%20t}">

dx/dt is the pixel velocity along the x axis, dy/dt is the velocity along the y axis, we mark it as u,v. At the same time, <img src="http://chart.googleapis.com/chart?cht=tx&chl=\partial%20I/\partial%20x">is the point in this image grads along the x axis, the other component is the grads along y axis, mark them as Ix and Iy. Note it in matrix, we could get:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cbegin%7Bbmatrix%7D%20I_x%20%26%20I_y%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20u%5C%5C%20v%20%5Cend%7Bbmatrix%7D%3D-I_t">

We want to solve u and v but lack of constrains. Then we introduce an extra constrain to compute u,v. In LK optical flow, we assume the pixels in a window have the same motion.

Consider a w x w window, we have w^2 equations, then using Least squares to solve this equation group.

## Direct method

a spatial point in world coordinate P[X, Y, Z], its inhomogeneous coordinate through the two cameras are p_1, p_2. The thought of direct method is to estimate the camera pose and try to find the position of p_2, If the pose isn't good enough, the appearance of p_2 and p_1 will be obviously different. To minimize the difference, we optimize the pose of camera by minimizing photometric error, which is the gap between two images:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=e=I_1(p_1)-I_2(p_2)">

and the minimizing value is the 2nd norm of this error, which is:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%5Cxi%20J%28%5Cxi%29%3D%5Cleft%20%5C%7C%20e%20%5Cright%20%5C%7C%5E2">

It's also based on gray invariant. We suppose that in different views, the gray of image is invariant. The pose estimation problem turns to be:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%5Cxi%20J%28%5Cxi%29%3D%5Cleft%20%5C%7C%20e%20%5Cright%20%5C%7C%5E2">

### Discussion on direct method
To get better result, we must assure that most of the pixel grads could lead to right direction.
 However, when we go along the image, we should be careful if the grads turn down all the time. Then images are always non-convex function, so we could only get the good enough image if the motion is small enough.

### Conclusion

pros:

* save the time computing key-points and descriptors.

* little key-points

* dense or semi-dense map

cons:

* non-convex: so the motion must be very small

* not useful for a single pixel

* gray invariant
