# Lesson 2: File Handling

## Objective
In this lesson, you will learn:
1. How to read from and write to files in Python.
2. How to handle file operations safely using `with` statements.
3. Different file modes such as reading, writing, and appending.

By the end of this lesson, you should be able to perform basic file operations like creating, reading, writing, and updating files.

---

## 1. Introduction to File Handling
File handling allows you to work with files directly in Python, such as reading data from a file or writing data to a file.

### Key Points:
- Files must be opened before reading or writing.
- Files should always be closed after use to free up system resources.
- The `with` statement automatically handles file closing for you.

### File Modes:
| Mode   | Description                        |
|--------|------------------------------------|
| `r`    | Read (default mode).               |
| `w`    | Write (overwrites if file exists). |
| `a`    | Append (adds to the end of file).  |
| `r+`   | Read and write.                    |

---

## 2. Writing to a File
You can write data to a file using the `write()` method. Use the `w` mode to create a new file or overwrite an existing one.

### Example:
```python
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")
```

This will create a file named `example.txt` with the specified content.

---

## 3. Reading from a File
You can read data from a file using the `read()` or `readlines()` methods.

### Example: Reading the Entire File
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Example: Reading Line by Line
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes the newline character
```

---

## 4. Appending to a File
To add data to the end of a file without overwriting its content, use the `a` mode.

### Example:
```python
with open("example.txt", "a") as file:
    file.write("\nAppending this line to the file.")
```

---

## 5. Checking if a File Exists
Before performing operations, you may want to check if a file exists using the `os` module.

### Example:
```python
import os

if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File does not exist.")
```

---

## Practice Exercises

1. **Write and Read**: Create a file called `notes.txt`. Write a few lines to it, then read and print its content.
2. **Append Data**: Write a program to append new lines to an existing file and display the updated content.
3. **Word Counter**: Write a program to read a text file and count the number of words in it.

---

## Homework

1. **Simple Log File**: Create a file called `log.txt`. Write a program that appends a timestamp and a log message every time it runs.
2. **File Copy**: Write a program that reads the content of one file and writes it to a new file (e.g., `copy.txt`).
3. **Search in File**: Write a program that searches for a specific word in a file and prints how many times it appears.

---

## Summary
- File handling in Python allows you to read, write, and update files.
- The `with` statement is a safe and efficient way to handle file operations.
- Practice reading and writing files to become comfortable with file handling in Python.

Try the exercises and homework to reinforce your understanding of file handling!
