"""
DAY 1 - LESSON 4: Functions
============================

Learning Objectives:
- Define and call functions
- Understand parameters and return values
- Learn function scope
"""

print("=== FUNCTIONS ===\n")

# Simple function
def greet():
    print("Hello! Welcome to Python!")

greet()
greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ahmed")
greet_person("Fatima")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"\n5 + 3 = {result}")

# Multiple return values
def calculate(a, b):
    sum_val = a + b
    product = a * b
    return sum_val, product

s, p = calculate(4, 5)
print(f"Sum: {s}, Product: {p}")

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"\n2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")

# Practical example
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(f"\n10 is even: {is_even(10)}")
print(f"7 is even: {is_even(7)}")

print("\n✅ Lesson 4 Complete!")
