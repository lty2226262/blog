# 3D rigid body motion

## inner-product:

<img src="http://latex.codecogs.com/gif.latex?a\cdot%20b%20=%20a%20^%20T%20b%20=%20\sum_{i=1}^{3}a_ib_i=\mid%20a%20\mid%20\mid%20b%20\mid%20cos%3Ca,%20b%3E" >

inner-product could represent the projection between two vectors.

## outer-product:

<img src="http://latex.codecogs.com/gif.latex?a%5Ctimes%20b%3D%5Cbegin%7Bbmatrix%7D%20i%20%26%20j%20%26%20k%5C%5C%20a_1%20%26%20a_2%20%26%20a_3%5C%5C%20b_1%20%26b_2%20%26b_3%20%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%20a_2b_3-a_3b_2%5C%5C%20a_3b_1-a_1b_3%5C%5C%20a_1b_2-a_2b_1%20%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%200%20%26%20-a_3%20%26%20a_2%5C%5C%20a_3%20%26%200%20%26%20-a_1%5C%5C%20-a_2%20%26%20a_1%20%26%200%20%5Cend%7Bbmatrix%7D%20b%20%3D%20a%20%5Cwedge%20b" >

the direction of outer-product is perpendicular to these two vectors, the length is  <img src="http://latex.codecogs.com/gif.latex?\mid%20a\mid\mid%20b\mid%20sin<a,b>" >. we introduce a mark <img src="http://latex.codecogs.com/gif.latex?\wedge" >, and a is a matrix.

outer-product is only meaning to 3D vector. we could represent rotation with this.

## Euclidean transformation

define an orthonormal basis <img src="http://latex.codecogs.com/gif.latex?(e_1,e_2,e_3)" > rotate to <img src="http://latex.codecogs.com/gif.latex?(e'_1,e'_2,e'_3)" > and a fixed vector <img src="http://latex.codecogs.com/gif.latex?a" > (do not change along with the coordinate rotate). According to the coordination,

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20e_1%20%26e_2%20%26e_3%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20a_1%5C%5C%20a_2%5C%5C%20a_3%20%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%20e%27_1%20%26e%27_2%20%26e%27_3%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20a%27_1%5C%5C%20a%27_2%5C%5C%20a%27_3%20%5Cend%7Bbmatrix%7D" >

then left multiply <img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20e_1%5ET%5C%5C%20e_2%5ET%5C%5C%20e_3%5ET%20%5Cend%7Bbmatrix%7D" >, so the parameter becomes an identity , so:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20a_1%5C%5C%20a_2%5C%5C%20a_3%20%5Cend%7Bbmatrix%7D%3D%20%5Cbegin%7Bbmatrix%7D%20e_1%5ETe%27_1%20%26%20e_1%5ETe_2%27%20%26%20e_1%5ETe_3%27%5C%5C%20e_2%5ETe_1%27%20%26%20e_2%5ETe_2%27%20%26%20e_2%5ETe_3%27%5C%5C%20e_3%5ETe_1%27%20%26%20e_3%5ETe_2%27%20%26%20e_3%5ETe_3%27%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20a_1%27%5C%5C%20a_2%27%5C%5C%20a_3%27%20%5Cend%7Bbmatrix%7D%3DRa%27" >

R represent the rotation matrix. it is an orthogonal matrix (inverse equals to transposition)， and its determinant equals to 1.so:

<img src="http://latex.codecogs.com/gif.latex?SO%28n%29%3D%5C%7BR%5Cin%20%5Ctextsc%7BR%7D%5E%7Bn%20%5Ctimes%20n%7D%20%5Cmid%20RR%5ET%3DI%2Cdet%28R%29%3D1%5C%7D" >

SO(n) means Special Orthogonal Group. For example SO(3) means a 3D group. The rotation matrix could describe the rotation of cameras.

because rotation matrix is an orthogonal matrix, its transposition represents a inverse rotation. <img src="http://latex.codecogs.com/gif.latex?a%27%3DR%5E%7B-1%7Da%3DR%5ETa" >

Obviously, it describe a inverse rotation.

Besides, there's also translation in a rigid motion.

<img src="http://latex.codecogs.com/gif.latex?a'=Ra+t" >

##Transform Matrix and Homogeneous coordinates

so a->b->c:

<img src="http://latex.codecogs.com/gif.latex?b=R_1a+t_1,c=R_2b+t_2" >

