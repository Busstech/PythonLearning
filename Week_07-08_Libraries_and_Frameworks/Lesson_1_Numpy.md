
# Lesson 1: Introduction to NumPy

## Objective
In this lesson, you will learn:
1. What NumPy is and why it is important in Python programming.
2. How to create and manipulate arrays using NumPy.
3. Basic operations and functionalities provided by NumPy.

By the end of this lesson, you should be able to create NumPy arrays, perform basic mathematical operations, and understand their advantages over Python lists.

---

## 1. What is NumPy?
NumPy (Numerical Python) is a powerful library for numerical computing in Python. It provides support for:
- Multidimensional arrays and matrices.
- Mathematical operations on arrays (e.g., addition, subtraction, multiplication).
- Functions for linear algebra, statistics, and more.

### Why Use NumPy?
- **Speed**: NumPy is faster than Python lists for numerical computations.
- **Convenience**: It offers many functions for array manipulation and mathematical calculations.
- **Scalability**: It supports large datasets efficiently.

To use NumPy, you must first install it (if not already installed):
```bash
pip install numpy
```

---

## 2. Creating NumPy Arrays
A NumPy array is a grid of values, all of the same type. It is created using the `numpy.array()` function.

### Example:
```python
import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
```

### Array Properties
- `array.shape`: Returns the dimensions of the array.
- `array.size`: Returns the total number of elements.
- `array.dtype`: Returns the data type of elements.

### Example:
```python
print("Shape:", array_2d.shape)  # Output: (2, 3)
print("Size:", array_2d.size)    # Output: 6
print("Data type:", array_2d.dtype)  # Output: int64 (or int32 on some systems)
```

---

## 3. Array Operations
NumPy allows you to perform element-wise operations directly on arrays.

### Example:
```python
# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Perform element-wise operations
print("Addition:", a + b)       # Output: [5 7 9]
print("Multiplication:", a * b) # Output: [4 10 18]
print("Power:", a ** 2)         # Output: [1 4 9]
```

### Broadcasting
Broadcasting allows NumPy to perform operations on arrays of different shapes.
```python
a = np.array([1, 2, 3])
b = 2  # Scalar value
print("Addition with scalar:", a + b)  # Output: [3 4 5]
```

---

## 4. Array Indexing and Slicing
You can access elements in a NumPy array using indexing and slicing, similar to Python lists.

### Example:
```python
# 1D array indexing
array = np.array([10, 20, 30, 40, 50])
print(array[2])  # Output: 30

# 2D array indexing
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix[1, 2])  # Output: 6

# Slicing
print(array[1:4])  # Output: [20 30 40]
```

---

## 5. Useful NumPy Functions
### Creating Arrays
- `np.zeros(shape)`: Creates an array of zeros.
- `np.ones(shape)`: Creates an array of ones.
- `np.arange(start, stop, step)`: Creates an array with a range of values.

### Example:
```python
zeros = np.zeros((2, 3))
print("Zeros array:\n", zeros)

ones = np.ones((3, 3))
print("Ones array:\n", ones)

range_array = np.arange(0, 10, 2)
print("Range array:", range_array)
```

### Mathematical Functions
- `np.sum(array)`: Sum of all elements.
- `np.mean(array)`: Average of elements.
- `np.max(array)`: Maximum value in the array.
- `np.min(array)`: Minimum value in the array.

### Example:
```python
array = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(array))       # Output: 15
print("Mean:", np.mean(array))     # Output: 3.0
print("Max:", np.max(array))       # Output: 5
print("Min:", np.min(array))       # Output: 1
```

---

## Practice Exercises

1. **Array Creation**: Create a 1D array with values from 10 to 50 (inclusive). Then create a 2D array of shape (3, 3) filled with ones.
2. **Element-Wise Operations**: Create two arrays `[1, 2, 3]` and `[4, 5, 6]`. Perform addition, subtraction, and multiplication on them.
3. **Array Slicing**: Create an array `[10, 20, 30, 40, 50]` and print the slice `[20, 30, 40]`.
4. **Matrix Operations**: Create a 2D array `[[1, 2], [3, 4]]`. Calculate the sum of all elements and the mean.

---

## Homework

1. **Matrix Multiplication**: Create two 2D arrays and perform matrix multiplication using `np.dot()`.
2. **Statistics**: Create an array of random numbers between 0 and 100. Calculate the sum, mean, max, and min of the array.
3. **Reshape**: Create a 1D array of 12 numbers and reshape it into a 2D array of shape (3, 4).

---

## Summary
- NumPy provides efficient and easy-to-use tools for numerical computing.
- Arrays are the core structure of NumPy, and they are faster and more efficient than Python lists.
- Practice creating and manipulating arrays to become familiar with NumPy's functionality.

Try the exercises and homework to reinforce your understanding of NumPy basics!
