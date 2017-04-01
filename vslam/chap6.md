# Nonlinear optimization

## status estimation problem

### maximum a posteriori and maximum likelihood

Recall the classical SLAM model, it's composed of a state equation and a motion equation, shown below:

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x_k%3Df%28x_%7Bk-1%7D%2Cu_k%29&plus;w_k%5C%5C%20z_%7Bk%2Cj%7D%3Dh%28y_j%2Cx_k%29&plus;v_%7Bk%2Cj%7D%20%5Cend%7Bmatrix%7D%5Cright.">

We know through the camera position estimation that the <img src="http://latex.codecogs.com/gif.latex?x_k"> is the pose of camera. We could express it with the transformation matrix or the Lie Algebra. The pose <img src="http://latex.codecogs.com/gif.latex?x_k"> could be expressed by <img src="http://latex.codecogs.com/gif.latex?T_k"> or <img src="http://latex.codecogs.com/gif.latex?\xi^\wedge_k">, which are equal. Because that the motion equations is common, so we mainly discuss the measurement equations. Suppose that we observe y_j at x_k which maps the position z_{k,j} on the image, then we could express the observation equations as:

<img src="http://latex.codecogs.com/gif.latex?sz_%7Bk%2Cj%7D%3DKexp%28%5Cxi%20%5E%5Cwedge%29y_j">

K is the intriscs of the camera, s is the distance of pixel, the z_{k,j} and y_j must format in homogeneous coordinates.

we often assume that there are two noise components in this formula.

<img src="http://latex.codecogs.com/gif.latex?w_k%20%5Csim%20N%280%2C%20R_k%29%2C%20v_k%20%5Csim%20N%280%2CQ_%7Bk%2Cj%7D%29">

Because of these noises, we should estimate the pose x and map y through these noisy data, these build a state estimate problem. In a long period, we use Filter to solve this problem, while