<img src="http://latex.codecogs.com/gif.latex?c=R_2(R_1a+t_1)+t_2" >

This is too complex if we transform several times. So we use a trick in math:

<img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20a%27%5C%5C%201%20%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20R%20%26%20t%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20a%5C%5C%201%20%5Cend%7Bbmatrix%7D%3DT%5Cbegin%7Bbmatrix%7D%20a%5C%5C%201%20%5Cend%7Bbmatrix%7D" >

<img src="http://latex.codecogs.com/gif.latex?T" > is called transform matrix.

so when we normalize the last element to 1, we get the coordinate:

<img src="http://latex.codecogs.com/gif.latex?%5Cvec%7Bx%7D%3D%5Bx%2Cy%2Cz%2Cw%5D%5ET%3D%5Bx/w%2Cy/w%2Cz/w%2C1%5D%5ET" >

then the transformation becomes:

<img src="http://latex.codecogs.com/gif.latex?%5Cvec%7Bb%7D%3DT_1%5Cvec%7Ba%7D%2C%20%5Cvec%7Bc%7D%3DT_2%5Cvec%7Bb%7D%5CRightarrow%20%5Cvec%7Bc%7D%3DT_2T_1%5Cvec%7Ba%7D" >

As for the transformation matrix, it has a special structure: left-top is the rotation matrix, right-top is the translation vector, left-bottom is zero vector, right-bottom is 1. These matrixes are called Special Euclidean Group:

<img src="http://latex.codecogs.com/gif.latex?SE%283%29%3D%5Cbegin%7BBmatrix%7D%20T%3D%5Cbegin%7Bbmatrix%7D%20R%20%26t%20%5C%5C%200%5ET%20%261%20%5Cend%7Bbmatrix%7D%20%5Cin%20R%5E%7B4%20%5Ctimes%204%7D%20%5Cmid%20R%20%5Cin%20SO%283%29%2C%20t%20%5Cin%20R%5E3%20%5Cend%7BBmatrix%7D" >

The same as SO(3), its inverse means an opposite transformation.

## Rotation vector

rotation matrix has too many useless information, so we could replace this kind of expression with a more effective expression. Every rotation could be expressed with a rotation axis and a rotation angle. So we use a vector, whose direction is the rotation angle's direction and its length equals to the rotation angle. This vector is called rotation vector(or Axis-Angle)

In fact, the rotation vector is the Lie algebra. suppose a vector, the rotation axis is <img src="http://latex.codecogs.com/gif.latex?n" >, the rotation angle is <img src="http://latex.codecogs.com/gif.latex?\theta" >, obviously, its rotation vector is <img src="http://latex.codecogs.com/gif.latex?\theta%20n" >. we could transform rotation vector to rotation matrix by Rodrigues's Formula.:

 <img src="http://latex.codecogs.com/gif.latex?R%20%3D%20cos%5Ctheta%20I%20&plus;%20%281-cos%5Ctheta%20%29nn%5ET&plus;sin%5Ctheta%20n%20%5Cwedge" >

 <img src="http://latex.codecogs.com/gif.latex?%5Cwedge" > means the anti-symmetric matrix. Shown before at "outer-product"

Besides, for rotation angle  <img src="http://latex.codecogs.com/gif.latex?%5Ctheta" >:

<img src="http://latex.codecogs.com/gif.latex?tr(R)=cos\theta%20tr(I)+(1-cos\theta%20)tr(nn^T)+sin\theta%20tr(n\wedge)" >

<img src="http://latex.codecogs.com/gif.latex?=3cos\theta+(1-cos\theta)" >

<img src="http://latex.codecogs.com/gif.latex?=1+2cos\theta" >

Hence,

<img src="http://latex.codecogs.com/gif.latex?theta=arccos(\frac{tr(R)-1}{2})" >

the rotation n, because the vector at the rotation axis does not change when they rotate, so

<img src="http://latex.codecogs.com/gif.latex?Rn=n" >

##Eulerian angle

rotate three times, the most famous is the ZYX rotation

1. rotate by Z axis, get yaw

2. rotate by the after rotated Y axis, get pitch

3. rotate by the after rotated X axis, get roll

Its weakness: Gimbal Lock. when the pitch is <img src="http://latex.codecogs.com/gif.latex?%5Cpm%2090%5E%7B%5Ccirc%7D" >, the rotation axis of the 1th and 3rd is the same, so this kind of rotation will lose a freedom. So this kind of expression doesn't fit the iteration or interpolation.

