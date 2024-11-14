
# Lesson 1: Variables and Data Types

## Objective
In this lesson, you will learn:
1. What variables are and how to create them in Python.
2. The different data types in Python and when to use each one.
3. How to use and display variables effectively.

By the end of this lesson, you should be able to create variables, assign values to them, and understand the basic data types in Python.

---

## 1. Introduction to Variables
A **variable** is like a container that holds information you want to use later. In Python, variables can store different types of data, such as numbers, text, or true/false values.

### Key Points:
- Variables are created when you assign a value to them.
- Use the `=` sign to assign a value to a variable.

### Syntax:
```python
variable_name = value
```

### Example:
```python
name = "Alice"    # Stores a string
age = 25          # Stores an integer
height = 5.8      # Stores a float
is_student = True # Stores a boolean
```

In this example:
- `name` is a variable storing text ("Alice").
- `age` holds a whole number.
- `height` holds a decimal (float).
- `is_student` holds a True or False value (boolean).

---

## 2. Rules for Naming Variables
- Variable names should start with a letter or an underscore (`_`).
- They cannot start with a number or contain spaces.
- Only letters, numbers, and underscores are allowed.
- Variable names are case-sensitive (`name` and `Name` are different).

### Good Examples:
```python
my_age = 30
favorite_color = "blue"
```

### Bad Examples:
```python
1st_name = "Alice"  # Invalid, starts with a number
my age = 30         # Invalid, contains a space
```

---

## 3. Python Data Types

### Common Data Types in Python:
1. **Integer (`int`)**: Whole numbers, without a decimal.
   ```python
   age = 25
   ```
2. **Float (`float`)**: Numbers with decimals.
   ```python
   height = 5.8
   ```
3. **String (`str`)**: Text data, written inside single or double quotes.
   ```python
   name = "Alice"
   ```
4. **Boolean (`bool`)**: Represents True or False values.
   ```python
   is_student = True
   ```

### Data Type Examples:
```python
# Integer
num_apples = 5

# Float
price_per_apple = 0.5

# String
greeting = "Hello, world!"

# Boolean
is_raining = False
```

---

## 4. Using `print()` to Display Variables
You can use the `print()` function to display the value of a variable. This is useful for checking the values you've stored.

### Example:
```python
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)
```

**Output:**
```
Name: Alice
Age: 25
```

### Combining Text and Variables:
You can also combine strings and variables in a print statement.
```python
print("Hello, my name is", name, "and I am", age, "years old.")
```

---

## 5. Checking Data Types with `type()`
You can use the `type()` function to check the data type of a variable.

### Example:
```python
name = "Alice"
print(type(name))  # Output: <class 'str'>
```

---

## Practice Exercises

1. **Define Variables**: Create variables for your name, age, height, and whether you like pizza (True or False).
2. **Print Statements**: Use `print()` to display each variable.
3. **Type Checking**: Use `type()` to check the data type of each variable and print the result.

---

## Homework

1. **Create Personal Info Variables**: Write a script that stores your name, age, and favorite color in variables, and then prints a message using those variables.
2. **Calculator Exercise**: Create two variables, `num1` and `num2`, and store two numbers in them. Write code that:
   - Adds them and prints the result.
   - Multiplies them and prints the result.
3. **Data Type Exploration**: Experiment with assigning different types of data (like text and numbers) to variables and use `type()` to see the data type of each.

---

## Summary
- Variables allow you to store information.
- Python has different data types, including integers, floats, strings, and booleans.
- You can use `print()` to display variable values and `type()` to check data types.

Continue practicing with these concepts to get comfortable with using variables and understanding data types!
