[TOC]

# Strings, Vectors, and arrays

## Headers should not include using declarations

A program that didn't intend to use the specified library name might encounter unexpected name conflicts.

## Library `string` Type

```
#include <string>
using std::string;
```

Ways to Initialize a `string`.

```
string s1;              //Default initialization; s1 is the empty string.
string s2(s1); 			//s2 is a copy of s1
string s2 = s1; 		//Equivalent to s2(s1), s2 is a copy of s1.
string s3("value");		//s3 is a copy of the string literal, not including the null.
string s3 = "value";	//Equivaluent to s3("value"), s3 is a copy of the string literal.
string s4(n,'c');		//Initialize s4 with n copies of the character 'c'.
```

### operations on `string`

```

os << s 				//Writes s onto output stream os. Return os.
is >> s 				//Reads whitespace-separated string from is into s. Return is.
getline(is, s)			//Reads a line of input from is into s. Return is.
s.empty()				// Return trus if s is empty; otherwise returns false.
s.size()				//Returns the number of characters in s.
s[n]					//Returns a reference to the char at position n is s; positions start at 0.
s1 + s2					//Returns a string thst is the concatenation of s1 and s2.
s1 = s2					//Replaces characters in s1 with a copy of s2.
s1 == s2				//The strings s1 and s2 are equal if they contain the same characters.
s1 != s2				//Equality is case-sensitive.
<, <=, >, >=			//Comparisons are case-sensitive and use dictionary ordering.

```

### Reading an Unknown Number of strings

```
int main(){
	string word;
	while (cin >> word) // read until end-of-file
		cout << word << endl; // write each word followed by a new line
	return 0;	
}
```

### Using `getline` to Read an entire line

Sometimes we do not want to ignore the whitespace in our input. In such cases, we can use the getline function instead of the `>>` operator.

```
int main()
{
	string line;
	// read input a line at a time until end-of-file 
	while (getline(cin, line))
		cout << line << endl;
	return 0;
}

```

### Dealing with the characters in a `string`

Defined in `cctype` header. `c` is the character.

```cpp

isalnum(c)			//true if c is a letter or a digit
isalpha(c)			//true if c is a letter
iscntrl(c)			//true if c is a control character
isdigit(c)			//true if c is a digit
isgraph(c)			//true if c is not a space but is printable
```


### C++ 11 new feature: `range-based for`

If we want to do something to every character in a `string`, the best approach is to use a `range for`. The syntactic form is

```
	for (declaration: expression)
		statement
```

As a simple example, we can use a range `for` to print each character from a `string` on its own line of output:

```
	string str("some string");
	//print the characters in str one character to a line
	for (auto c : str)
		cout << c << endl;
```

### The `decltype` Type Specifier

`decltype` return the type of its operand. The compiler analyzes the experssion to determine its type but does not evaluate the expression:

```
decltype(f()) sum = x; // sum has whatever type f types
```

When we apply `decltype` to a variable without any parentheses, we get the type of that variable. If we wrap the variable's name in one or more sets of parentheses, the compiler will evaluate the operand as an expression.

```
//decltype of a parenthesized variable is always a reference
decltype((i)) d; //error: d is int& and must be initialized
decltype(i) e; //ok: e is an(uninitialized) int
```

As a somewhat more complicated example, we'll use a range `for` and the `ispunct` function to count the number of punctuation characters in a `string`:

```
string s("Hello World!!!");
//punct_cnt has the same type that s.size returns;
decltype(s.size()) punct_cnt = 0;
//count the number of punctuation characters in s
for (auto c:s)			//for every char in s
	if (ispunct(c))		//if the character is punctuation
		++punct_cnt;	//increment the punctuation counter
cout << punct_cnt
	<< "punctuation characters in " << s << endl;
```

#### Using a range `for` to change the characters in a `string`

```
	string s("Hello World!!!");
	//convert s to uppercase
	for (auto &c: s)	// for every char in s (note: c is a reference)
		c = toupper(c);	// c is a reference, so the assignment changes the char in s 
	cout << s << endl;
```

## Library `vector` Type

`vector` is a `container`. A `vector` is a class template. C++ has both class and function templates. 

Templates are not themselves functions or classes. They can be thought of a sinstructions to the compilier for generating classes or functions. The process that the compiler uses to create classes or functions from is called instantiation. 

We use a pair of angle brackets following the template's name.

```
Note

vector is a template, not a type. Types generated from vector must include the element type, for expample, vector<int>.
```

### Defining and Initializing `vector`

How to define vectors.