## Quaternion

<img src="http://latex.codecogs.com/gif.latex?q=q_0+q_1i+q_2j+q_3k" >

q has one real part, 3 virtual part. And they are in the form of

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20i%5E2%3Dj%5E2%3Dk%5E2%3D-1%5C%5C%20ij%3Dk%2C%20ji%3D-k%5C%5C%20jk%3Di%2Ckj%3D-i%5C%5C%20ki%3Dj%2Cik%3D-j%20%5Cend%7Bmatrix%7D%5Cright." >

suppose a rotation is something rotate round an unit vector <img src="http://latex.codecogs.com/gif.latex?n=[n_x,n_y,n_z]^T" >,  the rotation angle is <img src="http://latex.codecogs.com/gif.latex?\theta" >, so the quaternion is:

<img src="http://latex.codecogs.com/gif.latex?q=[cos\frac{\theta}{2},n_xsin\frac{\theta}{2},n_ysin\frac{\theta}{2},n_zsin\frac{\theta}{2}]^T" >

otherwise, we could also compute the rotation angle and axis from the unit quaternion:

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20%5Ctheta%3D2arccosq_0%5C%5C%20%5Bn_x%2Cn_y%2Cn_z%5D%5ET%3D%5Bq_1%2Cq_2%2Cq_3%5D%5ET/sin%5Cfrac%7B%5Ctheta%7D%7B2%7D%20%5Cend%7Bmatrix%7D%5Cright." >

In quaternion, a rotation could be represented by a pair of opposite numbers. That is, when  <img src="http://latex.codecogs.com/gif.latex?\theta=0" >, we could get a quaternion without rotation:

<img src="http://latex.codecogs.com/gif.latex?q_0%3D%5B%5Cpm%201%2C%200%2C0%2C0%5D%5ET" >

## Quaternion Operation

### Plus and minus

<img src="http://latex.codecogs.com/gif.latex?q_a%5Cpm%20q_b%3D%5Bs_a%5Cpm%20s_b%2C%20v_a%5Cpm%20v_b%5D" >

### multiply

<img src="http://latex.codecogs.com/gif.latex?q_aq_b%3Ds_as_b-x_ax_b-y_ay_b-z_az_b%5C%5C%20&plus;%28s_ax_b&plus;x_as_b&plus;y_az_b-z_ay_b%29i%5C%5C%20&plus;%28s_ay_b&plus;x_az_b&plus;y_as_b&plus;z_ab_b%29j%5C%5C%20&plus;%28s_az_b&plus;x_ay_b-x_by_a&plus;z_as_b%29k" >

written in vector form:

<img src="http://latex.codecogs.com/gif.latex?q_aq_b%3D%5Bs_as_b-v_a%5ETv_b%2Cs_av_b&plus;s_bv_a&plus;v_a%5Ctimes%20v_b%5D" >

notice: quaternion multiply is noncommuting

### conjugate

<img src="http://latex.codecogs.com/gif.latex?q_a%5E*%3Ds_a-x_ai-y_aj-z_ak%3D%5Bs_a%2C-v_a%5D" >

a conjugate quaternion multiply itself will get a real quaternion:

<img src="http://latex.codecogs.com/gif.latex?q%5E*q%3Dqq%5E*%3D%5Bs_a%5E2&plus;v%5ETv%2C0%5D" >

### module length

<img src="http://latex.codecogs.com/gif.latex?%5Cleft%20%5C%7C%20q_a%20%5Cright%20%5C%7C%3D%5Csqrt%7Bs_a%5E2&plus;x_a%5E2&plus;y_a%5E2&plus;z_a%5E2%7D" >

we could verify that the product of two quaternions' module equals to the module of two quaternions' product.

 <img src="http://latex.codecogs.com/gif.latex?%5Cleft%20%5C%7C%20q_aq_b%20%5Cright%20%5C%7C%3D%5Cleft%20%5C%7C%20q_a%20%5Cright%20%5C%7C%5Cleft%20%5C%7C%20q_b%20%5Cright%20%5C%7C" >

 ### inverse

 the inverse of a quaternion equals to:

 <img src="http://latex.codecogs.com/gif.latex?q%5E%7B-1%7D%3Dq%5E*/%5Cleft%20%5C%7C%20q%20%5Cright%20%5C%7C%5E2" >

 So:

 <img src="http://latex.codecogs.com/gif.latex?qq^{-1}=q^{-1}q=1" >

 If q is an unit quaternion, its inverse and its conjugate have the same value. Besides,

  <img src="http://latex.codecogs.com/gif.latex?(q_aq_b)^{-1}=q^{-1}_bq_a^{-1}" >

