# Day 4 - Prime Number Checker
# Date: 2026-07-10

print("=== Day 4: Prime Number Checker ===")

# Taking input from the user
num = int(input("Enter a number: "))

# Checking whether the number is prime
if num <= 1:
    print(f"{num} is not a Prime Number.")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a Prime Number.")

print("\nProgram Completed Successfully!")
