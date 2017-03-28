# Lie Group

## Intro

3D rotation matrixes comprise Special Orthogonal Group SO(3), and the transformation matrixes comprise the Special Euclidean Group SE(3):

<img src="http://latex.codecogs.com/gif.latex?SO%283%29%3D%5C%7BR%5Cin%20R%5E%7B3%5Ctimes%203%7D%5Cmid%20RR%5ET%3DI%2Cdet%28R%29%3D1%5C%7D">

<img src="http://latex.codecogs.com/gif.latex?SE%283%29%3D%5Cleft%20%5C%7B%20T%3D%5Cbegin%7Bbmatrix%7D%20R%20%26%20t%20%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D%5Cin%20R%5E%7B4%5Ctimes%204%7D%5Cmid%20R%20%5Cin%20SO%283%29%2C%20t%20%5Cin%20R%5E3%20%5Cright%20%5C%7D">

suppose two rotation matrixes <img src="http://latex.codecogs.com/gif.latex?R_1,R_2">,

<img src="http://latex.codecogs.com/gif.latex?R_1+R_2\notin%20SO(3)">

however, when we multiply these two rotation matrixes,

<img src="http://latex.codecogs.com/gif.latex?R_1R_2\in%20SO(3),T_1T_2\in%20SE(3)">

we call these sets which only have one operation Group.

### Group

#### Closure

For all a, b in G, the result of the operation, a<img src="http://latex.codecogs.com/gif.latex?\cdot">b, is also in G.

#### Associativity

For all a, b and c in G, (a<img src="http://latex.codecogs.com/gif.latex?\cdot">b)<img src="http://latex.codecogs.com/gif.latex?\cdot">c=a<img src="http://latex.codecogs.com/gif.latex?\cdot">(b<img src="http://latex.codecogs.com/gif.latex?\cdot">c)

#### Identity element

There exists an element e in G such that, for every element a in G, the equation e<img src="http://latex.codecogs.com/gif.latex?\cdot">a=a<img src="http://latex.codecogs.com/gif.latex?\cdot">e=a holds. Such an element is unique, and thus one speaks of the identity element.

#### Inverse element

For each a in G, there exists an element b in G, commonly denoted <img src="http://latex.codecogs.com/gif.latex?a^{-1}"> (or -a, if the operation is denoted "+"), such that a<img src="http://latex.codecogs.com/gif.latex?\cdot">b = b<img src="http://latex.codecogs.com/gif.latex?\cdot">a = e, where e is the identity element.

a Lie group is a group that is also a differentiable manifold, with the property that the group operations are compatible with the smooth structure.

### Lie algebra basic

consider any rotation matrixes R, we know that:

<img src="http://latex.codecogs.com/gif.latex?RR^T=I">

R is the rotation of a camera, is a function of time: R(t). because R(t) is still a rotation matrix, so:

<img src="http://latex.codecogs.com/gif.latex?R(t)R(t)^T=I">

when differentiate with respect to time, we could get:

<img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%28t%29%7DR%28t%29%5ET&plus;R%28t%29%5Cdot%7BR%28t%29%7D%5ET%3D0">

to conclude:

<img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%28t%29%7DR%28t%29%5ET%3D-%28%5Cdot%7BR%28t%29%7DR%28t%29%5ET%29%5ET">

so <img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%28t%29%7DR%28t%29%5ET"> is an antisymmetric matrix, when we introduce an inner product, we introduce the character <img src="http://latex.codecogs.com/gif.latex?%5Cwedge">, this character could make a vector an antisymmetric matrix. At the same time, we could find a vector matching an antisymmetric matrix. We introduce the character <img src="http://latex.codecogs.com/gif.latex?%5Cvee">

<img src="http://latex.codecogs.com/gif.latex?a%5E%20%5Cwedge%20%3DA%3D%5Cbegin%7Bbmatrix%7D%200%20%26%20-a_3%20%26%20a_2%20%5C%5C%20a_3%20%26%200%26-a_1%20%5C%5C%20-a_2%20%26%20a_1%20%26%200%20%5Cend%7Bbmatrix%7D%2C%20A%5E%5Cvee%20%3Da">

Hence, we could find a 3D vector <img src="http://latex.codecogs.com/gif.latex?%5Cphi%20%28t%29"> that matches the antisymmetric matrix <img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%28t%29%7DR%28t%29%5ET">:

<img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%28t%29%7DR%28t%29%5ET%3D%5Cphi%20%28t%29%20%5E%20%5Cwedge">

we right multiply <img src="http://latex.codecogs.com/gif.latex?R%28t%29">, becuase R is an orthogonal matrix, so:

<img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%28t%29%7D%3D%5Cphi%20%28t%29%5E%20%5Cwedge%20R%28t%29%3D%5Cbegin%7Bbmatrix%7D%200%20%26-%5Cphi%20_3%20%26%5Cphi%20_2%20%5C%5C%20%5Cphi%20_3%20%26%200%20%26%20-%5Cphi%20_1%20%5C%5C%20-%5Cphi%20_2%20%26%5Cphi%20_1%20%26%200%20%5Cend%7Bbmatrix%7DR%28t%29">

