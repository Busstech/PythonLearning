# Project 1: To-Do App

## Objective
The goal of this project is to build a simple command-line to-do list application. This project will help you practice skills like managing user input, storing data, and implementing basic logic.

---

## Features
The to-do app will include the following features:
1. Add a new task.
2. View all tasks.
3. Mark a task as completed.
4. Delete a task.
5. Exit the application.

---

## Requirements
- Use a list or dictionary to store tasks.
- Use functions to handle different operations (e.g., add, view, delete).
- Make the app interactive by allowing the user to choose actions from a menu.

---

## Project Plan

### Step 1: Display a Menu
The program should display a menu of options for the user to choose from.

**Example:**
```
1. Add a new task
2. View tasks
3. Mark task as completed
4. Delete a task
5. Exit
```

### Step 2: Add a New Task
Allow the user to input a task description and store it in a list or dictionary.

**Example:**
```python
tasks = []
task = input("Enter a new task: ")
tasks.append({"task": task, "completed": False})
```

### Step 3: View Tasks
Display all tasks with their status (completed or not).

**Example Output:**
```
1. [ ] Buy groceries
2. [x] Finish homework
```

### Step 4: Mark a Task as Completed
Allow the user to select a task by its number and mark it as completed.

**Example:**
```python
tasks[1]["completed"] = True
```

### Step 5: Delete a Task
Allow the user to remove a task by its number.

**Example:**
```python
tasks.pop(1)
```

### Step 6: Exit the Application
Provide an option to exit the app and save the tasks (if required).

---

## Example Code Structure

Here is a suggested structure for the project:

```python
tasks = []

def display_menu():
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")

def mark_completed():
    view_tasks()
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted!")
    else:
        print("Invalid task number.")

while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the app... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

---

## Extensions (Optional)
1. **Persistent Storage**: Save tasks to a file and load them when the app starts.
2. **Task Deadlines**: Add a due date for tasks and sort them by deadline.
3. **Priority Levels**: Assign priority levels (e.g., High, Medium, Low) to tasks.

---

## Homework
1. Extend the app to allow users to edit an existing task.
2. Add functionality to save tasks to a file (e.g., `tasks.json`) and load them at startup.
3. Implement a feature to display only completed or incomplete tasks.

---

## Summary
This project provides hands-on experience with Python fundamentals such as:
- Lists and dictionaries for data storage.
- Functions for modular programming.
- Loops and conditionals for interactivity.

Build the app step-by-step and try the extensions to enhance its functionality!
