"""
DAY 1 - LESSON 4: Functions and Code Organization
================================================

Learning Objectives:
- Understand what functions are and why they're important
- Learn how to define and call functions
- Learn about parameters and return values
- Understand function scope
- Practice writing reusable code

Key Concepts:
- Function: A reusable block of code that performs a specific task
- Parameters: Inputs that a function receives
- Return value: Output that a function produces
- Scope: Where variables can be accessed
- Abstraction: Hiding complexity behind simple function names
"""

# ===== SECTION 1: Basic Function Definition =====
print("=== BASIC FUNCTIONS ===\n")

# Define a simple function
def greet():
    """A simple greeting function."""
    print("Hello! Welcome to Python Workshop!")

# Call the function
greet()
greet()  # Can call it multiple times


# Another simple function
def say_goodbye():
    print("Thank you for learning Python!")
    print("Goodbye! 👋")

say_goodbye()


# ===== SECTION 2: Functions with Parameters =====
print("\n=== FUNCTIONS WITH PARAMETERS ===\n")

# Function with one parameter
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}! Welcome to Python!")

greet_person("Ahmed")
greet_person("Fatima")
greet_person("Ali")

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and print the result."""
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 20)
add_numbers(100, 50)

# Function with multiple parameters
def introduce(name, age, city):
    """Introduce a person."""
    print(f"My name is {name}, I'm {age} years old, and I live in {city}.")

introduce("Sara", 25, "Cairo")
introduce("Omar", 30, "Dubai")


# ===== SECTION 3: Functions with Return Values =====
print("\n=== FUNCTIONS WITH RETURN VALUES ===\n")

# Function that returns a value
def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

result = multiply(4, 5)
print(f"4 * 5 = {result}")

# Use return value directly
print(f"3 * 7 = {multiply(3, 7)}")

# Function that returns a string
def get_greeting(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to Python Workshop!"

message = get_greeting("Ali")
print(message)

# Store multiple return values
def calculate(a, b):
    """Return both sum and product."""
    sum_result = a + b
    product = a * b
    return sum_result, product

sum_val, prod_val = calculate(5, 3)
print(f"Sum: {sum_val}, Product: {prod_val}")


# ===== SECTION 4: Default Parameters =====
print("\n=== DEFAULT PARAMETERS ===\n")

# Function with default parameter values
def greet_with_title(name, title="Friend"):
    """Greet someone with an optional title."""
    print(f"Hello {title} {name}!")

greet_with_title("Ahmed")  # Uses default title "Friend"
greet_with_title("Sara", "Dr.")  # Uses provided title
greet_with_title("Ali", "Mr.")

# Another example
def power(base, exponent=2):
    """Calculate base raised to exponent (default is 2)."""
    return base ** exponent

print(f"2^2 = {power(2)}")        # Uses default exponent 2
print(f"2^3 = {power(2, 3)}")     # Uses provided exponent
print(f"5^2 = {power(5)}")


# ===== SECTION 5: Practical Functions =====
print("\n=== PRACTICAL FUNCTIONS ===\n")

# Function 1: Calculate area of a rectangle
def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

print(f"Rectangle (5x10) area: {rectangle_area(5, 10)}")
print(f"Rectangle (3x4) area: {rectangle_area(3, 4)}")

# Function 2: Check if number is even
def is_even(number):
    """Check if a number is even."""
    if number % 2 == 0:
        return True
    else:
        return False

print(f"\n10 is even: {is_even(10)}")
print(f"7 is even: {is_even(7)}")

# Function 3: Convert temperature
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(f"\n25°C = {celsius_to_fahrenheit(25)}°F")
print(f"0°C = {celsius_to_fahrenheit(0)}°F")

# Function 4: Generate multiplication table
def print_multiplication_table(number):
    """Print multiplication table for a number."""
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")

print_multiplication_table(5)


# ===== SECTION 6: Functions with Loops =====
print("\n=== FUNCTIONS WITH LOOPS ===\n")

# Function 1: Sum numbers from 1 to n
def sum_to_n(n):
    """Calculate sum of numbers from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(f"Sum 1 to 5: {sum_to_n(5)}")
print(f"Sum 1 to 10: {sum_to_n(10)}")
print(f"Sum 1 to 100: {sum_to_n(100)}")

# Function 2: Count specific character in string
def count_character(text, char):
    """Count how many times a character appears in text."""
    count = 0
    for c in text:
        if c == char:
            count = count + 1
    return count

text = "Programming is awesome!"
print(f"\n'{text}'")
print(f"Letter 'a' appears: {count_character(text, 'a')} times")
print(f"Letter 'm' appears: {count_character(text, 'm')} times")

# Function 3: Reverse a string
def reverse_string(text):
    """Reverse a string."""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

word = "Python"
print(f"\nOriginal: {word}")
print(f"Reversed: {reverse_string(word)}")


# ===== SECTION 7: Functions Calling Other Functions =====
print("\n=== FUNCTIONS CALLING FUNCTIONS ===\n")

# Helper function
def square(x):
    """Return the square of a number."""
    return x * x

# Function that uses another function
def sum_of_squares(a, b):
    """Return the sum of squares of two numbers."""
    return square(a) + square(b)

print(f"Square of 3: {square(3)}")
print(f"Square of 4: {square(4)}")
print(f"Sum of squares (3, 4): {sum_of_squares(3, 4)}")


# ===== SECTION 8: Interactive Functions =====
print("\n=== INTERACTIVE FUNCTIONS ===\n")

def ask_for_name():
    """Ask user for their name."""
    name = input("What's your name? ")
    return name

def calculate_age_range(age):
    """Determine age category."""
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

# Uncomment to interact with user
# user_name = ask_for_name()
# user_age = int(input("How old are you? "))
# category = calculate_age_range(user_age)
# print(f"{user_name}, you are a {category}")


# ===== SECTION 9: Practice - Simple Automation Examples =====
print("\n=== PRACTICE: SIMPLE AUTOMATION ===\n")

# Example 1: Simple Calculator
def calculator():
    """Simple calculator function."""
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == "5":
            print("Thank you for using Calculator!")
            break
        elif choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print(f"Result: {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1 * num2}")
            elif choice == "4":
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
        else:
            print("Invalid choice!")

# Uncomment to run calculator
# calculator()

# Example 2: Password checker
def check_password_strength(password):
    """Check password strength."""
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*" for char in password):
        strength += 1
    
    if strength < 2:
        return "Weak"
    elif strength < 3:
        return "Moderate"
    else:
        return "Strong"

print("Password Strength Checker:")
print(f"'pass' strength: {check_password_strength('pass')}")
print(f"'Pass123' strength: {check_password_strength('Pass123')}")
print(f"'MyPass123!@' strength: {check_password_strength('MyPass123!@')}")


print("\n✅ Lesson 4 Complete!")
print("🎉 You've completed Day 1 - Python Fundamentals!")
print("\nNext: Day 2 - Automation & File Handling")
