# environment settings

## driver download

1. MDK5.21A
2. ST LINK driver(simulation and code download)
3. CH340(serial download)
4. XCOM or SSCOM3.3 (serial debugging assistant)

# MCU minimal system

The simplest circuitry which could let a MCU works normally.

1. power
2. download programs
3. reset
4. timer
5. boot launch mode option
6. backup battery(optional)

## power

1. 数字电源vdd +3.3v
2. vss数字地 0
3. vdda模拟电源 +3.3v
4. vssa模拟地 0

vdd和vdda之间一般接一个简单的低通滤波器即可

vss和vssa之

查datasheet引脚功能描述

多个数字地，数字电源

## 复位电路

复位引脚：nrst 设计复位电路：通过按键，与51单片机相同

## 时钟电路

高速时钟，低速时钟（外部时钟）

高速时钟：产生系统时钟。25MHz(F767)

低速时钟：外界稳定的，给RTC或com口使用。 osc\_in,osc\_out接晶振的引脚。

## BOOT启动模式选择

boot0和boot1引脚。选择启动模式，直接通过跳线帽进行不同模式的启动。

下载，从flash启动等。。

硬件下载电路：下载程序时不用更改跳线帽，阿波罗。

## 下载电路

1. swd（多），需要两根通信线连接到单片机的引脚，通信引脚只有两个
2. jtag（最小系统用的不多，电路复杂）
3. 串口isp下载（多）不需要进行程序的调试。usb转ttl或者232等。。。

## 后备电池电路

并不是必须的vbat，纽扣电池给后备区域，可以用后备区域保存一些数据。

#开发板资源介绍

## F429和F767区别

F429 只支持SPI FLASH， F7支持QSPI FLASH，外部看不出来。

F767 没有boot1引脚，只有boot0

## 参考资料
开发指南（寄存器版本）第1，2章

## 核心板

### 电源
1. 5v，3.3v电源输入/输出焊点。
2. micro usb接口。
3. 底板上的电源供电。板对板接口。

### 复位

复位电路连接到复位引脚

### 下载

SWD接口，串口1的焊盘，地，rx，tx

### 启动模式引脚

100k电阻接地。通过两个跳线帽连接。

### 时钟部分

核心板上晶振

### 后备电池

焊接在底板上

spi flash 32MB

eeprom 断电保存

rgb lcd接口连接到rgb屏幕上

nand flash存储器 512mb

sdram 存储器 32mb

LED指示灯 红色

WAKEUP按键 连接到引脚上

## 底板

右上角电源适配器，6v-24v宽电压输入。

两个usb口可以给开发板供电。

右部 5v, 3.3v输入/输出排针，若有外部电源则可向外部输出供电。

核心板上有复位按钮。

开发板左边有20pin jtag接口swd/jtag都支持。串口下载。连接到ch340。

四个按键，io口引脚。

# stm32初探

### 什么是stm32

* 新的基于arm内核的32位mcu系列。
	* 内核为arm公司为要求高性能、低成本、低功耗的嵌入式应用专门设计的cortex-M内核
	* 标准的arm架构
* 超前的体系结构
	- 高性能
	- 低电压
	- 低功耗
	- 创新的内核以及外设
* 简单易用/自由/低风险

### Cortex内核

* Cortex-M4采用ARMv7-ME架构

ARMv7架构定义了三大分工明确的系列：

"A"系列：面向尖端的基于虚拟内存的操作系统和用户应用

"R"系列：针对实时系统

"M"系列：对微控制器。

* Cortex-M3采用ARMv7-M架构，Cortex-M0采用ARMv6-M架构，Cortex-A5/A8采用ARMv7-A架构，传统的ARM7系列采用的是ARMv4T架构。

### M3 vs M4

更低的功耗

更高级的外设等等

# MDK安装

1. 在官方下载，填表

2. 芯片支持包获取

## USB串口使用

### USB串口作用

1. 可以当串口使用。
2. 如果连接到STM32的串口1可以用串口下载程序。（F7不支持）
3. 也可以用usb供电。

### 安装驱动

CH340驱动

插到下面的usb口会自动下载驱动。

st-link一端插到电脑，另一端插到stlink口。安装stlink驱动

# ST-LINK

## ST-LINK 与stm32的硬件连接

jtag接口，20pin

## 配置过程

参考ppt： 8，程序下载方法2：STLINK程序下载

## 编译程序

点击mdk里的左边小箭头编译一次。

## 下载程序

点击mdk里的魔术棒，debug选项卡，use st-link debugger， 点击右侧settings

unit里选st-link, 选择port和max。选择 flash download选项卡

erase sector， 右侧三个小对号点上。

选择add，添加相应类型的芯片，查手册可以查到

debug选项卡内run to main()选择上

utilities选项卡中选择use debug driver 和 update target before debugging

配置完成，点击下载load

# 新建工程模板：寄存器版本

