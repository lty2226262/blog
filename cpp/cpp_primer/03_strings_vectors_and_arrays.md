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

```
isalnum(c)			//true if c is a letter or a digit
isalpha(c)			//true if c is a letter
iscntrl(c)			//true if c is a control character
isdigit(c)			//true if c is a digit
isgraph(c)			//true if c is not a space but is printable

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

```
string s("some string");
if(s.beigin() != s.end()) //make sure s is not empty
{
  auto it = s.begin();
  *it = toupper(*it); //只把第一个字符变成大写的了
}
```

