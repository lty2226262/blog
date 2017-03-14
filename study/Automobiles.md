# Automobiles

## Lesson 1 localization

### localization

traditional way: satellites (GPS) mot very accurate ~10m need:2cm-10cm

### total probability

x-axis: location

y-axis: belief

all same: uniform maximum confusion

other: posterior

If you see a door, then more probability behind a door. Others: sensor error.

After move, the peak move: convolution.

### sense and move

sense : gain information

move : lose information

sense : initial belief

Bayes theorem reminder:

<img src="http://latex.codecogs.com/gif.latex?P(A\mid%20B)=\frac{P(B\mid%20A)%20\times%20P(A)}{P(B)}">

## Motion-Total Probability

<img src="http://latex.codecogs.com/gif.latex?P(X_i^{t})%20=%20\sum_j%20P(X^{t-1}_j)%20\dot%20P(X_i\mid%20X_j)">


t - time

i - grid cell

## Kalman Filters

kalman filter: continuous

distribution: gaussian

**two steps:**

* measurement update : Bayes rule, product
* prediction: total probability, convolution

### measurement update

Notice: the new mean is between the previous two means and the new variance is LESS than either of the previous variance.

<img src="http://latex.codecogs.com/gif.latex?\mu'=\frac{1}{\sigma&space;^2&space;&plus;&space;\gamma^2}[\gamma^2&space;\mu&space;&plus;&space;\sigma&space;^&space;2&space;\nu]\\&space;\sigma'^2&space;=&space;\frac{1}{\frac{1}{\sigma^2}&plus;\frac{1}{\gamma^2}}" title="\mu'=\frac{1}{\sigma ^2 + \gamma^2}[\gamma^2 \mu + \sigma ^ 2 \gamma]\\ \sigma'^2 = \frac{1}{\frac{1}{\sigma^2}+\frac{1}{\gamma^2}}" />

### motion

<img src="http://latex.codecogs.com/gif.latex?\mu'&space;=&space;\mu&space;&plus;&space;\nu&space;\\\sigma'^2&space;=&space;\sigma&space;^2&space;&plus;&space;\gamma&space;^2" title="\mu' = \mu + \nu \\\sigma'^2 = \sigma ^2 + \gamma ^2" />


### 2-d kalman

<img src="http://latex.codecogs.com/gif.latex?x'&space;\leftarrow&space;x&space;&plus;&space;\dot{x}&space;\\&space;\dot{x}'&space;\leftarrow&space;\dot{x}" title="x' \leftarrow x + \dot{x} \\ \dot{x}' \leftarrow \dot{x}" />

design a kalman filter

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20x%27%5C%5C%20%5Cdot%7Bx%7D%27%20%5Cend%7Bpmatrix%7D%5Cleftarrow%20%5Cbegin%7Bpmatrix%7D%201%20%26%201%5C%5C%200%20%26%201%20%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7D%20x%5C%5C%20%5Cdot%7Bx%7D%20%5Cend%7Bpmatrix%7D" />

<img src="http://latex.codecogs.com/gif.latex?z%5Cleftarrow%20%5Cbegin%7Bpmatrix%7D%201%20%26%200%20%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7D%20x%5C%5C%20%5Cdot%7Bx%7D%20%5Cend%7Bpmatrix%7D" />

prediction:

x: estimate

P: uncertainty covariance

F: state transition matrix
<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%201%20%26%201%5C%5C%200%20%26%201%20%5Cend%7Bpmatrix%7D%" />

v: motion vector

<img src="http://latex.codecogs.com/gif.latex?x%27%20%3D%20Fx%20&plus;%20v" />

<img src="http://latex.codecogs.com/gif.latex?P%27%20%3D%20F%5Ccdot%20P%20%5Ccdot%20F%5ET" />

measurement update

z: measurement

H: measurement function <img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%201%20%26%200%20%5Cend%7Bpmatrix%7D" />

R: measurement noise

I: identity matrix

<img src="http://latex.codecogs.com/gif.latex?y%20%3D%20z%20-H%20%5Ccdot%20x" />

<img src="http://latex.codecogs.com/gif.latex?S%20%3D%20H%20%5Ccdot%20P%20%5Ccdot%20H%20%5E%20T%20&plus;%20R" />

