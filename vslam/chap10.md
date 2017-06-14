# Backend

## The probability of state estimate

VO has a short memory, so we wish the motion trajectory keeps in a optimized state. We may utilize the newest knowledge to update the state long before. So at the backend optimization, we use the former(or all)information to update the state, as well as the future information. This is called Batch method. Otherwise, if we only utilize the latest information, it is called incremental.

The motion and observation equation as, from poses <img src="http://chart.googleapis.com/chart?cht=tx&chl=x_0"> to <img src="http://chart.googleapis.com/chart?cht=tx&chl=x_N">, and the landmark <img src="http://chart.googleapis.com/chart?cht=tx&chl=y_0"> to <img src="http://chart.googleapis.com/chart?cht=tx&chl=y_M">,u_k is the motion equation, w_k and v_k are noises:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x_k%3Df%28x_%7Bk-1%7D%2Cu_k%29%2Bw_k%5C%5C%20z_%7Bk%2Cj%7D%3Dh%28y_j%2C%20x_k%29%20%2B%20v_%7Bk%2Cj%7D%20%5Cend%7Bmatrix%7D%5Cright.">

Attention:

1. only when x_k has seen y_j, we could generate the observation data, otherwise, there will be no data. In fact, we could get only a small part of landmarks when we are at a position. Besides, because the number of key-points are very large, so the number of observation equations is more than that of motion equation.
2. We might have no sensor to measure motion, so we might have no motion  equation. Under this situation, we have several ways: to assume that there is no motion equation, or assume that the camera is fixed, or assume that the camera is moving in a static velocity. Without motion equation, this is like the sfM(structure from motion) problem, we refine the motion and structure from a series of images.

Since we have motion data `u` and observation data `z`, how should we dertermine the distribution of `x,y`. We assume `x,y` fit Gaussian distribution. So the problem turns to be: how to estimate the Gaussian distribution of the state value.

How to solve this problem?

First, change the signal: mark `x_k` as all the unknown variables at the time `k`. It contains landmarks.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=x_k%5Cequiv%20%5C%7Bx_k%2Cy_1%2C...%2Cy_m%5C%7D">

Besides, mark all the observations at time `k` as `z_k`. so the equation becomes:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x_k%3Df%28x_%7Bk-1%7D%2Cu_k%29%2Bw_k%5C%5C%20z_%7Bk%2Cj%7D%3Dh%28x_k%29%20%2B%20v_%7Bk%7D%20%5Cend%7Bmatrix%7D%5Cright.">

Consider time `k`, we wish to estimate the state using data from `0` to `k`

<img src="http://chart.googleapis.com/chart?cht=tx&chl=P%28x_k%5Cmid%20x_0%2C%20u_%7B1%3Ak%7D%2C%20z_%7B1%3Ak%7D%29.">

`0:k` means from time `0` to time `k`

According to Bayesian:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=P%28x_k%5Cmid%20x_0%2C%20u_%7B1%3Ak%7D%2C%20z_%7B1%3Ak%7D%29%20%5Cpropto%20P%28z_k%20%5Cmid%20x_k%29P%20%28x_k%5Cmid%20x_0%2C%20u_%7B1%3Ak%7D%2C%20z_%7B1%3Ak-1%7D%29">

expand the equation,

<img src="http://chart.googleapis.com/chart?cht=tx&chl=P%28x_k%20%5Cmid%20x_0%2C%20u_%7B1%3Ak%7D%2C%20z_%7B1%3Ak-1%7D%29%3D%5Cint%20P%28x_k%5Cmid%20x_%7Bk-1%7D%2C%20x_0%2C%20u_%7B1%3Ak%7D%2C%20z_%7B1%3Ak-1%7D%29P%28x_%7Bk-1%7D%5Cmid%20x_0%2C%20u_%7B1%3Ak%7D%2C%20z_%7B1%3Ak-1%7D%29dx_%7Bk-1%7D">

If Markov is set up, the state only correspond with the latest state. However, if the state corresponds with all time before, we could get a frame that uses non-linear optimization. The later is more useful.

### Linear system and KF

Assume the state only relate with the latest state, we could simplify:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=P%28x_k%5Cmid%20x_%7Bk-1%7D%2Cx_0%2Cu_%7B1%3Ak%7D%2Cz_%7B1%3Ak-1%7D%29%3D%20P%28x_k%5Cmid%20x_%7Bk-1%7D%2Cu_k%29">

### Nonlinear system and EKF

Taylor expand the motion and observation equation and then calculate.

Some other filters: IF, IKF, UKF, PF, SWF

What's the limitation of filters?

1. We assume the Markov property, so the state only corresponds with the near frame's state.
2. When the robot run away, it doesn't follow the Taylor expansion.
3. A very large matrix to save the landmark.

## BA and graph-optimization

To extract the best camera 3D module and camera parameters from the reconstruction. From bundles of light rays to camera's pose adjustment, we call it BA.

### Projection module and BA cost function

1. Transform world coordinate to pixel coordinate, using the extrinsic `(R, t)`:

  <img src="http://chart.googleapis.com/chart?cht=tx&chl=P'=Rp%2Bt=[X',Y',Z']^T">
2. Project the P' to the normalized plane, get the normalized coordinate:

  <img src="http://chart.googleapis.com/chart?cht=tx&chl=P_c=[u_c,v_c,1]^T=[X'/Z',Y'/Z',1]^T">
3. Get the original coordinate before rectified.

  <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20u_c%27%3Du_c%281%2Bk_1r_c%5E2%2Bk_2r_c%5E4%29%5C%5C%20v_c%27%3Dv_c%281%2Bk_1r_c%5E2%2Bk_2r_c%5E4%29%20%5Cend%7Bmatrix%7D%5Cright.">

4. calculate the pixel coordinate according to the intrinsic module.

  <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20u_s%3Df_xu_c%27%2Bc_x%5C%5C%20v_s%3Df_yv_c%27%2Bc_y%20%5Cend%7Bmatrix%7D%5Cright.">
