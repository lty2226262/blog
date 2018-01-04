# 1. 四元数定义和性质

## 1. 1. 四元数定义

有两个复数`A = a + bi`，`C=c+di`，构造一个`Q = A + Cj`并且定义$k\triangleq ij$. 折到一个四元数空间$\mathbb{H}$,
$$
Q=a+bi+cj+dk\in \mathbb{H}
$$
所以我们可以得到，
$$
i^2=j^2=k^2=ijk=-1
$$
同时，
$$
ij=-ji=k, jk=-kj=i, ki=-ik=j
$$
所以，实数、虚数和复数都是四元数，
$$
Q=a\in\mathbb{R}\subset\mathbb{H}, Q = bi\in\mathbb{I}\subset\mathbb{H}, Q=a+bi\in\mathbb{Z}\subset\mathbb{H}
$$

### 1.1.1 其他的四元数表示法

`实部+虚部`的表达法有的时候不方便的。四元数也可以表示成一个`scalar+vector`.
$$
Q=q_w+q_xi+q_yj+q_zk \Leftrightarrow Q=q_w+\mathbf{q}_v
$$
所以，`Q`可以表达成`scalar-vector`对。
$$
Q=<q_w, q_v>
$$
我们经常把四元数`Q`表达成四维向量`q`,
$$
q\triangleq\begin{bmatrix}
q_w\\ 
\mathbf{q}_v
\end{bmatrix}=\begin{bmatrix}q_w\\
q_x\\
q_y\\
q_z
\end{bmatrix}
$$

## 1.2 四元数主要性质

### 1.2.1 加法

$$
\mathbf{p}\pm\mathbf{q}=\begin{bmatrix}p_w\\\mathbf{p}_v\end{bmatrix}\pm\begin{bmatrix}q_w\\\mathbf{q}_v\end{bmatrix}=\begin{bmatrix}p_w\pm q_w\\\mathbf{p}_v\pm \mathbf{q_v}\end{bmatrix}
$$

加法非常直接，有着交换律和结合律。

### 1.2.2 乘法

$$
\mathbf{p}\otimes \mathbf{q} = \begin{bmatrix}p_wq_w-p_xq_x-p_yq_y-p_zq_z\\
p_wq_x+p_xq_w+p_yq_z-p_zq_y\\
p_wq_y-p_xq_z+p_yq_w+p_zq_x\\
p_wq_z+p_xq_y-p_yq_x+p_zq_w\end{bmatrix}
$$

如果以`vector-scalar`对记，则为：
$$
\mathbf{p}\otimes \mathbf{q} = \begin{bmatrix}p_wq_w-\mathbf{p}^T_v\mathbf{q}_v\\
p_w\mathbf{q}_v+q_w\mathbf{p}_v+\mathbf{p}_v\times\mathbf{q}_v\end{bmatrix}
$$
四元数没有交换律，但是有结合律。也有分配律。
$$
\mathbf{p}\otimes\mathbf{q}\neq\mathbf{q}\otimes\mathbf{p}
$$

$$
(\mathbf{p}\otimes\mathbf{q})\otimes\mathbf{r}=\mathbf{p}\otimes(\mathbf{q}\otimes\mathbf{r})
$$

$$
\mathbf{p}\otimes(\mathbf{q}+\mathbf{r})=\mathbf{p}\otimes\mathbf{q}+\mathbf{p}\otimes\mathbf{r}
$$

乘积具有双线性，可以表示成两个等价的矩阵相乘的形式，
$$
\mathbf{q}_1\otimes\mathbf{q}_2=[\mathbf{q}_1]_L\mathbf{q}_2
$$

$$
\mathbf{q}_1\otimes \mathbf{q}_2 = [\mathbf{q}_2]_R\mathbf{q}_1
$$

其中$[\mathbf{q}]_L$和$[\mathbf{q}]_R$分别是四元数左乘和右乘矩阵，分别为
$$
[\mathbf{q}]_L=\begin{bmatrix}q_w& -q_x & -q_y & -q_z\\
q_x & q_w& -q_z & q_y\\
q_y & q_z & q_w & -q_x\\
q_z&-q_y&q_x&q_w\end{bmatrix}, [\mathbf{q}]_R=\begin{bmatrix}q_w& -q_x & -q_y & -q_z\\
q_x & q_w& q_z & -q_y\\
q_y & -q_z & q_w & q_x\\
q_z&q_y&-q_x&q_w\end{bmatrix}
$$
也可以表示为，
$$
[\mathbf{q}]_L=q_w\mathbf{I}+\begin{bmatrix}0 & -\mathbf{q}_v^T\\
\mathbf{q}_v & [\mathbf{q}_v]_\times\end{bmatrix}, [\mathbf{q}]_R=q_w\mathbf{I}+\begin{bmatrix}0 & -\mathbf{q}_v^T\\
\mathbf{q}_v & -[\mathbf{q}_v]_\times\end{bmatrix}
$$
在这里，$[\bullet]_\times$是skew operator(偏移算子)，可以得到叉乘cross-product的结果，
$$
[\mathbf{a}]_\times\mathbf{b}=\mathbf{a}\times\mathbf{b}, \forall\mathbf{a},\mathbf{b}\in\mathbb{R}^3
$$
最后，因为
$$
(\mathbf{q}\otimes\mathbf{x})\otimes\mathbf{p}=[\mathbf{p}]_R[\mathbf{q}]_L\mathbf{x}

\\\mathbf{q}\otimes(\mathbf{x}\otimes\mathbf{p})=[\mathbf{q}]_L[\mathbf{p}]_R\mathbf{x}
$$
所以，
$$
[\mathbf{p}]_R[\mathbf{q}]_L=[\mathbf{q}]_L[\mathbf{p}]_R
$$

### 1.2.3 单位四元数

$\mathbf{q}_1\otimes\mathbf{q}=\mathbf{q}\otimes\mathbf{q}_1=\mathbf{q}$代表着四元数的幺元。$\mathbf{q}_1=1=\begin{bmatrix}{1\\\mathbf{0}_v}\end{bmatrix}$。