As we see, when we derivate a rotation matrix, we should just left multiply a matrix <img src="http://latex.codecogs.com/gif.latex?%5Cphi%20%28t%29%5E%20%5Cwedge">. To simplify, we suppose <img src="http://latex.codecogs.com/gif.latex?t_0%3D0">, and the rotation matrix is <img src="http://latex.codecogs.com/gif.latex?R%280%29%3DI">. By the definition, we could Taylor expansion the R(t) at 0:

<img src="http://latex.codecogs.com/gif.latex?R%28t%29%5Capprox%20R%28t_0%29&plus;%5Cdot%7BR%28t_0%29%7D%28t-t_0%29%5C%5C%20%3DI&plus;%5Cphi%20%28t_0%29%5E%5Cwedge%20%28t%29">

we could see that <img src="http://latex.codecogs.com/gif.latex?\phi"> represent R's derivation at the original point, so we call it's on the Tangent Space at the original point. We suppose that near <img src="http://latex.codecogs.com/gif.latex?t_0">, <img src="http://latex.codecogs.com/gif.latex?%5Cphi"> is a constant <img src="http://latex.codecogs.com/gif.latex?%5Cphi%28t_0%29%20%3D%20%5Cphi%20_0">, so:

<img src="http://latex.codecogs.com/gif.latex?%5Cdot%7BR%7D%28t%29%20%3D%20%5Cphi%28t_0%29%5E%5Cwedge%20R%28t%29%20%3D%20%5Cphi%20_0%20%5E%20%5Cwedge%20R%28t%29">

The equation above is a differential equation, to solve it, we could get:

<img src="http://latex.codecogs.com/gif.latex?R(t)=exp(\phi%20_0^\wedge%20t)">

### Lie algebra definition

A Lie algebra is a vector space <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bg%7D" > over some field <img src="http://latex.codecogs.com/gif.latex?F"> together with a binary operation <img src="http://latex.codecogs.com/gif.latex?%5B%5Ccdot%2C%5Ccdot%5D%3A%5Cmathfrak%7Bg%5Ctimes%20g%5Crightarrow%20g%7D"> called the Lie bracket that satisfies the following axioms:

#### Bilinearity

<img src="http://latex.codecogs.com/gif.latex?%5Bax&plus;by%2Cz%5D%3Da%5Bx%2Cz%5D&plus;b%5By%2Cz%5D%2C%5Bz%2Cax&plus;by%5D%3Da%5Bz%2Cx%5D&plus;b%5Bz%2Cy%5D">

for all scalars a,b in F and all elements x,y,z in <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bg%7D">

#### Alternativity

<img src="http://latex.codecogs.com/gif.latex?%5Bx%2Cx%5D%3D0">

for all x in <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bg%7D">.

#### The Jacobi identity

<img src="http://latex.codecogs.com/gif.latex?%5Bx%2C%5By%2Cz%5D%5D&plus;%5Bz%2C%5Bx%2Cy%5D%5D&plus;%5By%2C%5Bz%2Cx%5D%5D%3D0">

for all x, y, z in <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bg%7D">.

Using bilinearity to expand the Lie bracket [x+y, x+y] and using alternativity shows that [x, y]+[y, x]=0 for all elements x, y in <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bg%7D">, showing that bilinearity and alternativity together imply

#### anticommutativity

[x,y] = -[y,x],

for all elements x,y in <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bg%7D">. If the field's characteristic is not 2 then anticommutativity implies alternativity.

### Lie algebra <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso(3)%7D">

SO(3) matches the Lie Algebra, it's defined in <img src="http://latex.codecogs.com/gif.latex?R^3">, we describe it as <img src="http://latex.codecogs.com/gif.latex?\phi">. Described above, every <img src="http://latex.codecogs.com/gif.latex?\phi"> could generate an antisymmetric matrix:

<img src="http://latex.codecogs.com/gif.latex?%5CPhi%20%3D%5Cphi%20%5E%20%5Cwedge%20%3D%20%5Cbegin%7Bbmatrix%7D%200%20%26%20-%5Cphi%20_3%20%26%20%5Cphi%20_2%20%5C%5C%20%5Cphi%20_3%20%26%200%20%26%20-%5Cphi%20_1%20%5C%5C%20-%5Cphi%20_2%20%26%20%5Cphi%20_%201%20%26%200%20%5Cend%7Bbmatrix%7D%5Cin%20R%20%5E%20%7B3%20%5Ctimes%203%7D">

By this definition, the Lie bracket of <img src="http://latex.codecogs.com/gif.latex?\phi_1,\phi_2"> is :

<img src="http://latex.codecogs.com/gif.latex?%5B%5Cphi%20_1%2C%20%5Cphi%20_2%5D%3D%28%5CPhi%20_1%20%5CPhi%20_2%20-%20%5CPhi%20_2%20%5CPhi%20_%201%29%20%5E%20%5Cvee">

we say that the elements of <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D"> are 3d vectors or 3d antisymmetric matrixes:

