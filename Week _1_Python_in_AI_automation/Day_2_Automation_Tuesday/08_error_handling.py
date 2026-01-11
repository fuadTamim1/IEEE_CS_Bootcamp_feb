"""
DAY 2 - LESSON 8: Error Handling and Debugging
============================================

Learning Objectives:
- Understand common Python errors
- Learn try-except-else-finally blocks
- Learn how to debug code
- Practice error handling
- Understand exception types

Key Concepts:
- Exception: An error that occurs during program execution
- try-except: Catch and handle exceptions
- else: Runs if no exception occurs
- finally: Always runs, for cleanup
- Debugging: Finding and fixing errors
"""

# ===== SECTION 1: Common Error Types =====
print("=== COMMON ERROR TYPES ===\n")

print("""
SyntaxError: Code syntax is wrong
  x = 5
  y = 10
  if x > y   # Missing colon
    print("x is greater")

NameError: Variable doesn't exist
  print(undefined_variable)

TypeError: Wrong data type for operation
  x = "hello"
  y = x + 5  # Can't add string and number

ValueError: Correct type but wrong value
  x = int("not_a_number")

IndexError: List index out of range
  my_list = [1, 2, 3]
  print(my_list[10])

KeyError: Dictionary key doesn't exist
  my_dict = {'name': 'Ali'}
  print(my_dict['age'])

ZeroDivisionError: Division by zero
  result = 10 / 0
""")


# ===== SECTION 2: try-except Blocks =====
print("\n=== TRY-EXCEPT BLOCKS ===\n")

# Example 1: Simple try-except
print("Example 1: Catching ValueError")
try:
    number = int("not_a_number")
except ValueError:
    print("❌ Error: Cannot convert to integer")

# Example 2: Multiple except blocks
print("\nExample 2: Multiple except blocks")
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero")
except ValueError:
    print("❌ Error: Invalid value")

# Example 3: Catching multiple exceptions
print("\nExample 3: Catching multiple exceptions in one except")
try:
    user_input = input("Enter a number: ")
    # Uncomment above to test interactively
    # For demo, we'll use a string that causes error
    test_input = "abc"
    number = int(test_input)
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"❌ Error: {e}")


# ===== SECTION 3: Generic Exception Handling =====
print("\n=== GENERIC EXCEPTION HANDLING ===\n")

# Catch any exception
print("Catching generic Exception:")
try:
    # This could fail in many ways
    my_list = [1, 2, 3]
    value = my_list[100]
except Exception as e:
    print(f"❌ An error occurred: {e}")
    print(f"Error type: {type(e).__name__}")


# ===== SECTION 4: try-except-else =====
print("\n=== TRY-EXCEPT-ELSE ===\n")

# else block runs only if no exception occurs
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
    else:
        print(f"✓ Result: {a} / {b} = {result}")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(15, 3)


# ===== SECTION 5: try-except-finally =====
print("\n=== TRY-EXCEPT-FINALLY ===\n")

# finally block ALWAYS runs
def read_file_demo(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"✓ File content: {content[:50]}...")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
    finally:
        print("(Cleanup code would go here)")
        # In real code: file.close()

read_file_demo("my_first_file.txt")


# ===== SECTION 6: Raising Exceptions =====
print("\n=== RAISING EXCEPTIONS ===\n")

# You can raise your own exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 150:
        raise ValueError("Age seems unrealistic")
    else:
        print(f"✓ Age {age} is valid")

# Test
try:
    validate_age(25)
    validate_age(-5)  # This will raise an error
except ValueError as e:
    print(f"❌ Validation error: {e}")


# ===== SECTION 7: Custom Exceptions =====
print("\n=== CUSTOM EXCEPTIONS ===\n")

# Create custom exception class
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Balance: {self.balance}"
            )
        self.balance -= amount
        print(f"✓ Withdrew {amount}. New balance: {self.balance}")

# Test
account = BankAccount(100)
try:
    account.withdraw(50)
    account.withdraw(80)  # Will raise error
except InsufficientFundsError as e:
    print(f"❌ Bank error: {e}")


# ===== SECTION 8: File Error Handling =====
print("\n=== FILE ERROR HANDLING ===\n")

import os

