# Quaternion and spatial rotation

When used to represent rotation, unit quaternions are also called rotation quaternions. When used to represent an orientation, they are called orientation quaternions or attitude quaternions.

A Euclidean vector such as (2,3,4) can be rewritten as 2i+3j+4k. A rotation through an angle of <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta" style="border:none;"> around the axis defined by a unit vector:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cvec%7Bu%7D%3D%28u_x%2Cu_y%2Cu_z%29%3Du_xi+u_yj+u_zk" style="border:none;">

This is called axis-angle rotation:

The corresponding quaternion is:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=q=cos(\theta/2)%2bsin(\theta/2)u_xi%2bsin(\theta/2)u_yj%2bsin(\theta/2)u_zk" style="border:none;">

## Quaternions

Three imaginary numbers: i, j, k

<img src="http://chart.googleapis.com/chart?cht=tx&chl=i^2=-1,j^2=-1,k^2=-1,ij=k,jk=i,ki=j,ji=-k,kj=-i,ik=-j" style="border:none;">

<img src="http://chart.googleapis.com/chart?cht=tx&chl=q=s%2bxi%2byj%2bzk" style="border:none;">

s,x,y,z are scalars.

* Quaternions are not commutative!

<img src="http://chart.googleapis.com/chart?cht=tx&chl=q_1q_2\neq%20q_2q_1" style="border:none;">

However, the following holds:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=(q_1q_2)q_3=q_1(q_2q_3)" style="border:none;">

<img src="http://chart.googleapis.com/chart?cht=tx&chl=(q_1%2bq_2)q_3=q_1q_3%2bq_2q_3" style="border:none;">

l.e. all usual manipulations are valid, except cannot reverse multiolication order.

## Quaternion Properties

<img src="http://chart.googleapis.com/chart?cht=tx&chl=q=s%2bxi%2byj%2bzk" style="border:none;">

Norm:<img src="http://chart.googleapis.com/chart?cht=tx&chl=\left%20|%20q%20\right%20|^2=s^2%2bx^2%2by^2%2bz^2" style="border:none;">

Conjugate quaternion: <img src="http://chart.googleapis.com/chart?cht=tx&chl=\bar{q}=s-xi-yj-zk" style="border:none;">

Inverse quaternion: <img src="http://chart.googleapis.com/chart?cht=tx&chl=q^{-1}=\bar{q}/\left%20|%20q%20\right%20|%20^2" style="border:none;">

Unit quaternion:<img src="http://chart.googleapis.com/chart?cht=tx&chl=\left%20|%20q%20\right%20|%20=1" style="border:none;">

Inverse of unit quaternion: <img src="http://chart.googleapis.com/chart?cht=tx&chl=q^{-1}=\bar{q}" style="border:none;">

## Quaternions and rotations

* Rotations are represented by unit quaternions

* q = s + xi + yj + zk

  s^2+x^2+y^2+z^2=1

* Unit quaternion sphere (unit sphere in 4D)

## Unit Quaternions to rotations

* Let v be a (3-dim) vector and let q be a unit quaternion

* Then, the corresponding rotation transforms vector v to <img src="http://chart.googleapis.com/chart?cht=tx&chl=qvq^{-1}" style="border:none;">
