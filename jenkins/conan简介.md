# conan 简介

1. 去中心化的包管理器

有几个小东西：

1. conan客户端： 包的创建和使用的逻辑。
2. conan服务器：可以方便地到自己的项目。
3. JFROG Artifactory： 提供repo。
4. JFROG BINTRAY： 给package提供免费的hosting 服务。可以免费提交repo。



## 二进制文件管理

1. 可以管理package的name，version，user和channel。

## 使用流程

1. 寻找依赖库

```
conan search Poco* --remote=conan-center
```

2. 得到一些版本信息

```
conan inspect Poco/1.9.0@pocoproject/stable
```

3. 在工程内写一个conanfile.txt

conanfile.txt

```
[requires]
Poco/1.9.0@pocoproject/stable

[generators]
cmake
```

4. 下一步：

```
conan profile new default --detect
conan profile update settings.compiler.libcxx=libstdc++11 default
```

之后执行

```
mkdir build && cd build
conan install ..
```





