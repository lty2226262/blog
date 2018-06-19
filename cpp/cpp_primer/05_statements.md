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





