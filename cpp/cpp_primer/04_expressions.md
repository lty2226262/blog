[TOC]

# 4. Expressions

## 4.1 Fundamentals

## 4.1.1 Basic Concepts

Unary（一元）操作符和binary（二元） 操作符。

Unary Operators: `&`,` *` 取地址和去引用。

二元操作符：`==`和`*`相等和乘法。

还有一个三元的操作符，一个无限元的操作符。

优先级和相同优先级的优先程度。

#### 右值和左值

右值： Expression that yields a value but not the associated location, if any, of that value.

左值：An expression that yields an object or function. A nonconst lvalue that denotes an object may be the left-hand operand of assignment.

左值可以在一个assignment的左手边，而右值就不行。

每一个c++里的表达式不是右值就是左值。在C++里，左值表达式表示一个对象或者一个函数。然而，一些左值，例如`const`，并不是代表赋值的。此外，一些能够返回对象的是右值表达式，不是左值。粗略滴说，当我们用一个对象的右值时我们用这个对象的数值，用左值时用这个对象的标志符（在内存中的位置）。当我们需要左值时我们可以用个右值，反过来不行🙅‍♂️。

* 赋值操作需要一个（非const）的左值作为它左手操作符，并且把它变成一个左值。
* 取址需要一个左手操作符，并且把它变成一个右值，返回一个指针。
* dereference和下标和迭代器的dereference还有string和vector的下标都是返回左值的。
* 递增和递减也都返回左值。

### 4.1.2 优先级 

有两个或多个操作符的表达式是复合表达式。优先级决定了谁和谁一组。编程的人可以重写这些规则：通过使用括号。

* Precedence: 3 + 4 * 5 = 23,不是35.
* associativity: 20-15-3 = 2 不是8.

如下表所示，每一个相同的栏有相同的优先级，比下一个栏的优先级高。

| Associativity     | Operator      | function               | use                   |
| ----------------- | ------------- | ---------------------- | --------------------- |
| L                 | ::            | Global scope           | ::name                |
| L                 | ::            | Class scope            | Class::name           |
| L                 | ::            | Namespace scope        | Namespace::name       |
| ---------------   | ------------  | ------------------     | -----------------     |
| L                 | .             | Member selectors       | Object.member         |
| L                 | ->            | Member selectors       | Pointer->member       |
| L                 | []            | Subscript              | expr[expr]            |
| L                 | ()            | function call          | name(expr_list)       |
| L                 | ()            | Type construction      | type(expr_list)       |
| ----------------  | ------------  | ----------------       | -----------------     |
| R                 | ++            | postfix increment      | lvalue++              |
| R                 | --            | postfix decrement      | lvalue--              |
| R                 | typeid        | type ID                | typeid(type)          |
| R                 | typeid        | Run-time type ID       | typeid(expr)          |
| R                 | explicit cast | type conversion        | cast_name<type>(expr) |
| ----------------- | ---------     | ------------------     | ------------------    |
| R                 | ++            | prefix increment       | ++lvalue              |
| R                 | --            | prefix decrement       | —lvalue               |
| R                 | ~             | bitwise NOT            | ~expr                 |
| R                 | !             | logical NOT            | !expr                 |
| R                 | -             | unary minus            | -expr                 |
| R                 | +             | Unary plus             | +expr                 |
| R                 | *             | dereference            | *expr                 |
| R                 | &             | Address-of             | &lvalue               |
| R                 | ()            | Type conversion        | (type)expr            |
| R                 | sizeof        | size of object         | sizeof expr           |
| R                 | sizeof        | size of type           | sizeof(type)          |
| R                 | sizeof..      | size of parameter pack | sizeof…(name)         |
| R                 | new           | allocate object        | new type              |
| R                 | new[]         | allocate array         | new type[size]        |
| R                 | delete        | deallocate object      | delete expr           |
| R                 | delete[]      | deallocate array       | delete[] expr         |
| R                 | noexcept      | can expr throw         | noexcept(expr)        |
| -------------     | ---------     | ----------------       | ----------------      |
| L                 | ->*           | ptr to member select   | ptr->*ptr_to_member   |
| L                 | .*            | ptr to member select   | obj.*ptr_to_member    |
| -------------     | --------      | -----------------      | -----------------     |
| L                 | *             | multiply               | expr * expr           |
| L                 | /             | divide                 | expr / expr           |
| L                 | %             | modulo(remainder)      | expr % expr           |
| --------------    | --------      | ------------------     | -----------------     |
| L                 | +             | add                    | expr + expr           |
| L                 | -             | subtract               | expr - expr           |
| --------------    | -------       | -----------------      | -----------------     |
| L                 | <<            | bitwise shift left     | expr << expr          |
| L                 | `>>`          | bitwise shift right    | expr >> expr          |
| -------------     | ---------     | ----------------       | -----------------     |
| L                 | <             | less than              | expr < expr           |
| L                 | <=            | less than or equal     | expr <= expr          |
| L                 | >             | greater than           | expr > expr           |
| L                 | `>=`          | greater than or equal  | expr >= expr          |
| ---------------   | ----------    | -----------------      | -------------------   |
| L                 | ==            | equality               | expr == expr          |
| L                 | !=            | inequality             | expr != expr          |
| ----------------  | ---------     | -----------------      | --------------------  |
| L                 | &             | bitwise AND            | expr & expr           |
| ----------------  | --------      | -----------------      | --------------------  |
| L                 | ^             | bitwise XOR            | expr ^ expr           |
| ---------------   | --------      | ----------------       | -----------------     |
| L                 | \|            | bitwise OR             | expr \| expr          |
| --------------    | ---------     | -----------------      | -----------------     |
| L                 | &&            | logical AND            | expr && expr          |
| -------------     | ---------     | ------------------     | -----------------     |
| L                 | \|\|          | logical OR             | expr \|\| expr        |
| -------------     | --------      | -----------------      | -----------------     |
| R                 | ?:            | conditional            | expr?expr:expr        |
| --------------    | -------       | ------------------     | -----------------     |
| R                 | =             | assignment             | lvalue = expr         |
| R                 | *=, /=, %=,   | compound assign        | lvalue += expr        |
| R                 | +=, -=,       |                        |                       |
| R                 | <<=, >>=,     |                        |                       |
| R                 | &=, \|=, ^=   |                        |                       |
| --------------    | ---------     | --------------------   | -----------------     |
| R                 | throw         | throw exception        | throw expr            |
| -----------       | -------       | ---------------        | ---------------       |
| L                 | ,             | comma                  | expr, expr            |
| ----------        | ---------     | ----------------       | --------------        |