1. 新建工程目录， 复制需要的文件到工程目录
2. 把工程需要的文件添加到工程
3. 在MDK中设置头文件存放路径
4. 配置MDK:全局宏定义等
5. 编写用户函数
6. 添加ALIENTEK系统文件夹SYSTEM

## 步骤

1. 新建文件夹/temp
2. 在/temp下新建文件夹/USER
3. 新建工程保存到/temp/USER/temp
4. 找到stm32f767寄存器工程所需文件和路径 .s文件直接放到USER/下，.h文件放到/temp/HEADER下。
5. 右键temp->manage project items->选中分组->add files选择启动.s文件。
6. 点击魔术棒,c/c++选项卡再添加头文件include path。
7. 全局宏定义，点击魔术棒,c/c++选项卡define下输入STM32F767xx

## 程序编写

		#include "stm32f7xx.h"
		
## 引入正点原子system文件夹

之后右键管理导入设置

# HAL库入门

## 固件库和寄存器的区别？

IO口的状态控制可以直接对寄存器进行控制。

stm32寄存器数量过多，直接操作寄存器

两种固件库：HAL库，标准库。

什么是固件库？

固件库就是函数的集合(API)，把寄存器操作封装起来。

## 是不是不需要对寄存器有了解？

固件库不是万能的。想要全面的掌握STM32，必须对寄存器有一定的了解。

对于寄存器，大家不需要死记硬背每个寄存器名称和作用，只需要大致的了解配置过程，这样在开发中遇到问题就可以通过调试直接查看寄存器配置，找出问题。

## HAL库包介绍

Drives/BSP 官方开发板支持文件

CMSIS 根据cmsis标准确定的一些文件， Cortex Microcontroller Software Interface Standard (CMSIS)

###HAL库描述

* 启动文件： stm32f767xx.s 自动文件，引导进入systemInit和main函数
* 外设和HAL库相关文件： stm32f7xx.h 顶层头文件，根据芯片型号包含具体芯片头文件。
* 内核头文件
* 用户程序文件

# HAL库版本

参考资料： stm32f7开发指南-hal库指南

## 新建工程模板

* 作用：方便编写用户代码
* 开发环境: MDK5
* 所需软件包: HAL库包

## 步骤

1. 复制所需要文件到工程包中。
2. 把工程文件引入工程中。
3. 设置头文件包含路径。
4. mdk设置（全局宏定义，编译文件存放路径等）
5. 编写用户程序
6. 添加ALIENTEK系统文件夹SYSTEM
7. 修改相关文件参数适配开发板

</br>

1. 按照excel表格引入
2. 选中target1右键，manage

# GPIO

GPIO general purpose input output

STM32共176个引脚中，140个是做io口，36个做电源引脚/复位引脚/启动模式引脚/晶振引脚/调试下载引脚。

* IO口有9组：PA~PI, PA0-PA15
* 其中PA~PH每组16个IO， PI只有12个引脚
* 一共有140个IO口

复用引脚： 一个IO既可以作为IO口使用，也可以作为通用IO口。

通过开关控制相同的IO口引脚组，可以大大节省IO口资源

## 如何查看外设资源：stm32参考资料 选型手册

##如何查看GPIO引脚功能： 硬件资料 芯片资料 STM32F767IGT6.pdf

# STM32 GPIO的8种工作模式：

##4种输入模式：

* 输入浮空
* 输入上拉
* 输入下拉
* 模拟输入：输入电压模拟信号

##4种输出模式（带上下拉）：

* 开漏输出（带上拉或者下拉）
* 开漏复用功能（带上拉或者下拉）
* 推挽式输出（带上拉或者下拉）
* 推挽式复用功能（带上拉或者下拉）

## 4种最大输出速度：

- 2MHz 低速
- 25M 中速
- 50M 快速
- 100M 高速

## 开漏输出模式

可以通过读取输入寄存器读取，只可以输出最低电平，高电平得靠外部电阻拉高。输出端相当于三极管的集电极 要得到高电平需要上拉电阻才行。适合于做电流型的驱动，其吸收电流的能力相对强。

## 推挽输出模式

可以输出强高低电平，连接数字器件

# GPIO寄存器配置

每组gpio端口的寄存器包括：

* 一个端口模式寄存器（GPIOx_MODER）
* 一个端口输出类型寄存器(GPIOx_OTYPER)
* 一个端口输出速度寄存器（GPIOx_OSPEEDR）
* 一个端口上拉下拉寄存器（GPIOx_PURDR）
* 一个端口输入数据寄存器（GPIOx_IDR）
* 一个端口输出数据寄存器（GPIOx_ODR）
* 一个端口置位/复位寄存器(GPIOx_BSRR)
* 一个端口配置锁存寄存器(GPIOx_LCKR)
* 两个复用功能寄存器（低位GPIOx_AFRL & GPIOx_AFRH）

0~3 称为32位配置寄存器
4~5 称为32位数据寄存器
6 为 32位置位/复位寄存器
7 为 32位锁存寄存器
8~9 为32位复用功能共寄存器

