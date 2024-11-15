
# Lesson 1: Basic Object-Oriented Programming (OOP)

## Objective
In this lesson, you will learn:
1. What Object-Oriented Programming (OOP) is and why it is useful.
2. How to create classes and objects in Python.
3. How to define and use attributes and methods in a class.

By the end of this lesson, you should be able to create basic classes, instantiate objects, and work with their properties and methods.

---

## 1. What is Object-Oriented Programming?
Object-Oriented Programming (OOP) is a programming paradigm that uses objects to represent data and functionality. Objects are created from **classes**, which act as blueprints.

### Why OOP?
- Helps organize and structure code.
- Allows for reusable and modular code.
- Makes complex programs easier to understand and maintain.

---

## 2. Classes and Objects
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

### Defining a Class
A class is defined using the `class` keyword, followed by the class name.

### Example:
```python
class Car:
    pass  # An empty class
```

### Creating an Object
An object is created by calling the class name like a function.

```python
my_car = Car()  # Creating an instance of the Car class
print(type(my_car))  # Output: <class '__main__.Car'>
```

---

## 3. Attributes and Methods
### Attributes
Attributes are variables that belong to an object. They are defined inside the class using the `__init__` method.

### Example:
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an object with specific attributes
my_car = Car("Toyota", "Camry", 2020)
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
```

### Methods
Methods are functions that belong to a class. They are defined inside the class and take `self` as the first parameter.

### Example:
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Create an object and call its method
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()  # Output: 2020 Toyota Camry
```

---

## 4. Example: Defining and Using Classes
Here’s a full example of creating and using a class:

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Create objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Call methods on objects
person1.greet()  # Output: Hi, my name is Alice and I am 25 years old.
person2.greet()  # Output: Hi, my name is Bob and I am 30 years old.
```

---

## Practice Exercises

1. **Define a Class**: Create a `Dog` class with attributes `name` and `breed`. Add a method `bark` that prints "Woof!" when called.
2. **Car Class**: Define a `Car` class with attributes `make`, `model`, and `year`. Add a method `start_engine` that prints "Engine started!".
3. **Rectangle Class**: Create a `Rectangle` class with attributes `length` and `width`. Add a method `area` that calculates and returns the area.

---

## Homework

1. **Book Class**: Create a `Book` class with attributes `title`, `author`, and `year`. Add a method `description` that prints a summary of the book.
2. **Bank Account Class**: Write a `BankAccount` class with attributes `account_holder` and `balance`. Add methods `deposit` and `withdraw` to modify the balance and a method `display_balance` to show the current balance.
3. **Student Class**: Create a `Student` class with attributes `name`, `grade`, and `subject`. Add a method `study` that prints a message like "Alice is studying Math."

---

## Summary
- Classes are blueprints for creating objects, and objects represent real-world entities.
- Attributes define the properties of an object, and methods define the actions it can perform.
- Practice defining classes and creating objects to get comfortable with the basics of OOP.

Try the exercises and homework to reinforce your understanding of basic object-oriented programming!