<img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D%3D%5C%7B%5Cphi%20%5Cin%20R%20%5E3%2C%20%5CPhi%20%3D%20%5Cphi%20%5E%20%5Cwedge%20%5Cin%20R%20%5E%7B3%20%5Ctimes%203%7D%5C%7D">

### Lie Algebra <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse(3)%7D">

As for SE(3), it also has Lie Algebra <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse(3)%7D">. <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse(3)%7D"> is in the <img src="http://latex.codecogs.com/gif.latex?R^6"> space:

<img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D%3D%5Cleft%20%5C%7B%20%5Cxi%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Crho%20%5C%5C%20%5Cphi%20%5Cend%7Bbmatrix%7D%20%5Cin%20R%20%5E%206%2C%5Crho%20%5Cin%20R%20%5E%203%2C%20%5Cphi%20%5Cin%20%5Cmathfrak%7Bso%283%29%20%7D%2C%20%5Cxi%20%5E%20%5Cwedge%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cphi%20%5E%20%5Cwedge%20%26%20%5Crho%20%5C%5C%200%5ET%20%26%200%20%5Cend%7Bbmatrix%7D%20%5Cin%20R%20%5E%7B4%5Ctimes%204%7D%20%5Cright%20%5C%7D">

we note every <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D"> element as <img src="http://latex.codecogs.com/gif.latex?%5Cxi">, it is a 6D vector. Former 3 are translation component<img src="http://latex.codecogs.com/gif.latex?%5Crho">, later 3 are rotation component<img src="http://latex.codecogs.com/gif.latex?%5Cphi">. At the same time, we expand the meaning of <img src="http://latex.codecogs.com/gif.latex?%5E%5Cwedge">. In <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D"> we convert a 6D vector to a 4D matrix using <img src="http://latex.codecogs.com/gif.latex?%5E%5Cwedge">, but it doesn't represent antisymmetric here.

<img src="http://latex.codecogs.com/gif.latex?%5Cxi%20%5E%5Cwedge%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cphi%20%5E%5Cwedge%20%26%20%5Crho%5C%5C%200%5ET%20%260%20%5Cend%7Bbmatrix%7D%20%5Cin%20R%20%5E%7B4%5Ctimes%204%7D">

At the same time, Lie algebra <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D"> also have the Lie bracket similar to <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D">:
<img src="http://latex.codecogs.com/gif.latex?%5B%5Cxi%20_1%2C%20%5Cxi%20_2%5D%3D%28%5Cxi%20_1%20%5E%20%5Cwedge%20%5Cxi%20_2%20%5E%5Cwedge%20-%20%5Cxi%20_2%20%5E%5Cwedge%20%5Cxi%20_1%20%5E%5Cwedge%29%5E%20%5Cvee">

## Exponent and Exponential Map

### The exponential map of SO(3)

How do we compute <img src="http://latex.codecogs.com/gif.latex?exp%28%5Cphi%20%5E%5Cwedge%29">? It is an exponential Map. At the same time, we will talk about the exponential map of <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D">first. Then talking about <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D">.

For a matrix, we could make a taylor expansion when using them, to make sense, this exponent must be convergent.

<img src="http://latex.codecogs.com/gif.latex?exp%28%5Cphi%20%5E%20%5Cwedge%29%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%20%7D%5Cfrac%7B1%7D%7Bn%21%7D%28%5Cphi%20%5E%20%5Cwedge%29%5En">

As for <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D">, we could get the exponential map:

<img src="http://latex.codecogs.com/gif.latex?exp%28%5Cphi%20%5E%5Cwedge%29%3D%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%20%7D%5Cfrac%7B1%7D%7Bn%21%7D%28%5Cphi%20%5E%5Cwedge%29%5En">

Due to <img src="http://latex.codecogs.com/gif.latex?%5Cphi"> is a 3D vector, so we introduce a module length <img src="http://latex.codecogs.com/gif.latex?%5Ctheta"> and a direction a, so <img src="http://latex.codecogs.com/gif.latex?%5Cphi%20%3D%20%5Ctheta%20a">. a is an unit vector whose length is 1. First of all, as for <img src="http://latex.codecogs.com/gif.latex?a%20%5E%20%5Cwedge">:

<img src="http://latex.codecogs.com/gif.latex?a%5E%5Cwedge%20a%5E%5Cwedge%20%3Daa%5ET%20-%20I">

and

<img src="http://latex.codecogs.com/gif.latex?a%5E%5Cwedge%20a%5E%5Cwedge%20a%5E%5Cwedge%20%3D%20-a%5E%5Cwedge">

using these two properties, we could conclude that:

