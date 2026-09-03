# Day 2 — Data Types, Type Conversion & Mathematical Operations

## Overview

Day 2 focuses on working with different data types in Python, identifying and converting between data types, handling type-related errors, and performing mathematical operations.

### Topics Covered

- Type Errors
- Type Checking
- Type Conversion
- Mathematical Operations
- Number Manipulation

---

# 1. Type Errors

A `TypeError` occurs when an operation is performed on incompatible data types.

For example:

```python
age = 19

print("I am " + age + " years old.")
```

This produces a `TypeError` because Python cannot directly concatenate a string and an integer using `+`.

The two values have different data types:

```text
"I am "  → str
19       → int
```

## Correct Approach

The integer can be converted into a string:

```python
age = 19

print("I am " + str(age) + " years old.")
```

---

# 2. Type Checking

Python provides the `type()` function to determine the data type of a value.

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

## Common Data Types

| Data Type | Description | Example |
|---|---|---|
| `str` | Text | `"Python"` |
| `int` | Whole number | `19` |
| `float` | Decimal number | `5.4` |
| `bool` | True/False value | `True` |

---

# 3. Type Conversion

Type conversion is the process of converting a value from one data type to another.

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
print(type(age))
```

Output:

```text
19
<class 'int'>
```

---

## String to Float

```python
price = "99.50"

price = float(price)

print(price)
print(type(price))
```

---

## Integer to String

```python
age = 19

age = str(age)

print(age)
print(type(age))
```

---

## Integer to Float

```python
number = 10

number = float(number)

print(number)
```

Output:

```text
10.0
```

---

# 4. Type Conversion with input()

The `input()` function always returns the user's input as a string.

For example:

```python
age = input("Enter your age: ")
```

Even if the user enters:

```text
19
```

Python receives it as:

```python
"19"
```

If we want to perform mathematical operations, the value should be converted.

```python
age = int(input("Enter your age: "))

print(age + 1)
```

If the user enters `19`, the output will be:

```text
20
```

---

# 5. Mathematical Operations

Python supports several mathematical operators.

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

## Addition

```python
result = 10 + 3
print(result)
```

Output:

```text
13
```

---

## Subtraction

```python
result = 10 - 3
print(result)
```

Output:

```text
7
```

---

## Multiplication

```python
result = 10 * 3
print(result)
```

Output:

```text
30
```

---

## Division

The `/` operator performs regular division.

```python
result = 10 / 3
print(result)
```

Output:

```text
3.3333333333333335
```

Division using `/` produces a floating-point result.

---

# 6. Floor Division

The `//` operator performs floor division.

It returns the whole-number portion of the division.

```python
result = 10 // 3

print(result)
```

Output:

```text
3
```

---

# 7. Modulus Operator

The `%` operator returns the remainder after division.

```python
result = 10 % 3

print(result)
```

Output:

```text
1
```

This is particularly useful when checking whether numbers are evenly divisible.

For example:

```python
number = 10

print(number % 2)
```

Output:

```text
0
```

A remainder of `0` means the number is evenly divisible by `2`.

---

# 8. Exponentiation

The `**` operator is used to raise a number to a power.

```python
result = 2 ** 3

print(result)
```

Output:

```text
8
```

This represents:

```text
2 × 2 × 2 = 8
```

---

# 9. Order of Operations

Python follows the standard mathematical order of operations.

For example:

```python
result = 3 + 5 * 2

print(result)
```

The multiplication is performed first:

```text
5 × 2 = 10
3 + 10 = 13
```

Therefore:

```text
13
```

Parentheses can be used when a specific operation needs to be performed first.

```python
result = (3 + 5) * 2

print(result)
```

Output:

```text
16
```

---

# 10. Number Manipulation

Python provides several ways to manipulate numerical values.

## Rounding Numbers

The `round()` function can be used to round a number.

```python
number = 3.14159

print(round(number))
```

Output:

```text
3
```

A specific number of decimal places can also be provided:

```python
number = 3.14159

print(round(number, 2))
```

