# Day 1 — Python Fundamentals

## Overview

Day 1 introduces the fundamental building blocks of Python programming. The topics covered establish the basic understanding required to write simple interactive Python programs.

### Topics Covered

- Print Statement
- String Manipulation
- User Input
- Variables
- Data Types
- Type Conversion
- Basic Arithmetic Operations

---

# 1. Print Statement

The `print()` function is used to display information in the Python console.

## Basic Syntax

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

The `print()` function can display strings, numbers, variables, calculations, and multiple values.

## Examples

```python
print("Hello")
print(25)
print(10 + 5)
```

Output:

```text
Hello
25
15
```

## Printing Multiple Values

Multiple values can be passed to `print()` by separating them with commas.

```python
name = "Sneha"
age = 19

print(name, age)
```

Output:

```text
Sneha 19
```

## Important Point

The `print()` function is primarily used to display information or results to the user.

---

# 2. Strings

A string is a sequence of characters used to represent text.

Strings are generally written inside single or double quotation marks.

```python
name = "Sneha"
city = 'Bangalore'
```

Both forms are valid.

```python
first_name = "Sneha"
message = 'Welcome to Python'
```

## String Concatenation

Concatenation means joining strings together.

The `+` operator can be used to concatenate strings.

```python
first_name = "Sneha"
last_name = "L"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Sneha L
```

The space between the two names is also a string:

```python
" "
```

---

# 3. String Indexing

Each character in a string has a position called an index.

Python uses **zero-based indexing**, meaning the first character is at index `0`.

For example:

```text
Python
012345
```

Therefore:

```python
word = "Python"

print(word[0])
print(word[1])
print(word[5])
```

Output:

```text
P
y
n
```

## Important Rule

The syntax for accessing a character is:

```python
string[index]
```

For example:

```python
name = "Python"

print(name[0])
```

Output:

```text
P
```

---

# 4. String Length

The `len()` function is used to determine the number of characters in a string.

```python
word = "Python"

print(len(word))
```

Output:

```text
6
```

The `len()` function counts all characters, including spaces.

Example:

```python
name = "Hello World"

print(len(name))
```

The space between the words is also counted.

---

# 5. User Input

The `input()` function allows a program to receive information from the user.

## Basic Syntax

```python
name = input("What is your name? ")
```

When the program runs, the user can enter a value.

Example:

```text
What is your name? Sneha
```

The entered value is stored in the variable `name`.

It can then be displayed using:

```python
print(name)
```

---

## Input and Print Together

```python
name = input("What is your name? ")

print("Hello " + name)
```

If the user enters:

```text
Sneha
```

The output will be:

```text
Hello Sneha
```

---

# 6. Important Property of input()

A very important concept is:

> `input()` returns the user's input as a string.

For example:

```python
age = input("What is your age? ")
```

If the user enters:

```text
19
```

Python initially treats the value as:

```python
"19"
```

rather than:

```python
19
```

This distinction becomes important when performing calculations.

---

# 7. Variables

A variable is a name that refers to a value stored by a program.

For example:

```python
name = "Sneha"
age = 19
```

Here:

- `name` refers to the value `"Sneha"`
- `age` refers to the value `19`

The `=` symbol is the **assignment operator**.

It assigns a value to a variable.

---

## Creating Variables

```python
name = "Sneha"
age = 19
course = "AI & DS"
```

The values can then be used throughout the program.

```python
print(name)
print(age)
print(course)
```

---

## Changing a Variable

The value stored in a variable can be changed.

```python
age = 19
age = 20

print(age)
```

Output:

```text
20
```

The most recent assignment determines the current value of the variable.

---

# 8. Variable Naming Rules

Python variable names should follow certain rules.

### Valid variable names

```python
name = "Sneha"
student_age = 19
total_marks = 450
first_name = "Sneha"
```

### Invalid variable names

```python
2name = "Sneha"
student age = 19
```

## Rules to Remember

A variable name:

