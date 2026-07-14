# Day 5 - Armstrong Number
# Date: 2026-07-11

print("=== Day 5: Armstrong Number Checker ===")

num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10

if original == sum:
    print(f"{original} is an Armstrong Number.")
else:
    print(f"{original} is not an Armstrong Number.")

print("\nProgram Completed Successfully!")
