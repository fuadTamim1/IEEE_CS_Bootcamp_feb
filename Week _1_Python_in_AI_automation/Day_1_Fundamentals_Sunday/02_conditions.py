"""
DAY 1 - LESSON 2: Conditions and Decision Making
================================================

Learning Objectives:
- Understand boolean values (True/False)
- Learn comparison operators (>, <, ==, !=, etc.)
- Learn logical operators (and, or, not)
- Write if/elif/else statements
- Make decisions based on conditions

Key Concepts:
- Boolean: A data type with only two values: True or False
- Comparison operators: ==, !=, >, <, >=, <=
- Logical operators: and, or, not
- if/elif/else: Control flow statements for decision making
"""

# ===== SECTION 1: Boolean Values =====
print("=== BOOLEAN VALUES ===\n")

is_raining = True
is_sunny = False

print(f"Is it raining? {is_raining}")
print(f"Is it sunny? {is_sunny}")

# Booleans are useful for making decisions
if is_raining:
    print("Bring an umbrella!")


# ===== SECTION 2: Comparison Operators =====
print("\n=== COMPARISON OPERATORS ===\n")

# These operators compare two values and return True or False

x = 10
y = 5

# Equal to (==)
print(f"{x} == {y}: {x == y}")        # False (10 is not equal to 5)

# Not equal to (!=)
print(f"{x} != {y}: {x != y}")        # True (10 is not equal to 5)

# Greater than (>)
print(f"{x} > {y}: {x > y}")          # True (10 is greater than 5)

# Less than (<)
print(f"{x} < {y}: {x < y}")          # False (10 is not less than 5)

# Greater than or equal to (>=)
print(f"{x} >= {y}: {x >= y}")        # True

# Less than or equal to (<=)
print(f"{x} <= {y}: {x <= y}")        # False


# ===== SECTION 3: Comparing Strings =====
print("\n=== STRING COMPARISON ===\n")

name = "Ahmed"
favorite_name = "Ahmed"

print(f"name: {name}")
print(f"favorite_name: {favorite_name}")
print(f"Are they the same? {name == favorite_name}")

# String comparison is case-sensitive
password = "python123"
entered_password = "Python123"
print(f"Passwords match? {password == entered_password}")  # False (case matters)


# ===== SECTION 4: if Statements =====
print("\n=== IF STATEMENTS ===\n")

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult!")

# If the condition is False, the code block doesn't execute
age = 15
if age >= 18:
    print("You are an adult!")    # This won't print
print("Age is:", age)


# ===== SECTION 5: if-else Statements =====
print("\n=== IF-ELSE STATEMENTS ===\n")

score = 75

if score >= 80:
    print("Grade: A")
else:
    print("Grade: B or lower")

# Another example
temperature = 30
if temperature > 25:
    print("It's hot! 🌞")
else:
    print("It's cool! 🌤️")


# ===== SECTION 6: if-elif-else Statements =====
print("\n=== IF-ELIF-ELSE STATEMENTS ===\n")

# When you need to check multiple conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Another example with age categories
age = 25

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Age: {age}, Category: {category}")


# ===== SECTION 7: Logical Operators =====
print("\n=== LOGICAL OPERATORS ===\n")

# Logical operators combine multiple conditions
# and: Both conditions must be True
# or: At least one condition must be True
# not: Reverses the boolean value

# AND operator
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive! 🚗")
else:
    print("You cannot drive.")

# OR operator
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("It's a free day! 🎉")
else:
    print("It's a work day.")

# NOT operator
is_raining = False

if not is_raining:
    print("Go outside! ☀️")
else:
    print("Stay inside.")


# ===== SECTION 8: Complex Conditions =====
print("\n=== COMPLEX CONDITIONS ===\n")

# Combining multiple logical operators
username = "admin"
password = "secret123"
attempts = 1

if username == "admin" and password == "secret123" and attempts < 3:
    print("✅ Login successful!")
else:
    print("❌ Login failed!")

# Another example: Check if number is in range
number = 15

if number >= 10 and number <= 20:
    print(f"{number} is between 10 and 20")

# More readable way using 'in range'
if 10 <= number <= 20:
    print(f"{number} is between 10 and 20")


# ===== SECTION 9: Practical Examples =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Traffic Light
print("--- Traffic Light ---")
light = "red"

if light == "red":
    action = "STOP"
elif light == "yellow":
    action = "CAUTION"
elif light == "green":
    action = "GO"

print(f"Light is {light}: {action}")

# Example 2: Student Eligibility
print("\n--- Student Eligibility ---")
age = 20
gpa = 3.5

if age >= 18 and gpa >= 3.0:
    print("✅ Eligible for scholarship")
else:
    print("❌ Not eligible")

# Example 3: E-commerce Discount
print("\n--- Discount Calculator ---")
amount = 150
is_member = True

discount = 0
if is_member and amount > 100:
    discount = amount * 0.10
elif amount > 100:
    discount = amount * 0.05

final_amount = amount - discount
print(f"Original: ${amount}")
print(f"Discount: ${discount}")
print(f"Final: ${final_amount}")


# ===== SECTION 10: Challenge =====
print("\n=== CHALLENGE ===")
print("What will this print?")
print()

x = 5
y = 10

if x < y and x != 0:
    print("Condition 1 is True")
elif x == y or x > y:
    print("Condition 2 is True")
else:
    print("Neither condition is True")

print("\n✅ Lesson 2 Complete!")
print("Next: Learn about Loops (for and while)")
