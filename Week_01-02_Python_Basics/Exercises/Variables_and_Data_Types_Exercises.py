# Variables and Data Types Exercises

# 1. Personal Information Display
# This exercise stores personal details in variables and displays them in a formatted message.

# Define variables for name, age, and favorite color
name = "Alice"  # Replace with your name
age = 25        # Replace with your age
favorite_color = "blue"  # Replace with your favorite color

# Display the message using the variables
print(f"Hello, my name is {name}. I am {age} years old and my favorite color is {favorite_color}.")

# 2. Calculator Exercise
# This exercise takes two numbers from the user and performs basic arithmetic operations.

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform addition, subtraction, multiplication, and division
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined"  # Check for division by zero

# Display the results of each operation
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# 3. Data Type Exploration
# This exercise demonstrates how different types of data can be stored in variables.

# Define different types of variables
int_variable = 10               # Integer
float_variable = 3.14           # Float
string_variable = "Python"      # String
boolean_variable = True         # Boolean

# Display the values and their data types
print("Integer:", int_variable, "| Type:", type(int_variable))
print("Float:", float_variable, "| Type:", type(float_variable))
print("String:", string_variable, "| Type:", type(string_variable))
print("Boolean:", boolean_variable, "| Type:", type(boolean_variable))
