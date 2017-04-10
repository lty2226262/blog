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

Because of these noises, we should estimate the pose x and map y through these noisy data, these build a state estimate problem. In a long period, we use Filter to solve this problem, while nonlinear optimization is more used recently.

 First of all, we could see what we are talking in probability. In nonlinear optimization, we set all of our estimation variables in a "state variable":

 <img src="http://latex.codecogs.com/gif.latex?x%3D%5C%7Bx_1%2C%20...%2C%20x_N%2C%20y_1%2C%20...%2C%20y_M%5C%7D">

 Now, we could get that to solve the input data u and observation data z, to compute the state x conditional probability distribution:

<img src="http://latex.codecogs.com/gif.latex?P%28x%5Cmid%20z%2Cu%29">

Similar to x, the u and z is the general name of the data. Especially, when we don't have sensor to measure the motion but only a series of images, which is we only consider the observation formula data, it's to estimate the conditional distribution of the <img src="http://latex.codecogs.com/gif.latex?P%28x%5Cmid%20z%2Cu%29">. If we ignore the time relationship of the image, this problem is a SfM problem (Structure from Motion), so we could structure a 3D spatial model from a series of images. In this situation, SLAM could be considered as a time series, we need to solve a sfM problem real time. To estimate the state variables' distribution, we use Bayes Rules:

<img src="http://latex.codecogs.com/gif.latex?P%28x%5Cmid%20z%29%3D%5Cfrac%7BP%28z%5Cmid%20x%29P%28x%29%7D%7BP%28z%29%7D%5Cpropto%20P%28z%5Cmid%20x%29P%28x%29">

The left part of Bayes Rules call Posterior probability, its right calls Likelihood, and P(x) calls a priori. It's difficult to compute the posterior, but it is possible to compute a best estimation of a state and maximize the posterior(MAP):

<img src="http://latex.codecogs.com/gif.latex?x%5E*_%7BMAP%7D%3DargmaxP%28x%5Cmid%20z%29%3DargmaxP%28z%5Cmid%20x%29P%28x%29">

We could know from the Bayes Rules that we could solve the maximum a posterior by maximize the product of maximum likelihood and the priori. Furthermore, we could also sat that we don't have the pose and that's we don't have the priori. That is, we could solve the maximize Likelihood estimation(MLE):

<img src="http://latex.codecogs.com/gif.latex?x%5E*_%7BMLE%7D%3DargmaxP%28z%5Cmid%20x%29">

The likelihood means what we could get the observation data through current pose, and the MLE means which condition we could get the observation data.

### Least squares

So how could we get the SLE? For once observation:

<img src="http://latex.codecogs.com/gif.latex?z_%7Bk%2Cj%7D%3Dh%28y_j%2Cx_k%29&plus;v_%7Bk%2Cj%7D">

Due to we suppose the noise <img src="http://latex.codecogs.com/gif.latex?v_k%20%5Csim%20N%280%2C%20Q_%7Bk%2Cj%7D%29">, so we could get the conditional probability:

<img src="http://latex.codecogs.com/gif.latex?P%28z_%7Bj%2Ck%7D%5Cmid%20x_k%2C%20y_j%29%3DN%28h%28y_j%2C%20x_k%29%2CQ_%7Bk%2Cj%7D%29">

It is also a Gaussian distribution. To compute its maximum <img src="http://latex.codecogs.com/gif.latex?x_k%2Cy_j">, we could also use a minimize negative logarithm to compute the most likelihood of a Gaussian distribution.

Gaussian distribution has a good form under the negative logarithm. Consider a multi-dimension Gaussian distribution <img src="http://latex.codecogs.com/gif.latex?x%5Csim%20N%28%5Cmu%2C%20%5CSigma%29">, its probability frequency function is:

<img src="http://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B%282%5Cpi%29%5ENdet%28%5CSigma%29%7D%7Dexp%28-%5Cfrac%7B1%7D%7B2%7D%28x-%5Cmu%29%5ET%5CSigma%20%5E%7B-1%7D%28x-%5Cmu%29%29">

To compute the negative logarithm, it turns to be:

<img src="http://latex.codecogs.com/gif.latex?-ln%28P%28x%29%29%3D%5Cfrac%7B1%7D%7B2%7Dln%28%282%5Cpi%29%5EN%20det%28%5CSigma%29%29&plus;%5Cfrac%7B1%7D%7B2%7D%28x-%5Cmu%29%5ET%5CSigma%20%5E%7B-1%7D%28x-%5Cmu%29">

To maximum the original distribution equals to minimize the negative logarithm. Because the first component is not correspond with x, so we could neglect it. So we could get the MEL to minimize the quadratic component. We aims to solve:

<img src="http://latex.codecogs.com/gif.latex?x%5E*%3Dargmin%28%28z_%7Bk%2Cj%7D-h%28x_k%2Cy_j%29%29%5ETQ_%7Bk%2Cj%7D%5E%7B-1%7D%28z_%7Bk%2Cj%7D-h%28x_k%2Cy_j%29%29%29">

We could also find that this formula equals to minimize the error's square. Hence, we could define the error between the data and the estimation:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20e_%7Bv%2Ck%7D%3Dx_k-f%28x_%7Bk-1%7D%2Cu_k%29%5C%5C%20e_%7By%2Cj%2Ck%7D%3Dz_%7Bk%2Cj%7D-h%28x_k%2Cy_j%29%20%5Cend%7Bmatrix%7D">

And compute the sum of the error's square:

<img src="http://latex.codecogs.com/gif.latex?J%28x%29%3D%5Csum_ke%5ET_%7Bv%2Ck%7DR%5E%7B-1%7D_ke_%7Bv%2Ck%7D&plus;%5Csum%20_k%20%5Csum%20_j%20e%5ET_%7By%2Ck%2Cj%7DQ%5E%7B-1%7D_%7Bk%2Cj%7De%5E%7B-1%7D_%7By%2Ck%2Cj%7D">

Then we could get a general Least Square Problem, it is a MLE of the state. Because of the noise, the formula won't be right if we introduce the estimated trajectory and the map to the SLAM motion and observation formula. We could adjust the estimated value to decrease the error. And then we could get a small value. It is a typical nonlinear optimization.

The SLAM problem has a special structure:

* The problem is a sum of many errors' square. Though the state dimension is very high, but every error is simple, only corresponds with one or two state variables. For example, motion error is only related to x_{k-1}, x_k, and the observation error is only related to x_k, y_j. And we will set the error component a Jacobian matrix and put the block into a whole Jacobian matrix. For this, we call all these error components parameter Block.

* The increment equations are sparse, so they are solvable even in a high dimension.

* If represent in Lie algebra, it will be a non-restrict LSP problem.

* If we represent the error in a quadratic form, it is direct as well as some problems.

## Nonlinear least square problem

1. compute the derivatives
2. iteration

### Newton's method
https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
### Gauss-Newton method
https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm
### Levernberg-Marquardt method
https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm
