# Day 8 - Palindrome Number Check
# Date: 2026-07-17

print("==== Day 8 : Palindrome Number Check ====\n")

num = input("Enter a number: ")

reverse = num[::-1]

if num == reverse:
    print(f"{num} is a Palindrome Number.")
else:
    print(f"{num} is NOT a Palindrome Number.")

print("\nProgram Completed Successfully!")
