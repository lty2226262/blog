# 2011年KinectFusion

是微软研究院提出首次实现基于RGB-D实时三维重建。作者Newcombe提出单目实时稠密重建算法
STAM、RGB-D实时稠密重建KinectFusion以及动态非刚体4D重建算法DynamicFusion。Davison是Newcombe的导师，SLAM领域的开山鼻祖级人物，伦敦帝国学院教授。

项目主页：https://www.microsoft.com/en-us/research/project/kinectfusion-project-page/

算法要点：在RGB-D相机出现以前，采用普通相机很难实现稠密重建(高精度结构光可以)，KinectFusion首次实现基于廉价小飞机相机的

实时刚体重建，把实时三维重建推广到商业化的地步。ICP算法估计位姿信息，TSDF模型表示重建场景（基于GPU的frame to model形式的RGB-D直接法和ICP算法成为位姿估计的标配，TSDF模型更新通常采用GPU实现）。使用固定体积的网格模型表示重建的三维场景，
只能重建固定大小的场景；TSDF模型将整个待重建的空间划分成等大小的网格，当重建体积较大或网格的空间分辨率较高时很消耗显
存；没有回环检测和回环优化，当相机移动距离较大时不可避免产生累计误差，造成重建场景漂移（虽然该算法使用frame to model形
式配准会减小累计误差，但当移动距离较大时重建的三维场景也会飘起来）

开源代码：可以使用KinFu，KinFu包含在PCL中，下载地址：http://pointclouds.org，预编译的Windows版本只有VS2008和VS2010，

因此如果想使用VS2013必须重新编译PCL源码

使用PCL中的KinectFusion：http://blog.csdn.net/fuxingyin/article/details/51508333

如何使用KinFu参考：http://pointclouds.org/documentation/tutorials/using_kinfu_large_scale.php#using-kinfu-large-scale

KinectFusion对显卡计算能力要求较高，估计计算能力要求在2.0以上，显存750MB

PCL实现的KinFu_Large_Scale可以重建大场景，但是没有做回环检测和回环优化，重见效果并不好

参考文献：

1. 2011-KinectFusion: Real-Time 3D Reconstruction and Interaction Using a MovingDepth Camera

2. 2011-KinectFusion: Real-Time Dense Surface Mapping and Tracking

关于KinectFusion算法网上很多资料介绍，这里不一一列举

# 2012年Kintinuous

ThomasWhelan在RSS Workshop on RGB-D会议上提出的，Whelan曾师从Davison，2017年就职
于Oculus。

算法要点：该算法是个比较完备的三维重建系统，位姿估计结合了ICP和直接法，GPU实现，位姿估计的精度鲁棒性都相对于其他算法如
InfiniTAM较好；使用TSDF模型重建三维模型；融合了回环检测和回环优化，史无前例的在实时三维刚体重建中使用embedded
deformation graph做非刚体变换，根据回环优化的结果更新点坐标，使回环的地方两次重建可以对齐。适合做大场景的三维重建。作者
发布的Demo视频中会还处理的比较赞，但发布代码中会还处理并不理想，可能作者没有开源比较好的源码

开源代码：https://github.com/mp3guy/Kintinuous，Ubuntu14.04

参考文献：

1. 2011-Kintinuous: Spatially Extended KinectFusion
2. A method and system for mapping an environment(US9412173B2)
3. 2013-Robust Real Time Visual Odometryfor Dense RGB-D Mapping
4. 2013-Deformation based Loop Closure forLarge Scale Dense RGB-D SLAM
5. 2014-Real Time large Scale Dense RGB-D SLAM with VolumereicFusion

分析参考：
1. http://blog.csdn.net/fuxingyin/article/details/51647750
2. http://blog.csdn.net/cattylsy/article/details/52239590

# 2013年VoxelHashing

斯坦佛大学的MatthiasNießner

项目主页：http://www.graphics.stanford.edu/~niessner/niessner2013hashing.html