<img src="http://latex.codecogs.com/gif.latex?K%20%3D%20P%20%5Ccdot%20H%5ET%20%5Ccdot%20S%20%5E%7B-1%7D" />

<img src="http://latex.codecogs.com/gif.latex?x%27%20%3D%20x%20&plus;%20%28K%20%5Ccdot%20y%29" />

<img src="http://latex.codecogs.com/gif.latex?P%27%20%3D%20%28I%20-%20K%20%5Ccdot%20H%29%5Ccdot%20P" />

#### Notice

The kalman filter introduced above is only fit the linear system. When it comes to nonlinear system, EKF or UKF or PF are more useful.

#### Extended Kalman filter

##### A simple example

Imagine an airplane, we can think of the current altitude as a fraction of the previous altitude. The altitude at the current time is 98% of its altitude at the previous time:

<img src="http://latex.codecogs.com/gif.latex?altitude_{current\_time}%20=%200.98%20\times%20altitude_{previous\_time}" />

##### Dealing with noise

Real-world measurement like altitude are obtained from sensors like a GPS or barometer. These sensors offer varying degrees of accuracy. So these noises add a "noisy" to the observed sensor reading.

 <img src="http://latex.codecogs.com/gif.latex?observed\_altitude_{current\_time}%20=%20altitude_{current\_time}+noise_{current\_time}" />

##### Putting it together

To make the above two equations more general:

 <img src="http://latex.codecogs.com/gif.latex?x" /> - current state of our system,

 <img src="http://latex.codecogs.com/gif.latex?x%20_%20{k%20-%201}" /> - previous state,

a - some constant,

<img src="http://latex.codecogs.com/gif.latex?z_k" /> - our current observation of the system,

<img src="http://latex.codecogs.com/gif.latex?v_k" /> - the current noise measurement,

<img src="http://latex.codecogs.com/gif.latex?x_k=ax_{k-1}" />

 <img src="http://latex.codecogs.com/gif.latex?z_k%20=%20x_k%20+%20v_k" />

 So the current altitude is defined as:

  <img src="http://latex.codecogs.com/gif.latex?altitude_{current\_time}=0.98\times%20altitude_{previous\_time}+turbulence_{current\_time}" />

  More generally:

<img src="http://latex.codecogs.com/gif.latex?w_k" /> - process noise, like turbulent, it is an inherent part of the process but not an artificial of observation or measurement. We will ignore process noise for a while in order to focus on the other topics.

<img src="http://latex.codecogs.com/gif.latex?x_k=ax_{k-1}+w_k" />

##### State Estimation

while our goal is to obtain the states x from the observation z, it writes:

<img src="http://latex.codecogs.com/gif.latex?x_k=z_k-v_k" />

However, we don't know the current noise <img src="http://latex.codecogs.com/gif.latex?v_k" />. Kalman defined that we can estimate the state by taking into account both the current observation and the previous estimate state. A hat means estimation. We can express the estimate as a tradeoff:

<img src="http://latex.codecogs.com/gif.latex?%g_k" /> - gain, express the tradeoff, range from 0 to 1, when equals 0, observation has no effect. when equals 1, the previous state doesn't matter.

<img src="http://latex.codecogs.com/gif.latex?%5Chat%7Bx%7D_k%3D%5Chat%7Bx%7D_%7Bk-1%7D&plus;g_k%28z_k-%5Chat%7Bx%7D_%7Bk-1%7D%29" />

##### Computing the gain

We compute the gain indirectly from the noise. Recall each observation is associated with a noise value<img src="http://latex.codecogs.com/gif.latex?v_k" />:

<img src="http://latex.codecogs.com/gif.latex?z_k=x_k+v_k" />

We know the average noise by the published accuracy but don't know the individual noise value. Call this value <img src="http://latex.codecogs.com/gif.latex?r" /> . It is a property of the sensor. Then by Kalman, we can compute:

<img src="http://latex.codecogs.com/gif.latex?p_k" /> - a prediction error that is computed recursively.

<img src="http://latex.codecogs.com/gif.latex?g_k=p_{k-1}/(p_{k-1}+r)" />

<img src="http://latex.codecogs.com/gif.latex?p_k=(1-g_k)p_{k-1}" />

If the error <img src="http://latex.codecogs.com/gif.latex?p_{k-1}" /> on our previous prediction was zero, then our current gain turns to be 0. our next estimation has no differences from the current one.

