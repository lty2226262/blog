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

<img src="http://latex.codecogs.com/gif.latex?SO(n)={R}" >