### number product and dot product

number product:

  <img src="http://latex.codecogs.com/gif.latex?kq=[ks,kv]" >

dot product:

<img src="http://latex.codecogs.com/gif.latex?q_a%5Ccdot%20q_b%3Ds_as_b&plus;x_ax_bi&plus;y_ay_bj&plus;z_az_bk" >

##Represent rotation with quaternion

suppose a dot <img src="http://latex.codecogs.com/gif.latex?p=[x,y,z]\in%20R^3" > and a rotation represent by Axis-Angle <img src="http://latex.codecogs.com/gif.latex?n,\theta" >, from <img src="http://latex.codecogs.com/gif.latex?p" > rotate to <img src="http://latex.codecogs.com/gif.latex?p'" >, If described in matrix, then <img src="http://latex.codecogs.com/gif.latex?p'=Rp" >

First of all, we represent a 3D point with a virtual quaternion:

<img src="http://latex.codecogs.com/gif.latex?p=[0,x,y,z]=[0,v]" >

That is, we match 3 virtual parts with 3 axis. And we represent the rotation referred to Quaternion definition.

<img src="http://latex.codecogs.com/gif.latex?q=[cos\frac{\theta}{2},nsin\frac{\theta}{2}]" >

the <img src="http://latex.codecogs.com/gif.latex?p'" > could be represent as following:

<img src="http://latex.codecogs.com/gif.latex?p'=qpq^{-1}" >

## switch between quaternion and rotation matrixes

<img src="http://latex.codecogs.com/gif.latex?q=q_0+q_1i+q_2j+q_3k" >,and the rotation matrix is:

<img src="http://latex.codecogs.com/gif.latex?R%3D%5Cbegin%7Bbmatrix%7D%201-2q_2%5E2-2q_3%5E2%20%262q_1q_2&plus;2q_0q_3%20%26%202q_1q_3-2q_0q_2%5C%5C%202q_1q_2-2q_0q_3%20%26%201-2q_1%5E2-2q_3%5E2%20%26%202q_2q_3&plus;2q_0q_1%5C%5C%202q_1q_3&plus;2q_0q_2%20%26%202q_2q_3-2q_0q_1%20%26%201-2q_1%5E2-2q_2%5E2%20%5Cend%7Bbmatrix%7D" >

Otherwise, suppose the matrix <img src="http://latex.codecogs.com/gif.latex?R=\{m_{ij}\},i,j\in%20[1,2,3]" >

<img src="http://latex.codecogs.com/gif.latex?q_0=\frac{\sqrt{tr(R)+1}}{2}" >, <img src="http://latex.codecogs.com/gif.latex?q_1=\frac{m_23-m_32}{4q_0}" >,<img src="http://latex.codecogs.com/gif.latex?\frac{m_31-m_13}{4q_0}" >,<img src="http://latex.codecogs.com/gif.latex?\frac{m_12-m_21}{4q_0}" >

To be mentioned, q and -q represent the same rotation so the result of computing quaternion from a rotation matrix R is not unique.

## Similarity transformation, Affine transformation, Projective transformation

<table border="1">
<tr>
<th>Transformation name</th>
<th>Transformation matrix</th>
<th>DOF</th>
<th>unchangable property</th>
</tr>
<tr>
<td>Euclidean transformation</td>
<td><img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20R%20%26%20t%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D" ></td>
<td>6 DOF</td>
<td>length, angle, volume</td>
</tr>
<tr>
<td>Similarity transformation</td>
<td><img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20sR%20%26%20t%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D" ></td>
<td>7 DOF</td>
<td>volume ratio</td>
</tr>
<tr>
<td>Affine transformation</td>
<td><img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20A%20%26%20t%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D" ></td>
<td>12 DOF</td>
<td>parallelism, volume ratio</td>
</tr>
<tr>
<td>Projective transformation</td>
<td><img src="http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20A%20%26%20t%5C%5C%20a%5ET%20%26%20v%20%5Cend%7Bbmatrix%7D" ></td>
<td>15 DOF</td>
<td>Intersection and tangency of contact surface</td>
</tr>
</table>
