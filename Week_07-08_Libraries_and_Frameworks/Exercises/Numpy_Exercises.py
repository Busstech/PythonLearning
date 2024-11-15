# NumPy Exercises

import numpy as np

# 1. Create a 1D Array
# Create an array of values from 10 to 50 (inclusive).

array_1d = np.arange(10, 51)
print("1D Array:", array_1d)

# 2. Create a 2D Array
# Create a 3x3 array filled with ones.

array_2d = np.ones((3, 3))
print("2D Array of Ones:\n", array_2d)

# 3. Element-Wise Operations
# Perform element-wise addition, subtraction, and multiplication on two arrays.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# 4. Array Slicing
# Create an array [10, 20, 30, 40, 50] and print the slice [20, 30, 40].

array = np.array([10, 20, 30, 40, 50])
sliced_array = array[1:4]
print("Sliced Array:", sliced_array)

# 5. Matrix Operations
# Create a 2D array and calculate the sum of all elements and the mean.

matrix = np.array([[1, 2], [3, 4]])
print("Matrix Sum:", np.sum(matrix))
print("Matrix Mean:", np.mean(matrix))

# 6. Reshape an Array
# Create a 1D array of 12 numbers and reshape it into a 3x4 array.

array_reshaped = np.arange(1, 13).reshape(3, 4)
print("Reshaped Array:\n", array_reshaped)

# 7. Random Array Statistics
# Generate an array of random numbers between 0 and 100. Calculate the sum, mean, max, and min.

random_array = np.random.randint(0, 101, size=10)
print("Random Array:", random_array)
print("Sum:", np.sum(random_array))
print("Mean:", np.mean(random_array))
print("Max:", np.max(random_array))
print("Min:", np.min(random_array))

# 8. Broadcasting Example
# Add 5 to every element of an array.

array = np.array([1, 2, 3, 4, 5])
broadcasted_array = array + 5
print("Array after Broadcasting:", broadcasted_array)

# 9. Matrix Multiplication
# Perform matrix multiplication on two 2D arrays.

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Product:\n", matrix_product)

# 10. Conditional Selection
# Create an array of numbers and filter out values greater than 5.

array = np.array([1, 6, 3, 8, 4, 9])
filtered_array = array[array > 5]
print("Filtered Array (values > 5):", filtered_array)
