# 时钟系统源码讲解

## 时钟系统配置一般步骤：

1. 使能pwr时钟： 调用函数
```
__HAL_RC_PWR_CLK_ENABLE()
```
2. 设置调压器输出电压级别：调用函数
```
__HAL_PWR_VOLTAGESCALING_CONFIG()
```
3. 选择是否开启Over-Driver功能：调用参数
```
HAL_PWREx_EnableOverDrive()
```
4. 配置时钟源相关参数：调用参数
```
HAL_RCC_OscConfig()
```
5. 配置系统时钟源以及AHB, APB1和APB2的分频系数：调用参数
```
HAL_RCC_ClockConfig()
```

# Systick滴答定时器

参考资料 cortexM3权威指南 第八章

* Systick定时器，是一个简单的定时器，对于ST的CM3，CM4，CM7内核芯片，都有Systick定时器。
* Systick定时器常用来做延时，或者实现系统的心跳时钟。这样可以节省MCU资源，不用浪费一个定时器。比如UCOS中，分时复用，需要一个最小的时间戳，一般在STM32+UCOS系统中，都采用Systick做UCOS心跳时钟。
* Systick定时器就是系统滴答定时器，一个24位的倒计数定时器，记到0时，将从RELOAD寄存器中自动重装载定时初值。只要不把它在SysTick控制及状态寄存器中的使能位清楚，就永不停息，即使在睡眠模式下也能正常工作。
* SysTick定时器被捆绑在NVIC中，用于产生SYSTICK异常(异常号)
* Systick中断的优先级也可以设置。

## 4个Systick寄存器

CTRL SysTick控制和状态寄存器

LOAD SysTick自动重装载除值寄存器

VAL SysTick当前值寄存器

CALIB SysTick校准值寄存器

## SysTick控制和状态寄存器-CTRL

|段位| 名称 |  类型  |复位值|描述|
| --------   | -----:   | :----: |:----: |:----: |
| 16        | COUNTFlAG     |   R    | 0 | 如果在上次读取本寄存器后，SysTick已经数到了0，则该位为1.如果读取该位，该位将自动清零|
| 2        | CLKSOURCE      |   R/W    | 0 | 0 = 外部时钟源(STCLK), 1 = 内核时钟(FCLK)|
| 1        | TICKINT      |   R/W    | 0 | SysTick定位器的使能位|

对于STM32，外部时钟源是HCLK(AHB总线时钟)的1/8，内核时钟是HCLK时钟

配置函数：HAL_SYSTICK_CLKSourceConfig();

SysTick_CLKSOurceConfig函数：

配置SysTick定时器经过多少个tick周期开启一次中断





