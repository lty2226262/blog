# STM32CubeMX环境搭建

## 参考资料

《STM32FX开发指南-HAL库版本》-4.8小节手把手入门STM32CubeMX

## 什么事STM32CubeMX？

STM32CubeMX是ST意法半导体近几年来大力推荐的STM32芯片图形化配置工具，允许用户使用图形化向导生成C初始化代码，可以大大减轻开发工作，时间和费用。

STM32CubeMX几乎覆盖了STM32全系列芯片。

##STM32CubeMX特性

1. 直观的选择MCU型号，可指定系列、封装、外设数量等条件
2. 微控制器图形化配置
3. 自动处理引脚冲突
4. 动态设置时钟树，生成系统时钟配置代码
5. 可以动态设置外围和中间件模式和初始化
6. 工号预测
7. c代码工程生成覆盖了STM32微控制器初始化编译软件，如IAR,KEIL,GCC等。。。

## STM32CubeMX和STM32Cube关系：

1. STM32Cube包含STM32CubeMX图形工具和STM32Cube库两个部分
2. 使用STM32CubeMX配置生成的代码，是基于STM32Cube库的
3. 不同的STM32系列芯片，会有不同的STM32Cube库支持，而STM32CubeMX图形工具只有一种

## 使用STM32Cube新建工程步骤

1. 初步建立工程
2. RCC基本配置
3. 时钟树配置：重要
4. 功能引脚配置
5. 生成工程源码
6. 编写用户程序

	1. 建立工程，配置RCC，HSE
	2. 从左至右： 25, HSE, M分频：25, N倍频: 360, P分频：2， PLLCLK， SYSCLK:180, 180， {/1，/4, /2}
	3. 在PinOut里查找引脚，单击选择功能
	4. 在configuration中找到gpio点击，设置参数。