If the error <img src="http://latex.codecogs.com/gif.latex?p_{k-1}" /> is 1, the gain will be <img src="http://latex.codecogs.com/gif.latex?1/(1+r)" /> . If r is very small then the gain will be 1.

If r is very large, then the gain turns to be zero, so the observation becomes less important.

##### prediction and update

so we prediction first:

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=a\hat{x}_{k-1}" />

finally, we use the constant a in a prediction of the error as well:

<img src="http://latex.codecogs.com/gif.latex?p_k=ap_{k-1}a" />

The idea is cycle predict/update...

##### running the Filter

two steps:

***PREDICT***:

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=a\hat{x}_{k-1}" />

<img src="http://latex.codecogs.com/gif.latex?p_k=ap_{k-1}a" />

***UPDATE***:

<img src="http://latex.codecogs.com/gif.latex?g_k=p_k/(p_k+r)" />

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=\hat{x}_k+g_k(z_k-\hat{x}k)" />

<img src="http://latex.codecogs.com/gif.latex?p_k=(1-g_k)p_k" />

##### A more realistic model

recall the two equations:

<img src="http://latex.codecogs.com/gif.latex?x_k=ax_{k-1}" />

<img src="http://latex.codecogs.com/gif.latex?z_k=x_k+v_k" />

we have not accounted for time-varying control like yoke. So we introduces another variable <img src="http://latex.codecogs.com/gif.latex?u_k" />. Just as the previous state <img src="http://latex.codecogs.com/gif.latex?x_{k-1}" /> was scaled by a constant amount a. Similar to b, so we introduce the equation below:

<img src="http://latex.codecogs.com/gif.latex?x_k=ax_k+bu_k" />

we also scale the <img src="http://latex.codecogs.com/gif.latex?x_k" /> with the constant c:

<img src="http://latex.codecogs.com/gif.latex?z_k=cx_k+v_k" />

##### Modify the estimates

As we might expect, add some noises to the observations and observation variables of our system:

***PREDICT***

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=a\hat{x}_{k-1}+bu_k" />

<img src="http://latex.codecogs.com/gif.latex?p_k=ap_{k-1}a" />

***UPDATE***:

<img src="http://latex.codecogs.com/gif.latex?g_k=p_kc/(cp_kc+r)" />

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=\hat{x}_k+g_k(z_k-c\hat{x}k)" />

<img src="http://latex.codecogs.com/gif.latex?p_k=(1-g_kc)p_k" />

##### Adding velocity to the system

Recall the equation:

<img src="http://latex.codecogs.com/gif.latex?x_k=ax_{k-1}" />

since the <img src="http://latex.codecogs.com/gif.latex?distance=velocity\times%20time" />, sp the equation above means <img src="http://latex.codecogs.com/gif.latex?distance_{current}=distance_{previous}+velocity_{previous}\times%20timestep" />

##### Linear algebra

Since we want to express distance by <img src="http://latex.codecogs.com/gif.latex?x_k=ax_{k-1}" />, we could use vector:

<img src="http://latex.codecogs.com/gif.latex?x_k%5Cequiv%20%5Cbegin%7Bbmatrix%7D%20diatance_k%5C%5C%20velocity_k%20%5Cend%7Bbmatrix%7D" />

and,

<img src="http://latex.codecogs.com/gif.latex?A%3D%5Cbegin%7Bbmatrix%7D%201%20%26%20timestep%20%5C%5C%200%20%26%201%20%5Cend%7Bbmatrix%7D" />

which works out as we want:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20distance_k%5C%5C%20velocity_k%20%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%201%20%26%20timestep%20%5C%5C%200%20%26%201%20%5Cend%7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%20distance_%7Bk-1%7D%5C%5C%20velocity_%7Bk-1%7D%20%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%20distance_%7Bk-1%7D&plus;timestep%20%5Ctimes%20velocity_%7Bk-1%7D%5C%5C%20velocity_%7Bk-1%7D%20%5Cend%7Bbmatrix%7D" />

Then we can easily modify our vector and matrix to include acceleration:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20distance_k%5C%5C%20velocity_k%5C%5C%20acceleration_k%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%201%20%26%20timestep%20%26%200%5C%5C%200%20%26%201%20%26%20timestep%5C%5C%200%20%26%200%20%26%201%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20distance_%7Bk-1%7D%5C%5C%20velocity_%7Bk-1%7D%5C%5C%20acceleration_%7Bk-1%7D%20%5Cend%7Bbmatrix%7D" />

