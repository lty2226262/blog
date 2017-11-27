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
```

## Library `vector` Type