### 1.2.4 共轭

共轭四元数定义如下：
$$
\mathbf{q}^*\triangleq q_w -\mathbf{q}_v= \begin{bmatrix}q_w \\ -\mathbf{q}_v\end{bmatrix}
$$
因此存在着性质：
$$
\mathbf{q}\otimes\mathbf{q}^*=\mathbf{q}^*\otimes\mathbf{q}=q_w^2+q_x^2+q_y^2+q^2_z=\begin{bmatrix}q_w^2+q_x^2+q_y^2+q_z^2\\\mathbf{0}_v\end{bmatrix}
$$

$$
(\mathbf{p}\otimes\mathbf{q})^*=\mathbf{q}^*\otimes\mathbf{p}^*
$$

### 1.2.5 范数

按照定义，范数为
$$
\left \| \mathbf{q} \right \|\triangleq\sqrt{\mathbf{q}\otimes\mathbf{q}^*}=\sqrt{\mathbf{q}^*\otimes\mathbf{q}}=\sqrt{q_w^2+q_x^2+q_y^2+q_z^2}\in\mathbb{R}
$$
存在关系：
$$
\left \| \mathbf{p}\otimes\mathbf{q} \right \| = \left \| \mathbf{q}\otimes\mathbf{p} \right \| = \left \| \mathbf{p} \right \|  \left \| \mathbf{q} \right \|  
$$

### 1.2.6 逆

逆四元数$\mathbf{q}^{-1}$是一个四元数，他的逆是，
$$
\mathbf{q}\otimes\mathbf{q}^{-1}=\mathbf{q}^{-1}\otimes\mathbf{q}=\mathbf{q}_1
$$
可以计算得到，
$$
\mathbf{q}^{-1}=\mathbf{q}^*/\left \| \mathbf{q} \right \|^2
$$

### 1.2.7 单位四元数或者标准化四元数

对于单位四元数，$\left\| \mathbf{q} \right\| = 1$, 因此则有
$$
\mathbf{q}^{-1}=\mathbf{q}^*
$$
单位四元数总是能够写成如下的形式，
$$
\mathbf{q}=\begin{bmatrix}\cos\theta\\\mathbf{u}\sin\theta\end{bmatrix}
$$
其中，$\mathbf{u}=u_xi+u_yj+u_zk$ 是一个单位向量，$\theta$是量度。

## 1.3 其他性质

### 1.3.1 四元数换位子 Quaternions commutator

四元数的换位子定义为$[\mathbf{p},\mathbf{q}]\triangleq\mathbf{p}\otimes\mathbf{q}-\mathbf{q}\otimes\mathbf{p}$
$$
\mathbf{p}\otimes\mathbf{q}-\mathbf{q}\otimes\mathbf{p}=2\mathbf{p}_v\times\mathbf{q}_v
$$

### 1.3.2 纯四元数乘积

纯四元数没有实部，$Q=\mathbf{q}_v$或者$\mathbf{q}=[0,\mathbf{q}_v]$.

所以,
$$
\mathbf{p}_v\otimes\mathbf{q}_v=-\mathbf{p}_v^T\mathbf{q}_v+\mathbf{p}_v\times\mathbf{q}_v=\begin{bmatrix}-\mathbf{p}_v^T\mathbf{q}_v\\
\mathbf{p}_v\times\mathbf{q}_v\end{bmatrix}
$$

$$
\mathbf{q}_v\otimes\mathbf{q}_v=-\mathbf{q}^T_v\mathbf{q}_v=-\left\|\mathbf{q}_v\right\|^2
$$

如果是单位纯四元数的话，$\left\|\mathbf{u}\right\|=1$,
$$
\mathbf{u}\otimes\mathbf{u}=-1
$$
与纯虚数相似。

### 1.3.3 纯四元数的乘方

定义$\mathbf{q}^n$,是$\mathbf{q}$的n次幂($\otimes$)如果$\mathbf{v}$是纯四元数，设$\mathbf{v}$是纯四元数且$\mathbf{v}=\mathbf{u}\theta$,其中$\theta=\left\|v\right\|\in\mathbb{R}$,$\mathbf{u}$是单位向量，我们能得到cyclic pattern.
$$
\mathbf{v}^2=-\theta^2, \mathbf{v}^3=-\mathbf{u}\theta^3,\mathbf{v}^4=\theta^4, \mathbf{v}^5=\mathbf{u}\theta^5,\mathbf{v}^6=-\theta^6,...
$$

### 1.3.4 纯四元数的指数形式

四元数的级数展开，
$$
e^\mathbf{q}\triangleq\sum^\infty_{k=0}\frac{1}{k!}\mathbf{q}^n\in\mathbb{H}
$$
对于纯四元数$\mathbf{v}=v_xi+v_yj+v_zk$，设$\theta=\left\|v\right\|\in \mathbb{R}$,写成级数展开的形式，
$$
e^\mathbf{v}=e^\mathbf{u}\theta=\cos\theta+\mathbf{u}\sin\theta=\begin{bmatrix}\cos\theta\\\mathbf{u}\sin\theta\end{bmatrix}
$$
这个居然和欧拉公式的形式相似，$e^{i\theta}=\cos\theta+i\sin\theta$, 所以有如下的性质：
$$
e^{-\mathbf{v}}=(e^\mathbf{v})^*
$$

### 1.3.5 普通四元数的指数

由于四元数不可交换，我们不能得到$e^\mathbf{p+q}=e^\mathbf{p}e^\mathbf{q}$,但是我们却具有性质：
$$
e^\mathbf{q}=e^{q_w+\mathbf{q}_v}=e^{qw}e^{\mathbf{q}v}
$$
同时，我们也可以使用$\mathbf{u}\theta=\mathbf{q}_v$,
$$
e^\mathbf{q}=e^{qw}\begin{bmatrix}\cos\left\|\mathbf{q}_v\right\|\\\frac{\mathbf{q}_v}{\left\|\mathbf{q}_v\right\|}\sin\left\|\mathbf{q}_v\right\|\end{bmatrix}
$$

