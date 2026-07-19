# Day 10 - Factorial of a Number
# Date: 2026-07-19

print("==== Day 10 : Factorial of a Number ====\n")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")

print("\nProgram Completed Successfully!")