Output:

```text
3.14
```

---

# 11. Assignment Operators

Python provides shorthand operators for modifying variables.

For example:

```python
score = 10

score += 5

print(score)
```

Output:

```text
15
```

The following operators are commonly used:

| Operator | Meaning |
|---|---|
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |

Example:

```python
score = 10

score += 5
score -= 2
score *= 2

print(score)
```

---

# 12. Working with Large Numbers

Python allows underscores to make large numbers easier to read.

Instead of:

```python
population = 1000000
```

we can write:

```python
population = 1_000_000
```

Both represent the same integer.

```python
print(1_000_000)
```

Output:

```text
1000000
```

The underscores are ignored by Python and are only used to improve readability.

---

# 13. Combining Input, Conversion and Mathematics

The concepts learned on Day 2 can be combined to create useful programs.

Example:

```python
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
```

This program demonstrates:

- User input
- Type conversion
- Variables
- Mathematical operators
- Output

---

# 14. Common Mistakes

## Mistake 1 — Adding a string and integer

Incorrect:

```python
age = 19

print("Age: " + age)
```

Correct:

```python
print("Age: " + str(age))
```

Or:

```python
print("Age:", age)
```

---

## Mistake 2 — Performing arithmetic on input without conversion

Incorrect:

```python
number = input("Enter a number: ")

print(number + 5)
```

`number` is a string.

Correct:

```python
number = int(input("Enter a number: "))

print(number + 5)
```

---

## Mistake 3 — Confusing `/`, `//`, and `%`

For:

```python
10 / 3
10 // 3
10 % 3
```

The results are approximately:

```text
3.333...
3
1
```

Remember:

- `/` → normal division
- `//` → floor division
- `%` → remainder

---

# 15. Practice Exercises

## Exercise 1 — Type Checker

Create variables containing:

- Your name
- Your age
- Your height
- Whether you are a student

Print the type of each variable using `type()`.

---

## Exercise 2 — Age in Different Units

Ask the user for their age in years.

Calculate approximately:

- Age in months
- Age in days

---

## Exercise 3 — Two Number Calculator

Ask the user for two numbers.

Display:

- Addition
- Subtraction
- Multiplication
- Division
- Floor division
- Remainder
- Exponentiation

---

## Exercise 4 — Even or Odd

Ask the user for an integer.

Use the modulus operator to determine whether the number is even or odd.

---

## Exercise 5 — BMI Calculator

Ask the user for:

- Weight in kilograms
- Height in metres

Calculate BMI using:

```text
BMI = weight / height²
```

---

# 16. Mini Project — Tip Calculator

Create a program that calculates how much each person should pay when splitting a restaurant bill.

The program should ask for:

- Total bill
- Number of people
- Tip percentage

Then calculate the final amount each person should pay.

Example:

```text
Welcome to the Tip Calculator!

What was the total bill? 100
How many people are splitting the bill? 4
What percentage tip would you like to give? 10

Each person should pay: 27.5
```

### Concepts Used

- `input()`
- `float()`
- `int()`
- Variables
- Arithmetic operators
- Division
- Percentage calculations
- `round()`
- `print()`

---

# 17. Key Takeaways

After completing Day 2, I should understand:

- What a `TypeError` is.
- Why incompatible data types can cause errors.
- How to check a value's type using `type()`.
- How to convert between common Python data types.
- Why `input()` generally produces a string.
- How to convert user input into numbers.
- Basic mathematical operators.
- The difference between `/`, `//`, and `%`.
- How exponentiation works using `**`.
- How Python follows mathematical order of operations.
- How to round numerical values.
- How assignment operators such as `+=` and `-=` work.
- How to improve readability of large numbers using underscores.

---

# Day 2 Completion Checklist

- [x] Type Errors
- [x] Type Checking
- [x] Type Conversion
- [x] Mathematical Operations
- [x] Number Manipulation
- [x] Practice Exercises
- [x] Tip Calculator
- [x] Notes documented
```