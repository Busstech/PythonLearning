
# Lesson 2: Introduction to Pandas

## Objective
In this lesson, you will learn:
1. What Pandas is and why it is useful in data analysis.
2. How to create and manipulate DataFrames and Series.
3. Basic operations and functionalities provided by Pandas.

By the end of this lesson, you should be able to use Pandas to handle tabular data efficiently.

---

## 1. What is Pandas?
Pandas is a powerful library for data analysis and manipulation in Python. It provides two main structures:
- **Series**: A one-dimensional labeled array.
- **DataFrame**: A two-dimensional table with rows and columns.

### Why Use Pandas?
- Handles large datasets efficiently.
- Simplifies data cleaning and manipulation.
- Integrates seamlessly with other libraries like NumPy and Matplotlib.

To use Pandas, you must first install it (if not already installed):
```bash
pip install pandas
```

---

## 2. Creating a Series
A Series is a one-dimensional labeled array capable of holding any data type.

### Example:
```python
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)
```

### Output:
```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

### Customizing Index
You can provide custom labels (indices) for a Series.
```python
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series)
```

### Accessing Elements
You can access elements by index or label.
```python
print(series[2])  # Access by index
print(series["c"])  # Access by label
```

---

## 3. Creating a DataFrame
A DataFrame is a two-dimensional labeled table.

### Example:
```python
# Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
}
df = pd.DataFrame(data)
print(df)
```

### Output:
```
      Name  Age           City
0    Alice   25      New York
1      Bob   30  San Francisco
2  Charlie   35   Los Angeles
```

### Accessing Rows and Columns
- Access a column: `df["column_name"]`
- Access a row by index: `df.iloc[index]`
- Access a row by label: `df.loc[label]`

### Example:
```python
print(df["Name"])  # Output: Series of names
print(df.iloc[1])  # Output: Row with index 1
```

---

## 4. Basic DataFrame Operations

### Adding a New Column
```python
df["Salary"] = [50000, 60000, 70000]
print(df)
```

### Filtering Rows
```python
# Rows where Age > 28
filtered = df[df["Age"] > 28]
print(filtered)
```

### Summary Statistics
- `df.describe()`: Provides summary statistics.
- `df.mean()`: Calculates the mean of numeric columns.

### Example:
```python
print(df.describe())
print("Average Age:", df["Age"].mean())
```

---

## 5. Reading and Writing Data
Pandas can read and write data to various formats like CSV, Excel, and JSON.

### Reading a CSV File
```python
df = pd.read_csv("data.csv")
print(df.head())  # Displays the first 5 rows
```

### Writing to a CSV File
```python
df.to_csv("output.csv", index=False)
```

---

## Practice Exercises

1. **Create a DataFrame**: Create a DataFrame with columns for `Product`, `Price`, and `Quantity`. Add a new column for `Total` (Price × Quantity).
2. **Filtering Data**: Create a DataFrame for students with columns `Name`, `Grade`, and `Subject`. Filter students with grades above 80.
3. **Reading/Writing**: Read a CSV file into a DataFrame, make some changes (e.g., add a column), and save it to a new file.

---

## Homework

1. **Analyze a Dataset**: Load a dataset (e.g., CSV file of sales data) into a DataFrame. Calculate total sales, average sales per product, and the product with the highest sales.
2. **Modify a DataFrame**: Create a DataFrame with columns `Employee`, `Department`, and `Salary`. Add a new column for `Bonus` (10% of Salary) and save the updated DataFrame to a CSV file.
3. **Find Missing Data**: Create a DataFrame with some missing values (`NaN`). Use Pandas methods to find and fill the missing data.

---

## Summary
- Pandas is a versatile library for working with structured data.
- Series and DataFrames are the core structures of Pandas, enabling easy manipulation and analysis.
- Practice creating, manipulating, and analyzing data with Pandas.

Try the exercises and homework to reinforce your understanding of Pandas basics!