| `vector<T> v1`                | vector里的类型是T，v1是空的     |
| ----------------------------- | ---------------------- |
| `vector<T> v2(v1)`            | v2 copy v1里的每一个元素      |
| `vector<T> v2 = v1`           | V2 copy v1里的每一个元素      |
| `vector<T> v3(n, val)`        | v3有着n个元素，每一个都是val      |
| `vector<T> v5{a, b, c,...}`   | v5有着很多对象，每一个调用相应的初始化函数 |
| `vector<T> v4(n)`             | v4有着n个初始值的元素           |
| `vector<T> v5 = {a, b, c...}` | 与v5一样的                 |

### List Initializing a vector

使用列表进行初始化

```Cpp
vector<string> articles = {"a", "an", "the"};
```

1. 84页使用复制构造函数，我们只能提供一个单独的initializer.
2. 73页使用in-class initializer, 可以使用copy initialization或者`{}`curly braces. 
3. 提供一个列表的元素，只能用`{}`curly brace.

### Creating a Specified number of elements.

```
vector<int> ivec(10, -1); //ten int elements, each initialized to -1
vector<string> svec(10, "hi!"); //ten strings; each element is "hi!"
```

### Value Initialization

圆括号和尖括号的区别

```
vector<int> v1(10); // v1 has ten elements with value 0
vector<int> v2{10}; //v2 has one element with value 10
vector<int> v3(10, 1); //v3 has ten elements with value 1
vector<int> v4{10, 1}; //v4 has two elements with values 10 and 1
```

当使用尖括号初始化的时候，我们就不能使用initializer对对象进行列表初始化，这些值将会被用于构造对象。例如，为了列表初始化一个string的vector，我们必须提供那些可以被当作string的值，所以就不会混淆列表初始化和指定size了。

```
vector<string> v5{"hi"}; //list initialization: v5 has one element
vector<string> v6("hi"); //error: can't construct a vector from a string literal
vector<string> v7{10};  // v7 has ten default-initialized elements
vector<string> v8{10, "hi"}; //v8 has ten elements with value "hi"
```

只有v5是list initialized。我们不能使用int来初始化string，所以v7和v8不是元素的initlaizer。如果列表初始化不可能的话，编译器将会寻找其他方式利用给定的值初始化目标。

### 增加`vector`的元素

使用`push_back`.

#### 重要概念：使`vector`有效率的变大

vector能够有效的增长，所以没必要定义一个固定长度的vector。例外为所有的元素必须要是相同的值。定义一个空的`vector`然后增加元素是很有效率的。

#### `vector`的其他操作

```
v.empty()		//Returns trus if v is empty
v.size()
v.push_back(t)
v[n]
v1 = v2  		//Replaces the elements in v1 with a copy of the elements in v2
v1 = {a, b, c}	//Replaces the elements in v1 with a copy of the elements in the comma-separated list.
v1 == v2 		//v1 and v2 are equal if they have the same number and each element in v1 is equal to the corresponding element in v2.
<, <=, >, >=	//Have their normal meanings using dictionary ordering.
```

对于取vector中的元素，我们的取法和在`string`中取字符相同。我们可以用一个range for 来处理`vector`中的所有元素。

```cpp
vector<int> v{1,2,3,4,5,6,7,8,9};
for (auto &i : v) 	//for each element in v(i is a reference)
  i *= i;			//square the element value
for (auto i : v)	//for each element in v
  cout << i << " ";	//print the element
cout << endl;
```

## 3.4 迭代器

迭代器给我们对象的非直接获取方式。有效的迭代器denote容器中的一个元素或者容器最后一个元素的后面的position。其他的迭代器是无效的。

与指针类似，迭代器不直接给我们对象。这个对象是容器中的元素或者是string里的一个字符。

### 3.4.1 使用迭代器

与指针不同，我们不用迭代器的地址。替代的事，有有迭代器的类型都存在返回迭代器的成员。举例来说，这些类型有着叫`begin`或者`end`的成员。使用方法为：

```cpp
auto b = v.begin(), e = v.end(); //b和e有着相同的类型
```

`end`迭代器返回的是容器里`one past the end`的位置。这个迭代器指向的位置是不存在任何元素的。只是作为一个记号。

```
如果容器是空的时候，start和end是相等的，都为off-the-end迭代器。
```

#### 迭代器的运算符

| *iter        | 返回element的reference |
| ------------ | ------------------- |
| Iter->mem    | 取成员，与(*iter).mem相同  |
| ++iter       | 下一个元素               |
| —iter        | 上一个元素               |
| iter1==iter2 | 比较两个迭代器是否相同         |
| Iter1!=iter2 | 是否不同                |

