# Day 12 - Count Vowels in a String
# Date: 2026-07-21

print("==== Day 12 : Count Vowels in a String ====\n")

text = input("Enter a string: ")

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(f"\nNumber of vowels: {count}")

print("\nProgram Completed Successfully!")
