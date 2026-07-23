# Day 14 - Find the Largest Number in a List
# Date: 2026-07-23

print("==== Day 14 : Find the Largest Number in a List ====\n")

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"\nThe Largest Number is: {largest}")

print("\nProgram Completed Successfully!")