# Safe file reading
def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
        return None
    except IOError:
        print(f"❌ Cannot read file '{filename}'")
        return None

content = safe_read_file("nonexistent.txt")
print(f"Content: {content}")

# Safe file writing
def safe_write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"✓ Successfully wrote to {filename}")
    except IOError:
        print(f"❌ Cannot write to {filename}")

safe_write_file("safe_output.txt", "This is safe content")


# ===== SECTION 9: Input Validation =====
print("\n=== INPUT VALIDATION ===\n")

def get_integer(prompt="Enter an integer: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Please enter a valid integer")

# Uncomment to test interactive input
# num = get_integer("Enter your favorite number: ")
# print(f"You entered: {num}")

# For demo, we'll use preset value
def get_integer_demo(value):
    try:
        result = int(value)
        print(f"✓ Converted '{value}' to integer: {result}")
        return result
    except ValueError:
        print(f"❌ Cannot convert '{value}' to integer")
        return None

get_integer_demo("42")
get_integer_demo("hello")
get_integer_demo("3.14")


# ===== SECTION 10: Debugging with Print Statements =====
print("\n=== DEBUGGING WITH PRINTS ===\n")

def find_bug():
    x = 10
    print(f"DEBUG: x = {x}")
    
    y = 5
    print(f"DEBUG: y = {y}")
    
    result = x + y
    print(f"DEBUG: result = {result}")
    
    # Add more debug info
    print(f"DEBUG: result type = {type(result)}")
    
    return result

print("Debugging function:")
final_result = find_bug()


# ===== SECTION 11: Debugging Techniques =====
print("\n=== DEBUGGING TECHNIQUES ===\n")

print("""
1. Use print statements to track values
   print(f"Variable x = {x}")

2. Check variable types
   print(type(variable))

3. Use len() to check collections
   print(len(my_list))

4. Use conditional breakpoints
   if x > 100:
       print("x is suspiciously large!")

5. Use assertions for assumptions
   assert x > 0, "x must be positive"

6. Test with simple inputs first
   Always start with simple test cases

7. Read error messages carefully
   They usually tell you what's wrong and where
""")


# ===== SECTION 12: Assertion Statements =====
print("\n=== ASSERTIONS ===\n")

def calculate_percentage(earned, total):
    assert total > 0, "Total must be greater than zero"
    assert earned >= 0, "Earned cannot be negative"
    assert earned <= total, "Earned cannot exceed total"
    
    return (earned / total) * 100

# Test
try:
    print(f"90/100: {calculate_percentage(90, 100)}%")
    print(f"Trying invalid input:")
    print(f"100/100: {calculate_percentage(100, 100)}%")
    print(f"120/100: {calculate_percentage(120, 100)}%")  # Will fail assertion
except AssertionError as e:
    print(f"❌ Assertion failed: {e}")


# ===== SECTION 13: Practical Error Handling Example =====
print("\n=== PRACTICAL EXAMPLE: ROBUST CALCULATOR ===\n")

def robust_calculator():
    try:
        print("\n--- Robust Calculator ---")
        
        # Get first number
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("❌ Please enter a valid number")
        
        # Get operation
        operation = input("Enter operation (+, -, *, /): ")
        
        # Get second number
        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("❌ Please enter a valid number")
        
        # Calculate
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("❌ Cannot divide by zero")
                return
            result = num1 / num2
        else:
            print("❌ Invalid operation")
            return
        
        print(f"✓ Result: {num1} {operation} {num2} = {result}")
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Uncomment to test interactive
# robust_calculator()


# ===== SECTION 14: Logging Errors =====
print("\n=== LOGGING ERRORS ===\n")

import datetime

def log_error(error_message):
    \"\"\"Log error to file with timestamp.\"\"\"
    filename = "error_log.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, 'a') as file:
        file.write(f"[{timestamp}] ERROR: {error_message}\n")

# Simulate errors and log them
try:
    x = int("invalid")
except ValueError as e:
    log_error(f"ValueError: {e}")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    log_error(f"ZeroDivisionError: {e}")

print("✓ Errors logged to error_log.txt")


print("\n✅ Lesson 8 Complete!")
print("🎉 You've completed Day 2 - Automation & File Handling!")
print("\nNext: Day 3 - AI & Automation Systems")
