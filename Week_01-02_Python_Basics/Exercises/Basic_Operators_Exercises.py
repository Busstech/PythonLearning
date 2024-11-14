
# Basic Operators Exercises

# 1. Rectangle Area and Perimeter Calculation
# This exercise calculates the area and perimeter of a rectangle based on user-provided length and width.

# Get the length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area (length * width)
area = length * width
# Calculate perimeter (2 * (length + width))
perimeter = 2 * (length + width)

# Display the results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

# 2. Even or Odd Check
# This exercise checks if a given number is even or odd using the modulus operator.

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even (remainder when divided by 2 is 0)
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. Power Calculation
# This exercise raises a base to a given exponent, which the user provides.

# Get base and exponent from the user
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Calculate the power (base ** exponent)
result = base ** exponent

# Display the result
print(f"{base} raised to the power of {exponent} is: {result}")