##### Sensor fusion intro

So now we have complete set of equations for our Kalman Filter in linear algebra (vector, matrix) form:

***MODEL:***

<img src="http://latex.codecogs.com/gif.latex?x_k%20=%20Ax_{k-1}%20+%20Bu_k" />

<img src="http://latex.codecogs.com/gif.latex?z_k=Cx_k+v_k" />

***PREDICT:***

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=A\hat{x}_{k-1}+Bu_k" />

<img src="http://latex.codecogs.com/gif.latex?P_k=AP_{k-1}A^T" />

***UPDATE:***

<img src="http://latex.codecogs.com/gif.latex?G_k=P_kC^T(CP_kC^T+R)^{-1}" />

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=\hat{x}_k+G_k(z_k-C\hat{x}_k)" />

<img src="http://latex.codecogs.com/gif.latex?P_k=(I-G_kC)P_k" />

It comes to sensor fusion, our observation equation is:

<img src="http://latex.codecogs.com/gif.latex?z_k=Cx_{k-1}+v_k" />

equals:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20barometer_k%5C%5C%20compass_k%5C%5C%20pitot_k%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%201%20%26%200%20%26%200%5C%5C%200%20%26%201%20%26%200%5C%5C%200%20%26%200%20%26%201%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20altitude_%7Bk-1%7D%5C%5C%20heading_%7Bk-1%7D%5C%5C%20airspeed_%7Bk-1%7D%20%5Cend%7Bbmatrix%7D" />

now when adds another sensor, says GPS. Both the barometer and the GPS will be affected by altitude. So the equation becomes:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20barometer_k%5C%5C%20compass_k%5C%5C%20pitot_k%5C%5C%20gps_k%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%201%20%26%200%20%26%200%5C%5C%200%20%26%201%20%26%200%5C%5C%200%20%26%200%20%26%201%5C%5C%201%20%26%200%20%26%200%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20altitude_%7Bk-1%7D%5C%5C%20heading_%7Bk-1%7D%5C%5C%20airspeed_%7Bk-1%7D%20%5Cend%7Bbmatrix%7D" />

Kalman gives us a better state estimate than one alone.

##### sensor fusion example

To simplify the thing, we assume that we have no knowledge of the state-transition model. So we just set our state-transition matrix to 1:

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=A\hat{x}_{k-1}=1*\hat{x}_{k-1}=\hat{x}_{k-1}" />

so the

<img src="http://latex.codecogs.com/gif.latex?P_k=AP_{k-1}A^T=1\times%20P{k-1}\times%201=P_{k-1}" />

when we update the model, the <img src="http://latex.codecogs.com/gif.latex?P_k" /> never updates. Then we must introduce the "process noise".  

<img src="http://latex.codecogs.com/gif.latex?Q" /> - the covariance of the process noise <img src="http://latex.codecogs.com/gif.latex?w_k" />

<img src="http://latex.codecogs.com/gif.latex?P_k=AP_{k-1}A^T+Q" />

even very small value of nonzero element in Q turn out to be very helpful in keeping the estimate value on track.

##### nonlinear

Since we know that all our equations below represents a linear situation, but most of our daily movements are nonlinear.

In a linear situation:

<img src="http://latex.codecogs.com/gif.latex?f%28%5Cbegin%7Bbmatrix%7D%20x%20%5C%5C%20y%20%5Cend%7Bbmatrix%7D%29%3D%20%5Cbegin%7Bbmatrix%7D%20a%26b%5C%5C%20c%26d%20%5Cend%7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%20x%5C%5C%20y%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%20ax&plus;by%5C%5C%20cx&plus;dy%20%5Cend%7Bbmatrix%7D" />

but in a nonlinear situation:

<img src="http://latex.codecogs.com/gif.latex?f%28%5Cbegin%7Bbmatrix%7D%20x%20%5C%5C%20y%20%5Cend%7Bbmatrix%7D%29%3D%20%5Cbegin%7Bbmatrix%7D%20a%26b%5C%5C%20c%26d%20%5Cend%7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%20x%5C%5C%20y%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%20ax&plus;by%5C%5C%20cx&plus;dy%20%5Cend%7Bbmatrix%7D" />