1. Can contain letters, numbers, and underscores.
2. Cannot begin with a number.
3. Cannot contain spaces.
4. Cannot be a Python keyword.
5. Is case-sensitive.
6. Should preferably have a meaningful name.

For example:

```python
student_age = 19
```

is clearer than:

```python
x = 19
```

---

# 9. Python Naming Convention

Python commonly uses **snake_case** when naming variables.

Examples:

```python
first_name = "Sneha"
last_name = "L"
student_age = 19
total_score = 95
```

Using meaningful variable names improves readability and makes programs easier to maintain.

---

# 10. Data Types

A data type describes the kind of value stored in a variable.

Python has several built-in data types.

The basic types introduced on Day 1 are:

| Data Type | Meaning | Example |
|---|---|---|
| `str` | String/Text | `"Hello"` |
| `int` | Integer/Whole number | `19` |
| `float` | Decimal number | `19.5` |
| `bool` | Boolean value | `True` |

---

# 11. String — `str`

A string represents text.

```python
name = "Sneha"
```

The type of `name` is:

```text
str
```

Strings can contain letters, numbers, spaces, and special characters.

```python
message = "Welcome to Python!"
```

Even though numbers can appear inside quotation marks, they are still treated as strings.

```python
age = "19"
```

Here, `"19"` is a string.

---

# 12. Integer — `int`

An integer is a whole number without a decimal point.

Examples:

```python
age = 19
marks = 95
year = 2026
```

These values have the data type:

```text
int
```

---

# 13. Float — `float`

A float represents a number containing a decimal value.

Examples:

```python
height = 5.4
price = 99.50
temperature = 28.6
```

These values have the data type:

```text
float
```

---

# 14. Boolean — `bool`

A Boolean represents one of two possible values:

```python
True
False
```

Example:

```python
is_student = True
```

Boolean values are commonly used when a program needs to represent a yes/no or true/false condition.

---

# 15. Checking Data Types

The `type()` function can be used to determine the data type of a value.

```python
name = "Sneha"
age = 19
height = 5.4
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Understanding data types is important because different types of values behave differently in Python.

---

# 16. Type Conversion

Type conversion means changing a value from one data type into another.

Common conversion functions include:

```python
int()
float()
str()
bool()
```

---

## String to Integer

```python
age = "19"

age = int(age)

print(age)
```

The string `"19"` is converted into the integer `19`.

---

## Integer to String

```python
age = 19

age = str(age)

print(age)
```

The integer `19` is converted into the string `"19"`.

---

## String to Float

```python
price = "99.5"

price = float(price)

print(price)
```

The string is converted into a floating-point number.

---

# 17. Input with Type Conversion

Since `input()` returns a string, type conversion is often required when working with numerical input.

Instead of:

```python
age = input("Enter your age: ")
```

we can write:

```python
age = int(input("Enter your age: "))
```

Now the user's input is converted into an integer.

For example:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

If the user enters:

```text
19
```

The output is:

```text

# 20. Key Takeaways

By completing Day 1, the following concepts should be understood:

- The purpose of the `print()` function.
- How strings are created and manipulated.
- How string indexing works.
- How `len()` determines string length.
- How to receive user input using `input()`.
- How variables store and reference values.
- The rules for naming variables.
- Basic Python data types.
- The difference between strings, integers, floats, and Booleans.
- How to inspect a value's type using `type()`.
- How to convert values between common data types.
- Why numerical input often requires type conversion.
- Basic arithmetic operators.
- How these concepts can be combined to create simple interactive programs.

---

# 24. Day 1 Reflection

## Concepts I Understand

- Print statements
- Strings
- Input
- Variables
- Data types
- Type conversion
- Basic arithmetic

## Concepts I Need to Revise

- all basic concepts of python 


## What I Built

- Student Introduction Generator
- Other practice programs: 

---

# Day 1 Completion Checklist

- [x] Print statement
- [x] String manipulation
- [x] String indexing
- [x] User input
- [x] Variables
- [x] Basic data types
- [x] Type conversion
- [x] Arithmetic operators
- [x] Practice exercises
- [x] Mini project
- [x] Notes documented
```