<img src="http://latex.codecogs.com/gif.latex?exp%28%5Cphi%20%5E%5Cwedge%29%3Dexp%28%5Ctheta%20a%5E%5Cwedge%29%3D%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%20%7D%5Cfrac%7B1%7D%7Bn%21%7D%28%5Ctheta%20a%20%5E%5Cwedge%29%5En%5C%5C%20%3DI&plus;%5Ctheta%20a%5E%5Cwedge%20&plus;%20%5Cfrac%7B1%7D%7B2%21%7D%5Ctheta%20%5E2%20a%20%5E%5Cwedge%20a%20%5E%5Cwedge%20&plus;%20%5Cfrac%7B1%7D%7B3%21%7D%5Ctheta%20%5E3%20a%20%5E%5Cwedge%20a%20%5E%5Cwedge%20a%20%5E%5Cwedge%20&plus;%20%5Cfrac%7B1%7D%7B4%21%7D%5Ctheta%20%5E4%28a%5E%5Cwedge%29%5E4&plus;...%5C%5C%20%3Daa%5ET-a%5E%5Cwedge%20a%5E%5Cwedge%20&plus;%5Ctheta%20a%5E%5Cwedge%20&plus;%20%5Cfrac%7B1%7D%7B2%21%7D%5Ctheta%20%5E2%20a%20%5E%5Cwedge%20a%20%5E%5Cwedge%20-%20%5Cfrac%7B1%7D%7B3%21%7D%5Ctheta%20%5E3%20a%20%5E%5Cwedge%20-%20%5Cfrac%7B1%7D%7B4%21%7D%5Ctheta%20%5E4%28a%20%5E%5Cwedge%29%5E2&plus;...%5C%5C%20%3Daa%5ET%20&plus;%20%28%5Ctheta%20-%20%5Cfrac%7B1%7D%7B3%21%7D%5Ctheta%20%5E3%20&plus;%20%5Cfrac%7B1%7D%7B5%21%7D%5Ctheta%20%5E5-...%29a%5E%5Cwedge-%281-%5Cfrac%7B1%7D%7B2%21%7D%5Ctheta%20%5E2&plus;%5Cfrac%7B1%7D%7B4%21%7D%5Ctheta%20%5E4-...%29a%5E%5Cwedge%20a%5E%5Cwedge%5C%5C%20%3Da%5E%5Cwedge%20a%5E%5Cwedge%20&plus;%20I%20&plus;sin%20%5Ctheta%20a%5E%20%5Cwedge%20-%20cos%20%5Ctheta%20a%5E%5Cwedge%20a%5E%5Cwedge%5C%5C%20%3D%281-cos%20%5Ctheta%29a%5E%5Cwedge%20a%5E%5Cwedge%20&plus;%20I%20&plus;sin%5Ctheta%20a%5E%5Cwedge%5C%5C%20%3Dcos%5Ctheta%20I%20&plus;%20%281-cos%20%5Ctheta%29aa%5ET&plus;sin%5Ctheta%20a%5E%5Cwedge">

This equation is the same as Rodrigues rotation equation. By this equation, we could convert any vector in <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D"> to a rotation matrix in SO(3). Otherwise, if we define the log map, we could convert an element in SO(3) to <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bso%283%29%7D">:

<img src="http://latex.codecogs.com/gif.latex?%5Cphi%20%3D%20ln%28R%29%20%5E%20%5Cvee%20%3D%20%28%5Csum_%7B%5Cinfty%20%7D%5E%7Bn%3D0%7D%5Cfrac%7B%28-1%29%5En%7D%7Bn&plus;1%7D%28R-I%29%5E%7Bn&plus;1%7D%29%5E%5Cvee">

### the exponential map in SE(3)

<img src="http://latex.codecogs.com/gif.latex?exp%28%5Cxi%20%5E%5Cwedge%29%3D%5Cbegin%7Bbmatrix%7D%20%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%20%7D%5Cfrac%7B1%7D%7Bn%21%7D%28%5Cphi%20%5E%5Cwedge%29%5En%20%26%20%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%20%7D%5Cfrac%7B1%7D%7B%28n&plus;1%29%21%7D%28%5Cphi%20%5E%5Cwedge%29%5En%20%5Crho%20%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D%5C%5C%20%3D%5Cbegin%7Bbmatrix%7D%20R%20%26%20J%20%5Crho%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D%3DT">

The left-top element of <img src="http://latex.codecogs.com/gif.latex?%5Cxi">is R, which is the same as SO(3), and matches the rotation component <img src="http://latex.codecogs.com/gif.latex?%5Cphi"> of <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D">. And the right-top element of J is:

<img src="http://latex.codecogs.com/gif.latex?J%3D%5Cfrac%7Bsin%5Ctheta%7D%7B%5Ctheta%7DI&plus;%281-%5Cfrac%7Bsin%5Ctheta%7D%7B%5Ctheta%7D%29aa%5ET&plus;%5Cfrac%7B1-cos%5Ctheta%7D%7B%5Ctheta%7Da%5E%7B%5Cwedge%7D">

Similar to Rodrigues, but not the same.

The relationship of Lie Group and Lie Algebra shown below:

<img src="https://github.com/lty2226262/blog/blob/master/MarkdownPhotos/vslam_chap4_1.png?raw=true">

## Lie Algebra Derivation

### BCH function and approximate formula

The product of two lie algebras is given by Baker-campbell-hausdorff(BCH formula), becuase this formula is too complicated, so we just give the former components:

