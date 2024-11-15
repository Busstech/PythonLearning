
# Lesson 1: Lists and Dictionaries

## Objective
In this lesson, you will learn:
1. What lists and dictionaries are in Python.
2. How to create and manipulate lists and dictionaries.
3. When to use lists versus dictionaries.

By the end of this lesson, you should be able to create lists and dictionaries, access their elements, and perform basic operations on them.

---

## 1. Introduction to Lists
A **list** is a collection of items in a specific order. Lists are useful for storing groups of related items, such as a list of names, numbers, or other data types.

### Creating a List
Lists are created using square brackets `[]` and can contain items of any data type.

### Example:
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["apple", 3.14, True]
```

### Accessing List Elements
You can access individual items in a list by their index. Note that list indexing starts at `0`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
```

### Common List Operations
- **Adding items**: Use `append()` to add an item to the end of the list.
- **Inserting items**: Use `insert()` to add an item at a specific position.
- **Removing items**: Use `remove()` to delete a specific item or `pop()` to remove an item by index.

### Examples:
```python
# Adding an item
fruits.append("orange")
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]

# Inserting an item
fruits.insert(1, "blueberry")
print(fruits)  # Output: ["apple", "blueberry", "banana", "cherry", "orange"]

# Removing an item
fruits.remove("banana")
print(fruits)  # Output: ["apple", "blueberry", "cherry", "orange"]

# Removing an item by index
fruits.pop(2)
print(fruits)  # Output: ["apple", "blueberry", "orange"]
```

---

## 2. Introduction to Dictionaries
A **dictionary** is a collection of key-value pairs. Each key is associated with a value, and dictionaries are useful for storing data that is organized by unique identifiers.

### Creating a Dictionary
Dictionaries are created using curly braces `{}` and contain key-value pairs separated by colons `:`.

### Example:
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

### Accessing Dictionary Values
You can access a value in a dictionary by referencing its key.

```python
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 25
```

### Adding and Modifying Dictionary Items
- **Adding a new key-value pair**: Use square brackets with the new key.
- **Modifying an existing key**: Reassign a value to an existing key.

```python
# Adding a new key-value pair
person["job"] = "Engineer"
print(person)

# Modifying an existing key
person["city"] = "San Francisco"
print(person)
```

### Removing Dictionary Items
- **Using `del`**: Deletes a specific key-value pair.
- **Using `pop()`**: Removes a key and returns its value.

```python
# Using del
del person["age"]
print(person)

# Using pop
city = person.pop("city")
print(person)
print("Removed city:", city)
```

---

## 3. Lists vs Dictionaries
- **Lists** are ordered collections and are best when you need to store items in sequence.
- **Dictionaries** are unordered collections and are ideal for storing data that can be identified with a unique key.

---

## Practice Exercises

1. **Favorite Movies**: Create a list of your favorite movies and print each movie on a new line.
2. **Shopping List**: Create a list of items to buy. Add a few items to the list, then remove an item and print the updated list.
3. **Phone Book**: Create a dictionary that stores names as keys and phone numbers as values. Add a few entries and print the dictionary.
4. **Dictionary Modification**: Take a dictionary with keys `name`, `age`, and `city`, and modify the `city` to a new location.

---

## Homework

1. **To-Do List**: Write a program that stores a to-do list in a list. Allow the user to add items to the list, mark items as completed (remove them), and print the updated list.
2. **Student Info**: Create a dictionary that stores information about a student (name, age, and grades in different subjects). Update the grades, add a new subject, and print the modified dictionary.
3. **Glossary**: Create a small glossary (dictionary) with programming terms as keys and their definitions as values. Print each term and its definition in a formatted way.

---

## Summary
- Lists are used to store ordered collections of items, accessible by index.
- Dictionaries store key-value pairs, allowing data to be accessed by unique keys.
- Practice adding, modifying, and removing elements in both lists and dictionaries to get comfortable with these data structures.

Try the exercises and homework to reinforce your understanding of lists and dictionaries in Python!
