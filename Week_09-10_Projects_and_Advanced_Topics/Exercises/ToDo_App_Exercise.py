
# Exercise for Project 1: To-Do App

# This exercise implements a basic structure of the to-do app. Your task is to extend it
# with additional functionality like saving tasks to a file.

tasks = []

def display_menu():
    """Displays the menu options."""
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Exit")

def add_task():
    """Allows the user to add a new task."""
    task = input("Enter the task description: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def view_tasks():
    """Displays all tasks with their completion status."""
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Exiting the app... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