### 1.3.6 单元四元数的对数

如果$\left\|\mathbf{q}\right\|=1$,即为单位四元数，则有
$$
\log\mathbf{q}=\log(\cos\theta+\mathbf{u}\sin\theta)=\log(e^{\mathbf{u}\theta})= \mathbf{u}\theta=\begin{bmatrix}0\\\mathbf{u}\theta\end{bmatrix}
$$
即为单位四元数的对数是纯四元数。轴角值为，
$$
\mathbf{u}=\mathbf{q}_v/\left\|\mathbf{q}_v\right\|
$$

$$
\theta=\arctan(\left\|\mathbf{q}_v\right\|,q_w)
$$

对于微小角度的四元数，为了避免分母为0我们用了泰勒级数进行展开。
$$
\log(\mathbf{q})=\mathbf{u}\theta = \mathbf{q}_v\frac{\arctan(\left\|\mathbf{q}_v\right\|,q_w)}{\left\|\mathbf{q}_v\right\|}\approx\frac{\mathbf{q}_v}{q_w}(1-\frac{\left\|\mathbf{q}_v\right\|^2}{3q^2_w})
$$

### 1.3.7 普通四元数的对数

$$
\log\mathbf{q}=\log(\left\|\mathbf{q}\right\|\frac{\mathbf{q}}{\left\|\mathbf{q}\right\|})=\log\left\|\mathbf{q}\right\|+\log\frac{\mathbf{q}}{\left\|\mathbf{q}\right\|}=\log\left\|\mathbf{q}\right\|+\mathbf{u}\theta=\begin{bmatrix}\log\left\|\mathbf{q}\right\|\\\mathbf{u}\theta\end{bmatrix}
$$

### 1.3.8 $\mathbf{q}^t$的指数形式

对于$\mathbf{q}\in\mathbb{H}, t\in\mathbb{R}$,
$$
\mathbf{q}^t=\exp(\log(\mathbf{q}^t)) = \exp(t\log(\mathbf{q}))
$$
如果$\left\|\mathbf{q}\right\|=1$,我们可以得到$\mathbf{q}=[\cos\theta, \mathbf{u}\sin\theta]$,因此$\log(\mathbf{q})=\mathbf{u}\theta$,所以，
$$
\mathbf{q}^t=\begin{bmatrix}\cos t\theta\\\mathbf{u}\sin t\theta\end{bmatrix}
$$

# 2. 旋转和cross-relation

## 2.1 3D Vector 旋转公式

根据右手定则，一个3D向量$\mathbf{x}$ 和一个角度$\phi$,绕着的轴设为单位向量$\mathbf{u}$.可以把向量$\mathbf{x}$分解为和$\mathbf{u}$平行的分量$\mathbf{x}_\parallel $和正交分量$\mathbf{x}_\perp $，所以，
$$
\mathbf{x}=\mathbf{x}\parallel+\mathbf{x}\perp
$$
这些部分可以很容易的计算，
$$
\mathbf{x}_\parallel=\mathbf{u}(\left\|\mathbf{x}\right\|\cos\alpha)=\mathbf{u}\mathbf{u}^T\mathbf{x}\\
\mathbf{x}_\perp=\mathbf{x}-\mathbf{x}_\parallel=\mathbf{x}-\mathbf{u}\mathbf{u}^T\mathbf{x}
$$
对于旋转，平行分量不旋转,正交部分绕着以$\mathbf{u}$为法向量的平面旋转，也就是，如果我们创造一对正交基
$$
\mathbf{e}_1=\mathbf{x}_\perp\\
\mathbf{e}_2=\mathbf{u}\times\mathbf{x}_\perp=\mathbf{u}\times\mathbf{x}
$$
满足$\left\|e_1\right\|=\left\|e_2\right\|$,然后$\mathbf{x}_\perp=\mathbf{e}_1\cos\phi+\mathbf{e}_2\sin\phi$

可以得到，
$$
\mathbf{x}'=\mathbf{x}_\parallel + \mathbf{x}_\perp\cos\phi+(\mathbf{u}\times\mathbf{x})\sin\phi
$$

## 2.2 旋转群SO(3)

旋转群是绕原点旋转的群，旋转过程中保持向量的长度不变和向量间的夹角不变，他表示了刚体在三维的转动。刚体在旋转过程中要保持距离、角度和相对运动不变。

一个旋转操作$r(\mathbf{v})$表达了向量$\mathbf{v}\in\mathbb{R}^3$在欧几里得空间的变化，由点乘和叉乘组成。如下所示。

* 旋转保持向量的范数，

$$
\left\|r(\mathbf{v})\right\|=\sqrt{r(\mathbf{v})^Tr(\mathbf{v})}=\sqrt{\mathbf{v}^T\mathbf{v}}\triangleq\left\|\mathbf{v}\right\|, \forall\mathbf{v}\in\mathbb{R}^3
$$

* 旋转保持向量之间的角度

$$
r(\mathbf{v})^Tr(\mathbf{w})=\mathbf{v}^T\mathbf{w}=\left\|\mathbf{v}\right\|\left\|\mathbf{w}\right\|\cos\alpha, \forall \mathbf{v},\mathbf{w}\in\mathbb{R}^3
$$

* 旋转保持向量之间的相对朝向

$$
\mathbf{u}\times\mathbf{v}=\mathbf{w}\Leftrightarrow r(\mathbf{u})\times r(\mathbf{v})=r(\mathbf{w})
$$

容易证明前两个条件是相等的。我们能够因此得到旋转群SO(3):
$$
SO(3):\{r:\mathbb{R}3 →\mathbb{R}3/∀\mathbf{v,w}∈\mathbb{R}^3 , ∥r(\mathbf{v})∥=∥\mathbf{v}∥, r(\mathbf{v})×r(\mathbf{w})=r(\mathbf{v}×\mathbf{w})\}
$$
旋转可以表达为旋转矩阵，四元数也是很好的。

## 2.3 旋转群和旋转矩阵

