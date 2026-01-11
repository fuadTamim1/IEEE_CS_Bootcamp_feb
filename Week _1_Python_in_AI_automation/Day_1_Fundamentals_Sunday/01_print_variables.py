"""
DAY 1 - LESSON 1: Print Statements and Variables
================================================

Learning Objectives:
- Understand how to use print() to display output
- Learn about variables and how to store data
- Understand basic data types (int, float, string)
- Practice variable assignment and arithmetic operations

Key Concepts:
- print() function: Displays output on the screen
- Variables: Named containers that store values
- Data types: int (integer), float (decimal), str (text)
- Operators: +, -, *, /, //, %, **
"""

# ===== SECTION 1: Basic Print Statements =====
print("Hello World!")

# Print multiple values
print("Python is awesome!")
print("The year is", 2026)

# Print with multiple lines
print("\n--- Welcome to Python Workshop ---\n")


# ===== SECTION 2: Variables =====
# Variables are containers for storing data values
# Think of them as labeled boxes that hold information

# Variable naming rules:
# 1. Start with letter (a-z, A-Z) or underscore (_)
# 2. Can contain letters, numbers, and underscores
# 3. Names are case-sensitive (name ≠ Name)
# 4. Cannot use Python keywords (if, for, while, etc.)

# Example of variable assignment
name = "Ahmed"              # String (text)
age = 25                    # Integer (whole number)
height = 5.9                # Float (decimal number)
is_student = True           # Boolean (True/False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# ===== SECTION 3: Arithmetic Operations =====
print("\n--- Arithmetic Operations ---\n")

x = 10
y = 3

# Addition
print(f"{x} + {y} = {x + y}")

# Subtraction
print(f"{x} - {y} = {x - y}")

# Multiplication
print(f"{x} * {y} = {x * y}")

# Division (returns float)
print(f"{x} / {y} = {x / y}")

# Floor Division (returns integer, rounds down)
print(f"{x} // {y} = {x // y}")

# Modulus (remainder after division)
print(f"{x} % {y} = {x % y}")

# Exponentiation (power)
print(f"{x} ** {y} = {x ** y}")


# ===== SECTION 4: Variable Assignment and Modification =====
print("\n--- Modifying Variables ---\n")

counter = 5
print("Initial counter:", counter)

counter = counter + 1
print("After counter + 1:", counter)

counter = counter * 2
print("After counter * 2:", counter)

# Shorthand operators
counter += 3          # Same as: counter = counter + 3
print("After counter += 3:", counter)

counter -= 2          # Same as: counter = counter - 2
print("After counter -= 2:", counter)

counter *= 2          # Same as: counter = counter * 2
print("After counter *= 2:", counter)


# ===== SECTION 5: String Operations =====
print("\n--- String Operations ---\n")

first_name = "Ali"
last_name = "Ahmed"

# String concatenation (joining strings)
full_name = first_name + " " + last_name
print("Full name:", full_name)

# String repetition (repeating strings)
print("Separator:", "-" * 10)
print("Echo:", "Hello! " * 3)

# String length
message = "Python is powerful"
print(f"Message: {message}")
print(f"Length: {len(message)} characters")


# ===== SECTION 6: Type Conversion =====
print("\n--- Type Conversion ---\n")

# Converting to different types
number_as_string = "42"
number_as_int = int(number_as_string)
number_as_float = float(number_as_string)

print(f"Original (string): {number_as_string}, Type: {type(number_as_string)}")
print(f"As integer: {number_as_int}, Type: {type(number_as_int)}")
print(f"As float: {number_as_float}, Type: {type(number_as_float)}")

# Converting to string
age = 25
age_as_string = str(age)
print(f"Age as string: '{age_as_string}', Type: {type(age_as_string)}")


# ===== SECTION 7: Formatted Strings (f-strings) =====
print("\n--- Formatted Strings ---\n")

name = "Sarah"
score = 95.5
items_sold = 1234

# Old way (not recommended)
# print("Name: " + name + ", Score: " + str(score))

# New way (f-strings) - more readable
print(f"Name: {name}, Score: {score}")
print(f"Items sold today: {items_sold:,}")  # Format with comma separator
print(f"Score with 1 decimal: {score:.1f}")


# ===== PRACTICE EXAMPLE: Simple Calculator =====
print("\n--- Practice Example: Simple Calculator ---\n")

# Given values
price_per_item = 50
quantity = 3
tax_rate = 0.15

# Calculate
subtotal = price_per_item * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# Display results
print(f"Price per item: ${price_per_item}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal}")
print(f"Tax (15%): ${tax:.2f}")
print(f"Total: ${total:.2f}")


print("\n✅ Lesson 1 Complete!")
print("Next: Learn about Conditions (if/else statements)")
