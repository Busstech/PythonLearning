
# Lesson 2: Basic Operators

## Objective
In this lesson, you will learn:
1. How to use basic arithmetic operators in Python.
2. The role of assignment operators.
3. How to combine operators to perform calculations.

By the end of this lesson, you should be comfortable using operators to manipulate data in Python.

---

## 1. Arithmetic Operators
Arithmetic operators are used to perform mathematical calculations. Here are the most common ones:

| Operator | Description              | Example       | Result |
|----------|--------------------------|---------------|--------|
| `+`      | Addition                 | `5 + 3`      | `8`    |
| `-`      | Subtraction              | `5 - 3`      | `2`    |
| `*`      | Multiplication           | `5 * 3`      | `15`   |
| `/`      | Division                 | `5 / 2`      | `2.5`  |
| `//`     | Floor Division (no remainder) | `5 // 2` | `2`    |
| `%`      | Modulus (remainder)      | `5 % 2`      | `1`    |
| `**`     | Exponentiation           | `2 ** 3`     | `8`    |

### Example:
```python
a = 10
b = 3
print("Addition:", a + b)         # Output: 13
print("Subtraction:", a - b)      # Output: 7
print("Multiplication:", a * b)   # Output: 30
print("Division:", a / b)         # Output: 3.3333...
print("Floor Division:", a // b)  # Output: 3
print("Modulus:", a % b)          # Output: 1
print("Exponentiation:", a ** b)  # Output: 1000
```

---

## 2. Assignment Operators
Assignment operators are used to assign values to variables. The most common one is `=`, but there are others that combine assignment with an arithmetic operation.

| Operator | Example       | Equivalent To    | Description |
|----------|---------------|------------------|-------------|
| `=`      | `a = 5`      | `a = 5`         | Assigns value `5` to `a` |
| `+=`     | `a += 3`     | `a = a + 3`     | Adds `3` to `a` |
| `-=`     | `a -= 2`     | `a = a - 2`     | Subtracts `2` from `a` |
| `*=`     | `a *= 2`     | `a = a * 2`     | Multiplies `a` by `2` |
| `/=`     | `a /= 2`     | `a = a / 2`     | Divides `a` by `2` |
| `//=`    | `a //= 2`    | `a = a // 2`    | Floor-divides `a` by `2` |
| `%=`     | `a %= 2`     | `a = a % 2`     | Calculates the remainder of `a` divided by `2` |
| `**=`    | `a **= 3`    | `a = a ** 3`    | Raises `a` to the power of `3` |

### Example:
```python
x = 5
x += 3  # x is now 8
x -= 2  # x is now 6
x *= 4  # x is now 24
x /= 2  # x is now 12
print("Final value of x:", x)
```

---

## 3. Combining Operators
You can use multiple operators in a single line to perform complex calculations. Parentheses `()` are used to control the order of operations (just like in math).

### Example:
```python
result = (5 + 3) * 2 ** 2 / 4
print("Result:", result)  # Output: 8.0
```

### Explanation:
1. **Exponentiation** (`2 ** 2`) is calculated first.
2. **Addition** (`5 + 3`) is next because of the parentheses.
3. **Multiplication** and **Division** are performed from left to right.

---

## Practice Exercises

1. **Basic Arithmetic**: Write a program that calculates the area of a rectangle (length times width) and the perimeter (2 times the sum of length and width).
2. **Modulus Exercise**: Ask the user to input a number, then check if it’s even or odd using the modulus operator.
3. **Power Calculation**: Write a program that asks for a base and an exponent, then calculates the result.

---

## Homework

1. **Create a Basic Calculator**: Write a script that asks the user for two numbers and then performs the following calculations:
   - Adds them
   - Subtracts the second number from the first
   - Multiplies them
   - Divides the first number by the second
   - Outputs all results
2. **Savings Growth**: Imagine you have $100 in savings, and each year you increase it by 5%. Write a program that calculates how much you will have after 10 years, using assignment operators like `+=`.
3. **BMI Calculator**: Write a program that asks for a user’s weight (in kg) and height (in meters), then calculates their BMI using the formula `BMI = weight / (height ** 2)`. Display the result.

---

## Summary
- Python has arithmetic operators for performing basic math and assignment operators for updating variable values.
- You can use parentheses to control the order of operations in complex calculations.
- Practice combining operators to get comfortable with calculations in Python.

Try out the exercises and homework to solidify your understanding of operators!