操作符$r()$是线性的，因为它通过scalar和vector的乘积得到，这两个都是线性的。因此，旋转矩阵可以表示为$\mathbf{R}\in\mathbb{R}^{3\times3}$,
$$
r(\mathbf{v})= \mathbf{R}\mathbf{v}
$$
因此对于所有的$\mathbf{v}$,
$$
(\mathbf{Rv})^T(\mathbf{Rv})=\mathbf{v^TR^T}\mathbf{Rv}=\mathbf{v^Tv}
$$
由于存在正交约束，所以存在，
$$
\mathbf{R}^T\mathbf{R}=\mathbf{I}=\mathbf{R}\mathbf{R}^T
$$

|                 | Rotation matrix, R                       | Quanternion,                             |
| --------------- | ---------------------------------------- | ---------------------------------------- |
| 参数              | $3\times3=9$                             | $1+3=4$                                  |
| 自由度             | 3                                        | 3                                        |
| 约束数量            | 6                                        | 1                                        |
| 约束              | $\mathbf{RR^T=I},\det(\mathbf{R})=+1$    | $\mathbf{q}\otimes\mathbf{q}^*=1$        |
| ODE常微分方程        | $\dot{\mathbf{R}}=\mathbf{R}[\omega]_\times$ | $\dot{\mathbf{q}}=\frac{1}{2}\mathbf{q}\otimes\mathbf{\omega}$ |
| 指数映射            | $\mathbf{R}=\exp([\mathbf{u}\phi]_\times)$ | $\mathbf{q}=\exp(\mathbf{u}\phi/2)$      |
| 对数映射            | $\log(\mathbf{R})=[\mathbf{u}\phi]_\times$ | $\log(\mathbf{q})=\mathbf{u}\phi/2$      |
| 与SO(3)的关系       | single cover                             | double cover                             |
| identity        | $\mathbf{I}$                             | 1                                        |
| 逆               | $\mathbf{R}^T$                           | $\mathbf{q}^*$                           |
| Composition     | $\mathbf{R}_1\mathbf{R}_2$               | $\mathbf{q}_1\otimes\mathbf{q}_2$        |
| 旋转表示            | $\mathbf{R}=\mathbf{I}+\sin\phi[\mathbf{u}]_\times+(1-\cos\phi)[\mathbf{u}]^2_\times$ | $\mathbf{q}=\cos\phi/2+\mathbf{u}\sin\phi/2$ |
| 旋转操作            | $\mathbf{R}\mathbf{x}$                   | $\mathbf{q}\otimes\mathbf{x}\otimes\mathbf{q}^*$ |
| 插值              | $\mathbf{R}_1(\mathbf{R}_1^T\mathbf{R}_2)^t$ | $\mathbf{q}_1\otimes(\mathbf{q}_1^*\otimes\mathbf{q}_2)^t$ |
| Cross relations | $\mathbf{R\{q\}}=(q_\omega^2-\mathbf{q}^T_v\mathbf{q}_v)\mathbf{I}+2\mathbf{q}_v\mathbf{q}^T_v+2q_\omega[\mathbf{q}_v]$ |                                          |
|                 | $\mathbf{R\{-q\}}=\mathbf{R\{q\}}$       | double cover                             |
|                 | $\mathbf{R}\{1\}=\mathbf{I}$             | identity                                 |
|                 | $\mathbf{R}\{\mathbf{q}^*\}=\mathbf{R}\{\mathbf{q}\}^T$ | Inverse                                  |
|                 | $\mathbf{R}\{\mathbf{q}_1\otimes\mathbf{q}_2\}=\mathbf{R}\{\mathbf{q}_1\}\mathbf{R}\{\mathbf{q}_2\}$ | Composition                              |
|                 | $\mathbf{R}\{\mathbf{q}^t\}=\mathbf{R}\{\mathbf{q}\}^t$ | interpolation                            |

这个正交约束其实就是正交条件，我们可以从$\mathbf{R}$的列向量$\mathbf{r}_i$得知：
$$
\left \langle \mathbf{r}_i ,\mathbf{r}_j=\mathbf{r}_i^T\mathbf{r}_j=1, \text{if } i=j\right \rangle\\\left \langle \mathbf{r}_i ,\mathbf{r}_j=\mathbf{r}_i^T\mathbf{r}_j=0, \text{if } i\ne j\right \rangle
$$
能够保持范数和角度转换关系的集合叫做正交群，记为$O(3)$。正交群包括旋转（刚体变换）和reflection（非刚体变换）。群表示了两个两个正交矩阵的乘积也总是正交的，每个正交阵也都有逆。实际上，正交也满足了：
$$
\mathbf{R}^{-1}=\mathbf{R}^T
$$
由于刚体运动的关系，使得矩阵$\mathbf{R}$也存在着特殊性，
$$
\det(\mathbf{R})=1
$$
这种特殊正交群是O(3)的子群，记为$SO(3)$。

### 2.3.1 指数映射

旋转是刚体运动的一部分。刚体也指SO(3)的$r(t)$路径轨迹是连续的。刚体从初始朝向$r(0)$到当前朝向$r(t)$的旋转是连续的。由于是连续的，研究这些变换的时间微分就是有意义的。

