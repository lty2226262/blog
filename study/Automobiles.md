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

<img src="http://latex.codecogs.com/gif.latex?\theta%20%27%20=%20(\theta%20+%20\beta)%20mod%202%20\pi" />
