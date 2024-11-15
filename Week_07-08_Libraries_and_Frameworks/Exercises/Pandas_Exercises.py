# Pandas Exercises

import pandas as pd

# 1. Create a DataFrame
# Create a DataFrame with columns for Product, Price, and Quantity.

data = {
    "Product": ["Apple", "Banana", "Cherry"],
    "Price": [0.5, 0.3, 0.2],
    "Quantity": [10, 20, 15]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Add a new column for Total (Price * Quantity).
df["Total"] = df["Price"] * df["Quantity"]
print("Updated DataFrame with Total:\n", df)

# 2. Filtering Data
# Create a DataFrame for students with columns Name, Grade, and Subject.
# Filter students with grades above 80.

students_data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Grade": [85, 78, 92, 65],
    "Subject": ["Math", "Science", "History", "Math"]
}
students_df = pd.DataFrame(students_data)
print("Students DataFrame:\n", students_df)

# Filter students with grades above 80.
high_achievers = students_df[students_df["Grade"] > 80]
print("High Achievers:\n", high_achievers)

# 3. Read and Write CSV
# Read a CSV file into a DataFrame, modify it, and save it back.

# Create a sample CSV (if running for the first time).
df.to_csv("products.csv", index=False)

# Read the CSV file
products_df = pd.read_csv("products.csv")
print("Products DataFrame from CSV:\n", products_df)

# Add a Discount column (10% off the Price).
products_df["Discounted Price"] = products_df["Price"] * 0.9
print("Products DataFrame with Discount:\n", products_df)

# Save the updated DataFrame to a new file.
products_df.to_csv("products_with_discounts.csv", index=False)

# 4. Summary Statistics
# Calculate summary statistics for numeric columns in a DataFrame.

summary = products_df.describe()
print("Summary Statistics:\n", summary)

# Calculate the mean of the Total column.
mean_total = products_df["Total"].mean()
print("Mean Total:", mean_total)

# 5. Handling Missing Data
# Create a DataFrame with some missing values and handle them.

data_with_missing = {
    "Name": ["Eve", "Frank", "Grace"],
    "Age": [25, None, 30],
    "Salary": [50000, 60000, None]
}
df_missing = pd.DataFrame(data_with_missing)
print("DataFrame with Missing Values:\n", df_missing)

# Fill missing values with default values.
df_filled = df_missing.fillna({
    "Age": df_missing["Age"].mean(),  # Fill with mean of Age
    "Salary": 0                       # Fill with 0 for Salary
})
print("DataFrame after Filling Missing Values:\n", df_filled)

# Drop rows with missing values.
df_dropped = df_missing.dropna()
print("DataFrame after Dropping Missing Values:\n", df_dropped)

# 6. Grouping and Aggregation
# Group a DataFrame by Subject and calculate the average Grade.

grouped = students_df.groupby("Subject")["Grade"].mean()
print("Average Grade by Subject:\n", grouped)