例子：

```cpp
string s("some string");
if(s.beigin() != s.end()) //make sure s is not empty
{
  auto it = s.begin();
  *it = toupper(*it); //只把第一个字符变成大写的了
}
```



#### 小贴士

在`for`循环中使用`!=`和迭代器，而不是使用`<`。因为迭代器不一定会有`<`。

#### 迭代器的类型

`string`类的`size()`的返回值数据类型为`string::size_type`。但是我们经常都用`auto`。相似的，我们也不知道迭代器的准确类型。实际上，有以下几种：

```cpp
vector<int>::iterator it; //it 又可读又可写，为vector<int>元素
string::iterator it2;    //it2 可以读写，是string
vector<int>::const_iterator it3; //it3只读
string::const_iterator it4; //it4 只读
```

`const_iterator`和`const 指针`一样。只能读，不能写。如果一个vector是const的，iterator只能用`const_iterator`。否则两个都能用。

#### `begin`和`end`操作

这个类型是取决于对象是不是`const`的。如果对象是`const`类型为`const_iterator`。否则返回为`iterator`。

```Cpp
vector<int> v;
const vector<int> cv;
auto it1 = v.begin(); //it1是vector<int>::iterator
auto it2 = cv.begin(); //it2是vector<int>::const_iterator
```

所以说我们经常会不想用默认构造类型而用`const`的。另外一种是`cbegin`和`cend`。这两个是只读。

```cpp
auto it3 = v.cbegin(); //it3是vector<int>::const_iterator
```

#### 结合dereference和member access的情况

如果两个都有的话，比如`it`是一个`vector<string>`的迭代器，则加括号是必要的。没有括号就错了。为了简化，可以用`->`

```cpp
(*it).empty();
*it.empty(); //错的
it->empty(); //对的
```

#### 可能使迭代器失效的一些情况

有一些操作，比如说像`push_back`可能会改变`vector`的大小，可能导致迭代器失效。

```cpp
值得注意的是，在循环中不能在容器中添加或删除元素（改变size的操作），否则会造成迭代器混乱。
```

### 3.4.2 迭代器的算术

| `iter+n`           | 后向的第n个元素，必须保证在容器里 |
| ------------------ | ----------------- |
| `iter-n`           | 前向                |
| `iter+=n, iter-=n` | 类似                |
| `iter1-iter2`      | 得到元素个数            |
| `>,>=,<,<=`        | 关系                |

#### 算术的应用

`auto mid = vi.begin() + vi.size()/2`

如果vi有20个元素，指向第十个。可以用于二分搜索。

```Cpp
//text must be sorted
//beg and end will denote the range we're searching

auto beg = text.begin(), end = text.end();
auto mid = text.begin() + (end - beg)/2; // original midpoint // while there are still elements to look at and we haven't yet found sought 
while (mid != end && *mid != sought) {
	if (sought < *mid)// is the element we want in the first half?
      end = mid;// if so, adjust the range to ignore the secondhalf.
	else// the element we want is in the second half
      beg = mid + 1;// start looking with the element just after mid
  	mid = beg + (end - beg)/2; // new midpoint
}
```

## 3.5 Array

定长，不能加元素。初始化用`a[d]`，`a`是名字`d`是元素个数。必须是const。

```Cpp
unsigned cnt = 42; // not a constant expression 
constexpr unsigned sz = 42; // constant expression
// constexpr see § 2.4.4 (p. 66)

int arr[10];// array of ten ints
int *parr[sz];// array of 42 pointers to int
string bad[cnt];// error: cnt is not a constant expression
string strs[get_size()]; // ok if get_size is constexpr, error otherwise
```



#### `constexpr`

Constant expression. 常量表达式，数值不能改变，在编译时候已经运行。

```Cpp
const int max_files = 20; // max_files is a constant expression const 
int limit = max_files + 1; // limit is a constant expression 
int staff_size = 27; // staff_size is not a constant expression 
const int sz = get_size(); // sz is not a constant expression
```

虽然`staff_size`是字符初始化的，但是不是常量。虽然sz是常量但是是等到运行时才能运行，并不是编译时运行的，不是常量。

我们有时候可以把一个表达式声明成常量表达式。使用`constexpr`也就代表着默认其中所有的量都为`const`。

```Cpp
constexpr int mf = 20; // 20 is a constant expression 
constexpr int limit = mf + 1; // mf + 1 is a constant expression 
constexpr int sz = size(); // ok only if size is a constexpr function
```

#### Array元素的默认初始化

可以用list初始化。如果用list初始化我们可以忽略维数。如果声明的维数比list里的多，则后面的调用默认值。