<img src="http://latex.codecogs.com/gif.latex?ln%28exp%28A%29exp%28B%29%29%3DA&plus;B&plus;%5Cfrac%7B1%7D%7B2%7D%5BA%2CB%5D&plus;%5Cfrac%7B1%7D%7B12%7D%5BA%2C%5BA%2CB%5D%5D-%5Cfrac%7B1%7D%7B12%7D%5BB%2C%5BA%2CB%5D%5D&plus;...">

[]is Lie bracket, especially, when we consider Lie Algebra on SO(3) <img src="http://latex.codecogs.com/gif.latex?ln%28exp%28%5Cphi%20%5E%5Cwedge%29exp%28%5Cphi%20%5E%5Cwedge%29%29%5E%5Cvee%20%5Capprox%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20J_l%28%5Cphi%20_2%29%5E%7B-1%7D%5Cphi%20_1%20&plus;%20%5Cphi%20_2%2C%20%5C%3B%20if%5C%3B%20%5Cphi%20_1%5C%3B%20is%5C%3B%20small%5C%5C%20J_r%28%5Cphi%20_1%29%5E%7B-1%7D%5Cphi%20_2%20&plus;%20%5Cphi%20_1%2C%20%5C%3B%20if%5C%3B%20%5Cphi%20_2%5C%3B%20is%5C%3B%20small%20%5Cend%7Bmatrix%7D%5Cright.">

