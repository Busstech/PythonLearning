def display_menu():
    """Display the calculator's main menu."""
    print("\n==== Simple Calculator ====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Clear")
    print("6. Exit")
    print("========================")

def get_numbers():
    """
    Get two numbers from the user with error handling.
    Returns tuple of (first_number, second_number) or (None, None) if invalid input.
    """
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract two numbers and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """
    Divide two numbers and return the result.
    Handles division by zero error.
    """
    if y == 0:
        print("Error: Cannot divide by zero!")
        return None
    return x / y

def main():
    """Main calculator loop."""
    result = None
    
    while True:
        # Display the current result if it exists
        if result is not None:
            print(f"\nCurrent Result: {result}")
        
        display_menu()
        
        # Get user choice with error handling
        try:
            choice = input("\nEnter your choice (1-6): ")
        except ValueError:
            print("Error: Please enter a valid choice!")
            continue

        # Handle exit
        if choice == '6':
            print("\nThank you for using the calculator!")
            break
        
        # Handle clear
        if choice == '5':
            result = None
            print("\nCalculator memory cleared!")
            continue
        
        # Get numbers for calculation
        if choice in '1234':
            # If there's a previous result, use it as the first number
            if result is not None:
                print(f"Using previous result: {result}")
                num1 = result
                num2 = float(input("Enter number: "))
            else:
                num1, num2 = get_numbers()
                if num1 is None:  # Invalid input
                    continue
            
            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                if result is not None:
                    print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nError: Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    print("Welcome to the Simple Calculator!")
    main()