# Basic OOP Exercises

# 1. Dog Class
# This exercise creates a class for a dog with attributes and a method.

class Dog:
    def __init__(self, name, breed):
        """Initialize the dog with a name and breed."""
        self.name = name
        self.breed = breed

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says Woof!")

# Create instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Call the bark method
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Max says Woof!

# 2. Rectangle Class
# This exercise creates a class for a rectangle and calculates its area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

# Create an instance of the Rectangle class
rect = Rectangle(5, 3)

# Calculate and display area and perimeter
print(f"Area: {rect.area()}")  # Output: Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 16

# 3. Bank Account Class
# This exercise creates a class for a bank account with deposit and withdraw methods.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        """Initialize the account with a holder and balance."""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def display_balance(self):
        """Display the current balance."""
        print(f"Account balance: ${self.balance}")

# Create an instance of the BankAccount class
account = BankAccount("Alice", 100)

# Perform deposit, withdrawal, and display balance
account.deposit(50)       # Output: Deposited $50. New balance: $150
account.withdraw(30)      # Output: Withdrew $30. New balance: $120
account.display_balance() # Output: Account balance: $120

# 4. Book Class
# This exercise creates a class for a book with a description method.

class Book:
    def __init__(self, title, author, year):
        """Initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        """Print a description of the book."""
        print(f"'{self.title}' by {self.author}, published in {self.year}.")

# Create an instance of the Book class
book = Book("1984", "George Orwell", 1949)
book.description()  # Output: '1984' by George Orwell, published in 1949.

# 5. Student Class
# This exercise creates a class for a student with a study method.

class Student:
    def __init__(self, name, grade, subject):
        """Initialize the student with name, grade, and subject."""
        self.name = name
        self.grade = grade
        self.subject = subject

    def study(self):
        """Print a message that the student is studying."""
        print(f"{self.name} is studying {self.subject}.")

# Create an instance of the Student class
student = Student("Alice", "A", "Math")
student.study()  # Output: Alice is studying Math.