### 4.1.3 等式的顺序

Precedence 指定了操作符是如何分组的。在下面的表达式中：

```cpp
int i = f1() * f2();
```

我们知道了$f1$和$f2$一定是在乘法完成之前被调用的。但是我们不能知道$f1$是不是在$f2$之前被调用的。

由于没有指定执行顺序，`<<`符号并不保证什么时候运行该程序。例如，下面的表达式就是undefined：

```cpp
int i = 0;
cout << i << " " << ++i << endl; //undefined
```

如果先运行了`++i`则结果是`1 1`，否则可能是`0 1`。这个结果是没有明确定义的。

还有一个例子：

```cpp
f() + g() * h() + j()
```

并没有保证四个函数谁先运行谁后运行。

#### 小建议：管理复合表达式

1. 使用括号
2. 当该一个表达式值时候，不要在另一个地方也用这个表达式。

## 算术表达式

precedence：

| 表达式         | 函数            | 使用           |
| ----------- | ------------- | ------------ |
| +           | 一元加           | + expr       |
| -           | 一元减           | - expr       |
| ----------- | ------------- | -----------  |
| *           | 乘法            | expr * expr  |
| /           | 除法            | expr / expr  |
| %           | 取余数           | expr % expr  |
| ----------  | -----------   | ------------ |
| +           | 加法            | expr + expr  |
| -           | 减法            | expr - expr  |

#### 注意： 溢出和其它算术错误

例如 `short i = 32767;` 

`i++`将导致溢出。undefined value

取整新标准都是将小数剪掉（向0规约）。

`m % (-n)`和`m % n`等价

`(-m) % n`和 `- m % n`等价

## 4.3 逻辑和关系操作符

所有的逻辑操作符和关系操作符都是右值，返回值也是右值。

`&&`和`||`都是先运行左面再运行后面。采取short-circuit evaluation策略：

* 当且仅当`&&`的左边是`true`的时候才接着算。
* 当且仅当`||`的左边是`false`的时候才接着算。

一些利用这些特质的写法：

```
index != s.size() && !isspace(s[index])
```

首先先运行前面的没有达到末尾，如果符合则运行后面。

```cpp
// s 是常数的引用，传址但是不能更改
for (const auto &s : text){ //for each element in text
  cout << s; //print the current element
  //blank lines and those that end with a period get a newline
  if (s.empty() || s[s.size() - 1] == '.')
  {
    cout << endl;
  } else
  {
    cout << " "; //otherwise just separate with a space
  }
}
```

值得注意的是，我们使用s是reference，因为text和string会很大，copy起来很占内存，因为不想改所以写成const。

### 关系操作符

```cpp
//oops! this condition compares k to the bool result of i < j
if (i < j < k) //true if k is larger than 1!
```

`i<j`返回的是0或者1

## 4.4 赋值操作符

