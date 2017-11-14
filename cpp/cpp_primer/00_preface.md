# Preface

## New standard

1. `auto` make the code in this edition easier to read and to understand.
2. smart pointers and move-enabled containers, let us write more sophisticated classes without having to contend with the intricacies of resource management.

## Run the GNU compilier `g++` to compile programs

```
g++ -o prog1 prog1.cc -std=c++0x
```

## Standard Input and Output Objects.

* cin - standard input, an object of type **istream** named **cin**.
* cout - standard output, an **ostream** object named **cout**.
* cerr - standard error, for warning and error messages.
* clog - for general information about the execution of the program.

## A program that uses IO library

The first line of our program

```
#include <iostream>
```
tells the compiler that we want to use the iostream library. 

### Writing to a stream

**endl** - a manipulator, has the effect of ending the current line and flushing the buffer associated with that device. Flushing the buffer ensures that all the output the program has generated so far is actually written to the output stream, rather than sitting in memory waiting to be written.

`<<` - The `<<` operator takes two operands: the left-hand operand must be an `ostream` object, the right-hand operand is a value to print. If we use `<<` twice, the operator returns its left-hand operand, the result of the first operator becomes the left-hand operand of the second. As a result, we can chain together output requests.

`>>` - The input operator. It takes an `istream` as its left-hand operand and an object an object as its right-hand operand. It reads data from the given `istream` and stores what was read in the given object. So,

`std::cin >> v1 >> v2;` is equivalent to `(std::cin >> v1) >> v2;`

## Primitive Built-in Types

| Type | Meaning | Minimum Size|
|------|---------|-------------|
| bool | boolean | NA|
| char | character| 8 bits|
| wchar_t | wide character | 16 bits|
| char16_t | Unicode character | 16 bits|
| char32_t | Unitcode character | 32 bits|
| short | short integer | 16 bits|
| int | integer | 16 bits |
| long | long integer | 32 bits|
| long long | long integer | 64 bits|
| float | single-precision floating-point | 6 | 6 significant digits|
| double | double-precision floating-point | 10 significant digits|
|long double | extended-precision floating-point| 10 significant digits|

### Machine-Level Representation of the Built-in Types

Computers store data as a sequence of bits, each holding a 0 or 1, such as 000110110111... Most computers deal with memory as chunks of bits of sizes that are powers of 2. The smallest chunk of addressable memory is referred to as a "byte." The basic unit of storage usually a small number of bytes, is referred to as a "word". In C++ a byte has at least as many bits as are needed to hold a character in the machine's basic character set.

Most computers associate a number (called an "address") with each byte in memory. This is address.

### Signed char

There are three distinct basic character types: `char`, `signed char` and `unsigned char`. In particular, `char` is not the same type as `signed char`. There are only two representations: signed and unsigned. The (plain) `char` type uses one of these representations. It depends on the **compilier**.

### Advice: Deciding which type to use

1. use `int` for integer arithmetic. `long` often have the same size as `int`. If your data values are larger than the minimum guranteed size of an `int`, use `long long`.
2. Do not use `char` or `bool` in arithmetic expressions. Computations using `char` are problematic because `char` is `signed` on some machines and `unsigned` on others. If need a tiny integer, explicitly specify either `signed char` or `unsigned char`.
3. Use `double` for floating-point computations; `float` usually does not have enough precision, and the cost of double-precision calculations versus single-precision is negligible. In fact, on some machines, double-precision operations are faster than single. The precision offered by long double usually is unnecessary and often entails considerable run-time cost.

### Type conversions

1. If we assign an out-of-range value to an object of unsigned type, the result is the remainer of the value modulo the number of values the target can hold. For example, assigning -1 to an 8-bit `unsigned char` we could get 255.
2. If we assign an out-of-range value to an object of signed type, the result is undefined. The program might appear to work, might crash, or produce garbage values.

### Caution: Don't Mix Signed and Unsigned Types

### Literals

| Prefix | Meaning | Type|
|---|---|---|
|0 | octal | - |
|0x | hexadecimal | - |
| u | Unicode 16 character | char16_t |
| U | Unicode 32 character | char32_t |
| L | wide character | wchar_t |
|u8 | utf-8 (string literals only) | char | 

| Suffix | Minimum Type |
|---|---|
|u or U | unsigned |
|l or L | long|
|ll or LL | long long |
| f or F | float |
| l or L | long double |

exponent specified using scientific notation

the exponent is indicated by either E or e:

|3.14159 | 3.14159E0 |0. |0e0 |.001|
|---|---|---|---|---|

A character enclosed within single quotes is a literal of type `char`. Zero or more characters enclosed in double quotation marks is a string literal:

```
'a' // character literal
"Hello world!" // string literal
```

The compiler appends a null character ('\0') to every string literal.

So
 
```
'A' represents the single character A,
the string literal "A" represents an array of two characters, the letter A and the null character. 
```
###Escape sequence 

Some characters that have special meanings. 

Newline `\n` horizontal tab `\t` alert(bell) `\a`
Vertical tab `\v` backspace `\b` double quote `\”`
Backslash `\\` question mark `\?` Single quote`\’`
Carriage return `\r` formfeed `\f`

### Boolean and pointer literals

True, false, nullptr

## initialization

Initialization is not assignment. Initialization happens when a variable is given a value when it is created. Assignment obliterates and object’s current value and replaces that value with a new one. 

## list initialization 

Initialization use curly brace. 

```
Int units_sold = 0;
Int units_sold = {0};
Int units_sold{0};
Int units_sold(0);
```

One important property: the compiler will not let us list initialize variables of built-in type if the initializer might lead to loss of information:

```
Long double ld=3.1415926536;
Int a{ld}, b = {ld}; //error
Int c{ld}, d = ld;//ok, but value will be truncated
```

With one exception, variables of built-in type defined inside a function are uninitialized. The value of an uninitialized variable of built-in type is undefined.

A declaration makes a name known to the program. A file that wants to use a name defined elewhere includes a declaration for that name.

A definition creates the associated entity.

In addition to specifying the name and type, a definition also allocates storage and may provide the variable with an initial value.

To obtain a declaration that is not also a definition, we add the `extern` keyword and may not provide an explicit initializer:

```
extern int i; //declares but does not define i
int j; //declares and defines j
```

Any declaration that includes an explicit initializeris a definition. Variables must be defined exactly once but can be declared many times.

## Nested Scopes

Once a name has been declared in a scope, that name can be used by scopes nested inside that scope. Names declared in the outer scope can also be redefined in an inner scope:

```
#include <iostream>
// Program for illustration purposes only: It is bad style for a function
// to use a global variable and also define a local variable with the same name int reused = 42; // reused has global scope
int main()
{
	int unique = 0; // unique has block scope
	// output #1: uses global reused; prints 42 0
	std::cout << reused << " " << unique << std::endl;
	int reused = 0; // new, local object named reused hides global reused // output #2: uses local reused; prints 0 0
	std::cout << reused << " " << unique << std::endl;
	// output #3: explicitly requests the global reused; prints 42 0
	std::cout << ::reused << " " << unique << std::endl;
	return 0; 
}
```

Output \# uses the operator to override the default scoping rules. The glocal scope has no name. Hence, when the scope operator has an empty left-hand side, it is a request to fetch the name on the right-hand side from the global scope. Thus, this expression uses the global `reused` and prints `42 0`.

### References

A reference defines an alternative name for an object. A reference type "refers to" another type. We define a reference type by writing a declarator of the form `&d`, where `d` is the name being declared:

```
int ival = 1024;
int &refVal = ival; //refVal refers to (is another name for) ival
int &refVal2; //error:a reference must be initialized
```

A reference is not an object. Instead, a reference is just another name for an already existing object.

After a reference has been defined, all operations on that reference are actually operations on the object to which the reference is bound:

```
refVal = 2; // assigns 2 to the object to which refVal refers, i.e., to ival int ii = refVal; // same as ii = ival
```

Because references are not objects, we may not define a reference to a reference.

```
// ok: refVal3 is bound to the object to which refVal is bound, i.e., to ival int &refVal3 = refVal;
// initializes i from the value in the object to which refVal is bound
int i = refVal; // ok: initializes i to the same value as ival
```

### Pointers

A pointer is a compound type that "points to" another type.We define a pointer type by writing a declarator of the form `*d`, where d is the name being defined. The `*` must be repeated for each pointer variable:

```
int *ip1, *ip2; // both ip1 and ip2 are pointers to int double dp, *dp2; // dp2 is a pointer to double; dp is a double

double dval;
double *pd = &dval; // ok: initializer is the address of a double
double *pd2 = pd; // ok: initializer is a pointer to double
int *pi = pd; // error: types of pi and pd differ
pi = &dval; // error: assigning the address of a double to a pointer to int

int ival = 42;
int *p = &ival; // p holds the address of ival; p is a pointer to ival cout << *p; // * yields the object to which p points; prints 42

```

#### Null Pointers

A null pointer does not point to any object.

```
int *p1 = nullptr; // equivalent to int *p1 = 0;
int *p2 = 0; // directly initializes p2 from the literal constant 0 // must #include cstdlib
int *p3 = NULL; // equivalent to int *p3 = 0;
```