```Cpp
const unsigned sz = 3;
int ia1[sz] = {0,1,2}; // array of three ints with values 0, 1, 2
int a2[] = {0, 1, 2};// an array of dimension 3
int a3[5] = {0, 1, 2}; // equivalent to a3[] = {0, 1, 2, 0, 0}
string a4[3] = {"hi", "bye"}; // same as a4[] = {"hi", "bye", ""} 
int a5[2] = {0,1,2}; // error: too many initializers
```

#### String的特殊初始化方法

可以用literal形式初始化，会自动补`null`。

```Cpp
char a1[] = {'C', '+', '+'}; // list initialization, no null
char a2[] = {'C', '+', '+', '\0'}; // list initialization, explicit null 
char a3[] = "C++"; // null terminator added automatically
const char a4[6] = "Daniel"; // error: no space for the null!
```

`a1`的维度是3，`a2,a3`的维度是4，`a4`为错的。

#### No copy or assignment

array不存在复制或者赋值。

```cpp
int a[] = {0, 1, 2}; // array of three ints
int a2[] = a; // error: cannot initialize one array with another 
a2 = a; // error: cannot assign one array to another
```

#### 理解复杂的array声明

array里什么都可以存，即使是指针也可以存。

```cpp
int *ptrs[10]; // ptrs is an array of ten pointers to int 
int &refs[10] = /* ? */; // error: no arrays of references
int (*Parray)[10] = &arr; // Parray points to an array of ten ints
int (&arrRef)[10] = arr; // arrRef refers to an array of ten ints
```

类型定义应该从右往左看。首先看到的是array的size是10，名字叫`ptrs`, 类型是到`int`的指针。

读`Parray`的时候要注意从里往外读，`Parray`代表这是一个指针，向右看能知道它的大小是10，向左看能知道元素是`int`。因此，`Parray`是一个有着十个整数的数组的指针。同样的,`&arrRef`里的`&`也代表着他是一个引用。

当然，这个用多少个modifier也没什么限制。

```cpp
int *(&arry)[10] = ptrs; //arry is a reference to an array of ten pointers
```

与`string`和`vector`相类似，我们也可以用`for`循环来遍历。

```
int scores[10] = {};
for (auto i: scores){
  cout <<i << " " << endl;
}
```

### 3.5.3 指针和数组

当我们用数组时，编译器经常把它转化成了指针。通常来说，当我们使用下标时，实际上是告诉了我们在数组中的位置。所以我们也可以用引用符号得到指针。

```
string nums[] = {"one", "two", "three"}; // array of strings string *p = &nums[0]; // p points to the first element in nums

string *p2 = nums; // equivalent to p2 = &nums[0]
```

默认使用的数组是地址。

```cpp
int ia[] = {0,1,2,3,4,5,6,7,8,9}; // ia is an array of ten ints
auto ia2(ia); // ia2 is an int* that points to the first element in ia
ia2 = 42; // error: ia2 is a pointer, and we can't assign an int to a pointer

auto ia2(&ia[0]); // now it's clear that ia2 has type int*
```

值得注意的是当我们用decltype时并不是这样的，例如`decltype(ia)`就是一个十个元素的数组。

```cpp
decltype(ia) ia3 = {0,1,2,3,4,5,6,7,8,9};
ia3 = p; // error: can't assign an int* to an array 
ia3[4] = i; // ok: assigns the value of i to an element in ia3
```

#### 指针是可以迭代的

我们可以用递增操作来使元素指向下一个。

```cpp
int arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int *p = arr; //p points to the first element in arr
++p;
```

与容器中的迭代器一样，我们可以指定off-the-end指针。这个仅仅能用于初始化`e`的时候。

```cpp
int *e = &arr[10];

for(int *b = arr; b!= e; ++b)
	cout << *b << endl; //print the elements in arr
```

虽然我们可以指定off-the-end指针，但是这样做是“错误的”。所以，在c++11里，我们用`begin`和`end`。然而，数列并不是类，所以我们不能用成员函数。我们写成：

```Cpp
int ia[] = {0,1,2,3,4,5,6,7,8,9}; // ia is an array of ten ints 
int *beg = begin(ia); // pointer to the first element in ia
int *last = end(ia); // pointer one past the last element in ia
```

也可以很方便安全的处理循环。

```cpp
// pbeg points to the first and pend points just past the last element in arr 
int *pbeg = begin(arr), *pend = end(arr);
// find the first negative element, stopping if we've seen all the elements 
while (pbeg != pend && *pbeg >= 0)
	++pbeg;
```

