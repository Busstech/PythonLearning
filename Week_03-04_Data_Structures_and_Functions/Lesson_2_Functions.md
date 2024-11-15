
# Lesson 2: Functions

## Objective
In this lesson, you will learn:
1. What functions are and why they are important in programming.
2. How to define and call functions in Python.
3. How to pass arguments to functions and return values.

By the end of this lesson, you should be able to create your own functions, call them, and work with inputs and outputs.

---

## 1. What is a Function?
A **function** is a block of code designed to perform a specific task. Functions help you organize your code, avoid repetition, and make it more readable.

### Key Points:
- Functions can take input (parameters) and return output (values).
- A function is defined using the `def` keyword.

### Example:
```python
def greet():
    print("Hello, world!")

# Calling the function
greet()
```

**Output:**
```
Hello, world!
```

---

## 2. Defining Functions
To define a function:
1. Use the `def` keyword, followed by the function name and parentheses `()`.
2. Write the function body (indented) with the actions you want the function to perform.

### Example:
```python
def say_hello():
    print("Hello!")
    print("Welcome to Python!")
```

### Calling the Function:
To run the function, use its name followed by parentheses:
```python
say_hello()
```

---

## 3. Functions with Parameters
Functions can take inputs called **parameters**. These allow you to pass information into the function.

### Example:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```

**Output:**
```
Hello, Alice!
Hello, Bob!
```

---

## 4. Functions with Return Values
Functions can return a value using the `return` keyword. This allows you to store the result of a function for later use.

### Example:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print("The sum is:", result)
```

**Output:**
```
The sum is: 8
```

---

## 5. Default Parameters
You can assign default values to parameters. If a value is not provided when calling the function, the default is used.

### Example:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!
```

---

## 6. Multiple Parameters
A function can take multiple parameters separated by commas.

### Example:
```python
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print("The area is:", area)
```

**Output:**
```
The area is: 15
```

---

## Practice Exercises

1. **Simple Greeting Function**: Write a function called `greet_user` that takes a name as input and prints a greeting message.
2. **Addition Function**: Create a function called `add_numbers` that takes two numbers as input, adds them, and returns the result.
3. **Rectangle Area**: Write a function called `area_of_rectangle` that takes the length and width as arguments, calculates the area, and returns it.

---

## Homework

1. **Temperature Converter**: Write a function `convert_to_fahrenheit` that takes a temperature in Celsius as input and returns the temperature in Fahrenheit. (Formula: `F = C * 9/5 + 32`)
2. **Factorial Function**: Create a function `factorial` that takes an integer as input and returns its factorial. (Factorial of 5 is `5 * 4 * 3 * 2 * 1`).
3. **Shopping Cart**: Write a program that uses a function `calculate_total` to calculate the total cost of items in a shopping cart. The function should take a list of prices as input and return the total.

---

## Summary
- Functions are reusable blocks of code that make programs more organized and efficient.
- You can pass data to functions using parameters and get results using return values.
- Practice writing your own functions to gain confidence in using them.

Try the exercises and homework to reinforce your understanding of functions in Python!