赋值符号的左手边必须是一个可以更改的左值，

```cpp
int i = 0, j = 0, k = 0; //initializations, not assignment
const int ci = i; //initilization, not assignment
```

以下的几个都是不合法的：

```cpp
1024 = k; //数字是右值
i + j = k; //算术表达式是右值
ci = k; // ci是常量
```

右手边的类型会被转化成左手边的类型。

在新标准里，可以用花括号。

```cpp
k = {3.14}; //error: narrowing conversion
vector<int> vi;
vi = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; //vi now have 10 elements
```

每个数据类型定义了上面的操作的具体含义，对于vector，vector模板定义了操作符。

#### 赋值符号是right associative

```cpp
int ival, jval;
ival = jval = 0; //ok: each is 0
```

#### 赋值符号有着低的precedence

为什么在条件里使用赋值符号是有必要的呢？

```cpp
// a verbose and therefore more error-prone way to write this loop
int i = get_value(); // get remaining values
while (i != 42){
  // do something ...
  i = get_value(); // get remaining values
}
```

分开写了，容易出错

```cpp
int i;
// a better way to write our loop -- what the condition does is now clearer
while ((i = get_value()) != 42){
  // do something ...
}
```

如果没有括号呢，`!=`将会比较`get_value`和42。i将会变成true或者false，明显不对哦。

#### 复合赋值符号

```cpp
+= -= *= /= %= <<= >>= &= ^= |=
```

## 4.5 递增符号和递减符号

两种方式，一种写前面，一种写后面。

```cpp
int i = 0, j;
j = ++i;  // j = 1; i = 1: prefix yields the incremented value
j = i++;  // j = 1; i = 2: postfix yields the unicremented value
```

#### 建议：仅仅在不得不用的时候再用后缀表达式

这个可能对c语言使用者很震惊。原因很简单： 避免了不必要的操作。使用后置运算符首先需要一个容器来存放未增加的值，对于复杂的容器，是一笔不小的开销，养成习惯！

#### 结合dereference和递增

后缀递增的优先级是高于解引用的，所以`*pbeg++`是与`*(pbeg++)`等价的。所以解引用作用的是未进行递增操作的。返回的是原对象的一个copy。

#### 建议：简洁就是美

写成

 ```cpp
cout << *iter++ << endl;
 ```

而不要写成

```cpp
cout << *iter << endl;
++iter;
```

下面这种虽然更清楚，但是要习惯使用上面的表达式，不容易出错。

## 4.6 成员获取操作符

点和箭头。注意.的优先级比`*`优先级更高。所以`*p.size()`是不合法的。

## 4.7 条件操作符

可以嵌套。

```cpp
finalgrade = (grade > 90) ? "high pass"
						  : (grade < 60) ? "fail" : "pass";
```

但是很难懂，尽量避免超过2层的嵌套。

条件操作符优先级非常之低。所以尽量都要用括号。

```cpp
cout << ((grade < 60) ? "fail" : "pass"); //prints pass or fail
cout << (grade < 60) ? "fail" : "pass"; //prints 1 or 0!
cout << grade < 60 ? "fail" : "pass"; //error: compares cout to 60
```

## 4.8 按位操作符



### 移位操作符的优先级问题

```cpp
cout << "hi" << "there" << endl;
```

实际上是

```cpp
((cout << "hi") << "there") << endl;
```

注意优先级情况。

```cpp
cout << 42 + 10; //ok: + has higher precedence, so the sum is printed
cout << (10 < 42); //ok: parentheses force intended grouping; prints 1
cout << 10 < 42; // error: attempt to compare cout to 42
```

## 4.9 sizeof 操作符

sizeof会返回字节大小，返回值是const。

可以有两种表示方式：

```cpp
sizeof(type)
sizeof expr
```



```cpp
Sales_data data, *p;
sizeof(Sales_data); //Sales_data的大小
sizeof data; //data类型的大小，与sizeof(Sales_data)一样
sizeof p; //size of a pointer
sizeof *p; //size of the type to which p points.和sizeof(Sales_data)一样
sizeof data.revenue; //Sales_data的revenue的大小
sizeof Sales_data::revenue; //和上面的一样
```

sizeof使用：

1. `sizeof char` 是`char`的字节数大小
2. `sizeof` 一个引用返回的是引用类型的大小。
3. `sizeof`指针返回的是要存一个指针所需要的大小
4. `sizeof`一个解引用的指针返回的是这个东西的类型。
5. `sizeof`一个数组是全数组的大小，注意sizeof不会把数组转化成一个指针。
6. `sizeof`一个string或者vector返回的是fixed part的大小，并不是使用的大小。

## 4.10 逗号操作符

 从左到右执行的。左边的执行了但是结果被忽略掉。右边执行结果是返回值。当处在for循环的时候：