首先，我们可以注意到当矩阵满足正交单位条件时，矩阵的运算不可能escape单位条件，因为取值范围会从+1跳到-1。因此我们只需要研究时变系统的正交条件，即：
$$
\frac{d}{dt}(\mathbf{R^TR})=\dot{\mathbf{R}}^T\mathbf{R}+\mathbf{R}^T\dot{\mathbf{R}}=0
$$
所以，
$$
\mathbf{R}^T\dot{\mathbf{R}}=-(\mathbf{R}^T\dot{\mathbf{R}})^T
$$
这意味着$\mathbf{R}^T\dot{\mathbf{R}}=-(\mathbf{R}^T\dot{\mathbf{R}})^T$是一个反对称阵。这个$3\times3$反对称阵的集合叫做so(3)，它是SO(3)的李代数。这个矩阵有三个自由度，很方便写成叉乘形式，
$$
[\mathbf{\omega}]_\times\triangleq\begin{bmatrix}0&-\omega_x&\omega_y\\
\omega_z&0&-\omega_x\\
-\omega_y&\omega_x&0\end{bmatrix}
$$
所以我们已经建立了一个一对一的映射$\mathbf{\omega}\in\mathbb{R}^3\leftrightarrow[\mathbf{\omega}]_\times\in so(3)$。所以我们建立了$\mathbf{\omega}\in\mathbf{R}^3$并且记为
$$
\mathbf{R}^T\dot{\mathbf{R}}=[\mathbf{\omega}]_\times
$$
根据常微分方程(ODE),
$$
\dot{\mathbf{R}}=\mathbf{R}[\mathbf{\omega}]_\times
$$
在原点附近，我们有着该性质：$\mathbf{R=I}$。所以该等式退化成$\dot{\mathbf{R}}=[\mathbf{\omega}]_\times$。因此，我们可以把李代数so(3)解释为r(t)在原点附近的微分。这也组成了SO(3)的正切空间，也可以表述为速度空间。根据这些事实，我们把$\mathbf{\omega}$叫为向量的瞬时角速度。

如果$\mathbf{\omega}$是常数，上面的微分方程存在时间积分解，
$$
\mathbf{R}(t)=\mathbf{R}(0)e^{\mathbf[\omega]_\times t}=\mathbf{R}(0)e^{[\mathbf\omega t]_\times}
$$
指数$e^{[\mathbf{v}]_\times}$可以写成泰勒级数形式，详见下一章。由于$\mathbf{R}(0)$和$\mathbf{R}(t)$是旋转矩阵，很明显$e^{[\omega t]_\times}$也是旋转矩阵。定义向量$\mathbf{v}\triangleq\omega\Delta t$作为旋转向量记录了在时间段$\Delta t$的全部转动量，因此则有指数映射，
$$
\mathbf{R}=e^{[\mathbf{v}_\times]}
$$
这被记为指数映射，应用于从so(3)到SO(3),
$$
exp:so(3)\rightarrow SO(3);[\mathbf{v}]_\times\rightarrow \exp([\mathbf{v}]_\times)=e^{[\mathbf{v}]_\times}
$$

### 2.3.2 大写的Exp映射

有时会冲突，比如有的时候会滥用标记，比如有时候会混淆$\mathbf{v}\in\mathbb{R}^3$和$[\mathbf{v}]_\times\in so(3)$。为了避免这些混淆，我们利用了一种大写记号：
$$
\text{Exp}:\mathbb{R}^3\rightarrow SO(3);\mathbf{v}\rightarrow\text{Exp}(\mathbf{v})=e^{[\mathbf{v}]_\times}
$$
与小exp的关系为：
$$
\text{Exp}(\mathbf{v})\triangleq\exp([\mathbf{v}]_\times)
$$
在接下来的几章我们会见到旋转向量$\mathbf{v}$,或者称为轴角向量有$\mathbf{v}=\mathbf{\omega}\Delta t=\phi \mathbf{u}$,角度是$\phi$,轴是$\mathbf{u}$。

### 2.3.3 旋转矩阵和旋转向量：罗德里格斯公式

旋转矩阵是由旋转向量$\mathbf{v}=\phi\mathbf{u}$通过指数映射，通过矩阵的叉乘运算$[\mathbf{v}]_\times=\phi[\mathbf{u}]_\times$定义的。$\mathbf{v}=\phi\mathbf{u}$泰勒展开是，
$$
\mathbf{R}=e^{\phi[\mathbf{u}]_\times}=\mathbf{I}+\phi[\mathbf{u}]_\times+\frac{1}{2}\phi^2[\mathbf{u}]_\times^2+\frac{1}{3!}\phi^3[\mathbf{u}]^3_\times+\frac{1}{4!}\phi^4[\mathbf{u}]_\times^4+...
$$
当应用了单位向量$\mathbf{u}$时，矩阵$[\mathbf{u}]_\times$满足：
$$
[\mathbf{u}]^2_\times=\mathbf{uu^T-I}\\
[\mathbf{u}]^3_\times=-[\mathbf{u}]_\times
$$
由于纯虚数的性质，有：
$$
[\mathbf{u}]^4_\times=-[\mathbf{u}]^2_\times, [\mathbf{u}]^5_\times=[\mathbf{u}]_\times, [\mathbf{u}]^6_\times=[\mathbf{u}]^2_\times, [\mathbf{u}]^7_\times=-[\mathbf{u}]_\times,  ...
$$
分别将级数就$[\mathbf{u}]_\times$和$[\mathbf{u}]_\times^2$分成两组，分别以$\sin\phi$和$\cos\phi$表示，则会有罗德里格斯公式，
$$
\mathbf{R=I+}\sin\phi[\mathbf{u}]_\times+(1-\cos\phi)[\mathbf{u}]^2_\times
$$
将$\mathbf{R}=\mathbf{R}\{\mathbf{v}\}\triangleq\text{Exp}(\mathbf{v})$。这个公式也有一些变化，
$$
\mathbf{R}=\mathbf{I}\cos\phi+[\mathbf{u}]_\times\sin\phi+\mathbf{uu}^T(1-\cos\phi)
$$

### 2.3.4 对数变换

我们定义对数变换为指数变换的逆，
$$
\log: SO(3)\rightarrow so(3); \mathbf{R}\rightarrow\log(\mathbf{R})=[\mathbf{u}\phi]_\times
$$
同时，有：
$$
\phi=\arccos(\frac{\text{trace}(\mathbf{R})-1}{2})\\
\mathbf{u}=\frac{(\mathbf{R}-\mathbf{R}^T)^\vee}{2\sin\phi}
$$
$\bullet^\vee$与$[\bullet]_\times$相反，也就是$([\mathbf{v}]_\times)^\vee=\mathbf{v}$而且有$[\mathbf{V}^\vee]_\times=\mathbf{V}$。