算法要点：使用TSDF模型对三维进行建模，在建模时不是对整个空间都划分等大小的网格（解决TSDF模型显存消耗和计算消耗的问
题），只是在场景表面的周围划分网格。模型更新速度快、显存资源消耗少。2015年牛津大学Kähler提出的InfiniTAM是对
VoxelHashing的改进，算法不开源

开源代码：https://github.com/niessner/VoxelHashing，VS2012

参考文献：

1. 2013-Real-time 3D Reconstruction at Scale using Voxel Hashing

分析参考：
1. http://blog.csdn.net/fuxingyin/article/details/51707057
2. http://blog.csdn.net/fuxingyin/article/details/51721053(InfiniTAM)

# 2014年RGBDSLAMv2

德国弗莱堡大学的Felix Endres

项目主页：http://felixendres.github.io/rgbdslam_v2/

算法要点：Pose graph图优化，后端采用g2o，代码之间兼容ROS hydro版，基本不用配置即可运行

开源代码：
1. https://codeload.github.com/felixendres/rgbdslam_v2/legacy.zip/hydro zip
2. https://codeload.github.com/felixendres/rgbdslam_v2/legacy.tar.gz/hydro tar.gz

参考文献：
1. 2014-3D Mapping with an RGB-D Camera

运行参考：
1. http://blog.csdn.net/hitszzzc/article/details/41747173
2. http://www.cnblogs.com/gaoxiang12/p/4462518.html

# 2015年DynamicFusion

CVPR2015上获得最佳论文奖，Newcombe提出实现非刚体4D重建算法，可以用作人体重建

项目主页：http://grail.cs.washington.edu/projects/dynamicfusion/

算法要点：采用deformation graph进行优化
没有开源算法，顾暂不考虑

参考文献：
1. CVPR2015-DynamicFusion：Reconstruction and Tracking of Non-rigid Scenesin Real-Time

分析参考：
1. http://blog.csdn.net/u011091739/article/details/54408213

# 2015年ElasticFusion

Oculus的ThomasWhelan，Whelan曾师从Davison

算法要点：算法融合RGB-D估计位姿，对颜色图像通过颜色一致性约束计算位姿，对点云通过ICP算法计算位姿；使用Surfel模型，模型
更新通常采用OpenGL实现；通过全局和局部回环检测约束优化，deformation graph。适合重建房间大小的场景，适合静态场景重建，
代码没有做优化，重建较大场景时不适用

开源代码：https://github.com/mp3guy/ElasticFusion，Ubuntu14.04

参考文献：
1. 2015-ElasticFusion：Dense SLAM without A Pose Graph
2. 2016-ElasticFusion：Real-time Dense SLAM and Light Source Estimation

分析参考：
1. http://www.2cto.com/kf/201605/509969.html
2. http://blog.csdn.net/fuxingyin/article/details/51436430（重定位、回环检测）

# 2016年ORBSLAMv2

西班牙萨拉戈萨大学的

项目主页：http://webdiis.unizar.es/~raulmur/orbslam/

开源代码：https://github.com/raulmur/ORB_SLAM2

参考文献：
1. ORB-SLAM2: an Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras

运行参考：
1. http://www.cnblogs.com/gaoxiang12/p/5161223.html高博的视觉SLAM实战

# 2017年BundleFusion

斯坦佛大学的MatthiasNießner，使用局部小块优化和全局优化解决漂移和回环检测，并且使用
integration和de-integration方式解决位姿优化后重建场景更新问题；双显卡可以跑到30HZ，位姿优化和重建场景同时进行；算法适合
做小场景的三维扫描，不适合做AR

开放源码：暂未开放

参考文献：

1. 2017-BundleFusion: Real-time Globally Consistent 3D Reconstruction using Online Surface Re-integration

分析参考：
1、http://blog.csdn.net/fuxingyin/article/details/52921958
