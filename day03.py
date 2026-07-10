# Day 3 - Largest of Three Numbers
# Date: 2026-07-09

print("=== Day 3: Largest of Three Numbers ===")

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Finding the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Displaying the result
print(f"\nThe largest number is: {largest}")

print("\nProgram completed successfully!")