```cpp
vector<int>::size_type cnt = ivec.size();
// assign values from size... 1 to the elements in ivec
for (vector<int>::size_type ix = 0; ix != ivec.size(); ++ix, --cnt)
	ivec[ix] = cnt;
```

## 4.11 类型转换

举例：

```cpp
int ival = 3.541 + 3; // the compiler might warn about loss of precision
```

默认情况下，3.541是double，3是int。

#### 什么时候会发生implicit conversions？

* 在大多数表达式中，比int还小的整型类型首先会转成一个比整型大一点的整型。
* 在条件表达式中，非布尔的表达式将会转化成bool。
* 在初始化过程中，initializer会把类型转化成变量的类型；在赋值时，右手边的表达式类型会转成左手边的类型。
* 在算术表达式或关系表达式等使用多种类型的表达式时，类型被转化为一个常用类型。
* 第六章里还会有详解，发生在调用函数时。

### 4.11.1 算术转化

算术转化的代表着一个分级的转化过程，其余的形式都转化成widest的类型。

#### 整型提升(Integral Promotions)

把一个小整型转化成一个大整型。例如，在当所有的值都满足`int`时，把`bool, char, signed char, unsigned char, short, unsigned short`等都提升成int。如果不符合的话，提升为`unsigned int`。就比如，bool的false是0，true是1。

大的char（wchar_t, char16_t, char32_t）会被转成int, unsigned int, long, unsigned long, long long, 或者unsigned long long等一个能盛下该变量的值。

#### 无符号类型操作的操作对象

如果一个操作符的操作对象有着不同的类型，这些操作对象会转化成统一的类型。如果有操作对象是unsigned类型的话，操作对象转成什么就取决于整型对象在机器中的相对大小。

就一般而言，首先会发生整型提升。如果结果类型符合标准，就不进行额外的转换了。如果同号就小的转成大的。

unsigned符号要比signed大。

```cpp
bool flag; 
short sval; 
int ival; 
long lval; 
float fval;
char cval; 
unsigned short usval; 
unsigned int uival; 
unsigned long ulval; 
double dval;

3.14159L + 'a'; //'a' promoted to int, then that int converted to long double
dval + ival; // ival converted to double
dval + fval; // fval converted to double
ival = dval; // dval converted (by truncation) to int
flag = dval; // if dval is 0, then flag is false, otherwise true
cval + fval; // cval promoted to int, then that int converted to float
sval + cval; // sval and cval promoted to int
cval + lval; // cval converted to long
ival + ulval; // ival converted to unsigned long
usval + ival; // promotion depends on the size of unsigned short and int
uival + lval; // conversion depends on the size of unsigned int and long

```

### 4.11.2 其他种类的implicit 转换

Array to pointer转换：

```cpp
int ia[10]; //array of ten ints
int* ip = ia; //convert ia to a pointer to the first element
```

pointer 转换：

整数数值常数0或者nullptr可以转化成任何指针类型。非常数类型的指针可以转化成`void *`。任何类型的指针都可以转为`const void *`。

bool转换：

如果一个指针或者arithmetic值是0，则转成false，否则就是true。

const转换：

非常指针可以转化为常指针，引用也是。

```cpp
int i;
const int &j = i; //convert a nonconst to a reference to const int
const int *p = &i; //convert address of a nonconst to the address of a const
int &r = j, *q = p; //error: conversion from const to nonconst not allowed
```

反过来是不行的。

### 4.11.3 显式转换

#### Warning

casts是危险的操作，虽然有时候必须要有。

```cpp
cast-name<type>(expressions);
```

其中，type是转换的目标类型。expressions是转换原始值。

cast-name包括：

```c
static_cast
dynamic_cast
const_cast
reinterpret_cast
```

static_cast用于把一个大类型转化为小的类型。防止编译器报警。

#### const_cast

const_cast可以转换一个低级别的操作对象。

```cpp
const char *pc;
char *p = const_cast<char*>(pc); // ok: but writing through p is undefined
```

使用这个将非const的转成const的是有效的。然而，使用`const_cast`来使const可写是没有定义的。

```cpp
const char *cp;
char *q = static_cast<char*>(cp); // error: static_cast can't cast away const
static_cast<string>(cp); //ok: converts string literal to string
const_cast<string>(cp); //error: const_cast only changes constness
```

const_cast常常用于重载。

#### reinterpret_cast

这个是很危险的。

```cpp
int *ip;
char* pc = reinterpret_cast<char*>(ip);
```

这个什么错都不会报。但是当运行：

``` cpp
string str(pc);
```

时候，就会报run-time behavior错。

#### warning

这个reinterpret_cast本质上依赖于机器。必须对编译实现非常了解才能知道怎么不用错。

 



