
# 2-Week Python Learning Plan

## Week 1: Python Fundamentals

### Day 1: Variables and Data Types
- **Concepts**: Variables, data types (integers, floats, strings, booleans)
- **Examples**:
  ```python
  name = "Alice"
  age = 25
  height = 5.8
  is_student = True
  ```
- **Practice**: Create variables for your name, age, favorite number, and whether you like coding (True/False).
- **Homework**: Write a script that stores your name, age, and favorite color in variables, then prints each.

### Day 2: Basic Operators
- **Concepts**: Arithmetic operators (`+`, `-`, `*`, `/`, `**`), assignment operators
- **Examples**:
  ```python
  a = 10
  b = 5
  sum = a + b
  product = a * b
  ```
- **Practice**: Write code that calculates your age in months, days, and hours.
- **Homework**: Create a calculator program that takes two numbers and performs addition, subtraction, multiplication, and division.

### Day 3: Input and Output
- **Concepts**: `input()` for user input, `print()` for displaying output
- **Examples**:
  ```python
  name = input("Enter your name: ")
  print("Hello, " + name)
  ```
- **Practice**: Prompt the user for their age, then print their age in dog years (multiply by 7).
- **Homework**: Write a program that asks for a user’s height in meters and weight in kg, then calculates and prints their BMI.

### Day 4: Conditional Statements (if/else)
- **Concepts**: `if`, `else`, `elif` statements
- **Examples**:
  ```python
  age = 18
  if age >= 18:
      print("Adult")
  else:
      print("Minor")
  ```
- **Practice**: Write a program that checks if a number is even or odd.
- **Homework**: Create a program that asks for the user’s age and outputs “Child”, “Teen”, “Adult”, or “Senior” based on the input.

### Day 5: Loops (for and while)
- **Concepts**: `for` loop, `while` loop
- **Examples**:
  ```python
  for i in range(5):
      print(i)
  
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```
- **Practice**: Write a `for` loop that prints numbers 1 to 10.
- **Homework**: Create a program that calculates the sum of numbers from 1 to a user-inputted number using a loop.

### Day 6: Basic Error Handling
- **Concepts**: `try`, `except` blocks
- **Examples**:
  ```python
  try:
      number = int(input("Enter a number: "))
      print("Your number is", number)
  except ValueError:
      print("That’s not a valid number!")
  ```
- **Practice**: Write a program that asks for a number and catches invalid inputs.
- **Homework**: Create a program that asks for two numbers, tries to divide them, and catches any division by zero errors.

### Day 7: Review and Mini-Project
- **Project**: Write a simple “guess the number” game where the user tries to guess a randomly generated number within a certain range.
- **Homework**: Reflect on the week. Review any difficult topics and write questions or areas for improvement.

## Week 2: Core Python Structures and Functions

### Day 8: Lists and List Operations
- **Concepts**: Lists, adding/removing items, indexing
- **Examples**:
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits.append("orange")
  print(fruits[1])
  ```
- **Practice**: Create a list of your favorite movies and print each one.
- **Homework**: Write a program that takes a list of numbers and calculates their average.

### Day 9: Dictionaries
- **Concepts**: Key-value pairs, accessing/updating values
- **Examples**:
  ```python
  person = {"name": "Alice", "age": 25}
  print(person["name"])
  ```
- **Practice**: Create a dictionary for a book with keys for title, author, and year.
- **Homework**: Write a program that creates a contact list, storing names and phone numbers in a dictionary.

### Day 10: Functions
- **Concepts**: Defining and calling functions
- **Examples**:
  ```python
  def greet(name):
      return "Hello, " + name

  print(greet("Alice"))
  ```
- **Practice**: Write a function that takes a number and returns its square.
- **Homework**: Create a function that takes a list of numbers and returns the sum.

### Day 11: File Handling
- **Concepts**: Reading from and writing to files
- **Examples**:
  ```python
  with open("test.txt", "w") as file:
      file.write("Hello, world!")
  ```
- **Practice**: Write a program that writes a user’s input to a file.
- **Homework**: Create a program that reads a file line by line and prints each line.

### Day 12: Working with Strings
- **Concepts**: Basic string operations and formatting
- **Examples**:
  ```python
  text = "hello world"
  print(text.upper())
  ```
- **Practice**: Write a program that takes a sentence and counts the number of words.
- **Homework**: Create a program that asks for a sentence, reverses it, and prints the result.

### Day 13: Basic Object-Oriented Programming (OOP)
- **Concepts**: Classes and objects
- **Examples**:
  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

  p1 = Person("Alice", 30)
  ```
- **Practice**: Create a `Car` class with `make`, `model`, and `year` attributes.
- **Homework**: Create a `Book` class with `title`, `author`, and `read()` method that prints a message when the book is read.

### Day 14: Review and Project
- **Project**: Write a program that stores a list of tasks (like a to-do list) and allows the user to add, view, or delete tasks.
- **Homework**: Reflect on your progress, review any challenging concepts, and practice further if needed.