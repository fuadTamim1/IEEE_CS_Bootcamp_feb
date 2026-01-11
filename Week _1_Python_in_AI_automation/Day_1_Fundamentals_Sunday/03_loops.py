"""
DAY 1 - LESSON 3: Loops and Iteration
====================================

Learning Objectives:
- Understand for loops and how to iterate
- Learn about the range() function
- Understand while loops and loop control
- Learn break and continue statements
- Practice nested loops

Key Concepts:
- for loop: Repeats code for each item in a sequence
- range(): Generates a sequence of numbers
- while loop: Repeats code while a condition is True
- break: Exits a loop immediately
- continue: Skips the current iteration
"""

# ===== SECTION 1: Basic for Loop =====
print("=== BASIC FOR LOOPS ===\n")

# for loop iterates over a sequence
print("Simple for loop:")
for i in range(5):  # range(5) creates 0, 1, 2, 3, 4
    print(i)

# Loop through a list
print("\nLoop through a list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop through a string
print("\nLoop through a string:")
word = "Python"
for letter in word:
    print(letter)


# ===== SECTION 2: range() Function =====
print("\n=== RANGE() FUNCTION ===\n")

# range(stop) - from 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) - from start to stop-1
print("\nrange(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print()

# range(start, stop, step) - from start to stop-1, increment by step
print("\nrange(0, 10, 2):")  # Every 2nd number
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Negative step (counting backward)
print("\nrange(10, 0, -1):")  # Counting down
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Step of 3
print("\nrange(0, 20, 3):")
for i in range(0, 20, 3):
    print(i, end=" ")
print()


# ===== SECTION 3: for Loop with Conditions =====
print("\n=== FOR LOOP WITH CONDITIONS ===\n")

print("Numbers from 1 to 10, only odd numbers:")
for i in range(1, 11):
    if i % 2 != 0:  # Check if odd
        print(i, end=" ")
print()

print("\nMultiples of 3 from 0 to 30:")
for i in range(0, 31):
    if i % 3 == 0:
        print(i, end=" ")
print()


# ===== SECTION 4: Accumulation in Loops =====
print("\n=== ACCUMULATION IN LOOPS ===\n")

# Sum of numbers from 1 to 5
total = 0
for i in range(1, 6):
    total = total + i
    print(f"i={i}, total={total}")

print(f"\nSum of 1 to 5: {total}")

# Factorial (5! = 5 * 4 * 3 * 2 * 1)
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"\nFactorial of {n}: {factorial}")

# Count specific items
numbers = [10, 20, 15, 20, 30, 20]
count = 0
for num in numbers:
    if num == 20:
        count = count + 1

print(f"\nThe number 20 appears {count} times in the list")


# ===== SECTION 5: Nested Loops =====
print("\n=== NESTED LOOPS ===\n")

print("Multiplication table:")
for i in range(1, 4):           # Outer loop
    for j in range(1, 4):       # Inner loop
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # New line after each row

print("\nPattern with asterisks:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line


# ===== SECTION 6: while Loop =====
print("\n=== WHILE LOOPS ===\n")

print("Count from 1 to 5 using while:")
count = 1
while count <= 5:
    print(count)
    count = count + 1

print("\nCount down from 10 to 1:")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("Blastoff! 🚀")


# ===== SECTION 7: break Statement =====
print("\n=== BREAK STATEMENT ===\n")

print("Exit loop when finding a number:")
for i in range(1, 11):
    if i == 5:
        print(f"Found {i}! Exiting...")
        break
    print(i)

print("\nSearch for a number in a list:")
numbers = [2, 4, 6, 8, 10, 3, 5]
search = 10

for num in numbers:
    if num == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found")


# ===== SECTION 8: continue Statement =====
print("\n=== CONTINUE STATEMENT ===\n")

print("Skip multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

print("\nSkip negative numbers:")
numbers = [5, -2, 3, -1, 4]
for num in numbers:
    if num < 0:
        continue
    print(num)


# ===== SECTION 9: Practical Examples =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Print a simple menu repeatedly
print("--- Simple Menu Loop ---")
choice = ""
while choice != "quit":
    print("\n1. Greet")
    print("2. Say goodbye")
    print("Type 'quit' to exit")
    choice = input("Enter choice: ").lower()
    
    if choice == "1":
        print("Hello! 👋")
    elif choice == "2":
        print("Goodbye! 👋")
    elif choice != "quit":
        print("Invalid choice!")

# Example 2: Sum and average of numbers
print("\n--- Sum and Average ---")
numbers = [10, 20, 30, 40, 50]
total = 0
count = 0

for num in numbers:
    total = total + num
    count = count + 1

average = total / count
print(f"Numbers: {numbers}")
print(f"Total: {total}")
print(f"Average: {average}")

# Example 3: Check if a number is prime
print("\n--- Prime Number Check ---")
n = 17
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a prime number! ✓")
else:
    print(f"{n} is not a prime number.")


# ===== SECTION 10: Common Loop Patterns =====
print("\n=== COMMON LOOP PATTERNS ===\n")

# Pattern 1: Counter pattern
print("Counter pattern:")
count = 0
for i in range(5):
    count = count + 1
print(f"Total iterations: {count}")

# Pattern 2: Accumulator pattern (sum all)
print("\nAccumulator pattern:")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# Pattern 3: Search pattern
print("\nSearch pattern:")
fruits = ["apple", "banana", "orange", "grape"]
target = "orange"
found = False
for fruit in fruits:
    if fruit == target:
        found = True
        break

if found:
    print(f"Found {target}! ✓")
else:
    print(f"{target} not found")

print("\n✅ Lesson 3 Complete!")
print("Next: Learn about Functions")
