
# Lists and Dictionaries Exercises

# 1. Favorite Movies
# This exercise creates a list of favorite movies and prints each movie on a new line.

# Define a list of favorite movies
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Print each movie on a new line
print("My favorite movies are:")
for movie in favorite_movies:
    print(movie)

# 2. Shopping List
# This exercise creates a shopping list, adds and removes items, and prints the updated list.

# Create a shopping list
shopping_list = ["bread", "milk", "eggs"]

# Add items to the shopping list
shopping_list.append("butter")
shopping_list.append("cheese")

# Remove an item from the shopping list
shopping_list.remove("milk")

# Print the updated shopping list
print("Updated shopping list:", shopping_list)

# 3. Phone Book
# This exercise creates a dictionary to store names and phone numbers, then prints the dictionary.

# Create a phone book dictionary
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Add a new entry to the phone book
phone_book["David"] = "111-222-3333"

# Print the phone book
print("Phone book:")
for name, number in phone_book.items():
    print(f"{name}: {number}")

# 4. Dictionary Modification
# This exercise modifies an existing dictionary by updating a key and adding a new one.

# Define a dictionary with name, age, and city
student_info = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}

# Modify the city
student_info["city"] = "San Francisco"

# Add a new key-value pair for grade
student_info["grade"] = "A"

# Print the updated dictionary
print("Updated student information:", student_info)
