[TOC]

# 5. Statement

### 5.3.2 Switch表达式

switch一定要跟break。break会终止现在的控制流。如果没有的话就依次运行。如果没有break且什么都不满足则依次运行。。

所以不用break的时候也有用，计算元音个数：

```cpp
unsigned vowelCnt = 0;
// ...
switch (ch)
{
    //any occurrence of a, e, i, o, or u increments vowelCnt
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
    	++vowelCnt;
    	break;
}
```

#### 如果在switch里定义了变量

直接写会出错，必须加大括号。

### 5.4.2 for循环

#### 5.4.2.1 多重定义

```cpp
for (decltype(v.size()) i =0, sz = v.size(); i != sz; ++i)
	v.push_back(v[i]);
```

### 5.4.4 do while 条件式

先执行一次后判断。

## 5.5 跳转符

### 5.5.1 break声明

结束最近的while, do while, for 或者switch.

### 5.5.2 continue

只能在while, do while和for使用

### 5.5.3 用goto语句

程序不应该用goto，很难懂而且不好改。

```cpp
goto end;

end: return;
```

end是label。

## 5.6 try和exception handling

### 5.6.1 `throw`表达式

回忆一下：

```cpp
Sales_item item1, item2;
cin >> item1 >> item2;
// first check that item1 and item2 represent the same book
if (item1.isbn() == item2.isbn()) {
	cout << item1 + item2 << endl;
	return 0; // indicate success 
} else {
	cerr << "Data must refer to same ISBN" << endl;
	return -1; // indicate failure 
}
```

实际上，相加的程序必须与用户交互程序分离。

```cpp
//firsr check that the data are for the same item
if (item1.isbn() != item2.isbn())
    throw runtime_error("Data must refer to the same ISBN");
//if we're stll here, the ISBNs are the same
cout << item1 + item2 << endl;
```

### 5.6.2 `try` 字块

```cpp
try {
	program-statements
} catch (exception-declaration) {
	handler-statements
} catch (exception-declaration) {
	handler-statements 
} //...
```

#### 5.6.2.1 写一个handler

```cpp
while (cin >> item1 >> item2) { 
    try {
        // execute code that will add the two Sales_items
		// if the addition fails, the code throws a runtime_error exception
    } catch (runtime_error err) {
        // remind the user that the ISBNs must match and prompt for another pair 
        cout << err.what()
            << "\nTry Again? Enter y or n" << endl; char c;
        cin >> c;
        if (!cin || c == 'n')
            break; // break out of the while loop
    }
}
```

#### 函数在寻找handler的时候会退出

如果在一个catch chain里找不到的话，会执行一个库函数terminate。

#### 注意：写一个exception安全的代码是很难的

要好好理解这句话：异常中断了程序的正常流程。异常发生时，调用者请求的一部分计算可能已经完成了，另一部分尚未完成。那些在异常发生期间正确执行了“清理”工作的程序被称作异常安全（exception safe）的代码。编写异常安全的代码非常困难。

我们必须时刻清楚异常什么发生异常，资源没有泄漏，对象有效，程序状态正确等。

### 5.6.3 标准异常

这些类包含在四个头文件里：

* exception头文件包含最通用的头文件。只说了有异常没有额外的信息。
* stdexcept头文件提供了一些通用的错误类型。
* new头文件定义了一些`bad_alloc`异常类型。
* `type_info`头文件定义了一些`bad_cast`异常。

![image-20180622101032726](https://ws4.sinaimg.cn/large/006tNc79gy1fsjqg0azmyj310k0fok0e.jpg)

异常类型只有一个操作叫做what.没有参数并且返回一个c-style的字符串。