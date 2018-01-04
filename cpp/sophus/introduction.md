# Sophus 教程

## 1. 简介

李群是拓扑群，是光滑的流形。

| 群      | 描述              | 维度   | 矩阵代表      |
| ------ | --------------- | ---- | --------- |
| SO(3)  | 3D旋转            | 3    | 3D旋转矩阵    |
| SE(3)  | 3D刚体变换          | 6    | 齐次4向量线性变换 |
| SO(2)  | 2D旋转            | 1    | 2D旋转变化    |
| SE(2)  | 3D刚体变换          | 3    | 齐次3向量线性变换 |
| Sim(3) | 3D相似变换（刚体运动+缩放） | 7    | 齐次4向量线性变换 |

### 1.1 为什么用李群

方便composed，inverted,微分和插值。

### 1.2 李代数和其他性质

李代数是李群identity element附近的正切空间。正切空间和其他群元素有着相同的结构，但从一个正切空间到另一个正切空间要不断进行空间变换。基本元素叫做generator。所有的正切向量都是generator的线性组合。

重要的是，正切空间是用来表示群的微分性质的最优空间。速度，雅可比和变换的协方差都能在正切空间里很好的表示。

* 正切空间和群变换有着相同的自由度
* 指数映射可以把正切空间里的任何一个元素转换成矩阵变换
* Adjoint linearly和exactly可以把正切向量从一个正切空间变换到另一个正切空间

# 2. SO(3):三维空间的旋转

## 2.1 表达法

SO(3)代表着矩阵的三维旋转。composition和inversion是矩阵的乘法和转置。

李代数so(3)是3x3的skew-symmetric矩阵。generator是三个旋转的微分量，分别为：
$$
G_1=\begin{bmatrix}0 & 0 & 0\\
0 & 0 & -1\\
0 & 1 & 0\end{bmatrix},
G_2-1=\begin{bmatrix}0 & 0 & 1\\
0 & 0 & 0\\
-1 & 0 & 0\end{bmatrix},
G_3=\begin{bmatrix}0 & -1 & 0\\
1 & 0 & 0\\
0 & 0 & 0\end{bmatrix},
$$
后面的在：https://github.com/yujinrobot/sophus/blob/master/doc/lie_groups_for_2d_and_3d_transformations-ethan_eade.pdf