##### A nonlinear kalman filter

consider a nonlinear filter, we use <img src="http://latex.codecogs.com/gif.latex?h" /> to represent a nonlinear function like ln(x), and <img src="http://latex.codecogs.com/gif.latex?c_k" /> means its first derivative at timestep <img src="http://latex.codecogs.com/gif.latex?k" />

***MODEL:***

<img src="http://latex.codecogs.com/gif.latex?x_k=x_{k-1}+w_k" />

<img src="http://latex.codecogs.com/gif.latex?z_k=h(x_{k-1})+v_k" />

***PREDICT:***

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=\hat{x}_{k-1}" />

<img src="http://latex.codecogs.com/gif.latex?p_k=p_{k-1}+q" />

***UPDATE:***

<img src="http://latex.codecogs.com/gif.latex?g_k=p_kc_k(c_kp_kc_k+r)^{-1}" />

<img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=\hat{x}_k+g_k(z_k-h(\hat{x}_k))" />

<img src="http://latex.codecogs.com/gif.latex?p_k=(1-g_kc_k)p_k" />

##### Computing the derivative

now, we should compute the first derivative from an actual signal, without knowing the underlying function.

finite difference formula is often a very good approximation to the first derivative.

If one signal is a function of another signal, we can divide successive differences of the first signal by signal by successive differences of the second signal:

<img src="http://latex.codecogs.com/gif.latex?\frac{z_{k+1}-z_k}{x_{k+1}-x_k}" />

##### The Jacobian

now we should generalize our single-valued nonlinear observation model to a multi-valued system.

For a system with two state values and three sensors, we can rewrite this as:

<img src="http://latex.codecogs.com/gif.latex?z_k%3D%5Cbegin%7Bbmatrix%7D%20c_%7B11%7D%20%26c_%7B12%7D%20%5C%5C%20c_%7B21%7D%20%26c_%7B22%7D%20%5C%5C%20c_%7B31%7D%20%26c_%7B32%7D%20%5Cend%7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%20x_%7Bk1%7D%20%5C%5C%20x_%7Bk2%7D%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%20c_%7B11%7Dx_%7Bk1%7D&plus;c_%7B12%7Dx_%7Bk2%7D%20%5C%5C%20c_%7B21%7Dx_%7Bk1%7D&plus;c_%7B22%7Dx_%7Bk2%7D%20%5C%5C%20c_%7B31%7Dx_%7Bk1%7D&plus;c_%7B32%7Dx_%7Bk2%7D%20%5Cend%7Bbmatrix%7D" />

the <img src="http://latex.codecogs.com/gif.latex?c_{11}" /> means the coefficient relating the current value <img src="http://latex.codecogs.com/gif.latex?z_{k1}" /> of the first sensor to the second component <img src="http://latex.codecogs.com/gif.latex?x_{k2}" /> of the current state.

 For a nonlinear model, there will likewise be a matrix whose number of rows equals the number of sensors and number of columns equals the number of states. However, the matrix would contain the first derivative of the sensor value with respect to the state value. These are called partial derivative, and the matrix of such derivatives called the Jacobian.

 In other words, our linear model

 <img src="http://latex.codecogs.com/gif.latex?x_k=Ax_{k-1}+w_k" />

 becomes

 <img src="http://latex.codecogs.com/gif.latex?x_k=f(x_{k-1})+w_k" />

 where <img src="http://latex.codecogs.com/gif.latex?A" /> is replaced by the Jacobian of the state-transition function <img src="http://latex.codecogs.com/gif.latex?f" /> , and use <img src="http://latex.codecogs.com/gif.latex?H_k" /> for the Jacobian of the sensor function <img src="http://latex.codecogs.com/gif.latex?h" />.

 So:

 ***MODEL:***

 <img src="http://latex.codecogs.com/gif.latex?x_k=f(x_{k-1},u_k)+w_k" />

 <img src="http://latex.codecogs.com/gif.latex?z_k=h(x_{k})+v_k" />

 ***PREDICT:***

 <img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=f(\hat{x}_{k-1}, u_k)" />

 <img src="http://latex.codecogs.com/gif.latex?P_k=F_{k-1}P_{k-1}F_{k-1}^T+Q_{k-1}" />

 ***UPDATE:***

 <img src="http://latex.codecogs.com/gif.latex?G_k=P_kH_k^T(H_kP_kH_k^T+R)^{-1}" />

 <img src="http://latex.codecogs.com/gif.latex?\hat{x}_k=\hat{x}_k+G_k(z_k-h(\hat{x}_k))" />

 <img src="http://latex.codecogs.com/gif.latex?P_k=(I-G_kH_k)P_k" />

