# Day 9 - Armstrong Number Check
# Date: 2026-07-18

print("==== Day 9 : Armstrong Number Check ====\n")

num = int(input("Enter a number: "))

digits = len(str(num))
temp = num
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if sum_of_powers == num:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is NOT an Armstrong Number.")

print("\nProgram Completed Successfully!")
