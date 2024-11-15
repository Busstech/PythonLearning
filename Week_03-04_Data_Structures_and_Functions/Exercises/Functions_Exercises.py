
# Functions Exercises

# 1. Simple Greeting Function
# This exercise creates a function that takes a name as input and prints a greeting message.

def greet_user(name):
    """Prints a personalized greeting message."""
    print(f"Hello, {name}! Welcome to Python programming.")

# Call the function with example names
greet_user("Alice")
greet_user("Bob")

# 2. Addition Function
# This exercise creates a function that takes two numbers as input, adds them, and returns the result.

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

# Call the function and display the result
result = add_numbers(10, 5)
print("The sum is:", result)

# 3. Rectangle Area
# This exercise creates a function that calculates the area of a rectangle given its length and width.

def area_of_rectangle(length, width):
    """Calculates and returns the area of a rectangle."""
    return length * width

# Call the function with example dimensions
length = 7
width = 3
area = area_of_rectangle(length, width)
print(f"The area of a rectangle with length {length} and width {width} is: {area}")

# 4. Temperature Converter
# This exercise creates a function to convert Celsius to Fahrenheit.

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

# Call the function with an example temperature
celsius = 25
fahrenheit = convert_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

# 5. Factorial Function
# This exercise creates a function that calculates the factorial of a given number.

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with an example number
number = 5
fact = factorial(number)
print(f"The factorial of {number} is: {fact}")

# 6. Shopping Cart Total
# This exercise calculates the total cost of items in a shopping cart.

def calculate_total(prices):
    """Calculates the total cost of a list of item prices."""
    return sum(prices)

# Example shopping cart prices
cart_prices = [10.99, 5.49, 3.89, 8.99]
total = calculate_total(cart_prices)
print("The total cost of the shopping cart is:", total)