### Particle Filter

#### Resampling

draw N from the particles, every particle has a weight, the weight is proportional to the distance between the particle and the landmark



then build a resample wheel

### Bicycle models

TURNING ANGLE - <img src="http://latex.codecogs.com/gif.latex?\beta" />

MOVING DISTANCE - d

CAR LENGTH - L

STEERING ANGLE - <img src="http://latex.codecogs.com/gif.latex?\alpha" />

RADIUS - R

<img src="http://latex.codecogs.com/gif.latex?\beta%20=%20\frac{d}{L}\cdot%20tan(\alpha)" />

<img src="http://latex.codecogs.com/gif.latex?R%20=%20\frac{d}{\beta}" />

x-center of car - <img src="http://latex.codecogs.com/gif.latex?c_x" />

y-center of car - <img src="http://latex.codecogs.com/gif.latex?c_y" />

x-center of back wheel - x

y-center of back wheel - y

rotation angle of back wheel - <img src="http://latex.codecogs.com/gif.latex?\theta" />

<img src="http://latex.codecogs.com/gif.latex?c_x%20=%20x%20-%20sin%20(\theta)\cdot%20R" />

<img src="http://latex.codecogs.com/gif.latex?c_y%20=%20y%20-%20cos%20(\theta)\cdot%20R" />

<img src="http://latex.codecogs.com/gif.latex?x_1%27%20=%20c_x%20+%20sin(\theta%20+%20\beta)\cdot%20R" />

<img src="http://latex.codecogs.com/gif.latex?y_1%27%20=%20c_y%20+%20cos(\theta%20+%20\beta)\cdot%20R" />

<img src="http://latex.codecogs.com/gif.latex?\theta%27%20=%20(\theta%20+%20\beta)%20mod%202%20\pi" />

if <img src="http://latex.codecogs.com/gif.latex?\mid%20\beta%20\mid%20%3C%200.001" />

<img src="http://latex.codecogs.com/gif.latex?x%27%20=%20x%20+%20d%20\cdot%20cos%20\theta" />

<img src="http://latex.codecogs.com/gif.latex?y%27%20=%20y%20+%20d%20\cdot%20sin%20\theta" />

<img
 src="http://latex.codecogs.com/gif.latex?\theta%20%27%20=%20(\theta%20+%20\beta)%20mod%202%20\pi" />

### motion planning

A star disadvantages: cannot deal with branching outcomes, cannot deal with information gathering

### robot  

smooth:

<img src="http://latex.codecogs.com/gif.latex?y_i=y_i+\alpha%20(x_i%20-%20y_i)%20+%20\beta%20(y_{i+1}%20+%20y_{i-1}%20-2%20\times%20y_i)" />

### P control

p: steering = -tau * crosstrack_error

p may lead to overshoot

p larger -> oscillates faster

<img src="http://latex.codecogs.com/gif.latex?\alpha%20=%20-\tau%20_p%20\times%20CTE" />

### PD control

D to decrease overshooting

<img src="http://latex.codecogs.com/gif.latex?\alpha%20=%20-\tau%20_p%20\times%20CTE%20-%20\tau%20_d\frac{d}{dt}CTE" />

### PID control

I to decrease stead error

<img src="http://latex.codecogs.com/gif.latex?\alpha%20=%20-\tau%20_p%20\times%20CTE%20-%20\tau%20_d\frac{d}{dt}CTE-\tau_I%20\sum{CTE}" />

### how to assign parameters: TWIDDLE

    run() -> return a goodness, always the average crosstrack error
------------------------

    p = [0,0,0] #parameters
    dp = [1,1,1] #potential changes

    best_err = run(p)
    for i in range(len(p)):
      p[i] += dp[i]
      err = run(p)

    if err < best_err:
      best_err = err
      dp[i] *= 1.1
    else:
      p[i] -= 2dp[i]
    .
    .
    .
    else:
      p[i] += dp[i]
      dp[i] *= 0

  ### slam

  mu = omega^{-1}*xi
