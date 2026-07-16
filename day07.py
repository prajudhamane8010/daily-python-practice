# Day 7 - Prime Number Check
# Date: 2026-07-16

print("==== Day 7 : Prime Number Check ====\n")

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a Prime Number.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a Prime Number.")

print("\nProgram Completed Successfully!")