所以我们定义了一个大写Log，能够直接恢复旋转向量成旋转矩阵$\mathbf{v=u}\phi\in\mathbb{R}^3$。
$$
\text{Log}:SO(3)\rightarrow\mathbb{R}^3; \mathbf{R}\rightarrow\text{Log}(\mathbf{R})=\mathbf{u}\phi
$$
它与指数映射之间的关系是微不足道的，
$$
\text{Log}(\mathbf{R})\triangleq(\log(\mathbf{R}))^\vee
$$

### 2.3.5 旋转动作 

将一个向量$\mathbf{x}$绕轴$\mathbf{u}$旋转$\phi$，我们能得到：
$$
\mathbf{x^\text{'}=Rx}
$$
其中$\mathbf{R}=\text{Exp}(\mathbf{u}\phi)$,可以推导出如下结论，
$$
\mathbf{x}^\text{'}=\mathbf{Rx}\\
=(\mathbf{I}+\sin\phi[\mathbf{u}]_\times+(1-\cos\phi)[\mathbf{u}]^2_\times)\mathbf{x}\\
=\mathbf{x}+\sin\phi[\mathbf{u}]_\times\mathbf{x}+(1-\cos\phi)[\mathbf{u}]_\times^2\mathbf{x}\\
=\mathbf{x}+\sin\phi(\mathbf{u}\times\mathbf{x})+(1-\cos\phi)(\mathbf{uu^T-I})\mathbf{x}\\
=\mathbf{x}_\parallel+\mathbf{x}_\perp+\sin\phi(\mathbf{u}\times\mathbf{x})-(1-\cos\phi)\mathbf{x}_\perp\\
=\mathbf{x}_\parallel+(\mathbf{u}\times\mathbf{x})\sin\phi+\mathbf{x}_\perp\cos\phi
$$

## 2.4 旋转群和四元数

下面给出旋转矩阵（以旋转群SO（3）的表述方式）与四元数的关系，我们假设利用四元数进行旋转可以通过二次乘法实现，
$$
r(\mathbf{v})=\mathbf{q}\otimes\mathbf{v}\otimes\mathbf{q}^*
$$
将单位四元数的性质代入上式中，可以得到：
$$
\mathbf{\left\|q\otimes v\otimes q^*\right\|=\left\|q\right\|^2\left\|v\right\|=\left\|v\right\|}
$$
由于存在$\mathbf{\left\|q\right\|^2=1}$,也就是存在如下等式，
$$
\mathbf{q}^*\otimes\mathbf{q}=1=\mathbf{q\otimes q^*}
$$
同样的，我们可以推得：
$$
r(\mathbf{v})\times r(\mathbf{w})=\mathbf{(q\otimes v\otimes q^*)\times(q\otimes w\otimes q^*)}\\
=\frac{1}{2}\mathbf{((q\otimes v\otimes q^*)\otimes (q \otimes w \otimes q^*) - (q\otimes w \otimes q^*)\otimes(q \otimes v \otimes q^*))}\\
=\frac{1}{2}(\mathbf{q\otimes v \otimes w \otimes q ^* - q \otimes w \otimes v \otimes q ^*})\\
=\frac{1}{2}(\mathbf{q \otimes (v \otimes w - w \otimes v)\otimes q^*})\\
=\mathbf{q\otimes( v \times w)\otimes q^*}\\
=r(\mathbf{v\times w})
$$
单元范数条件与矩阵旋转有点类似，$\mathbf{q^*\otimes q=1=q\otimes q ^*, R^TR=I=RR^T}$

单元四元数的集合组成了乘法操作。这个群在拓扑结构上是3-sphere,是$\mathbb{R}^4$单元球面的三维表面。通常记为$S^3$。

### 2.4.1 指数映射

考虑单位四元数$\mathbf{q}\in S^3$,即为$\mathbf{q^*\otimes q = 1}$,我们处理正交条件$\mathbf{R^TR=I}$.

进行时间上的微分后，
$$
\frac{d(\mathbf{q}^*\otimes\mathbf{q})}{dt}=\dot{\mathbf{q}}^*\otimes\mathbf{q}+\mathbf{q}^*\otimes\dot{\mathbf{q}}=0
$$
之后可以推出:
$$
\mathbf{q^*\otimes \dot{q}=-(\dot{q}^*\otimes q)=-(q^*\otimes \dot{q})}^*,
$$
这也就意味着$\mathbf{q^*\otimes \dot{q}}$是纯四元数，我们因此可以得到$\Omega\in\mathbb{H}_p$并且可以写成,
$$
\mathbf{q^*\otimes\dot{q}=\Omega=}\begin{bmatrix}0\\\mathbf\Omega\end{bmatrix}\in\mathbb{H}_p
$$
左乘一个$\mathbf{q}$可以得到：
$$
\dot{\mathbf{q}}=\mathbf{q}\otimes\mathbf\Omega
$$
在原点附近呢，有${\mathbf{q}=1}$所以上面的公式则可以化为$\dot{\mathbf{q}}=\Omega\in\mathbb{H}_p$。因此，$\mathbb{H}_p$表示纯四元数，组成了正切空间，即李群SO(3)的李代数的单位四元数表示形式。在四元数的例中，这个空间不直接是速度空间，而是速度一半所组成的空间。

如果$\Omega$是常数，微分方程有解：
$$
\mathbf{q}(t)=\mathbf{q}(0)\otimes e^{\mathbf{\Omega}t}
$$
由于$\mathbf{q}(0)$和$\mathbf{q}(t)$是单元为四元数，所以指数$e^{\mathbf{\Omega}t}$也是单位四元数，定义$\mathbf{V}\triangleq\mathbf{\Omega}\Delta t$,我们则有，
$$
\mathbf{q}=e^\mathbf{V}
$$
这也是个指数映射：
$$
\exp: \mathbb{H}_p\to S^3;\mathbf{V}\to\exp(\mathbf{V})=e^{\mathbf V}
$$

### 2.4.2 大写Exp映射

纯四元数$\mathbf{V}$有性质$\mathbf{V}=\theta\mathbf{u}=\phi\mathbf{u}/2$,旋转轴为$\mathbf{u}$，旋转角的一半为$\theta=\phi/2$。我们会在2.4.5，2.4.6和2.8进行证明。当表示旋转时，向量乘了两次，即$\mathbf{x'}=\mathbf{q}\otimes\mathbf{x}\otimes\mathbf{q}^*$。

为了直接的表示轴角旋转参数的关系$\mathbf{v}=\phi\mathbf{u}\in\mathbb{R}^3$,我们将四元数定义为答谢的指数映射，表示了一半旋转角的影响，
$$
\text{Exp}:\mathbb{R}^3\to S^3;\mathbf{v}\to\text{Exp}(\mathbf{v})=e^{\mathbf{v}/2}
$$
有其他性质$\mathbf{\omega}=2\Omega\in\mathbb{R}^3$，所以也可以表示为：
$$
\dot{\mathbf{q}}=\frac{1}{2}\mathbf{q}\otimes\mathbf{\omega}\\
\mathbf{q}=e^{\omega t/2}
$$

### 2.4.3 四元数和旋转向量

设$\mathbf{v}=\phi\mathbf{u}$是旋转向量，代表着绕轴$\mathbf{u}$旋转$\phi$。所以通过欧拉公式可以推出：
$$
\mathbf{q}\triangleq\text{Exp}(\phi\mathbf{u})=e^{\phi\mathbf{u}/2}=\cos\frac{\phi}{2}+\mathbf{u}\sin\frac{\phi}{2}=\begin{bmatrix}\cos(\phi/2)\\\mathbf{u}\sin(\phi/2)\end{bmatrix}
$$
我们把从旋转向量转化为四元数的过程称为转换公式，记为$\mathbf{q}=\mathbf{q\{v\}}\triangleq\text{Exp}(\mathbf{v})$。

### 2.4.4 对数映射

定义对数映射为指数映射的逆过程，存在：
$$
\log: S^3 \to \mathbb{H}_p; \mathbf{q}\to \log(\mathbf{q}) = \mathbf{u}\theta
$$
我们也定义了大写的对数变换Log，可以直接提供笛卡尔系的轴$\mathbf{u}$角$\phi$关系。
$$
\text{Log}:S^3\to R^3;\mathbf{q}\to\text{Log}(\mathbf{q})=\mathbf{u}\phi 
$$
用四象限法的$\arctan(y,x)$可以得到：
$$
\phi=2\arctan(\left\|\mathbf{q}_v\right\|,q_w)\\
\mathbf{u}=\mathbf{q}_v/\left\|\mathbf{q}_v\right\|
$$
有一个比较微不足道的关系：
$$
\text{Log}(\mathbf{q})\triangleq2\log(\mathbf{q})
$$

### 2.4.5 旋转动作

绕着一个轴$\mathbf{u}$旋转一个角$\phi$，也叫做三明治乘法：
$$
\mathbf{x'}=\mathbf{q}\otimes\mathbf{x}\otimes\mathbf{q}^*
$$
其中$\mathbf{q}=\text{Exp}(\mathbf{u}\phi)$,向量$\mathbf{x}$写成四元数的形式，即为，
$$
\mathbf{x}=xi+yj+zk=\begin{bmatrix}0\\\mathbf{x}\end{bmatrix}\in\mathbb{H}_p
$$
推导过程如下：
$$
\mathbf{x}'=\mathbf{q}\otimes\mathbf{x}\otimes\mathbf{q}^*\\
=(\cos\frac{\phi}{2}+\mathbf{u}\sin\frac{\phi}{2})\otimes(0+\mathbf{x})\otimes(\cos\frac{\phi}{2}-\mathbf{u}\sin\frac{\phi}{2})\\
=\mathbf{x}\cos^2\frac{\phi}{2}+(\mathbf{u}⊗\mathbf{x}−\mathbf{x}⊗\mathbf{u})\sin\frac{\phi}{2}\cos\frac{\phi}{2}−\mathbf{u}⊗\mathbf{x}⊗\mathbf{u}\sin^2 \frac{\phi}{2}\\
=\mathbf{x}\cos^2\frac{\phi}{2}+2(\mathbf{u}\times\mathbf{x})\sin\frac{\phi}{2}\cos\frac{\phi}{2}−(\mathbf{x}(\mathbf{u}^T\mathbf{u})-2\mathbf{u}(\mathbf{u}^T\mathbf{u}))\sin^2\frac\phi2\\
= \mathbf{x}(\cos^2\frac{\phi}{2}− \sin^2 \frac\phi2)+(\mathbf{u}\times\mathbf{x})(2\sin\frac\phi2\cos\frac{\phi}2)+\mathbf{u}(\mathbf{u}^T\mathbf{x})(2\sin^2\frac{\phi}2)\\
= \mathbf{x}\cos \phi + (\mathbf{u}×\mathbf{x})\sin \phi+ \mathbf{u}(\mathbf{u}^⊤\mathbf{x})(1 − \cos \phi)\\
= (\mathbf{x} − \mathbf{u u^⊤x})\cos \phi + (\mathbf{u×x}) \sin \phi + \mathbf{u u^⊤x}\\
=\mathbf{x}_⊥\cos\phi+(\mathbf{u}×\mathbf{x})\sin\phi+\mathbf{x}_{||} 
$$

### 2.4.6 流形SO(3)的双重覆盖

假设有一个单位四元数$\mathbf{q}$。考虑一个四维向量，四元数$\mathbf{q}$和单位四元数$\mathbf{q}_1=[1, 0, 0, 0]$之间的夹角$\theta$代表着原点的朝向，
$$
\cos\theta=\mathbf{q}_1^T\mathbf{q}=\mathbf{q}(1)=q_\omega
$$
同时，以轴角之中的旋转角表示为,
$$
\mathbf{q}=\begin{bmatrix}q_w\\\mathbf{q}_v\end{bmatrix}=\begin{bmatrix}\cos\phi/2\\\mathbf{u}\sin\phi/2\end{bmatrix}
$$
所以，我们可以得到$q_w=\cos\theta=\cos\phi/2$,所以四元数向量所属的4D空间中的identity是四元数在3D空间旋转角的一半，
$$
\theta=\phi/2
$$
所以也就可以解释为，如果两个四元数向量中的$\theta=\pi/2$，真实的在3D中的旋转已经变成了$\phi=\pi$，是转弯的一半。当四元数转了$\pi < \theta < 2\pi$,实际上代表了真实的三维旋转$2\pi < \phi < 4 \pi$。是旋转流形的第二次覆盖。

## 2.5 旋转矩阵和四元数

给定一个旋转向量$\mathbf{v=u}\phi$, 单位四元数和旋转矩阵的指数映射叫作旋转operator: $\mathbf{q}=\text{Exp}(\mathbf{u}\phi)$并且存在$\mathbf{R}=\text{Exp}(\mathbf{u}\phi)$这将会绕着轴$\mathbf{u}$将向量$\mathbf{x}$旋转角度$\phi$。即为，如果
$$
\forall\mathbf{v,x}\in\mathbb{R}^3,\mathbf{q}=\text{Exp}(\mathbf{v}),\mathbf{R}=\text{Exp}(\mathbf{v})
$$
从而得到，
$$
\mathbf{q}\otimes\mathbf{x}\otimes\mathbf{q}^*=\mathbf{Rx}
$$
两侧都是线性的，我们可以把它叫做四元数到旋转矩阵公式，
$$
\mathbf{R}=\begin{bmatrix}q_w^2+q_x^2-q_y^2-q_z^2 &  2(q_xq_y-q_wq_z)& 2(q_xq_z+q_wq_y)\\
2(q_xq_y+q_wq_z) & q^2_w-q^2_x+q^2_y-q^2_z & 2(q_yq_z-q_wq_x)\\
2(q_xq_z-q_wq_y) & 2(q_yq_z+q_wq_x) & q^2_w-q^2_x-q_y^2+q_z^2\end{bmatrix}
$$
记为$\mathbf{R}=\mathbf{R}\{\mathbf{q}\}$.根据公式(17-19)也可以写做：
$$
\mathbf{q\otimes x\otimes q^*}=\mathbf{[q^*]}_R[\mathbf{q}]_L\begin{bmatrix}0\\\mathbf{x}\end{bmatrix}=\begin{bmatrix}0\\\mathbf{Rx}\end{bmatrix}
$$
也有如下的形式：
$$
\mathbf{R}=(q_w^w-\mathbf{q}^T_v\mathbf{q}_v)\mathbf{I}+2\mathbf{q}_v\mathbf{q}_v^T+2q_w[\mathbf{q}_v]_\times
$$
旋转矩阵有着如下的性质：
$$
\mathbf{R}\{[1,0,0,0]^T\}=\mathbf{I}\\
\mathbf{R}\{-\mathbf{q}\}=\mathbf{R}\{\mathbf{q}\}\\
\mathbf{R}\{\mathbf{q}^*\}=\mathbf{R}\{\mathbf{q}\}^T\\
\mathbf{R}\{\mathbf{q}_1\otimes\mathbf{q}_2\}=\mathbf{R}\{\mathbf{q_1}\}\mathbf{R\{q_2\}}
$$
第一个意味着单位四元数代表着不旋转，第二个意味着一个四元数的相反数和该四元数的旋转矩阵相等，也就是SO(3)的双重覆盖性。第三个代表着一个四元数的共轭代表着该旋转的逆。第四个代表着四元数的乘法可以分解为矩阵的连乘。

此外，还有一个性质：
$$
\mathbf{R\{q^t\}=R\{q\}^t}
$$
## 2.6 旋转的组成（比较重要哦）

四元数组成与旋转矩阵相似，例如，可以写成四元数乘法和矩阵乘法，
$$
\mathbf{q}_{AC}=\mathbf{q}_{AB}\otimes \mathbf{q}_{BC}, \text{ }\mathbf{R}_{AC}=\mathbf{R}_{AB}\mathbf{R}_{BC}
$$
与向量的性质相同，
$$
\mathbf{x}_A=\mathbf{q}_{AB}\otimes\mathbf{x}_B\otimes\mathbf{q}_{AB}^*\\
=\mathbf{q}_{AB}\otimes(\mathbf{q}_{BC}\otimes\mathbf{x}_C\otimes\mathbf{q}_{BC}^*)\otimes\mathbf{q}^*_{AB}\\
=\mathbf{(q_{AB}\otimes q_{BC})\otimes x_c \otimes(q^*_{BC} \otimes q^*_{AB})}\\
=\mathbf{(q_{AB}\otimes q_{BC})\otimes x_c \otimes(q_{AB} \otimes q_{BC})}^*\\
=\mathbf{q_{AC}\otimes x_c \otimes q _{AC}^*}
$$
矩阵中，则有，
$$
\mathbf{x_A=R_{AB}X_B\\
=R_{AB}(R_{BC}x_C)\\
=(R_{AB}R_{BC})x_C\\
=R_{AC}x_C}
$$
一个小注释。好的记号能够清楚的表达出因素组成成分。$\mathbf{q}_{ji}$表示从状态$i$转到状态$j$。
$$
\mathbf{x_j=q_{ji}\otimes x_i \otimes q_{ji}^*, \text{ }x_j=R_{ji}x_i}
$$
同时，还有性质，
$$
\mathbf{q_{ji}=q^*_{ij}}
$$

## 2.7 球面插值

四元数非常方便插值，有两个四元数$\mathbf{q}_0$和$\mathbf{q}_1$。存在一个函数$\mathbf{q}$使得$\mathbf{q}(t),t\in[0,1]$,且$\mathbf{q}(0)=\mathbf{q}_0,\mathbf{q}(1)=\mathbf{q}_1$。

方法1:

第一种方式是用四元数代数，首先，计算从$\mathbf{q}_0$转到$\mathbf{q_1}$的微元$\Delta\mathbf{q}$，$\mathbf{q}_1=\mathbf{q}_0\otimes\Delta\mathbf{q}$,

