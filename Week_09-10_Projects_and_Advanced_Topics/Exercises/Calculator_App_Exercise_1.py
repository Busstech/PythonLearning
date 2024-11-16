
# Exercise for Project 2: Calculator App

# This exercise implements a basic calculator with four operations.
# Extend the program to include advanced operations like modulus, exponentiation, and factorial.

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def display_menu():
    """Displays the calculator menu."""
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an operation (1-5): ")

    if choice == "5":
        print("Exiting the calculator... Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid choice. Please try again.")
