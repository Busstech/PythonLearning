# File Handling Exercises

# 1. Write and Read a File
# This exercise creates a file, writes multiple lines to it, and reads its content.

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Line 1: Python is fun!\n")
    file.write("Line 2: File handling is useful.\n")
    file.write("Line 3: Practice makes perfect.\n")

# Reading from the file
print("Content of 'notes.txt':")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# 2. Append Data to an Existing File
# This exercise appends data to an existing file and displays the updated content.

# Appending to the file
with open("notes.txt", "a") as file:
    file.write("Line 4: Appending is easy!\n")

# Reading the updated file
print("Updated content of 'notes.txt':")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Count Words in a File
# This exercise counts the number of words in a file.

# Reading the file and counting words
with open("notes.txt", "r") as file:
    lines = file.readlines()
    word_count = sum(len(line.split()) for line in lines)
    print(f"The file 'notes.txt' contains {word_count} words.")

# 4. Copy File Content
# This exercise copies the content of one file to another.

# Copying content from notes.txt to copy.txt
with open("notes.txt", "r") as source_file:
    content = source_file.read()

with open("copy.txt", "w") as target_file:
    target_file.write(content)

print("Content copied to 'copy.txt'.")

# 5. Search for a Word in a File
# This exercise searches for a specific word in a file and counts its occurrences.

search_word = "Python"

# Searching for the word in the file
with open("notes.txt", "r") as file:
    lines = file.readlines()
    occurrences = sum(line.count(search_word) for line in lines)
    print(f"The word '{search_word}' appears {occurrences} times in 'notes.txt'.")

# 6. Create a Log File
# This exercise appends a timestamped log message to a log file.

import datetime

# Appending a log entry with a timestamp
with open("log.txt", "a") as log_file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"{timestamp} - This is a log entry.\n")

print("Log entry added to 'log.txt'.")

# 7. Handle File Not Found Error
# This exercise demonstrates handling errors when a file is not found.

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")

# 8. Read File Line by Line
# This exercise reads a file line by line and prints each line.

print("Reading 'notes.txt' line by line:")
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# 9. Write a Function for File Handling
# This exercise creates a function that writes and reads from a file.

def write_and_read_file(filename, data):
    """Writes data to a file and reads it back."""
    with open(filename, "w") as file:
        file.write(data)
    with open(filename, "r") as file:
        return file.read()

file_content = write_and_read_file("example.txt", "This is an example file created using a function.")
print("Content of 'example.txt':")
print(file_content)
