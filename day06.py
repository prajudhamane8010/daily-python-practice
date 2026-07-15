# Day 6 - Fibonacci Series
# Date: 2026-07-12

print("=== Day 6: Fibonacci Series ===")

n = int(input("Enter the number of terms: "))

first = 0
second = 1

print("\nFibonacci Series:")

for i in range(n):
    print(first, end=" ")
    next_num = first + second
    first = second
    second = next_num

print("\n\nProgram Completed Successfully!")
