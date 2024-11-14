
# Lesson 3: Input and Output

## Objective
In this lesson, you will learn:
1. How to take user input in Python using the `input()` function.
2. How to display output using the `print()` function.
3. Ways to combine text and variables in output statements.

By the end of this lesson, you should be able to interact with users through basic input and output operations.

---

## 1. Taking Input with `input()`
The `input()` function allows you to get information from the user. Whatever the user types is returned as a string.

### Example:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

Here, `input("Enter your name: ")` prompts the user to enter their name. The result is stored in the `name` variable.

### Converting Input to Other Data Types
Since `input()` returns a string, you may need to convert it to other types (e.g., integer or float) for mathematical calculations.

### Example:
```python
age = int(input("Enter your age: "))  # Converts input to an integer
print("In 10 years, you will be", age + 10)
```

In this example, `int(input(...))` converts the user's input to an integer so it can be used in calculations.

---

## 2. Displaying Output with `print()`
The `print()` function is used to display information to the user. You can print text, numbers, and even the result of expressions.

### Example:
```python
print("Hello, world!")
print("The result of 5 + 3 is:", 5 + 3)
```

**Output:**
```
Hello, world!
The result of 5 + 3 is: 8
```

---

## 3. Combining Text and Variables in Output
You can combine variables and text within the `print()` function. There are several ways to do this in Python.

### 3.1 Using Commas in `print()`
Commas automatically add spaces between elements in the `print()` statement.
```python
name = "Alice"
age = 25
print("Hello,", name, "you are", age, "years old.")
```

### 3.2 Using String Concatenation
You can use the `+` operator to join strings, but it requires everything to be a string.
```python
name = "Alice"
print("Hello, " + name + "!")
```

### 3.3 Using f-Strings (Formatted Strings)
With f-strings, you can directly insert variables into curly braces `{}`.
```python
name = "Alice"
age = 25
print(f"Hello, {name}! You are {age} years old.")
```

**Output:**
```
Hello, Alice! You are 25 years old.
```

---

## Practice Exercises

1. **Basic Greeting**: Write a program that asks for your name and favorite color, then prints a message using both.
2. **Age in Months**: Ask the user for their age in years, then calculate and print their age in months.
3. **Temperature Conversion**: Write a program that asks the user for a temperature in Celsius, converts it to Fahrenheit, and prints the result. (Formula: `Fahrenheit = Celsius * 9/5 + 32`)

---

## Homework

1. **BMI Calculator**: Ask the user for their height (in meters) and weight (in kilograms), then calculate their BMI using the formula `BMI = weight / (height ** 2)`. Print the result.
2. **Simple Interest Calculator**: Write a program that takes inputs for principal (P), rate of interest (R), and time in years (T). Then, calculate and display the simple interest using the formula `Simple Interest = (P * R * T) / 100`.
3. **Personalized Message**: Ask the user for their name, favorite food, and favorite hobby. Print a sentence that combines all these details, such as "Hello, [name]! It's great to meet someone who enjoys [hobby] and loves [food]!"

---

## Summary
- `input()` is used to get information from the user and returns it as a string.
- `print()` is used to display information to the user.
- You can format output by combining text and variables with commas, concatenation, or f-strings.

Practice using `input()` and `print()` to get comfortable with user interactions in Python!