This formula tells us that if we left multiply a small rotation matrix <img src="http://latex.codecogs.com/gif.latex?R_1"> (Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cphi%20_1">) to a rotation matrix <img src="http://latex.codecogs.com/gif.latex?R_2"> (Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cphi%20_2">), we could approximately treat them as we add a <img src="http://latex.codecogs.com/gif.latex?J_l%28%5Cphi%20_2%29%5E%7B-1%7D%5Cphi%20_1"> to the original Lie algebra <img src="http://latex.codecogs.com/gif.latex?%5Cphi%20_2">.

If we left multiply BCH we could get the approximate Jacobi:

<img src="http://latex.codecogs.com/gif.latex?J_l%3DJ%3D%20%5Cfrac%7Bsin%5Ctheta%7D%7B%5Ctheta%7DI&plus;%281-%5Cfrac%7Bsin%5Ctheta%7D%7B%5Ctheta%7D%29aa%5ET&plus;%5Cfrac%7B1-cos%5Ctheta%7D%7B%5Ctheta%7Da%5E%5Cwedge">

Its inverse is:

<img src="http://latex.codecogs.com/gif.latex?J_l%5E%7B-1%7D%3D%5Cfrac%7B%5Ctheta%7D%7B2%7Dcot%5Cfrac%7B%5Ctheta%7D%7B2%7DI&plus;%281-%5Cfrac%7B%5Ctheta%7D%7B2%7Dcot%5Cfrac%7B%5Ctheta%7D%7B2%7D%29aa%5ET-%5Cfrac%7B%5Ctheta%7D%7B2%7Da%5E%5Cwedge">

when we right multiply Jacobi we should just negate the independent variables:

<img src="http://latex.codecogs.com/gif.latex?J_r%28%5Cphi%29%3DJ_l%28-%5Cphi%29">

suppose a rotation R, its Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cphi">. when we left multiply a small rotation, denoted as <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20R">, and its Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20%5Cphi">. Then on Lie group, we could get the result <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20R%20%5Ccdot%20R">, and on Lie algebra, due to BCH approximate, we could get the result is <img src="http://latex.codecogs.com/gif.latex?J_l%5E%7B-1%7D%28%5Cphi%29%5CDelta%20%5Cphi%20&plus;%20%5Cphi">. To conclude, we could get the result:

<img src="http://latex.codecogs.com/gif.latex?exp%28%5CDelta%5Cphi%20%5E%5Cwedge%29exp%28%5Cphi%20%5E%5Cwedge%29%3Dexp%28%28%5Cphi%20&plus;%20J_l%5E%7B-1%7D%28%5Cphi%29%5CDelta%20%5Cphi%29%5E%5Cwedge%29">

On contrary, we could do addition on Lie algebra, and let a <img src="http://latex.codecogs.com/gif.latex?%5Cphi"> add <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20%5Cphi">, then we could approximately left or right Jacobi multiply on Lie Group:

 <img src="http://latex.codecogs.com/gif.latex?exp%28%28%5Cphi%20&plus;%20%5CDelta%20%5Cphi%29%5E%5Cwedge%29%20%3D%20exp%28%28J_l%5CDelta%20%5Cphi%29%5E%5Cwedge%29exp%28%5Cphi%20%5E%5Cwedge%29%3Dexp%28%5Cphi%20%5E%20%5Cwedge%20%29exp%28%28J_r%5CDelta%20%5Cphi%29%5E%5Cwedge%29">

 As for SE(3), there exists BCH approximate formula:

 <img src="http://latex.codecogs.com/gif.latex?exp%28%5CDelta%20%5Cxi%20%5E%5Cwedge%29exp%28%5Cxi%20%5E%5Cwedge%29%5Capprox%20exp%28%28%5Ctau_l%5E%7B-1%7D%5CDelta%5Cxi%20&plus;%20%5Cxi%20%29%5E%5Cwedge%29%2C%20%5C%5C%20exp%28%5Cxi%20%5E%5Cwedge%29exp%28%5CDelta%20%5Cxi%5E%5Cwedge%29%5Capprox%20exp%28%28%5Ctau_r%5E%7B-1%7D%5CDelta%5Cxi&plus;%5Cxi%29%5E%5Cwedge%29">

 <img src="http://latex.codecogs.com/gif.latex?%5Ctau%20_l"> is a <img src="http://latex.codecogs.com/gif.latex?6%5Ctimes%206"> matrix. we don't introduce it in detail because we don't use them in computation.

 ### SO(3) Lie Algebra derivate

 On SLAM, we should estimate the position and orientation of a camera, this pose is described by the SO(3) or SE(3). Suppose the pose of robot is T. It watches a point whose ordinate in the world is p, and its observed measurement is z. Hence, due to ordinate transformation relationship, we could get:

 <img src="http://latex.codecogs.com/gif.latex?z%3DTp&plus;w">

 Because of the noise w, z could not be described exactly by <img src="http://latex.codecogs.com/gif.latex?z%3DTp">. So we could get the error of observation and the actual data:

 <img src="http://latex.codecogs.com/gif.latex?e%3Dz-Tp">

 suppose we have a number of N such landmarks or observations, so we have N formulas above. Then we could get the best estimation of T, which could minimize the global error:

 <img src="http://latex.codecogs.com/gif.latex?min_TJ%28T%29%3D%5Csum_%7Bi%3D1%7D%5E%7BN%7D%5Cleft%20%5C%7C%20z_i-Tp_i%20%5Cright%20%5C%7C_2%5E2">

 To solve this problem, we should differentiating the target J with respect to T. We should usually build the function with regard to the pose, and discuss the differentiating of this function with respect to the pose to adjust current estimation. However, SO(3) and SE(3) don't define the addition very well because we must consider the constrains. However, when we transform them to Lie algebra, so they have a good addition operation. Hence, to solve the differentiating problem we have two solution methods:

 1. We represent pose with Lie Algebra, and compute the derivation according to the Lie Algebra addition.

 2. Left or right multiply a small perturbation to the Lie group, and then compute the derivation of this perturbation, it's called left perturbation or right perturbation module.

### Lie algebra derivation

First of all, consider the situation of SO(3). Suppose we rotate a spatial point p, then get Rp. Now, we should compute the derivation with respect to the rotation after rotation, we could note it informally:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%28Rp%29%7D%7B%5Cpartial%20R%7D">

Because that SO(3) don't have the addition operation, so we couldn't compute this derivation according to the definition of the derivation. Suppose <img src="http://latex.codecogs.com/gif.latex?%5Cphi"> is the corresponding Lie algebra of R. so we turn to compute:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%28exp%28%5Cphi%20%5E%5Cwedge%29p%29%7D%7B%5Cpartial%20%5Cphi%7D">

According to the definition of derivation:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%28exp%28%5Cphi%20%5E%5Cwedge%29p%29%7D%7B%5Cpartial%20%5Cphi%7D%3Dlim_%7B%5Cdelta%20%5Cphi%20%5Crightarrow%200%7D%5Cfrac%7Bexp%28%28%5Cphi&plus;%5Cdelta%20%5Cphi%29%5E%5Cwedge%29p-exp%28%5Cphi%20%5E%5Cwedge%29p%7D%7B%5Cdelta%20%5Cphi%7D%5C%5C%20%3Dlim_%7B%5Cdelta%20%5Cphi%20%5Crightarrow%200%7D%5Cfrac%7Bexp%28%28J_l%5Cdelta%20%5Cphi%29%5E%5Cwedge%29%20exp%28%5Cphi%20%5E%5Cwedge%29p-exp%28%5Cphi%20%5E%5Cwedge%29p%7D%7B%5Cdelta%20%5Cphi%7D%5C%5C%20%5Capprox%20lim_%7B%5Cdelta%20%5Cphi%20%5Crightarrow%200%7D%5Cfrac%7B%28I&plus;%28J_l%5Cdelta%20%5Cphi%29%5E%5Cwedge%29exp%28%5Cphi%20%5E%20%5Cwedge%29p-exp%28%5Cphi%20%5E%5Cwedge%29p%7D%7B%5Cdelta%5Cphi%7D%5C%5C%20%3Dlim_%7B%5Cdelta%20%5Cphi%20%5Crightarrow%200%7D%5Cfrac%7B%28J_l%5Cdelta%5Cphi%29%5E%5Cwedge%20exp%28%5Cphi%20%5E%5Cwedge%29p%7D%7B%5Cdelta%20%5Cphi%7D%5C%5C%20%3Dlim_%7B%5Cdelta%20%5Cphi%20%5Crightarrow%200%7D%5Cfrac%7B-%28exp%28%5Cphi%20%5E%5Cwedge%29p%29%5E%5Cwedge%20J_l%20%5Cdelta%20%5Cphi%7D%7B%5Cdelta%5Cphi%7D%3D-%28Rp%29%5E%5Cwedge%20J_l">

The second line is approximately BCH linear transformation, the third line is the approximately Taylor expansion and round the higher order components. The fourth line and fifth line could be considered as a cross product and after transformation we change the sign. Hence, we get the derivation of the rotated point with respect to Lie algebra:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%28Rp%29%7D%7B%5Cpartial%5Cphi%7D%3D%28-Rp%29%5E%5Cwedge%20J_l">

but this also contains a complicated <img src="http://latex.codecogs.com/gif.latex?J_l"> , which is difficult to compute.

## Perturbation model(left multiply)

Another method of computing the derivation is to make a small perturbation to the rotation. This perturbation could be left multiply of right multiply, the result could be a little bit different, now we take the left multiply for instance. Suppose the left perturbation <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20R">'s corresponding Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cvarphi">. Then, compute the derivation with respect to <img src="http://latex.codecogs.com/gif.latex?%5Cvarphi">:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%28Rp%29%7D%7B%5Cpartial%20%5Cvarphi%7D%3Dlim_%7B%5Cvarphi%20%5Crightarrow%200%7D%5Cfrac%7Bexp%28%5Cvarphi%20%5E%5Cwedge%29exp%28%5Cphi%20%5E%5Cwedge%29p-exp%28%5Cphi%20%5E%5Cwedge%29p%7D%7B%5Cvarphi%7D">

To compute the derivation of this formula is easier:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%28Rp%29%7D%7B%5Cpartial%20%5Cvarphi%7D%3Dlim_%7B%5Cvarphi%20%5Crightarrow%200%7D%5Cfrac%7Bexp%28%5Cvarphi%20%5E%5Cwedge%29exp%28%5Cphi%20%5E%5Cwedge%29p-exp%28%5Cphi%20%5E%5Cwedge%29p%7D%7B%5Cvarphi%7D%20%5C%5C%20%5Capprox%20lim_%7B%5Cvarphi%20%5Crightarrow%200%7D%5Cfrac%7B%281&plus;%5Cvarphi%20%5E%5Cwedge%29exp%28%5Cphi%20%5E%5Cwedge%29p-exp%28%5Cphi%20%5E%20%5Cwedge%29p%7D%7B%5Cvarphi%7D%5C%5C%20%3Dlim_%7B%5Cvarphi%20%5Crightarrow%200%7D%5Cfrac%7B%5Cvarphi%20%5E%5Cwedge%20Rp%7D%7B%5Cvarphi%7D%3Dlim_%7B%5Cvarphi%20%5Crightarrow%200%7D%5Cfrac%7B-%28Rp%29%5E%5Cwedge%20%5Cvarphi%7D%7B%5Cvarphi%7D%3D-%28Rp%29%5E%5Cwedge">

## Lie algebra derivate on SE(3)

At last, we give the perturbation model of SE(3), suppose a spatial point p make a transformation T(whose lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cxi">), and get Tp. Now, give a left multiply perturbation to T, <img src="http://latex.codecogs.com/gif.latex?%5CDelta%20T%20%3D%20exp%28%5Cdelta%20%5Cxi%20%5E%20%5Cwedge%29">, and suppose the perturbation Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cdelta%20%5Cxi%20%3D%20%5B%5Cdelta%20%5Crho%2C%20%5Cdelta%5Cphi%5D%5ET">, and then:

<img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%28Tp%29%7D%7B%5Cpartial%20%5Cdelta%20%5Cxi%7D%3Dlim_%7B%5Cdelta%5Cxi%20%5Crightarrow%200%7D%20%5Cfrac%7Bexp%28%5Cdelta%20%5Cxi%20%5E%5Cwedge%29exp%28%5Cxi%20%5E%5Cwedge%29p-exp%28%5Cxi%20%5E%5Cwedge%29p%7D%7B%5Cdelta%20%5Cxi%7D%5C%5C%20%5Capprox%20lim_%7B%5Cdelta%5Cxi%20%5Crightarrow%200%7D%20%5Cfrac%7B%28I&plus;%5Cdelta%5Cxi%20%5E%5Cwedge%29exp%28xi%20%5E%5Cwedge%29p-exp%28%5Cxi%20%5E%5Cwedge%29p%20%7D%7B%5Cdelta%20%5Cxi%7D%5C%5C%20%3D%20lim_%7B%5Cdelta%20%5Cxi%20%5Crightarrow%200%7D%5Cfrac%7B%5Cdelta%20%5Cxi%20%5E%7B%5Cwedge%7Dexp%28%5Cxi%20%5E%5Cwedge%29p%7D%7B%5Cdelta%20%5Cxi%7D%5C%5C%20%3Dlim_%7B%5Cdelta%20%5Cxi%20%5Crightarrow%200%7D%5Cfrac%7B%5Cbegin%7Bbmatrix%7D%20%5Cdelta%5Cphi%20%5E%5Cwedge%20%26%5Cdelta%5Crho%20%5C%5C%200%5ET%20%260%20%5Cend%7Bbmatrix%7D%5Cbegin%7Bbmatrix%7D%20Rp&plus;t%20%5C%5C%201%20%5Cend%7Bbmatrix%7D%7D%7B%5Cdelta%20%5Cxi%7D%5C%5C%20%3Dlim_%7B%5Cdelta%5Cxi%20%5Crightarrow%200%7D%20%5Cfrac%7B%5Cbegin%7Bbmatrix%7D%20%5Cdelta%20%5Cphi%20%5E%5Cwedge%20%28Rp&plus;t%29&plus;%5Cdelta%20%5Crho%5C%5C%200%20%5Cend%7Bbmatrix%7D%7D%7B%5Cdelta%5Cxi%7D%3D%5Cbegin%7Bbmatrix%7D%20I%20%26-%28Rp&plus;t%29%5E%5Cwedge%20%5C%5C%200%5ET%20%26%200%5ET%20%5Cend%7Bbmatrix%7D%3D%20%28Tp%29%5E%5Codot">

We define a symbol <img src=http://latex.codecogs.com/gif.latex?%5E%5Codot>, it could convert  a homogenous coordinate spatial point to a <img src="http://latex.codecogs.com/gif.latex?4%5Ctimes%206"> matrix.

# Similarity transformations group and Lie algebra

In monocular vision, we use similarity transformations group Sim(3), and the corresponding Lie algebra is <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bsim%283%29%7D">. For a spatial point p, the camera coordination need a similarity transformation, but not a Euclidean transformation:

<img src="http://latex.codecogs.com/gif.latex?p%27%3D%5Cbegin%7Bbmatrix%7D%20sR%20%26%20t%20%5C%5C%200%5ET%20%261%20%5Cend%7Bbmatrix%7Dp%3DsRp&plus;t">

In the similar transformation, we express the transformation with the parameter s. Similar to SO(3) and SE(3), similarity transformation and the matrix multiply consist the similarity transformation group Sim(3):

<img src="http://latex.codecogs.com/gif.latex?Sim%283%29%3D%5Cleft%20%5C%7B%20%5Cleft%20%5B%20S%3D%5Cbegin%7Bmatrix%7D%20sR%20%26t%20%5C%5C%200%5ET%20%26%201%20%5Cend%7Bmatrix%7D%20%5Cright%20%5D%20%5Cin%20R%5E%7B4%5Ctimes%204%7D%20%5Cright%20%5C%7D">

Sim(3) also has its corresponding Lie algebra, exponential map, logical map. Lie algebra <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bsim%283%29%7D">'s element is a 7D vector <img src="http://latex.codecogs.com/gif.latex?%5Czeta">. Its former 6D element is the same as <img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bse%283%29%7D">, and plus an element <img src="http://latex.codecogs.com/gif.latex?%5Csigma">.

<img src="http://latex.codecogs.com/gif.latex?%5Cmathfrak%7Bsim%283%29%7D%3D%5Cleft%20%5C%7B%20%5Czeta%20%5Cmid%20%5Czeta%20%3D%5Cleft%20%5B%20%5Cbegin%7Bmatrix%7D%20%5Crho%5C%5C%20%5Cphi%5C%5C%20%5Csigma%20%5Cend%7Bmatrix%7D%20%5Cright%20%5D%20%5Cin%20R%5E7%2C%20%5Czeta%20%5E%5Cwedge%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Csigma%20I%20&plus;%20%5Cphi%20%5E%20%5Cwedge%20%26%20%5Crho%20%5C%5C%200%5ET%20%26%200%20%5Cend%7Bbmatrix%7D%20%5Cin%20R%20%5E%7B4%5Ctimes%204%7D%20%5Cright%20%5C%7D">

Exponential map is:

<img src="http://latex.codecogs.com/gif.latex?exp%28%5Czeta%20%5E%5Cwedge%29%3D%5Cbegin%7Bbmatrix%7D%20e%5E%5Csigma%20exp%28%5Cphi%20%5E%5Cwedge%29%20%26%20J_s%20%5Crho%20%5C%5C%200%5ET%20%26%201%20%5Cend%7Bbmatrix%7D">

and the <img src="http://latex.codecogs.com/gif.latex?J_s"> is:

<img src="http://latex.codecogs.com/gif.latex?J_s%3D%5Cfrac%7Be%20%5E%20%5Csigma%20-1%7D%7B%5Csigma%7DI&plus;%5Cfrac%7B%5Csigma%20e%20%5E%20%5Csigma%20sin%20%5Ctheta%20&plus;%20%281%20-%20e%20%5E%20%5Csigma%20cos%20%5Ctheta%29%5Ctheta%7D%7B%5Csigma%20%5E2%20&plus;%20%5Ctheta%20%5E%202%7Da%5E%5Cwedge%5C%5C%20&plus;%28%5Cfrac%7Be%5E%5Csigma%20-%201%7D%7B%5Csigma%7D%20-%20%5Cfrac%7B%28e%5E%5Csigma%20cos%20%5Ctheta%20-%201%29%5Csigma%20&plus;%20%28e%20%5E%20%5Csigma%20sin%20%5Ctheta%29%5Ctheta%7D%7B%5Csigma%20%5E2%20&plus;%20%5Ctheta%20%5E%202%7D%29a%5E%5Cwedge%20a%5E%5Cwedge">
